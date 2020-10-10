import sqlite3
import RepositoryFactory as RepoFactory
import Plotter as plotLib
import Analysis as analysis
import pandas as pd
import FifaDataSetCleaner as fifaCleaner
import DataCleaner as dc
import csv
import Utility as util
from sklearn.ensemble import RandomForestClassifier

#specify the file path for the FIFA sataset
filePath = r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\fifa_20_data.csv'

#get all possible playing positions from Fifa dataset
(goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions) = fifaCleaner.GetAllPositions(filePath)
arrayOfPositions = [goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions]


fifaData = pd.read_csv(filePath,encoding='utf-8')

#clean fifa data set convert height, weight and player value
fifaData = fifaCleaner.convertHeightAndWeight(fifaData)
fifaData = fifaCleaner.ConvertMonetaryValue(fifaData)

#save datasets into current file location.
for position in arrayOfPositions:
    players = fifaCleaner.getAllPlayersInPosition(position, fifaData)
    playerDataFrame = pd.DataFrame(players)
    print(playerDataFrame.info)
    analysis.CorrelationMatrix('Overall', playerDataFrame)

    index = arrayOfPositions.index(position)
    if index == 0:
        fileName = 'GoalKeepers'
    elif index == 1:
        fileName = 'Defenders'
    elif index == 2:
        fileName = 'Midfielders'
    elif index == 3:
        fileName = 'Strikers'

    #save players in csv file
    playerDataFrame.to_csv(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\TransformedData\{0}.csv'.format(fileName), index = False)

    # fittedData = fifaCleaner.standardizeValues(playerDataFrame)
    # print(fittedData)
print("done!!")