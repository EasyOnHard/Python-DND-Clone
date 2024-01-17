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
    stat_modifiers = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5
    }

    def __init__(self, name, classChosen, raceChosen, level=None):
        self.name = name
        self.classChosen = classChosen
        self.raceChosen = raceChosen
        # self.level = 5
        self.xp = 0
        self.hp = 0
        if level == None:
            self.level = 5
        else:
            self.level = int(level)
    
    def statsRoll(self):
        self.statScores = {stat: roll(20) for stat in self.stats}
 
    def statModifiers(self):
        self.statModifiers = {stat: self.stat_modifiers[value] for stat, value in self.statScores.items()}

    def charGen(self):
        self.classChosenData = next((c for c in classes if c['name'] == self.classChosen), None)
        self.raceChosenData = next((r for r in races if r['name'] == self.raceChosen), None)
        self.raceStat = self.raceChosenData['stat'][0]              # Define racial boosts

        if (self.classChosen is None):                              # Check Class
            print("Invalid Class")
            exit()
        if (self.raceChosen is None):                               # Check Race
            print("Invalid Race")
            exit()
        
        self.statsRoll()
        for stat, boost in self.raceStat.items():                   # Apply racial ability score boosts
            self.statScores[stat] += int(boost)
        for stat in self.statScores:                                # Cap the ability score at 20
            if self.statScores[stat] > 20:
                self.statScores[stat] = 20
        self.statModifiers()

        for x in range(self.level):                                 # Apply Health
            self.hp += roll(int(self.classChosenData['hp'])) + self.statModifiers['Con']
            if self.hp < 5:
                self.hp = 5

        self.inventory = self.classChosenData['starting_inventory'] # Append inventory from charAssets.json

        character = {                                               # Define character
            'class': self.classChosen,
            'race': self.raceChosen,
            'hp': self.hp,
            'level': self.level,
            'xp': self.xp,
            'inventory': self.inventory,
            'stats': self.statScores,
            'modifiers': self.statModifiers
        }
        return character                                            # Return character

    def addItem(self, item):
        return self.inventory.append(item)

    def removeItem(self, item):
        return self.inventory.remove(item)
    
    def __repr__(self):
        return f"charGen({self.name}, {self.classChosen}, {self.raceChosen}, {self.level})\n{self.statScores}"

    def __str__(self):
        return f"Name: {self.name}\nClass: {self.classChosen}\nRace: {self.raceChosen}\nHP: {self.hp}\nLevel: {self.level} ({self.xp})\nItems: {self.inventory} \nStats: {self.statScores}"