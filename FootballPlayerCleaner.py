import sqlite3
import RepositoryFactory as RepoFactory
import Plotter as plotLib

#plotLib.demo()
dbLocation = r'c:\Users\sosan\Documents\Dissertation\DataSets\database.sqlite'
conn = RepoFactory.create_connection(dbLocation)
print(conn)
#RepoFactory.select_all(conn,'Lionel Messi')
player_DF = RepoFactory.LeftJoin(conn, 'Player', 'Player_Attributes', 'player_api_id')
plotLib.Plot_Radar(player_DF)
plotLib.plot_Correlation(player_DF)
print("done!!")