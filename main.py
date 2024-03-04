from etl.extract_data import extract_from_csv, weather_data_extract
from etl.transform_data import transform_highway_data, transform_weather_data, normalization, combination
from etl.load_data import load_data
from pipelines.log import log_process

#original data
highway_file = "data/raw_data/2023_highway_stop_revenue.csv"
weather_file = "data/raw_data/weather.json"
nearest_station = "data/raw_data/nearest_station.csv"

#存放的目標位置
target_file_highway = "data/transformed_highway_data.csv"
target_file_weather = "data/transformed_weather_data.csv"
target_file_station_dim = "data/weatherStationDimTable.csv"
target_file_date_dim = "data/weatherDateDim.csv"
target_file_weather_fact = "data/weatherFactTable.csv"
tarfet_file_combined_table = "data/combined_table.csv"

#ETL Process
log_process("Start extract highway station revenue data")
extracted_highway_data = extract_from_csv(highway_file)
log_process("End of extracting highway station")

log_process("Start extract weather data")
extracted_weather_data = weather_data_extract(weather_file)
log_process("End of extracting weather data")

log_process("Start Transforming data")
transformed_highway_data = transform_highway_data(extracted_highway_data)
transformed_weather_data = transform_weather_data(extracted_weather_data)
log_process("End of transforming data")

log_process("Start load data")
load_data(target_file_highway,transformed_highway_data)
load_data(target_file_weather,transformed_weather_data)
log_process("End of load data")

log_process("start normalization process")
df = extract_from_csv(target_file_weather)
weather_station_dim, normalized_date_dim, weather_fact = normalization(df)
load_data(target_file_station_dim, weather_station_dim)
load_data(target_file_date_dim, normalized_date_dim)
load_data(target_file_weather_fact, weather_fact)
log_process("End of normalization data")

log_process("start output table for BI")
nearest_station_df = extract_from_csv(nearest_station)
combined_data = combination(nearest_station_df, transformed_highway_data,transformed_weather_data)
load_data(tarfet_file_combined_table, combined_data)
log_process("End of combining data")