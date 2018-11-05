import pandas as pd
import os.path
import urllib.request
import json
import threading



urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/BTC')
readTicker = urlTicker.read()

#json파일을 받아와 데이터프레임으로 가공합니다.
jsonTicker = pd.read_json(readTicker)
p1=pd.DataFrame(jsonTicker["data"]).T

print(p1.dtypes)