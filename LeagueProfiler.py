import requests
import json
import os

API = os.environ.get('RiotAPI')
KEY = "?api_key=" + API

userInput = input("Enter summoner name: ")

response = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + userInput + KEY)
accJSON = response.json()

id = accJSON['id']
accId = accJSON['accountId']
puuid = accJSON['puuid']
name = accJSON['name']
summonerLevel = accJSON['summonerLevel']

response = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/" + id + KEY)
masteryTotal = response.json()

response = requests.get("https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/" + puuid + KEY)
accJSON = response.json()

tagLine = accJSON['tagLine']

print("")
print("Summoner name: " + userInput)
print("ID: " + id)
print("Account ID: " + accId)
print("puuid: " + puuid)
print("Summoner Level: " + str(summonerLevel))
print("Tag Line: " + tagLine)
print("")

loop = True

while loop:
    print("What would you like to do?")
    print("1. Get list of champion mastery")
    print("2. Get ranked stats")
    print("3. Get TFT ranked stats")
    print("4. Exit")
    print("")

    userInput = input("Enter Option: ")

    if userInput == "1":
        response = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + KEY)

        print(response.json())
        print("")

    elif userInput == "2":
        response = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id + KEY)

        print(response.json())
        print("")

    elif userInput == "3":
        response = requests.get("https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/" + id + KEY)

        print(response.json())
        print("")

    elif userInput == "4":
        loop = False

print("Program end")