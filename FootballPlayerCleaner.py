import sqlite3
import RepositoryFactory as RepoFactory
import Plotter as plotLib
import Analysis as analysis

#plotLib.demo()
dbLocation = r'c:\Users\sosan\Documents\Dissertation\DataSets\Season 16-18\database.sqlite'
conn = RepoFactory.create_connection(dbLocation)
print(conn)
#RepoFactory.select_all(conn,'Lionel Messi')
player_DF = RepoFactory.LeftJoin(conn, 'Player', 'Player_Attributes', 'player_api_id')
analysis.CorrelationMatrix('overall_rating', player_DF)
plotLib.Plot_Radar(player_DF)
plotLib.plot_Correlation(player_DF)
print("done!!")