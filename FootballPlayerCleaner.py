import sqlite3
import RepositoryFactory as RepoFactory
import Plotter as plotLib
import Analysis as analysis
Cleaning the fifaCimport pandas as pd
import DataCleaner as dc
import csv

#plotLib.demo()

(goalkeepersPositions, defenderPositions, midfielderPositions, fowardPositions) = dc.GetAllPositions()
data = pd.read_csv(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\fifa_20_data.csv',encoding='utf-8')
data = dc.convertHeightAndWeight(data)

defenders = dc.getAllPlayersInPosition(defenderPositions, data)

defendersDataFrame = pd.DataFrame(defenders)
print(defendersDataFrame.info)
analysis.CorrelationMatrix('Overall', defendersDataFrame)

dbLocation = r'c:\Users\sosan\Documents\Dissertation\DataSets\Season 16-18\database.sqlite'
conn = RepoFactory.create_connection(dbLocation)
print(conn)
#RepoFactory.select_all(conn,'Lionel Messi')
player_DF = RepoFactory.LeftJoin(conn, 'Player', 'Player_Attributes', 'player_api_id')
dataFrame = dc.Spliting(player_DF)
dc.Merging(dataFrame)

#player_DF.to_csv(r'c:\Users\sosan\Documents\Dissertation\DataSets\Season 16-18\Test_Data.csv')

analysis.CorrelationMatrix('Overall', player_DF)
plotLib.Plot_Radar(player_DF)
plotLib.plot_Correlation(player_DF)
print("done!!")