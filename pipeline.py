from extrac import fetch_data, to_dataframe
from transform import clean
from load import load2, get_location_id
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@localhost:3307/air_pipeline")

raw = to_dataframe(fetch_data())
df = clean(raw)
load2(df)
print(f"Pipeline selesai: {len(df)} baris diproses")
