import sqlite3
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

def select_all(conn, player_name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return: DataFrame
    """
    query = 'SELECT * FROM Player'
     
    sqlitecur = conn.cursor()
    query_result = sqlitecur.execute(query)
    
    playerList = [dict(zip([key[0] for key in sqlitecur.description],row)) for row in query_result]
    playerList['Position'] = []
    
    jsonList = json.dumps(playerList)

    return playerList
    

def LeftJoin(conn, Table1, Table2, Key):
    """
    To perform left join between Table1 and Table2 with Key
    :param conn: the Connection object
    :param Table1: Left table 
    :param Table2: Rght table
    :Key: ID for table join
    :return: Dataframe
    """

    with sqlite3.connect(r'c:\Users\sosan\Documents\Dissertation\DataSets\Season 16-18\database.sqlite') as con:
        player = pd.read_sql_query("SELECT * from Player",con)
        attributes = pd.read_sql_query("SELECT * from Player_Attributes",con)

        player_attributes = player.merge(attributes,left_on="player_api_id",right_on="player_api_id",how="outer")
        player_attributes = player_attributes.drop("player_fifa_api_id_y",axis = 1)
        player_attributes = player_attributes.drop("id_y",axis = 1)
        player_attributes = player_attributes.rename(columns={'id_x':"id", 'player_fifa_api_id_x':"player_api_id"})
        print(player_attributes.head())
       
    query = 'SELECT * FROM {0} Player LEFT JOIN {1} STAT ON {0}.{2} = STAT.{2} Where STAT.overall_rating >= 85'.format(Table1, Table2, Key)
    sqlitecur = conn.cursor()
    query_result = sqlitecur.execute(query)

    playerList = [dict(zip([key[0] for key in sqlitecur.description],row)) for row in query_result]   
    
    dataFrame = pd.DataFrame(playerList)
    dataFrame['Position'] = np.nan
    
    return dataFrame