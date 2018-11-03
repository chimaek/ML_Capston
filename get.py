import pandas as pd
import os.path
import urllib.request
import json
import threading




#url을 받아와 실시간 비트코인 시세를 확인합니다.
urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')
readTicker = urlTicker.read()
#json파일을 받아와 데이터프레임으로 가공합니다.
jsonTicker = json.loads(readTicker.decode())
p1=pd.DataFrame(jsonTicker["data"])
P2=pd.DataFrame(p1["BTC"]).drop(["24H_fluctate"]).drop('24H_fluctate_rate').drop('average_price')\
    .drop('buy_price').drop('closing_price').drop('opening_price').drop('units_traded')\
    .drop('volume_1day').drop('volume_7day').T

if(os.path.exists("data.csv")):
    #파일이 있을때 csv파일에 추가합니다.
    print("파일이 있어 기존의 데이터에 추가합니다.")
    P2.to_csv('data.csv',mode='a',header=False)
else:
    #파일이 없을때 csv파일을 생성합니다.
    print("파일이 없어 새로운 데이터를 생성합니다.")
    P2.to_csv("data.csv",encoding='utf-8')

