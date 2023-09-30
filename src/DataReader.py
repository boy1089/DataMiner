import pandas as pd
import numpy as np


def inferDatetimeColumn(iloc):

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


path = r'/Volumes/T7/auto diary/data/processedData/raw.csv'
df = pd.read_csv(path)

print(df.iloc[0][0])

a, b = inferDatetimeColumn(df.iloc[0])
# find datetime
# if there is datetime, plot all columns with datetime
# if there is no datetime,


if __name__ == '__main__':
    df = pd.read_csv(path)
    print(df)

