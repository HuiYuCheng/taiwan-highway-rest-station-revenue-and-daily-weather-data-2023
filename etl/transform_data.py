import pandas as pd
import copy
import numpy as np

def transform_highway_data(df):
    #拆分日期資料格式，並轉型態為 date
    df_date = df["日期"].str.split("/", expand = True)
    df_date = df_date.rename(columns = {0:"year", 1:"month", 2:"day"})
    df_date = pd.to_datetime(df_date)
    #營收資料：各站收入資料結構從文字轉為數字
    df_revenue = df.iloc[:, 1:]
    for station in df_revenue.columns:
        df_revenue[station] = df_revenue[station].str.replace(",","").astype(int)
    #將日期資料與收入資料合併
    df = pd.concat([df_date, df_revenue],axis=1)
    df = df.rename(columns = {0:"date"})
   
    #資料轉置：將原本欄位名稱為各站名稱的資料表轉置成欄位名稱 = 「站名」、「營收」
    melted_df = df.melt(id_vars=["date"], var_name="rest stop", value_name='revenue')
    #把 date 資料再做拆分成三欄（為 BI 使用）
    melted_df["year"]=melted_df["date"].dt.year
    melted_df["month"]=melted_df["date"].dt.month
    melted_df["day"]=melted_df["date"].dt.day
    cols_order = ["date","year","month","day","rest stop","revenue"]
    melted_df = melted_df[cols_order]
    return melted_df

def transform_weather_data(df):
    #拆分日期資料（為 BI 使用）
    df_date = pd.DataFrame()
    df_date["Date"] = pd.to_datetime(df["Date"])
    df_date["year"] = df_date["Date"].dt.year
    df_date["month"] = df_date["Date"].dt.month
    df_date["day"] = df_date["Date"].dt.day
    #將日期資料與溫度合併
    df_station = df.iloc[:, 0:3]
    df_weather = df.iloc[:, 4:7]
    #空資料「X」處理
    df_weather.replace("X", np.nan, inplace = True )
    df_weather = df_weather.astype({"Maximum" : "float", "Minimum":"float", "Mean":"float"})
    dataframe = pd.concat([df_date, df_station, df_weather], axis = 1)
    return dataframe


#正規化資料表
def normalization(df):
    #將監測站資料獨立拉出一張表
    df_station_info = df[["StationID", "StationName", "StationNameEN"]].drop_duplicates().reset_index(drop = True)
    #將日期資料獨立拉出一張表
    df_date_info = df[["Date", "year", "month", "day"]].drop_duplicates().reset_index(drop = True)
    #建立 dateID 作為外鍵
    date_id_map = {} #一個字典 key:value
    current_id = 1
    for date in df["Date"]: #所有在 df 裡面的日期
        if date not in date_id_map: #如果這個 date 還沒出現在 key 值中
            date_id_map[date] = current_id #設定 key = date, value = current_id
            current_id += 1
    #在日期資料表中加入 dateID
    df_date_info["dateID"] = df_date_info["Date"].map(date_id_map)

    #複製一份 df
    copy_df = copy.deepcopy(df).reset_index(drop=True)
    copy_df['dateID'] = copy_df['Date'].map(date_id_map) #根據 Date 欄位 map 上對應的 ID 值
    copy_df.drop(["Date","year", "month", "day", "StationName", "StationNameEN"], axis = 1, inplace=True)
    return df_station_info, df_date_info, copy_df

# join 資料表（為 BI 使用）    
def combination(nearest_station, df_highway, df_weather):
    merged_df = pd.merge(df_highway, nearest_station, on="rest stop")
    merged_df2 = pd.merge(merged_df, df_weather[["Date","StationName","Maximum","Minimum","Mean"]], left_on = ["date","weather station"], right_on=["Date","StationName"], how = "left")
    merged_df2.drop(["Date", "StationName"], axis = 1, inplace= True)
    return merged_df2

