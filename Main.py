import pandas as pd
import numpy as np
dataX,dataY=[],[]

#csv파일에서 읽어와 넘파일 배열로 변환
data=pd.read_csv("data.csv","r",encoding='utf-8',delimiter=",").cummax(axis=0)

print(data)




