import random
import string

import time

def generateName():
    seed()
    return (''.join(random.choice(string.ascii_uppercase) for i in range(2)))+str(random.randint(100, 999))


class Robot:
    def __init__(self):
        self.name =  generateName()


    def reset(self):
        self.name = generateName()




seed = "Totally random."

# Initialize RNG using the seed
random.seed(seed)

# Call the generator
robot = Robot()
name = robot.name
print(name)
# Reinitialize RNG using seed
random.seed(seed)

# Call the generator again
robot.reset()
name2 = robot.name
print(name2)
