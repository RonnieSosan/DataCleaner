import pandas as pd
from datetime import datetime
import csv
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

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

def ConvertMonetaryValue(dataFrame):
    for index,player in dataFrame.iterrows():
        string_Value = player['Value'].replace('€','')
        if 'M' in string_Value:
            value = float(string_Value.replace('M', '')) * 1000000
        
        if 'K' in string_Value:
            value = float(string_Value.replace('K', '')) * 1000000

        dataFrame.loc[index, "Value"] = value

        string_wage = player['Wage'].replace('€','')
        if 'K' in string_wage:
            wage = float(string_wage.replace('K', '')) * 100000
        dataFrame.loc[index, "Wage"] = wage


        string_release_clause = player['Release Clause'].replace('€','')
        if 'M' in string_release_clause:
            release_clause = float(string_release_clause.replace('M', '')) * 1000000
        if 'K' in string_release_clause:
            release_clause = float(string_release_clause.replace('K', '')) * 1000000

        dataFrame.loc[index, "Release Clause"] = release_clause
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

def standardizeValues(dataFrame):
    min_max = MinMaxScaler()
    player = min_max.fit_transform(dataFrame[['Overall', 'Height']])
    return player
