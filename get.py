import pandas as pd
import os.path
import urllib.request
import json
import threading
import numpy as np

# 사용자가 입력한 수 간격만큼 데이터를 가져옵니다.
end=False
def Cycle(second=300):
    global end
    if end:
        return
    #url을 받아와 실시간 비트코인 시세를 확인합니다.
    url = urllib.request.urlopen('https://api.bithumb.com/public/ticker/BTC')
    readJson = url.read()

    # json파일을 받아와 데이터프레임으로 가공합니다.
    json = pd.read_json(readJson)
    p1 = pd.DataFrame(json).T.drop(["status"]).drop(["24H_fluctate"], axis=1).drop(['24H_fluctate_rate'], axis=1) \
        .drop(['average_price'], axis=1).drop(['max_price'], axis=1).drop(['closing_price'], axis=1) \
        .drop(['opening_price'], axis=1).drop(['units_traded'], axis=1).drop(['volume_1day'], axis=1) \
        .drop(['volume_7day'], axis=1).drop(['min_price'], axis=1).drop(["date"], axis=1)

    if(os.path.exists("data.csv")):
        #파일이 있을때 csv파일에 추가합니다.
        print("파일이 있어 기존의 데이터에 추가합니다.")
        p1.to_csv('data.csv',mode='a',header=False,encoding='utf-8',index=False)
    else:
        #파일이 없을때 csv파일을 생성합니다.
        print("파일이 없어 새로운 데이터를 생성합니다.")
        p1.to_csv("data.csv",encoding='utf-8',header=["buy","sell"],index=False)

    #반복 실행
    threading.Timer(second,Cycle,[second]).start()

print("파이썬을 활용한 비트코인 시세구하기 프로그램 입니다.")
num=input("반복될 시간을 정해주세요(초) : ")

if(num.isdigit()):
    Cycle(int(num))
else:
    print("잘못된 값을 입력하여 프로그램을 종료합니다.")
