import pandas as pd
import os.path
import urllib.request
import json
import threading

end=False
def Cycle(second=300):
    global end
    if end:
        return
    #url을 받아와 실시간 비트코인 시세를 확인합니다.
    urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/BTC')
    readTicker = urlTicker.read()

    # json파일을 받아와 데이터프레임으로 가공합니다.
    jsonTicker = pd.read_json(readTicker)

    p1 = pd.DataFrame(jsonTicker["data"]).drop(["24H_fluctate"]).drop(['24H_fluctate_rate']).drop(['average_price']) \
        .drop(['buy_price']).drop(['closing_price']).drop(['opening_price']).drop(['units_traded']) \
        .drop(['volume_1day']).drop(['volume_7day']).drop(['sell_price']).drop(["date"]).T

    if(os.path.exists("data.csv")):
        #파일이 있을때 csv파일에 추가합니다.
        print("파일이 있어 기존의 데이터에 추가합니다.")
        p1.to_csv('data.csv',mode='a',header=False,encoding='utf-8')
    else:
        #파일이 없을때 csv파일을 생성합니다.
        print("파일이 없어 새로운 데이터를 생성합니다.")
        p1.to_csv("data.csv",encoding='utf-8')
    #반복 실행
    threading.Timer(second,Cycle,[second]).start()

num=input("반복될 시간을 정해주세요(초) : ")

if(num.isdigit()):
    Cycle(int(num))
else:
    print("잘못된 값을 입력하여 프로그램을 종료합니다.")
