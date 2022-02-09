import json

players = {}
players["Lionel Messi"] = {} #line 17
players["Cristiano Ronaldo"] = {} #Line 24
players["Kylian Mbappe"] = {} # Line 31
players["Bruno Fernandes"] = {} #line 38
players["Mo Salah"] = {} #Line 45
players["Jude Bellingham"] = {} #line 52
players["Ousmane Dembele"] = {} #Line 59
players["Sadio Mane"] = {} # Line 66
players["Anthony Martial"] = {} # Line 73
players["Harry Kane"] = {} # Line 80
players["Raheem Sterling"] = {} # Line 87
players["Angel Di Maria"] = {} # Line 94
players["Jadon Sancho"] = {} # Line 103
players["Sergio Aguero"] = {} #Line 110

#Messi
players["Lionel Messi"]["Nation"] = "ARG"
players["Lionel Messi"]["League"] = "Ligue 1"
players["Lionel Messi"]["Club"] = "PSG"
players["Lionel Messi"]["Rating"] = 93
players["Lionel Messi"]["Position"] = "RW"

#Ronaldo
players["Cristiano Ronaldo"]["Nation"] = "POR"
players["Cristiano Ronaldo"]["League"] = "Premier League"
players["Cristiano Ronaldo"]["Club"] = "ManU"
players["Cristiano Ronaldo"]["Rating"] = 91
players["Cristiano Ronaldo"]["Position"] = "ST"

#Mbappe
players["Kylian Mbappe"]["Nation"] = "FRA"
players["Kylian Mbappe"]["League"] = "Ligue 1"
players["Kylian Mbappe"]["Club"] = "PSG"
players["Kylian Mbappe"]["Rating"] = 91
players["Kylian Mbappe"]["Position"] = "ST"

#Bruno Fernandes
players["Bruno Fernandes"]["Nation"] = "POR"
players["Bruno Fernandes"]["League"] = "Premier League"
players["Bruno Fernandes"]["Club"] = "ManU"
players["Bruno Fernandes"]["Rating"] = 88
players["Bruno Fernandes"]["Position"] = "CAM"

#Mo Salah
players["Mo Salah"]["Nation"] = "EGY"
players["Mo Salah"]["League"] = "Premier League"
players["Mo Salah"]["Club"] = "Liverpool"
players["Mo Salah"]["Rating"] = [89,91]
players["Mo Salah"]["Position"] = "RW"

#Jude Bellingham
players["Jude Bellingham"]["Nation"] = "ENG"
players["Jude Bellingham"]["League"] = "Bundesliga"
players["Jude Bellingham"]["Club"] = "Borussia Dortmund"
players["Jude Bellingham"]["Rating"] = 79
players["Jude Bellingham"]["Position"] = "CM"

#Ousmane Dembele
players["Ousmane Dembele"]["Nation"] = "FRA"
players["Ousmane Dembele"]["League"] = "LaLiga"
players["Ousmane Dembele"]["Club"] = "Real Madrid"
players["Ousmane Dembele"]["Rating"] = 83
players["Ousmane Dembele"]["Position"] = "RW"

#Sadio Mane
players["Sadio Mane"]["Nation"] = "SEN"
players["Sadio Mane"]["League"] = "Premier League"
players["Sadio Mane"]["Club"] = "Liverpool"
players["Sadio Mane"]["Rating"] = [89,90]
players["Sadio Mane"]["Position"] = ["LW","CAM"]

#Anthony Martial
players["Anthony Martial"]["Nation"] = "FRA"
players["Anthony Martial"]["League"] = "Premier League"
players["Anthony Martial"]["Club"] = "ManU"
players["Anthony Martial"]["Rating"] = 81
players["Anthony Martial"]["Position"] = "ST"

#Harry Kane
players["Harry Kane"]["Nation"] = "ENG"
players["Harry Kane"]["League"] = "Premier League"
players["Harry Kane"]["Club"] = "Tottenham"
players["Harry Kane"]["Rating"] = 88
players["Harry Kane"]["Position"] = "ST"

#Raheem Sterling
players["Raheem Sterling"]["Nation"] = "ENG"
players["Raheem Sterling"]["League"] = "Premier League"
players["Raheem Sterling"]["Club"] = "Man City"
players["Raheem Sterling"]["Rating"] = 88
players["Raheem Sterling"]["Position"] = "LW"

#Di Maria
players["Angel Di Maria"]["Nation"] = "ARG"
players["Angel Di Maria"]["League"] = "Ligue 1"
players["Angel Di Maria"]["Club"] = "PSG"
players["Angel Di Maria"]["Rating"] = 87
players["Angel Di Maria"]["Position"] = "RW"

#Jadon Sancho
players["Jadon Sancho"]["Nation"] = "ENG"
players["Jadon Sancho"]["League"] = "Premier League"
players["Jadon Sancho"]["Club"] = "ManU"
players["Jadon Sancho"]["Rating"] = 87
players["Jadon Sancho"]["Position"] = "RW"

#Sergio Aguero
players["Sergio Aguero"]["Nation"] = "Argentina"
players["Sergio Aguero"]["League"] = "LaLiga"
players["Sergio Aguero"]["Club"] = "Barcelona"
players["Sergio Aguero"]["Rating"] = 89
players["Sergio Aguero"]["Position"] = "ST"

with open('players.json','w') as json_file:
    (json.dump(players, json_file))
