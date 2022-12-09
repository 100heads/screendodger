
import pygame, sys
import random
import os, time
from pygame.locals import *
pygame.init()

namedict = {'Saurus':random.randint(0,1), "Ucritis":random.randint(0,1), "Telev":random.randint(0,1)}
namelist = list(namedict)

villagercount = "six"
while villagercount == str(villagercount):
  #villagercount = input("What is the population?\nEnter a whole number: ")
  villagercount = random.randint(1,3)
  try:
    villagercount = int(villagercount)
    break
  except:
    print("Enter a Whole number!")
    continue
villagers = dict()

def people():
  global name, villagers
  villagers = dict()
  name = list()
  # for i in namelist:
  for i in range(villagercount):
    whichN = random.randint(0,2)
    whichname = namelist[whichN]
    name.append(whichname)
  whichVN = 0
  for i in range(villagercount):
    personality1 = random.randint(0,9)
    personalities = {0: "cold-hearted", 1: "gruff", 2: "serious", 3: "annoying", 4: "suspicious", 5: "eccentric", 6: "kind-hearted", 7: "superstitious", 8: "light-hearted", 9: "foolish"}
    personality2 = personalities[personality1]
    villagers[name[whichVN]] = [1,"2"]
    villagers[name[whichVN]][0] = personality1
    villagers[name[whichVN]][1] = personality2
    whichVN += 1
  return villagers
  return name
people()
print(name)
# print(len(villagers))
# print(villagers)

while True:
  if len(villagers) < villagercount:
    # print("debug")
    people()
  elif len(villagers) == villagercount:
    break

print(name)
# print(len(villagers))
# print(villagers)
# print(name)

neatprint = list()
whichVN = 0
for i in range(villagercount):
  printstuff = list()
  printstuff.append(list(villagers)[whichVN])
  printstuff.append(villagers[name[whichVN]])
  neatprint.append(printstuff[0])
  neatprint.append(printstuff[1][1])
  whichVN += 1
neat = ""
whichVN = 0
for i in range(len(neatprint)//2):
  if whichVN + 2 < len(neatprint):
    neat = neat + neatprint[whichVN] + " is " + neatprint[whichVN + 1] + " | "
  else:
    neat = neat + neatprint[whichVN] + " is " + neatprint[whichVN + 1]
  whichVN += 2
print(neat)



# color (amount of red, green and blue)
BACKGROUND = (45, 135, 100)
RED = (255, 30, 70)
BLUE = (60, 100, 230)
# 150 blue is a great green color as well (100,200, | 190 steel) (100,240,255)
YELLOW = (50, 150, 130)

#Game set-up
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game!")

#character values
width = 60
height = 60
X = random.randint(WINDOW_WIDTH//2.5, WINDOW_WIDTH//1.5)
Y = random.randint(WINDOW_HEIGHT//2.5, WINDOW_HEIGHT//1.5)
charactermoveX = 0; charactermoveY = 0
X_speed = 0.02
Y_speed = 0.02
movecooldownX = 0; movecooldownY = 0
xfast = 0.007
xnormal = 0.014
yfast = 0.007
ynormal = 0.014
maxballs = 6

class entities:
  def __init__(self, name, ):
    for i in range(maxballs):
      i.name = random.choice(('Block', 'Square'))
      i.name = i

loop = random.choice((True,False)); loop2 = random.randint(0,1)
# the main function that controls the game
def main():
  global X, Y, width, height, loop, loop2, charactermoveY, charactermoveX, X_speed, Y_speed, movecooldownY, movecooldownX
  looping = True
  # main game loop
  while looping:
    #get inputs
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        #exit()
        sys.exit()
    #processing
    character = pygame.Rect(X, Y, width, height)
    
    if (Y == 0 and X == 0) or (Y == 0 and X == WINDOW_WIDTH - width) or (Y == WINDOW_HEIGHT - height and X == 0) or (Y == WINDOW_HEIGHT - height and X == WINDOW_WIDTH - width):
      print("--------------------\nIT HIT THE CORNER!!!\n--------------------")
    #check collision and set which way to move
    if X == WINDOW_WIDTH - width:
      loop = False
      #loop2 = random.randint(0,1)
      if X_speed == xnormal:
        X_speed = random.choice((xnormal,xfast))
      if X_speed == xfast:
        X_speed = random.choice((xnormal,xfast,xfast))
      Y_speed = ynormal
    
    if X == 0:
      loop = True
      #loop2 = random.randint(0,1)
      if X_speed == xnormal:
        X_speed = random.choice((xnormal,xfast))
      if X_speed == xfast:
        X_speed = random.choice((xnormal,xfast,xfast))
      Y_speed = ynormal
    
    if Y == WINDOW_HEIGHT - height:
      loop2 = 1
      if Y_speed == ynormal:
        Y_speed = random.choice((ynormal,yfast))
      if Y_speed == yfast:
        Y_speed = random.choice((ynormal,yfast,yfast))
      X_speed = xnormal
    
    if Y == 0:
      loop2 = 0
      if Y_speed == ynormal:
        Y_speed = random.choice((ynormal,yfast))
      if Y_speed == yfast:
        Y_speed = random.choice((ynormal,yfast,yfast))
      X_speed = xnormal
    
    # movement
    if charactermoveX == 0:
      if loop == True:
        X += 1
      if loop == False:
        X -= 1
      charactermoveX = X_speed
      if movecooldownX == 0:
        movecooldownX = 1
        time.sleep(charactermoveX)
        movecooldownX = 0
        charactermoveX = 0
      
    if charactermoveY == 0:
      if loop2 == 0:
        Y += 1
      if loop2 == 1:
        Y -= 1
      charactermoveY = Y_speed
      if movecooldownY == 0:
        movecooldownY = 1
        time.sleep(charactermoveY)
        movecooldownY = 0
        charactermoveY = 0
    #This section will be built out later
    
    #Render elements of the game
    WINDOW.fill(BLUE)
    pygame.draw.circle(WINDOW, BACKGROUND, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 355, 300)
    pygame.draw.circle(WINDOW, YELLOW, (200, 300), 165, 60, False, True, True, False)
    pygame.draw.circle(WINDOW, YELLOW, (400, 300), 165, 60, True, False, False, True)
    pygame.draw.rect(WINDOW, RED, character, 20)
    #pygame.draw.circle(WINDOW, RED, (X+width/2,Y+height/2), width/2)
    pygame.display.update()
    fpsClock.tick(FPS)
    
main()






