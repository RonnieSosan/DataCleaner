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

#plotLib.demo()
(goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions) = fifaCleaner.GetAllPositions()
arrayOfPositions = [goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions]

fifaData = pd.read_csv(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\fifa_20_data.csv',encoding='utf-8')

defenders = pd.DataFrame(fifaCleaner.getAllPlayersInPosition(defenderPositions, fifaData))
midfield = pd.DataFrame(fifaCleaner.getAllPlayersInPosition(midfielderPositions, fifaData))

defenders = fifaCleaner.convertHeightAndWeight(defenders)
midfield = fifaCleaner.convertHeightAndWeight(midfield)
defenders = fifaCleaner.ConvertMonetaryValue(defenders)
midfield = fifaCleaner.ConvertMonetaryValue(midfield)

defenders = defenders.fillna(defenders)
midfield = midfield.fillna(midfield)

missing_Defender_Data = util.Missing(defenders)
missing_midfielder_Data = util.Missing(midfield)
util.SideSide(missing_Defender_Data, missing_midfielder_Data)
print('Missing Data')

target = 
X_train, X_test, y_train, y_test = dc.Spliting(defenders, 'BP')
RF_Model = RandomForestClassifier(max_features = 'sqrt', max_leaf_nodes = 5)

analysis.ApplyModel(X_train, y_train, RF_Model)

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