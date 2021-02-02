#import
import pygame
import os,sys
import string
import time
import pygame as pg
from pygame.locals import *
from pygame.compat import geterror
from Player import *
from Dice import *




#print personal detail 
__author__ = "Ruby(Qiufeng Yi)"
print(__author__)
__author_number__ = "2169552/QXY953"
print(__author_number__)
__gametitle__ = "Snakes and Ladders Game"
print(__gametitle__)
__BGM__ = "poemofbird"
print(__BGM__)


#check available
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

#initialization
pygame.init()
pygame.font.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
retry = True
crashed = False
#Load  
#Loading Resources
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', fullname)
        raise SystemExit(message)
    return sound
#load BGM
pygame.mixer.music.load("poemofbird.mp3")
pygame.mixer.init()
pygame.mixer.music.play()
gameDisplay.fill((255, 255, 255))
board = pygame.image.load(r"snakes_ladders.png")

#text_objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def button (msg, x, y, w, h, ic, ac):
    mouse =pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

#Loading img
token1 = pygame.image.load(r"Gold_caster.jpg")
token2 = pygame.image.load(r"Gold_archer.jpg")
token3 = pygame.image.load(r"Gold_saber.jpg")
token4 = pygame.image.load(r"Gold_lancer.jpg")
player1 = Player(0, token1, "Player1")
player2 = Player(0, token2, "Player2")
player3 = Player(0, token3, "Player3")
player4 = Player(0, token4, "Player4")
player1_name = ''
player2_name = ''
player3_name = ''
player4_name = ''


dice = Dice()
clock = pygame.time.Clock()
fontP = pygame.font.SysFont("Times New Roman", 45, True)
#Title
gameDisplay.blit(board, (0, 60))
pygame.display.set_caption('Snakes and Ladders Game')
if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render("Roll the Dice, And get the number", 1, (10, 10, 10))
# get players_number
while True:
        players_NUM = int(input("please input the players number(1-4):"))
        if players_NUM <=4 and players_NUM >=1:
            print("please input the name of players")
            break
        else:
            print("reinput")
flag1=players_NUM
flag2=flag1
#get players_names
while True:
        player_name = input("Name of player"+str(players_NUM)+":")
        if int(players_NUM)<1:
            print("start game")
            break
        else:
            print("next")
            if players_NUM ==4:
               player4_name=player_name
            elif players_NUM ==3:
               player3_name=player_name
            elif players_NUM ==2:
               player2_name=player_name
            elif players_NUM ==1:
               player1_name=player_name              

            players_NUM += -1

#Display players_token
if player1_name.strip()!='':
  gameDisplay.blit(token1, (700, 300))
else :
   playernumber=1
if player2_name.strip()!='':
  gameDisplay.blit(token2, (700, 400))
else :
   playernumber=2
if player3_name.strip()!='':
  gameDisplay.blit(token3, (800, 300))
else :
   playernumber=3
if player4_name.strip()!='':
  gameDisplay.blit(token4, (800, 400))
else :
   playernumber=4

#
while not crashed:
        
    pygame.draw.rect(gameDisplay, (255, 64, 64), (700, 500, 100, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
#text form
    font = pygame.font.SysFont("arial", 20)
    font1 = pygame.font.SysFont("arial", 50)


# text
    player1_nametext = font.render(str(player1_name), True, (0, 0, 255), (0, 255, 0))
    player2_nametext = font.render(str(player2_name), True, (0, 0, 255), (0, 255, 0))
    player3_nametext = font.render(str(player3_name), True, (0, 0, 255), (0, 255, 0))
    player4_nametext = font.render(str(player4_name), True, (0, 0, 255), (0, 255, 0))
    player1_wintext = font.render(str(player1_name)+"WIN", True, (0, 0, 255), (0, 255, 0))
    player2_wintext = font.render(str(player2_name)+"WIN", True, (0, 0, 255), (0, 255, 0))
    player3_wintext = font.render(str(player3_name)+"WIN", True, (0, 0, 255), (0, 255, 0))
    player4_wintext = font.render(str(player4_name)+"WIN", True, (0, 0, 255), (0, 255, 0))
    buttontext = font1.render("ROLL", True, (0, 0, 255), (0, 255, 0))
    ruletext=font.render("click the roll button one by one", True, (0, 0, 255), (0, 255, 0))
    writertext=font.render("created by : "+str(__author_number__), True, (0, 0, 255), (0, 255, 0))
    datatext=font.render(str(__author_number__), True, (0, 0, 255), (0, 255, 0))
    

    # show 
    gameDisplay.blit(player1_nametext, (700,350))
    gameDisplay.blit(player2_nametext, (700,450))
    gameDisplay.blit(player3_nametext, (800,350))
    gameDisplay.blit(player4_nametext, (800,450))
    gameDisplay.blit(buttontext, (700,500))
    gameDisplay.blit(ruletext, (650,150))
    gameDisplay.blit(writertext, (650,180))
    gameDisplay.blit(datatext, (650,210))

    #check mouse
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] > 700 and mouse_pos[0] < 800 and mouse_pos[1] > 500 and mouse_pos[1] < 550:
        if pygame.mouse.get_pressed() == (True, False, False):
            #pygame.time.delay(100)
            
            if  flag2==4:
                num = dice.number(gameDisplay)
                player4.move(num)
                gameDisplay.blit(board, (0,60))
                player4_numtext = font.render("score:"+str(player4.num), True, (0, 0, 125), (255, 255,255))
                gameDisplay.blit(player4_numtext, (800,370))
                player4.draw(gameDisplay)
                flag2=3
            elif  flag2==3:
                num = dice.number(gameDisplay)
                player3.move(num)
                gameDisplay.blit(board, (0,60))
                player3_numtext = font.render("score:"+str(player3.num), True, (0, 0, 125), (255, 255,255))
                gameDisplay.blit(player3_numtext, (800,270))
                player3.draw(gameDisplay)
                flag2=2
            elif flag2==2:
                num = dice.number(gameDisplay)
                player2.move(num)
                gameDisplay.blit(board, (0,60))
                player2_numtext = font.render("score:"+str(player1.num), True,(0, 0, 125), (255, 255,255))
                gameDisplay.blit(player2_numtext, (700,370))
                player2.draw(gameDisplay)
                flag2=1
            elif flag2==1 :
                num = dice.number(gameDisplay)
                player1.move(num)
                gameDisplay.blit(board, (0,60))
                player1_numtext = font.render("score:"+str(player1.num), True, (0, 0, 125), (255, 255,255))
                gameDisplay.blit(player1_numtext, (700,270))
                player1.draw(gameDisplay)
                flag2=flag1

#Display WIN
    pygame.display.update()
    if player1.num == 100 or player2.num == 100 or player3.num == 100 or player4.num == 100:
        if player1.num == 100:
            print(player1.name + " wins!!")
            gameDisplay.blit(player1_wintext, (0,0))
            pygame.time.delay(100)
            crashed = True
        elif player2.num == 100:
            print(player2.name + " wins!!")
            gameDisplay.blit(player2_wintext, (0,0))
            pygame.time.delay(100)
            crashed = True
        elif player3.num == 100:
            print(player3.name + " wins!!")
            gameDisplay.blit(player3_wintext, (0,0))
            pygame.time.delay(100)
            crashed = True
        elif player4.num == 100:
            print(player4.name + " wins!!")
            gameDisplay.blit(player4_wintext, (0,0))
            pygame.time.delay(100)
            crashed = True
pygame.quit()





