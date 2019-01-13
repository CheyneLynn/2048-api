import pandas as pd
import os

location = 'E:/PyCharm 2018.2.4/2048_game/dataLibrary/data0'
SaveTo = 'E:/PyCharm 2018.2.4/2048_game/dataLibrary'
SaveAs = 'part_256_512.csv'
os.chdir(location)

thre1 = 8  # 256
thre2 = 9  # 512
fileList = os.listdir()
for i in range(0, len(fileList)):
    toDrop = []   # 存放要丢弃的棋盘
    df = pd.read_csv(location + '/' + fileList[i], header=None)
    for j in range(0, df.shape[0]):
        if max(df.iloc[j, 0:16]) > thre2 or max(df.iloc[j, 0:16]) < thre1:   # 去除 [thre1,thre2] 范围外的
            toDrop.append(j)
        # if max(df.iloc[j, 0:16]) > thre1:  # 去除256以上的
        #    list.append(j)
    df.drop(toDrop, inplace=True)    # 去除以上棋盘
    df.to_csv(SaveTo+'/' + SaveAs, encoding="utf_8_sig", index=False, header=False, mode='a+')
