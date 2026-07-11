import os
from flask import Flask, render_template, request
import requests
import pandas as pd
import joblib
import ephem
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

model_siap = joblib.load('model.pkl')
API_KEY = os.getenv("VISUAL_CROSSING_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    rekomendasi = []
    lokasi = ""
    
    if request.method == 'POST':
        lokasi = request.form.get('lokasi')

        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lokasi}?unitGroup=metric&key={API_KEY}&contentType=json"
        response = requests.get(url).json()

        data_jam = []
        for hari in response['days']:
            for jam in hari['hours']:
                data_jam.append({
                    'datetime': f"{hari['datetime']} {jam['datetime']}",
                    'cloudcover': jam['cloudcover'],
                    'humidity': jam['humidity'],
                    'precip': jam['precip'],
                    'visibility': jam['visibility'],
                    'windspeed': jam['windspeed']
                })
        
        df = pd.DataFrame(data_jam)
        df['datetime'] = pd.to_datetime(df['datetime'])

        df_malam = df[(df['datetime'].dt.hour >= 19) | (df['datetime'].dt.hour <= 4)].copy()

        df_malam['moonphase'] = df_malam['datetime'].apply(lambda x: ephem.Moon(x.strftime('%Y/%m/%d %H:%M:%S')).phase)

        fitur = ['cloudcover', 'humidity', 'precip', 'visibility', 'windspeed', 'moonphase']
        df_malam['Hasil_Prediksi'] = model_siap.predict(df_malam[fitur])

        df_rekomendasi = df_malam[df_malam['Hasil_Prediksi'] >= 1].copy()

        hari_indo = {
            'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu',
            'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu', 'Sunday': 'Minggu'
        }
        df_rekomendasi['Hari'] = df_rekomendasi['datetime'].dt.day_name().map(hari_indo)
        df_rekomendasi['Tanggal'] = df_rekomendasi['datetime'].dt.strftime('%d %b %Y')
        df_rekomendasi['Jam'] = df_rekomendasi['datetime'].dt.strftime('%H:%M WIB')
        df_rekomendasi['Status'] = df_rekomendasi['Hasil_Prediksi'].map({2: 'IDEAL', 1: 'CUKUP OKE'})

        df_rekomendasi = df_rekomendasi.sort_values(by='Hasil_Prediksi', ascending=False)

        rekomendasi = df_rekomendasi.head(10).to_dict(orient='records')
        
    return render_template('index.html', rekomendasi=rekomendasi, lokasi=lokasi)

if __name__ == '__main__':
    app.run(debug=True)