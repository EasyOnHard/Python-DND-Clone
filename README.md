# DnD game in Python

This project aims to recreate the DND game in Python. As of Jan. 13, 2024, this project can create a (heavily simplified) player for DnD. I plan to add a way to create monsters and NPCs, too, though I am still early in development. This is my first Github repo and it is my biggest project so far, so there will be bugs. Please leave reports if you can!

## How to use:
So far, this project is easy to use, and I have an example on how to use it in the main.py. To construct the character generation class, run "test = charGen.charGen(name, class, race)". These all have to be strings and the classes and races are defined in charAssets.json. I am using "test" as a variable, but any valid variable name should work. To apply stats and inventory, use "test.generate()". This should apply the ability scores and inventory. The charGen.generate() function returns a dictionary of the character. To view the character, simpily run "print(test)". The code is short enough to figure it out pretty fast. 

Thank you for reading the Readme! 

## Disclaimer:
This project is a fan made creation and is in no way affiliated with Wizards of the Coast or Dungeons and Dragons. 
Portions of the materials used are property of Wizards of the Coast.
