from sqlalchemy import create_engine, text
from transform import load_raw, clean


engine = create_engine("mysql+pymysql://root:@localhost:3307/air_pipeline")

def get_location_id(conn, name):
    result = conn.execute(
        text("SELECT location_id FROM dim_location WHERE name = :name"),
        {"name": name},
    )
    return result.scalar()

def load2(df):
    sql = text("""
        INSERT INTO fact_air_quality
            (location_id, time, pm10, pm2_5, nitrogen_dioxide, ozone, pm25_category)
        VALUES
            (:location_id, :time, :pm10, :pm2_5, :nitrogen_dioxide, :ozone, :pm25_category)
        ON DUPLICATE KEY UPDATE
            pm10 = VALUES(pm10), pm2_5 = VALUES(pm2_5),
            nitrogen_dioxide = VALUES(nitrogen_dioxide),
            ozone = VALUES(ozone), pm25_category = VALUES(pm25_category)
    """)
    with engine.begin() as conn:
        location_id = get_location_id(conn, "Jakarta")

        df["location_id"] = location_id
  
        df["pm25_category"] = df["pm25_category"].astype(str)
        records = df.to_dict("records")
        conn.execute(sql, records)

if __name__ == "__main__":
    df = clean(load_raw())
    load2(df)
    print("Load selesai")