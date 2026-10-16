CREATE DATABASE IF NOT EXISTS air_pipeline;
USE air_pipeline;

CREATE TABLE IF NOT EXISTS dim_location (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    latitude DOUBLE,
    longitude DOUBLE
);

INSERT IGNORE INTO dim_location (name, latitude, longitude)
VALUES ('Jakarta', -6.2, 106.82);

CREATE TABLE IF NOT EXISTS fact_air_quality (
    location_id INT,
    time DATETIME,
    pm10 DOUBLE,
    pm2_5 DOUBLE,
    nitrogen_dioxide DOUBLE,
    ozone DOUBLE,
    pm25_category VARCHAR(30),
    PRIMARY KEY (location_id, time),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id)
);