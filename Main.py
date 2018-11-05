import pandas as pd
import numpy as np
dataX,dataY=[],[]

#csv파일에서 읽어와 넘파일 배열로 변환
getData=pd.read_csv("data.csv","r",encoding='utf-8')
min_data=getData.min(axis=0).low


print(min_data)




