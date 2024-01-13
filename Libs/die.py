import sys
import random

def roll(sides):
    return random.randint(1, sides)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python die.py <number_of_sides>")
    else:
        sides = int(sys.argv[1])
        result = roll(sides)
        print(f"The result of rolling a d{sides} is: {result}")