# taiwan-highway-rest-station-revenue-2023
ETL pipeline for Taiwan highway rest station revenue and daily weather data in 2023.

# Project Name
臺灣高速公路服務區 每日營收與天氣關係

# What is this project about
    這個 project 利用台灣政府所提供的開放資料進行 ETL pipeline 建構（python）。
    整理出 2023 年台灣 15 座國道服務區每日的營業額、各氣象站每日的最高氣溫、最低氣溫、平均氣溫。
    資料使用者可以使用此整合好的資料集進行分析，例如：氣溫對於當日營業額的影響、追蹤每日營業額變化。

# Project files
    - data
        - raw_data: 存放原始資料
        - 完成 ETL 的成果資料
    - docs
        - 存放 README
        - log.txt 執行紀錄
    - etl
        - Extract, Transform, Load 步驟程式碼
    - pipelines
        - log 程式碼

# Project details
    ETL〈國道服務區每日營業額〉
    - extracted data from .csv files
    - transformed table schema
    - transformed data type
    - loaded data into .csv files and postgreSQL for different needs

    ETL〈自動氣象站-氣象觀測資料〉
    - extracted data from .json files
    - Selected essential data (daily maximum, minimum, and average temperatures) from the extensive dataset
    - transformed table schema
    - normalized data
    - loaded data into .csv files and postgreSQL for different needs

    BI〈臺灣高速公路服務區 每日營收與天氣關係〉
    - made a portal for analysis on IBM cognos

  You can check the portal demo video at: https://drive.google.com/file/d/1JBymasHLIEU2iJFGZsbIxR653wljUZp7/view?usp=sharing.
  ![ERD](https://drive.google.com/uc?export=view&id=1V7nKEJK3a2yxyg2Ss6CsLtKs47cE_ZRz)
  ![portal_1](https://drive.google.com/uc?export=view&id=1ylNnsvd1NNpyz_saIxIdFpwCA2dvHPhT)
  ![portal_2](https://drive.google.com/uc?id=1vFbMfNlIpVNkc-nJgnMcwfkD_FD352hC)


# If you want to use this project
    - 請注意這個專案僅是作為興趣的小專案，無營利行為
    - 若欲變更檔案目標位置，可在 main.py 中變更你想要的路徑
    - 若欲變更資料期間，可從下方 Rawdata source 中下載最新相關檔案

# Rawdata source
    〈國道服務區每日營業額〉政府資料開放平臺
    https://data.gov.tw/dataset/80081

    〈自動氣象站-氣象觀測資料〉氣象資料開放平臺
    https://opendata.cwa.gov.tw/dataset/observation/O-A0001-001

# Why this project
    台灣高速公路上設有 15 座舒適的國道服務區，是旅遊時休息的好夥伴，近年來，更是強調各站特色、主題，從歇腳的地方搖身一變成為景點之一。
    生在喜愛公路旅遊的家庭，從小就踩點各服務區，多少能感受到服務區大小、新舊與人潮的關係。
    看著人潮熙來攘往，不禁好奇：「國道服務區的營收狀況如何呢？既然是在國道上，那麼和假日、天氣好壞有關係嗎？」
    從政府開放資料中在找尋相關資料時發現，原始資料雖然完整，但營收資料格式並不適合用來分析；天氣資料則非常龐大、且包含許多非此需求所需的數據，需要進一步進行整理才有可能進行分析。
    因此，在學了 Data Engineering 的 ETL 後，想要給自己一個簡單、快速的練習機會，於是決定幫兒時的自己解惑，進行 side project 實作。
