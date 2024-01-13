# +-----------------------+ #
# |    DND Alpha Build    | #
# |  By Xander Iwanowicz  | #
# +-----------------------+ #

import sys
import random
################
sys.path.insert(0, 'Libs')
from die import roll
import charGen

test = charGen.charGen("Test", "Rouge", "Elf")
test.charGen()

print(test)
