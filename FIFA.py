#this is the giver of life, alpha and omega, king of kings, our lord and saviour, greatness incarnate
import json
#this imports random numbers
import random

#test to see if git works

#with open means that while the file is open, import players.json as a json file
with open('players.json') as json_file:
    #assigning players as this file
    players = json.load(json_file)

#this is pointless but is the beautified view of the whole json
playersNice = (json.dumps(players, indent=4))

def Filter(playersDict, searchTerm, searchValues):
    """
    Filters the player dict by the passed search terms and values
    args:
        playersDict (dict):  all the player json info
        searchTerm (str):    dict key you want to filter by ("Nation")
        searchValues (list): list of all the search values you want to filter by ([FRA,POR,...])
    returns:
        (dict) filtered dict
    """
    return {key: value for key, value in players.items() if value[searchTerm] in searchValues}

def Playerlist():
    print("")
    #this will iterate through the keys, or sub-dictionaries, of the leading json.
    for i in players.keys():
        print(i)
        #this just works like todd howard
    print("")

#assigning this key list as a variable
playerlist = list(players.keys())
#first player is chosen as a random player from the playerlist
fstplyr = playerlist[random.randint(0,len(playerlist)-1)]

# THIS IS A SHIT WAY HENRY MADE ME DO FUCK fstplyr = list(players.keys())[random.randint(0,len(playerlist))]

#prints first player
print(fstplyr)
#prints the keys within the subdictionary of the first player
print(players[fstplyr])

def NationCheck():
    print("")
    print("please pick a country code")
    codes = """
1. France
2. England
3. Argentina
4. Portugese
5. Other

"""
    AnsNationI = int(input(codes)) - 1
    print("")
    AnsNation = ['FRA','ENG','ARG','POR','OTH']
    AnsNationO = AnsNation[AnsNationI]

    if AnsNationO == "OTH":
        for player,playerstat in players.items():
            if playerstat["Nation"] in AnsNation:
                continue
            else:
                print(player)
    # test = Filter(players, "Nation", ["FRA", "ENG"]) <-- Example use case
    NationCheckFilter = Filter(players, "Nation", AnsNationO)

    for NationCheckFilterPlayers in NationCheckFilter.keys():
        print(NationCheckFilterPlayers)

def PositionCheck():
    Positions = ["LW","ST","RW","CAM","CM"]
    print("")

    for i,PlayerName in enumerate(Positions,1):
        print(str(i)+"."+PlayerName)

    print("please enter the position you wish to sort")
    PositionI = int(input())
    PositionO = Positions[PositionI-1]
    PositionCheckFilter = Filter(players,"Position",[PositionO])
    print("")
    for PositionCheckFilterPlayers in PositionCheckFilter:
        print(PositionCheckFilterPlayers)

def NatPosMultiCheck():
    Positions = ["LW","ST","RW","CAM","CM"]
    AnsNation = ['FRA','ENG','ARG','POR','OTH']

    for i,PlayerName in enumerate(Positions,1):
        print(str(i)+"."+PlayerName)
    PositionO = Positions[int(input())-1]
    for i,PlayerName in enumerate(AnsNation,1):
        print(str(i)+"."+PlayerName)
    AnsNationO = AnsNation[int(input())-1]

    PositionCheckFilter = Filter(players,"Position",[PositionO])
    NationCheckFilter = Filter(players,"Nation",[AnsNationO])
    for CommonPlayer in PositionCheckFilter:
        if CommonPlayer in NationCheckFilter:
            print(CommonPlayer)

def FirstPlayer():
    #assigning this key list as a variable
    playerlist = list(players.keys())
    #first player is chosen as a random player from the playerlist
    fstplyr = playerlist[random.randint(0,len(playerlist)-1)]
    #prints first player
    return fstplyr

def FirstPlayerNationLink():
    fstplyr = FirstPlayer()
    AnotherPlayer = False
    print("the player is "+fstplyr)
    #prints the keys within the subdictionary of the first player
    for PlayerName,ComparePlayerStat in players.items():
        if ComparePlayerStat["Nation"] == players[fstplyr]["Nation"]:
            if ComparePlayerStat == players[fstplyr]:
                continue
            else:
                print(PlayerName)
                AnotherPlayer = True
    if AnotherPlayer == False:
        print("There are no links to this player")

def ManeMultiPos():
    fstplyr = FirstPlayer()
    for PlayerName,ManePosition in players.items():
        if PlayerName == fstplyr:
            print(PlayerName)
            if "CAM" in ManePosition["Position"]:
                print("SUCCESS CAM")
            if "LW" in ManePosition["Position"]:
                print("SUCCESS LW")


def Menu():
    print("""
for playerlist press 1
for Nation Sorter press 2
for Position Sorter press 3
for weird stronk link vibes press 4
for First Player Jazz press 5
for dealing with Mane's shit press 6
""")
    MenuC = input("")
    if MenuC == "1":
        Playerlist()
    if MenuC == "2":
        NationCheck()
    if MenuC == "3":
        PositionCheck()
    if MenuC == "4":
        NatPosMultiCheck()
    if MenuC == "5":
        FirstPlayerNationLink()
    if MenuC == "6":
        ManeMultiPos()

def Maine():
    Menu()

Maine()
