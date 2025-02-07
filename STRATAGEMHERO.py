import pygame
import random as R
import json
from pytimedinput import timedInput

pygame.init()
pygame.font.init()

#Pygame Variables
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
hd2Font = pygame.font.Font("Fonts/AmericanCaptain-MdEY.otf", 60)
running = True
PixelArrayList = []
timerBarEvent = pygame.USEREVENT + 1
difficultyEvent = pygame.USEREVENT + 2

pygame.time.set_timer(timerBarEvent, 20)

#Game Variables
codelist = ["ijklijki"]
code = R.choice(codelist)
arrowlist = []
correct = 0
n = len(code)
codeswitch = True
color1 = pygame.color.Color(102, 102, 102)
color2 = pygame.color.Color(200, 80, 80)
colorswitch = False
barWidth = 500
difficulty = 1
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

    BackKeys = list(stratDict["Backpacks"].keys())
    BackVal = list(stratDict["Backpacks"].values())

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
                elif event.key == pygame.K_i and list(code)[correct] == "i":
                    correct += 1
                elif event.key == pygame.K_l and list(code)[correct] == "l":
                    correct += 1
                elif event.key == pygame.K_k and list(code)[correct] == "k":
                    correct += 1
                else:
                    correct = 0
                    for i in range(n):
                        PixelArrayList.append(pygame.PixelArray(arrowlist[i]))
                        if PixelArrayList[i] != None:
                            PixelArrayList[i].replace(color1, color2)
                    colorswitch = True
                    startTime = pygame.time.get_ticks()
            
            if event.type == timerBarEvent:
                barWidth -= (1 + (difficulty))
            if event.type == difficultyEvent:
                difficulty += 1000000
            print(event.type)
        
        if codeswitch == True:
            # typeIndex is the index for type of stratagems
            typeIndex = R.randrange(len(GenList))
            # randValList chooses a random Val List, (GenCodeList IS A LIST OF LISTS)
            randValList = GenCodeList[typeIndex]   
            # index that stays the same for Strat Names and Codes
            GenIndex = R.randrange(len(randValList))
            # code needs to choose a string of ilkj's. TempList chooses the code from a random Val List and random Index, outputting the string
            code = list(randValList[GenIndex])
            
            #Bar Reset
            if barWidth >= 400:
                barWidth += 500 - barWidth
            else:
                barWidth += 100
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
        #Error Color Reset
            if colorswitch:
                pygame.event.set_blocked(pygame.KEYDOWN)
                if pygame.time.get_ticks() - startTime > 800:
                    for i in range(n):
                            PixelArrayList.append(pygame.PixelArray(arrowlist[i]))
                            if PixelArrayList[i] != None:
                                PixelArrayList[i].replace(color2, color1)
                    colorswitch = False
                    pygame.event.post(pygame.event.Event(difficultyEvent))
                    pygame.event.set_allowed(pygame.KEYDOWN)
        #Arrow Unlocking after Color Replacing
            PixelArrayList = []
            arrowlist[index].unlock()
            screen.blit(arrowlist[index], (x, 400))
        #Arrow completion
            if correct >= i+1:
                screen.blit(arrowlist[index+4], (x, 400))
            x += 50

        #Color of Text corresponding to type of Stratagem
        if str(GenList[typeIndex]) == "Backpacks": #Blue
            StratColor = (20, 150, 150)
        if str(GenList[typeIndex]) == "Weapons": #Blue
            StratColor = (20, 150, 150)
        if str(GenList[typeIndex]) == "Eagles": #Red
            StratColor = (180, 30, 30)
        if str(GenList[typeIndex]) == "Exosuits": #Blue
            StratColor = (20, 150, 150)
        if str(GenList[typeIndex]) == "Mission": #Light Yellow
            StratColor = (200, 200, 80)
        if str(GenList[typeIndex]) == "Defensive": #Green
            StratColor = (25, 75, 25)
        if str(GenList[typeIndex]) == "Orbital": #Red
            StratColor = (180, 30, 30)

        #Bar Rendering
        pygame.draw.rect(surface=screen, color=(255, 255, 255), rect=pygame.Rect(400-(barWidth/2), 350, barWidth, 10))

        #Font Rendering
        pygame.time.delay(20)
        StratIndicator = hd2Font.render(f"{GenKeyList[typeIndex][GenIndex]}", True, StratColor)
        screen.blit(StratIndicator, (100, 100))

        #Centering
        if  n%2 == 1:
            x = 384 - 50*int(n/2 - 0.1)
        else:
            x = 384 - 50*(n/2) + 25

        pygame.display.flip()
        if correct == n:
            pygame.time.delay(100)
            codeswitch = True
            correct = 0
        clock.tick(60)