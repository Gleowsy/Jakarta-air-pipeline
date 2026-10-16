import requests
import pandas as pd

URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": -6.2,
    "longitude": 106.82,
    "hourly": "pm10,pm2_5,nitrogen_dioxide,ozone",
    "timezone": "Asia/Jakarta",
}

def fetch_data():
    response = requests.get(URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()

def to_dataframe(data):
    return pd.DataFrame(data["hourly"])
if __name__ == "__main__":
    data = fetch_data()
    df = to_dataframe(data)
    print(df.head())
    print(df.shape)
    df.to_csv("raw_air_quality.csv", index=False)