import pandas as pd
import os

location = 'E:/PyCharm 2018.2.4/2048_game/dataLibrary/data'
SaveAs = 'small_256_512.csv'
os.chdir(location)

fileList = os.listdir()
for i in range(0, len(fileList)):
    toDrop = []   # 存放要丢弃的棋盘
    df = pd.read_csv(location + '/' + fileList[i], header=None)
    for j in range(0, df.shape[0]-400000):
        toDrop.append(j)
    df.drop(toDrop, inplace=True)    # 去除以上棋盘
    df.to_csv(location + '/' + SaveAs, encoding="utf_8_sig", index=False, header=False, mode='a+')
