import sqlite3
import RepositoryFactory as RepoFactory
import Plotter as plotLib
import Analysis as analysis
import pandas as pd
import FifaDataSetCleaner as fifaCleaner
import csv

#plotLib.demo()
(goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions) = fifaCleaner.GetAllPositions()
fifaData = pd.read_csv(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\fifa_20_data.csv',encoding='utf-8')
fifaData = fifaCleaner.convertHeightAndWeight(fifaData)

fifaData = fifaCleaner.ConvertMonetaryValue(fifaData)

arrayOfPositions = [goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions]

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