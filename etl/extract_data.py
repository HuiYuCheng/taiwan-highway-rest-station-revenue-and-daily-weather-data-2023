import pandas as pd
import json
import copy

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process).reset_index(drop=True)
    return dataframe

def weather_data_extract(file_to_process):
    with open(file_to_process, "r") as file:
        data_str = file.read()
    data = json.loads(data_str)
    #找到所需資料在 json 中的位置
    locations = data["cwaopendata"]["resources"]["resource"]["data"]["surfaceObs"]["location"]
    info_list = []
    for location in locations:
        station_info = location["station"]
        daily_datas = location["stationObsStatistics"]["AirTemperature"]["daily"]
        #整理出氣象站資料
        for day_data in daily_datas:
            copy_station_info = copy.deepcopy(station_info)
            #將溫度資料（key = date, max, min, means）放入跟氣象站同一 dictionary 中
            for key in day_data.keys():
                copy_station_info[key] = day_data[key]
            #將字典存入 info_list 陣列
            info_list.append(copy_station_info) 
    dataframe = pd.DataFrame.from_dict(info_list)
    return dataframe