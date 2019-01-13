import pandas as pd
import os

location = 'E:/PyCharm 2018.2.4/2048_game/dataLibrary/data'
SaveAs = 'small_0_512.csv'
os.chdir(location)

fileList = os.listdir()
for i in range(0, len(fileList)):
    df = pd.read_csv(location + '/' + fileList[i], header=None)
    df.to_csv(location + '/' + SaveAs, encoding="utf_8_sig", index=False, header=False, mode='a+')
