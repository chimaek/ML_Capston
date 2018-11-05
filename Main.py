import pandas as pd
import numpy as np
dataX,dataY=[],[]

#csv파일에서 읽어와 빈값을 지우고 배열로 변환시킴문자열을 숫자로
data=pd.read_csv("data.csv","w",encoding='utf-8').dropna(axis=1,how='any')
print(data)




