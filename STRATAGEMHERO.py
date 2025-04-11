import pygame
import random as R
import json
from pytimedinput import timedInput

pygame.init()
pygame.font.init()

#Pygame Variables
screen = pygame.display.set_mode((800, 800))
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
    
    GenKEYList = list(stratDict.keys())
    GenVALList = list(stratDict.values())
    


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
            
            typeIndex = R.randrange(len(GenKEYList))
            print(GenKEYList[typeIndex])
            code = GenVALList[typeIndex]
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
        StratIndicator = hd2Font.render(f"{GenKEYList[typeIndex]}", True, (200, 160, 10))
        screen.blit(StratIndicator, ((screen.get_width()-StratIndicator.get_width())/2, 400))
        #TitleCard Rendering
        screen.blit(title, (((screen.get_width()-title.get_width())/2), 50))
        #STRATAGEM_ICON rendering
        strat_Name = GenKEYList[typeIndex].replace(' ', '_')
        try:
            screen.blit(pygame.image.load(f"StratagemIcons/{strat_Name}_Icon.png"), (((screen.get_width())-(44))/2, 600))
        except:
            print(f"StratagemIcons/{strat_Name}_Icon.png")
        #Centering
        if  n%2 == 1:
            x = (((screen.get_width())/2)-16) - 50*int(n/2 - 0.1)
        else:
            x = (((screen.get_width())/2)-16) - 50*(n/2) + 25

        #Lose condition
        if barWidth <= 0:
            running=False
        pygame.display.flip()
        if correct == n:
            pygame.time.delay(100)
            codeswitch = True
            correct = 0
        clock.tick(60)