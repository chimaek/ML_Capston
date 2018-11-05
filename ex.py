import pandas as pd
import os.path
import urllib.request
import json
import threading
import numpy as np


urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/BTC')
readTicker = urlTicker.read()

#json파일을 받아와 데이터프레임으로 가공합니다.
jsonTicker = pd.read_json(readTicker)
p1 = pd.DataFrame(jsonTicker).T.drop(["status"]).drop(["24H_fluctate"],axis=1).drop(['24H_fluctate_rate'],axis=1)\
        .drop(['average_price'],axis=1).drop(['buy_price'],axis=1).drop(['closing_price'],axis=1)\
        .drop(['opening_price'],axis=1).drop(['units_traded'],axis=1).drop(['volume_1day'],axis=1)\
        .drop(['volume_7day'],axis=1).drop(['sell_price'],axis=1).drop(["date"],axis=1)

print(data)
