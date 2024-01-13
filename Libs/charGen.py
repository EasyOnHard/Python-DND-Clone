from die import roll
import json
from os import path

jsonPath = path.dirname(path.abspath(__file__)) + "\\Assets\\charAssets.json"

with open(jsonPath, 'r') as file:
    jsonData = json.load(file)
    classes = jsonData['classes']
    races = jsonData['races']

class charGen:

    stats = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']

    def __init__(self, name, classChosen, raceChosen):
        self.name = name
        self.classChosen = classChosen
        self.raceChosen = raceChosen
        self.level = 0
        self.xp = 0

    def charGen(self):
        self.statScores = {stat: roll(20) for stat in self.stats}
        self.classChosenData = next((c for c in classes if c['name'] == self.classChosen), None)
        self.raceChosenData = next((r for r in races if r['name'] == self.raceChosen), None)
        self.raceStat = self.raceChosenData['stat'][0]              # Define racial boosts

        if (self.classChosen is None):                              # Check Class
            print("Invalid Class")
            exit()
        if (self.raceChosen is None):                               # Check Race
            print("Invalid Race")
            exit()
        
        self.inventory = self.classChosenData['starting_inventory'] # Append inventory from charAssets.json

        for stat, boost in self.raceStat.items():                   # Apply racial ability score boosts
            self.statScores[stat] += int(boost)
        
        for stat in self.statScores:                                # Cap the ability score at 20
            if self.statScores[stat] > 20:
                self.statScores[stat] = 20

        character = {                                               # Define character
            'class': self.classChosen,
            'race': self.raceChosen,
            'inventory': self.inventory,
            'stats': self.statScores
        }
        return character                                            # Return character

    def addItem(self, item):
        return self.inventory.append(item)

    def removeItem(self, item):
        return self.inventory.remove(item)
    
    def __repr__(self):
        return f"charGen({self.name}, {self.classChosen}, {self.raceChosen})\n{self.statScores}"

    def __str__(self):
        return f"Name: {self.name}\nClass: {self.classChosen}\nRace: {self.raceChosen}\nLevel: {self.level} ({self.xp})\nItems: {self.inventory} \nStats: {self.statScores}"