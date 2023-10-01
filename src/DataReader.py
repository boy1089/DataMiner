import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataManager():

    def __init__(self):
        self.df = None

    def readData(self, path):
        self.df = self.readCsv(path).iloc[:1000, :]
        self.df = self.parseDataFrame(self.df)
        self.mainColumn, _ = self.inferDatetimeColumn(self.df.iloc[0])



    def readCsv(self, path):
        df = pd.read_csv(path)

        return df

    def inferDatetimeColumn(self, iloc):

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

    def parseDataFrame(self, df):
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




# find datetime
# if there is datetime, plot all columns with datetime
# if there is no datetime,
# parsing the texts to float / datetime


