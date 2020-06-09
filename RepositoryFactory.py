import sqlite3
import json
import pandas as pd
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
    query = 'SELECT Player.id, Player.player_name, Player.birthday, Player.height, Player.weight, STAT.overall_rating, STAT.potential, STAT.stamina, STAT.crossing, STAT.finishing, STAT.heading_accuracy, STAT.short_passing, STAT.long_passing FROM {0} Player LEFT JOIN {1} STAT ON {0}.{2} = STAT.{2}'.format(Table1, Table2, Key)
    sqlitecur = conn.cursor()
    query_result = sqlitecur.execute(query)

    playerList = playerList = [dict(zip([key[0] for key in sqlitecur.description],row)) for row in query_result]   
    
    dataFrame = pd.DataFrame(playerList).head(10)
    
    return dataFrame