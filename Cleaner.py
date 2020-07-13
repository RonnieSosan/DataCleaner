import csv
import pandas as pd

with open(r'C:\Users\sosan\Documents\Dissertation\DataSets\Football Manager.csv',encoding='utf-8') as file:
  with open(r'C:\Users\sosan\Documents\Dissertation\DataSets\Fifa 20\fifa_20_data.csv',encoding='utf-8') as second_file:
    FM_data =  csv.DictReader(file, delimiter=',')
    Fifa_data =  csv.DictReader(second_file, delimiter=',')

    latest_fm_data = []
    for line in FM_data:
        latest_fm_data.append(line)

    basePositions = []

    for row in Fifa_data:
      currentPosition = row["team_position"]

      if currentPosition == '' or currentPosition == 'RES' or currentPosition == 'SUB':
        currentPosition = row["nation_position"]
        
        if currentPosition == '':
          playerPositions = str.split(row["player_positions"], ',')
          currentPosition = playerPositions[0]
      
        

      if currentPosition not in basePositions:
        basePositions.append(currentPosition)

    print(basePositions)


    for row in Fifa_data:
      
      searchResult = []
      indexer = 0

      # get the list of names of the player in this row indexed in a list
      NameIndex = row['long_name'].split(' ')

      #Extract and refprmat date to match FM dataset
      dob = row['dob'].split('-')
      correspondingDatFormat = '{}-{}-{}'.format(dob[2], dob[1], dob[0])


      #STEP2: get the initial search result of the payer
      filteredByClub = [player for player in latest_fm_data if  correspondingDatFormat == player['Born']]
      searchResult = [player for player in filteredByClub if NameIndex[indexer] in player['Name']]

      while len(searchResult) > 1:
        indexer = indexer + 1
        tempResult = [player for player in searchResult if NameIndex[indexer] in player['Name']]

        if len(tempResult) > 0:
          searchResult = tempResult 

        if indexer == (len(searchResult) -1) and len(searchResult) != 0:
          searchResult = [player for player in searchResult if row['age'] == player['Age']]
      
      print()
    