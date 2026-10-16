import pandas as pd

def load_raw():
    return pd.read_csv("raw_air_quality.csv")

def clean(df):
    df["time"] = pd.to_datetime(df["time"])
    df = df.drop_duplicates()
    df["location"] = "Jakarta"
    df["pm25_category"] = pd.cut(
    df["pm2_5"],
    bins=[0, 9, 35.4, 55.4, 125.4, 225.4, float("inf")],
    labels=["Good", "Moderate", "Unhealthy for Sensitive", "Unhealthy", "Very Unhealthy", "Hazardous"],
    )
    return df

if __name__ == "__main__":
    df = clean(load_raw())
    print(df.dtypes)
    print(df.isna().sum())
    print(df.head())
