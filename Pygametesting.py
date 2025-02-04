import pygame
import random as R
import json
from pytimedinput import timedInput
#
pygame.init()

#Pygame Variables
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#Game Variables
codelist = ["ijklijki"]
code = R.choice(codelist)
arrowlist = []
correct = 0
global n
n = len(code)
codeswitch = True

#Centering formulas
if  n%2 == 1:
    x = 384 - 50*int(n/2 - 0.1)
else:
    x = 384 - 50*(n/2) + 25

#Image Lists
for i in range(4):
    arrowlist.append(pygame.transform.rotate(pygame.image.load("StratagemHeroImages/Arrow.png"), 90*i))
for i in range(4):
    arrowlist.append(pygame.transform.rotate(pygame.image.load("StratagemHeroImages/CompleteArrow.png"), 90*i))

#Json File stuff
with open('stratdict.json') as f:
    stratDict = json.load(f)
    Boo = False
    GenList = ["Backpack", "Weapons", "Weapons", "Eagles", "Exosuits", "Mission", "Defensive", "Defensive", "Orbital", "Orbital"]

    BackKeys = list(stratDict["Backpack"].keys())
    BackVal = list(stratDict["Backpack"].values())

    WeaponKeys = list(stratDict["Weapons"].keys())
    WeaponVal = list(stratDict["Weapons"].values())

    EagleKeys = list(stratDict["Eagles"].keys())
    EagleVal = list(stratDict["Eagles"].values())

    ExoKeys = list(stratDict["Exosuits"].keys())
    ExoVal = list(stratDict["Exosuits"].values())

    MissionKeys = list(stratDict["Mission"].keys())
    MissionVal = list(stratDict["Mission"].values())

    DefensiveKeys = list(stratDict["Defensive"].keys())
    DefensiveVal = list(stratDict["Defensive"].values())

    OrbitalKeys = list(stratDict["Orbital"].keys())
    OrbitalVal = list(stratDict["Orbital"].values())

    GenCodeList = [BackVal, WeaponVal, WeaponVal, EagleVal, ExoVal, MissionVal, DefensiveVal, DefensiveVal, OrbitalVal, OrbitalVal]
    GenKeyList = [BackKeys, WeaponKeys, WeaponKeys, EagleKeys, ExoKeys, MissionKeys, DefensiveKeys, DefensiveKeys, OrbitalKeys, OrbitalKeys]

    while running:

        #Event Handling
        if pygame.event.get(pygame.QUIT):
            running = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #Key press detection
                if event.key == pygame.K_j and list(code)[correct] == "j":
                    correct += 1
                if event.key == pygame.K_i and list(code)[correct] == "i":
                    correct += 1
                if event.key == pygame.K_l and list(code)[correct] == "l":
                    correct += 1
                if event.key == pygame.K_k and list(code)[correct] == "k":
                    correct += 1
                else:
                    pass
        
        if codeswitch == True:
            # typeIndex is the index for type of stratagems
            typeIndex = R.randrange(len(GenList))
            # randValList chooses a random Val List, (GenCodeList IS A LIST OF LISTS)
            randValList = GenCodeList[typeIndex]   
            # index that stays the same for Strat Names and Codes
            GenIndex = R.randrange(len(randValList))
            # code needs to choose a string of ilkj's. TempList chooses the code from a random Val List and random Index, outputting the string
            code = list(randValList[GenIndex])
            codeswitch = False
            n = len(code)

        screen.fill((10, 10, 10))

        #Arrow direction deciding
        for i in range(n):
            if list(code)[i] == "l":
                index = 0
            if list(code)[i] == "i":
                index = 1
            if list(code)[i] == "j":
                index = 2
            if list(code)[i] == "k":
                index = 3
            screen.blit(arrowlist[index], (x, 400))
        #Arrow completion
            if correct >= i+1:
                screen.blit(arrowlist[index+4], (x, 400))
            
        #Centering
            x += 50
        if  n%2 == 1:
            x = 384 - 50*int(n/2 - 0.1)
        else:
            x = 384 - 50*(n/2) + 25

        #Center line(Remove later)
        pygame.draw.line(surface=screen, color="white", start_pos=(400, 0), end_pos=(400, 600))

        pygame.display.flip()
        if correct == n:
            pygame.time.delay(100)
            codeswitch = True
            correct = 0
        clock.tick(60)