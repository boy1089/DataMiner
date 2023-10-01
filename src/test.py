import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import glob
import numpy as np
path = r'/Volumes/T7/DataMiner/raw.csv'

plt.interactive(False)


def parseDataFrame( df):
    for j, column in enumerate(df.columns):
        try:
            df[column] = df[column].astype(float)
            continue
        except:
            pass

        try:
            df[column] = pd.to_datetime(df[column])
            print(f'{column} converted to datetime')
            continue
        except:
            pass

    return df


def inferDatetimeColumn( iloc):

    #convert values to datetime
    listOfInferredDatetime = []
    for j in range(len(iloc)):
        inferredDatetime = None
        try :
            inferredDatetime = pd.to_datetime(iloc[j])
        except :
            pass
        listOfInferredDatetime.append(inferredDatetime)
        print(inferredDatetime)
    listOfScore = []
    # scoring the inferred datetimes
    for i, inferredDatetime in enumerate(listOfInferredDatetime):
        score = 0

        if inferredDatetime is pd.NaT:
            listOfScore.append(score)
            continue


        if inferredDatetime.year != 1970:
            score +=1

        if (inferredDatetime.month != 1 ) & (inferredDatetime.day != 1):
            score +=1

        listOfScore.append(score)

    # choose datetime
    selectedColumn = np.argmax(listOfScore)

    return selectedColumn, listOfScore

df = pd.read_csv(path).iloc[:10000, :]

df = parseDataFrame(df)
mainColumn, b = inferDatetimeColumn(df.iloc[0])

print(df.iloc[0])

fig, ax = plt.subplots(4, 4)

for j, column in enumerate(df.columns[:16]):

    ax2 = ax[j % 4][int(j / 4)]
    ax2.plot(df.iloc[:100, mainColumn], df.iloc[:100, j])
    ax2.set_title(column)

plt.show()
print('aa')
