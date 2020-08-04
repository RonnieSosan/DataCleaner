import pandas as pd
from datetime import datetime
import csv
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# def Spliting(DataFrame):
#     twent_Eighteen = pd.DataFrame()
#     DataFrame['birthday'] = pd.to_datetime(DataFrame['birthday'])
#     DataFrame['date'] = pd.to_datetime(DataFrame['date'])
    
#     DataFrame = DataFrame[(DataFrame['date'].dt.year == 2016) &  (DataFrame['overall_rating'] >= 85)]
#     #with open(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 17\players_17.csv',encoding='utf-8') as second_file:
#     #    Fifa_data =  csv.DictReader(second_file, delimiter=',')
        
#     # for index, row in DataFrame.iterrows():
#     #     if row['overall_rating'] >= 85:
#     #         if row['date'].year == 2016:
#     #             print("{0} {1} {2}".format(index, row['player_name'], row['overall_rating']))
#     #             twent_Eighteen.append(row, ignore_index=False)
#     # twent_Eighteen = [player for player in DataFrame if player['overall_rating'] >= 85]
#     # print(twent_Eighteen)
#     return DataFrame

def Spliting(dataFrame, Target):
    X_train, X_test, y_train, y_test = train_test_split(dataFrame, Target, test_size=0.2)
    print (X_train.shape, y_train.shape)
    print (X_test.shape, y_test.shape)
    return(X_train, X_test, y_train, y_test)

def convertHeightAndWeight(dataFrame):

    for index,player in dataFrame.iterrows():
        height = str.split(player["Height"], "'")

        height_in_feet = (int(height[0]) * 12) + int(height[1].replace('"',''))
        height_in_cm = round(height_in_feet * 2.54, 1)

        dataFrame.loc[index, "Height"] = height_in_cm

        kilogram = round(int(player["Weight"].replace('lbs', '')) / 2.2,1)
        dataFrame.loc[index, "Weight"] = kilogram
        
    pd.to_numeric(dataFrame["Height"])
    pd.to_numeric(dataFrame["Weight"])
    return dataFrame

def GetAllPositions():
    with open(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\fifa_20_data.csv',encoding='utf-8') as second_file:
        Fifa_data =  csv.DictReader(second_file, delimiter=',')
        
        basePositions = []
        defenders = []
        midfielders = []
        fowards = []
        goalkeepers = []

        for row in Fifa_data:
            currentPosition = row["BP"]
            
            if currentPosition == '' or currentPosition == 'RES' or currentPosition == 'SUB':
                playerPositions = str.split(row["Position"], ',')
                currentPosition = playerPositions[0]
                   
                    
            if currentPosition not in basePositions:
                basePositions.append(currentPosition)
        
        for position in basePositions:
            if 'K' in position:
                goalkeepers.append(position)
            
            elif 'B' in position:
                defenders.append(position)
            
            elif 'M' in position:
                midfielders.append(position)
            
            elif 'F' in position or 'S' in position:
                fowards.append(position)
        
        return (goalkeepers, defenders, midfielders, fowards)

def getAllPlayersInPosition(arrayOfPosition, PlayerPool):
    players = []
    for index,player in PlayerPool.iterrows():
        currentPosition = player["BP"]
            
        if currentPosition == '' or currentPosition == 'RES' or currentPosition == 'SUB':
            playerPositions = str.split(player["Position"], ',')
            currentPosition = playerPositions[0]

        if  currentPosition in arrayOfPosition:
            players.append(player)
    
    return players

def Merging(DataFrame):
    labelledPlayers = DataFrame
    Fifa_data =  pd.read_csv(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 17\players_17.csv', )
    Fifa_data['dob'] = pd.to_datetime(Fifa_data['dob'])

    for index, row in DataFrame.iterrows():
        playerName = row['player_name'].split()

        #search by date of birth and firstname
        searchResult = Fifa_data[(Fifa_data['dob'].dt.year == row['birthday'].year) & (Fifa_data['dob'].dt.month == row['birthday'].month) & (Fifa_data['dob'].dt.day == row['birthday'].day)]
        if searchResult.empty == True:
            continue

        if searchResult.size > 1:
            searchResultTwo = searchResult[(searchResult['long_name'].str.contains(playerName[0]))]
            
            if searchResultTwo.empty == True:
                searchResultThree = searchResultTwo[(searchResult['long_name'].str.contains(playerName[1]))]
                
                if searchResultThree.empty == True:
                    searchResultThree = searchResultTwo[(searchResult['long_name'].str.contains(playerName[2]))]

        position = searchResult.iloc[0].team_position
        labelledPlayers.loc[index, 'position'] = position
    return labelledPlayers