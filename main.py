
import pygame, sys
import random, decimal
import os, time, datetime
from pygame.locals import *
pygame.init()

namedict = {'Saurus':random.randint(0,1), "Ucritis":random.randint(0,1), "Telev":random.randint(0,1), "Yylquin":random.randint(0,1)}
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

#----------------------------------------------------------------------------------------------------

#22,630 | 22,630
# color (amount of red, green and blue)
BACKGROUND = (45, 135, 100)
RED = (255, 30, 70)
BLUE = (60, 100, 230)
# 150 blue is a great green color as well (100,200, | 190 steel) (100,240,255)
YELLOW = (50, 150, 130)

#Game set-up
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 600 #600
WINDOW_HEIGHT = 600 #600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game!")

#character values
width = 60
height = 60
X = random.randint(WINDOW_WIDTH//2.5, WINDOW_WIDTH//1.5)
Y = random.randint(WINDOW_HEIGHT//2.5, WINDOW_HEIGHT//1.5)
charactermoveX = 0; charactermoveY = 0
X_speed = 0.0010
Y_speed = 0.0010
movecooldownX = 0; movecooldownY = 0
xfast = 100000 #0.001
xnormal = 100000 #0.015
yfast = 100000
ynormal = 100000
gravity = 0.25
gravitymove = 0
maxballs = 100
howmanyballs = 7

thetime = str(datetime.datetime.now())
thedelimiters = (" ",":","-"," ")
for i in range(len(thedelimiters)):
  delimiter = thedelimiters[i - 1]
  thetime = thetime.split(delimiter)
  #thetime = thedelimiters[len(thedelimiters) - 1].join(thetime)
  thetime = "".join(thetime)
#thetime = thetime.split(" ")
#thetime = float(thetime[4] + thetime[5])
#thetime = thetime.split(" ")
thetime = float(thetime)
oldtime = thetime
howmanytimes = 5

class entity:
  def __init__(self):   #self,i,name,width,height,x,y,xspeed,yspeed):
    for i in range(maxballs):
      if i == 0:
        self.width = list()
        self.height = list()
        self.x = list()
        self.y = list()
        self.stored_energy = list()
        self.using = 0
        self.leftenergy = list()
        self.rightenergy = list()
        self.upenergy = list()
        self.downenergy = list()
        
        self.downgravity = list()
        self.upgravity = list()
        self.rightgravity = list()
        self.leftgravity = list()
        self.thetime = list()
        self.oldtime = dict()
        self.movecooldownLEFT = list()
        self.movecooldownRIGHT = list()
        self.movecooldownUP = list()
        self.movecooldownDOWN = list()
      
      self.width.append(60)
      self.height.append(60)
      self.x.append(random.randint(WINDOW_WIDTH//2.5, WINDOW_WIDTH//1.5))
      self.y.append(random.randint(WINDOW_HEIGHT//2.5, WINDOW_HEIGHT//1.5))
      #energy in use must be 100,000 max, and 1 minimum; the higher the number, the less energy
      #and therefore speed (self.energy) (note: although we do not want a cap as to how slow
      #something can get, we also want something to be able of devoidability in energy)
      
      #self.energy.append(100)
      
      # Energy, based on a button pressed or transfer through other entity, or base energy given by
      # me, goes respectively from the stored energy (button press or AI) to it's direction. If there
      # is any energy anywhere in these four directions, it creates movement in which. There could
      # also be other types of energy, maybe, although likely determined by these four's supply.
      # Note: 0 = no speed. The smaller the whole number, the faster by seconds. The bigger the whole
      # number, the slower, of course as well in seconds.
      self.stored_energy.append(10) # leftenergy[i] += using; self.stored_energy[i] += using 
      # using = -0.1
      self.leftenergy.append(5000)
      # we would wait for (to move left):  (100,000/self.leftenergy)/(100,000)
      self.rightenergy.append(9670)
      self.upenergy.append(4000)
      self.downenergy.append(2700)
      
      self.downgravity.append(3000) #3000
      self.thetime.append(thetime)
      self.oldtime[i] = list()
      for whichtime in range(howmanytimes):
        self.oldtime[i].append(self.thetime[i])

ent = entity()

loop = random.choice((True,False)); loop2 = random.randint(0,1)
# the main function that controls the game
def main():
  global X, Y, width, height, loop, loop2, charactermoveY, charactermoveX, X_speed, Y_speed, movecooldownY, movecooldownX, xnormal, ynormal, gravity, gravitymove, thetime, oldtime
  # main game loop
  for i in range(howmanyballs):
    #character = pygame.Rect(self.x[i], self.y[i], self.width[i], self.height[i])
    #get inputs
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()
        sys.exit()
      #if event.type == KEYDOWN and event.key == K_r:
      if event.type == KEYDOWN and event.key == K_r:
        ent.x[i] = random.randint(100,500)
        ent.y[i] = random.randint(100,500)
      if event.type == KEYDOWN and event.key == K_e:
        os.system('cls')
        print("-----------------------")
        print("Right energy: ",i,ent.rightenergy[i])
        print("Left energy: ",i,ent.leftenergy[i])
        print("Up energy: ",i,ent.upenergy[i])
        print("Down energy: ",i,ent.downenergy[i])
        print("-----------------------")
      pressed = pygame.key.get_pressed()
      if (pressed[K_d] or pressed[K_RIGHT]):
        ent.x[i] += 10
      if (pressed[K_a] or pressed[K_LEFT]):
        ent.x[i] -= 10
      if (pressed[K_s] or pressed[K_DOWN]):
        ent.y[i] += 10
      if (pressed[K_w] or pressed[K_UP]):
        ent.y[i] -= 10
    
    #processing
    character = pygame.Rect(ent.x[i], ent.y[i], ent.width[i], ent.height[i])
    
    #thetime = str(datetime.datetime.now())
    #thedelimiters = (" ",":","-"," ")
    #for o in range(len(thedelimiters)):
      #delimiter = thedelimiters[o - 1]
      #thetime = thetime.split(delimiter)
      #thetime = "".join(thetime)
    #thetime = float(thetime)
    #ent.thetime[i] = thetime
    
    #if ent.thetime[i] >= ent.oldtime[i][0] + 2:
      #ent.oldtime[i][0] = ent.thetime[i]
      #print(ent.thetime[i])
    
    #if (ent.y[i] == 0 and ent.x[i] == 0) or (ent.y[i] == 0 and ent.x[i] == WINDOW_WIDTH - width) or (ent.y[i] == WINDOW_HEIGHT - height and ent.x[i] == 0) or (ent.y[i] == WINDOW_HEIGHT - height and ent.x[i] == WINDOW_WIDTH - width):
      #print("--------------------\nIT HIT THE CORNER!!!\n--------------------")
    
    #check collision and set which way to move
    if ent.x[i] >= WINDOW_WIDTH - ent.width[i]:
      ent.x[i] = WINDOW_WIDTH - ent.width[i]
      exchange = random.choice((100,200,300))
      if ent.rightenergy[i] >= exchange:
        ent.rightenergy[i] -= exchange
      #loop2 = random.randint(0,1)
      ent.leftenergy[i] += exchange
    
    if ent.x[i] <= 0:
      ent.x[i] = 0
      exchange = random.choice((100,200,300))
      if ent.leftenergy[i] >= exchange:
        ent.leftenergy[i] -= exchange
      #loop2 = random.randint(0,1)
      ent.rightenergy[i] += exchange
      
      #if ent.leftenergy[i] >= xnormal:
        #ent.leftenergy[i] = xnormal #random.choice((xnormal,xfast))
      #if ent.leftenergy[i] <= xfast:
        #ent.leftenergy[i] = xfast #random.choice((xnormal,xfast,xfast))
    
    if ent.y[i] >= WINDOW_HEIGHT - ent.height[i]:
      ent.y[i] = WINDOW_HEIGHT - ent.height[i]
      exchange = random.choice((100,200,300))
      if ent.downenergy[i] >= exchange:
        ent.downenergy[i] -= exchange
      ent.upenergy[i] += exchange
    
    if ent.y[i] <= 0:
      ent.y[i] = 0
      exchange = random.choice((100,200,300))
      if ent.upenergy[i] >= exchange:
        ent.upenergy[i] -= exchange
      ent.downenergy[i] += exchange
    
    # movement | decimal.Decimal(1) / decimal.Decimal(7)
    
    if ent.rightenergy[i] > 0:
      if ent.thetime[i] >= ent.oldtime[i][0] + (100000/ent.rightenergy[i]) / (10000):
        ent.oldtime[i][0] = ent.thetime[i]
        ent.x[i] += 1
    else:
      pass
    
    if ent.leftenergy[i] > 0:
      if ent.thetime[i] >= ent.oldtime[i][1] + (100000/ent.leftenergy[i]) / (10000):
        ent.oldtime[i][1] = ent.thetime[i]
        ent.x[i] -= 1
    else:
      pass
    
    if ent.upenergy[i] > 0:
      if ent.thetime[i] >= ent.oldtime[i][2] + (100000/ent.upenergy[i]) / (10000):
        ent.oldtime[i][2] = ent.thetime[i]
        ent.y[i] -= 1
    else:
      pass
    
    if ent.downenergy[i] > 0:
      if ent.thetime[i] >= ent.oldtime[i][3] + 100000/(ent.downenergy[i] + ent.downgravity[i]) / 10000:
        ent.oldtime[i][3] = ent.thetime[i]
        ent.y[i] += 1
    else:
      pass
    
    #if ent.thetime[i] >= ent.oldtime[i][4] + (100000/ent.downgravity[i]) / (10000):
      #ent.oldtime[i][4] = ent.thetime[i]
      #ent.y[i] += 1
    
      #if gravitymove == 0:
        #if gravitymove == 0:
          #gravitymove = 1
          #time.sleep(gravity)
          #gravitymove = 0
          #for i in range(1):           #maxballs):
            #Y += 1
        
    #This section will be built out later
  
  #Render elements of the game
  WINDOW.fill(BLUE)
  pygame.draw.circle(WINDOW, BACKGROUND, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 355, 300)
  pygame.draw.circle(WINDOW, YELLOW, (200, 300), 165, 60, False, True, True, False)
  pygame.draw.circle(WINDOW, YELLOW, (400, 300), 165, 60, True, False, False, True)
  for e in range(howmanyballs):
    character = pygame.Rect(ent.x[e], ent.y[e], ent.width[e], ent.height[e])
    pygame.draw.rect(WINDOW, RED, character, 0) #20
    #pygame.draw.circle(WINDOW, RED, (X+width/2,Y+height/2), width/2)
  pygame.display.update()
  fpsClock.tick(FPS)
  xnormal += 1; ynormal += 1
while True:
  main()














