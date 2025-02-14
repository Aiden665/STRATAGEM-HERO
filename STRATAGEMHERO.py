import pygame
import random as R
import json
from pytimedinput import timedInput

pygame.init()
pygame.font.init()

#Pygame Variables
screen = pygame.display.set_mode((1500, 800))
clock = pygame.time.Clock()
hd2Font = pygame.font.Font("Fonts/AmericanCaptain-MdEY.otf", 60)
title = pygame.image.load("StratagemHeroImages/TitleCard.png")
running = True
PixelArrayList = []
timerBarEvent = pygame.USEREVENT + 1

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
difficulty = 2
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
                barWidth -= difficulty
        
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
                    pygame.event.set_allowed(pygame.KEYDOWN)
        #Arrow Unlocking after Color Replacing
            PixelArrayList = []
            arrowlist[index].unlock()
            screen.blit(arrowlist[index], (x, 500))
        #Arrow completion
            if correct >= i+1:
                screen.blit(arrowlist[index+4], (x, 500))
            x += 50

        #Bar Rendering
        pygame.draw.rect(surface=screen, color=(255, 255, 255), rect=pygame.Rect((screen.get_width()/2)-(barWidth/2), 550, barWidth, 10))
        #Font Rendering
        StratIndicator = hd2Font.render(f"{GenKeyList[typeIndex][GenIndex]}", True, (200, 160, 10))
        screen.blit(StratIndicator, (400, 400))
        #TitleCard Rendering
        screen.blit(title, (((screen.get_width()-title.get_width())/2), 50))
        #STRATAGEM_ICON rendering
        strat_Name = GenKeyList[typeIndex][GenIndex].replace(' ', '_')
        try:
            screen.blit(pygame.image.load(f"StratagemIcons/{strat_Name}_Icon.png"), (100, 100))
        except:
            pass
        #Centering
        if  n%2 == 1:
            x = (((screen.get_width())/2)-16) - 50*int(n/2 - 0.1)
        else:
            x = (((screen.get_width())/2)-16) - 50*(n/2) + 25

        #Lose condition
        if barWidth <= 0:
            screen.blit("EndScreen")
        pygame.display.flip()
        if correct == n:
            pygame.time.delay(100)
            codeswitch = True
            correct = 0
        clock.tick(60)