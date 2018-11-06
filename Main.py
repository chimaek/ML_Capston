import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from IPython.display import SVG
from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
import matplotlib.pyplot as plt

#10개의 입력데이터를 사용할 것임.
happy=10

#값을 받을 리스트 생성
dataX,dataY=[],[]

#csv파일에서 읽어와 넘파일 배열로 변환
data=pd.read_csv("data.csv","r",encoding='utf-8',delimiter=",").values

# 데이터의 길이를 받아와 길이-10 의 입출력 데이터 생성
for i in range(len(data)-happy):
    dataX.append(data[i:(i+happy)])
    dataY.append(data[i+happy])

#numpy array로 모델훈련에 사용할 수 있도록함.
x_train=np.array(dataX)
y_train=np.array(dataY)

batch_size = 1
inputData = 10 # 입력으로 10개 데이터 사용
feature = 2 # columns값인 "max"와 "min"

#모델 생성
model=Sequential()

#5개 층을 생성합니다.
#1. LSTM(출력: 3*32)
#2. LSTM(출력: 2*32)
#3. LSTM(출력: 1*32)
#4. LSTM(출력: 32)
#5. Dense(출력: 2)

for i in range(3):
    model.add(LSTM(32,batch_input_shape=(batch_size,inputData,feature),stateful=True,return_sequences=True))
    model.add(Dropout(0.1))
model.add(LSTM(32,batch_input_shape=(batch_size,inputData,feature),stateful=True))
model.add(Dropout(0.1))
model.add(Dense(feature))

SVG(model_to_dot(model).create(prog='dot', format='svg'))
plot_model(model, to_file='model.png')

model.compile(loss='mean_squared_error', optimizer='adam')

#모델 훈련
train_count = 5
for i in range(train_count):
    print("train_step:{}".format(i+1))
    model.fit(x_train, y_train, epochs=1, batch_size=1, shuffle=False)
    model.reset_states()

xhat = x_train[0]
prediction = model.predict(np.array([xhat]), batch_size=1)

print("y:", y_train[0])
print("p:", prediction)


plt.plot(y_train)
plt.show()