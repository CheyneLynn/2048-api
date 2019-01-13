import numpy as np
from keras.layers import Input, concatenate, Dense, Activation, BatchNormalization, Flatten
from keras.layers.convolutional import Conv2D
from keras.models import Model, load_model

import pandas as pd
filePath = '/home/ubuntu/part_256_512.csv'
df = pd.read_csv(filePath)

# 读入数据
X = []  # 棋盘
Y = []  # 决策
decision = [0] * 4             # 存放决策，形式：[0, 0, 0, 0]
for i in range(1, df.shape[0]):
    tmp1 = df.iloc[i, 0:16]               # 每次取一个棋盘（第i行数据）
    tmp2 = np.array(tmp1)                 # 转换成矩阵
    tmp = np.reshape(tmp2, (4, 4))        # 重塑成 4*4
    chessboard = tmp[:, :, np.newaxis]    # 棋盘添加第3维
    decision[df.iloc[i, 16]] = 1          # 形式：[1,0,0,0] [0,1,0,0] ……
    X.append(chessboard)
    Y.append(decision)
    decision = [0] * 4
X_train = np.array(X)   # 转换成numpy可识别的形式
Y_train = np.array(Y)

inputs = Input((4, 4, 1))

conv = inputs
FILTERS = 128
# filters 卷积核的数目，也为输出的维度
# kernel_size 卷积核的大小，m * n
# 激活函数选为 relu
conv41 = Conv2D(filters=FILTERS, kernel_size=(4, 1), kernel_initializer='he_uniform')(conv)
conv14 = Conv2D(filters=FILTERS, kernel_size=(1, 4), kernel_initializer='he_uniform')(conv)
conv22 = Conv2D(filters=FILTERS, kernel_size=(2, 2), kernel_initializer='he_uniform')(conv)
conv33 = Conv2D(filters=FILTERS, kernel_size=(3, 3), kernel_initializer='he_uniform')(conv)
conv44 = Conv2D(filters=FILTERS, kernel_size=(4, 4), kernel_initializer='he_uniform')(conv)
# 加Flatten，数据一维化, 并将多个数组进行连接
hidden = concatenate([Flatten()(conv41), Flatten()(conv14), Flatten()(conv22), Flatten()(conv33), Flatten()(conv44)])
x = BatchNormalization()(hidden)
x = Activation('relu')(hidden)

for width in [512, 128]:
    x = Dense(width, kernel_initializer='he_uniform')(x)   # 全连接层
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
outputs = Dense(4, activation='softmax')(x)    # 概率表示

# model = Model(inputs, outputs)
# model.summary()
# 编译模型
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# 导入模型
model = load_model('/home/ubuntu/model_0_512_1.h5')
# 训练model
model.fit(X_train, Y_train, epochs=80)   # 轮数
# 保存模型
model.save('/home/ubuntu/model_0_512_2.h5')


