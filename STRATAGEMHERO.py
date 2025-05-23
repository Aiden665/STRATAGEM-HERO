import pygame
import random as R
import json
from pytimedinput import timedInput
import time

pygame.init()
pygame.font.init()

#Pygame Variables
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
hd2Font = pygame.font.Font("/Users/za9019476/Documents/GitHub/STRATAGEM-HERO/Fonts/Swiss 721 Extended Bold.otf", 30)
title = pygame.image.load("StratagemHeroImages/TitleCard.png")
running = True
PixelArrayList = []
timerBarEvent = pygame.USEREVENT + 1

pygame.time.set_timer(timerBarEvent, 20)

#Game Variables
codelist = ["ijklijki"]
code = ""
arrowlist = []
correct = 0
n = 0
codeswitch = True
color1 = pygame.color.Color(102, 102, 102)
color2 = pygame.color.Color(200, 80, 80)
barWidth = 500
strataQue = []
round = 1
colorswitch = False
score = 0

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
            if event.type == pygame.KEYDOWN and len(strataQue) > 0:
                #Key press detection
                if (event.key == pygame.K_j or event.key == pygame.K_a or event.key == pygame.K_LEFT) and list(strataQue[0][0])[correct] == "j":
                    correct += 1
                elif (event.key == pygame.K_i or event.key == pygame.K_w or event.key == pygame.K_UP) and list(strataQue[0][0])[correct] == "i":
                    correct += 1
                elif (event.key == pygame.K_l or event.key == pygame.K_d or event.key == pygame.K_RIGHT) and list(strataQue[0][0])[correct] == "l":
                    correct += 1
                elif (event.key == pygame.K_k or event.key == pygame.K_s or event.key == pygame.K_DOWN) and list(strataQue[0][0])[correct] == "k":
                    correct += 1
                else:
                    correct = 0
                    for i in range(n):
                        PixelArrayList.append(pygame.PixelArray(arrowlist[i]))
                        if PixelArrayList[i] != None:
                            PixelArrayList[i].replace(color1, color2)
                    colorswitch = True
                    startTime = pygame.time.get_ticks()
        
        if codeswitch == True:
            #Bar Reset
            if barWidth <= 500:
                barWidth = 500
            
            while len(strataQue) < 5 + round:
                #Initial Stratagem Que Creation
                typeIndex = R.randrange(len(GenKEYList))
                code = GenVALList[typeIndex], GenKEYList[typeIndex]
                if code not in strataQue:
                    strataQue.append(code)
                    
            codeswitch = False

        if event.type == timerBarEvent:
                barWidth -= 1.5 + (round)/5
        screen.fill((10, 10, 20))

        #Arrow direction deciding
        if len(strataQue) > 0:
            n = len(strataQue[0][0])
            for i in range(n):
                if list(strataQue[0][0])[i] == "l":
                    index = 0
                if list(strataQue[0][0])[i] == "i":
                    index = 1
                if list(strataQue[0][0])[i] == "j":
                    index = 2
                if list(strataQue[0][0])[i] == "k":
                    index = 3
            #Error Color Reset
                if colorswitch:
                    pygame.event.set_blocked(pygame.KEYDOWN)
                    if pygame.time.get_ticks() - startTime > 600:
                        for i in range(n):
                                PixelArrayList.append(pygame.PixelArray(arrowlist[i])) 
                                if PixelArrayList[i] != None:
                                    PixelArrayList[i].replace(color2, color1) #9 indents baby
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
        pygame.draw.rect(surface=screen, color=(255, 231, 16), rect=pygame.Rect((screen.get_width()/2)-(barWidth/2), 550, barWidth, 10))

        #Font Rendering
        if len(strataQue) > 0:
            StratIndicator = hd2Font.render(f"{strataQue[0][1]}", True, (0, 0, 0))
        pygame.draw.rect(surface=screen, color=(255, 231, 16), rect=pygame.Rect((screen.get_width()/2) - 270, 450, 540, 34))
        screen.blit(StratIndicator, ((screen.get_width()-StratIndicator.get_width())/2, 450))
        #TitleCard Rendering
        screen.blit(title, (((screen.get_width()-title.get_width())/2), 120))
    
        #STRATAGEM_ICON rendering
        pygame.draw.rect(screen, (240, 240, 10), (screen.get_width()/2-22 - 100, 400, 44, 44), 2)
        for i in range(5):
            try:
                screen.blit(pygame.transform.scale(pygame.image.load(f"StratagemIcons/{strataQue[i][1].replace(' ', '_')}_Icon.png"), (45,45)), ((((screen.get_width())-(44))/2)- 100 + 50*i, 400))
            except:
                pass
       
        #Score Rendering
        screen.blit(pygame.font.Font("Fonts/Swiss 721 Extended Bold.otf", 20).render(f"Score: {score}", True, (255, 255, 255)), (550, 400))
        
        #Round Rendering
        screen.blit(pygame.font.Font("Fonts/Swiss 721 Extended Bold.otf", 20).render(f"Round: {round}", True, (255, 255, 255)), (150, 400))

        #Extra Decoration Rendering
        pygame.draw.rect(surface=screen, color=(250, 250, 250), rect=pygame.Rect((screen.get_width()/2) - 270, 580, 540, 5))    
        pygame.draw.rect(surface=screen, color=(250, 250, 250), rect=pygame.Rect((screen.get_width()/2) - 270, 380, 540, 5))    

        #Centering
        if  n%2 == 1:
            x = (((screen.get_width())/2)-16) - 50*int(n/2 - 0.1)
        else:
            x = (((screen.get_width())/2)-16) - 50*(n/2) + 25

        #Correct checking
        if correct == n:
            correct = 0
            barWidth += 20 * len(strataQue[0][0]) + 10 * round
            pygame.display.flip()
            pygame.time.delay(40)
            score += 5 * len(strataQue[0][0])
            strataQue.pop(0)

        #Round increment
        if len(strataQue) == 0:
            barWidth = 500
            round += 1
            score += 100 + 50*round
            screen.fill((10, 10, 20))
            pygame.draw.rect(surface=screen, color=(255, 231, 16), rect=pygame.Rect((screen.get_width()/2) - 250, 450, 500, 34))
            screen.blit(title, (((screen.get_width()-title.get_width())/2), 120))
            screen.blit(hd2Font.render(f"Round {round}", True, (0, 0, 0)), (screen.get_width()/2 - 50, 450))
            screen.blit(pygame.font.Font("Fonts/Swiss 721 Extended Bold.otf", 20).render(f"Score: {score}", True, (255, 255, 255)), (screen.get_width()/2 - 50, 490))
            pygame.draw.rect(surface=screen, color=(255, 231, 16), rect=pygame.Rect((screen.get_width()/2)-(barWidth/2), 550, barWidth, 10))
            pygame.draw.rect(surface=screen, color=(250, 250, 250), rect=pygame.Rect((screen.get_width()/2) - 270, 580, 540, 5))    
            pygame.draw.rect(surface=screen, color=(250, 250, 250), rect=pygame.Rect((screen.get_width()/2) - 270, 380, 540, 5))    
            pygame.display.flip()
            time.sleep(1.5)
            codeswitch = True
        #Lose condition
        if barWidth <= 0:
            screen.fill((10, 10, 20))
            screen.blit(title, (((screen.get_width()-title.get_width())/2), 120))
            screen.blit(hd2Font.render("GAME OVER", True, (240, 240, 240)), (screen.get_width()//2 - 100, 360))
            screen.blit(hd2Font.render("Press any key to Restart", True, (240, 240, 240)), (screen.get_width()//2 - 200, 420))
            pygame.display.flip()
            pygame.time.delay(500)

            if pygame.event.get(pygame.KEYDOWN):
                strataQue = []
                barWidth = 500
                correct = 0
                codeswitch = True
                colorswitch = False
                PixelArrayList = []
                code = ""
                n = 0
                round = 1
        pygame.display.flip()

        #Bar Width limit
        if barWidth >= 500:
            barWidth = 500

        clock.tick(60)