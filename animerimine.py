import pygame,sys
import random
def esimene():
    global posx,posy
    if posx == 0 and posy == 0:
        sammx = 0
        sammy = 1
    if posx == 0 and posy >= Y - snoopy.get_rect().width:
        sammx = 1
        sammy = 0
    if posx <= X - snoopy.get_rect().width and posy == Y - snoopy.get_rect().height:
        sammx = 0
        sammy = -1
    if posx >= X - snoopy.get_rect().width and posy <= Y - snoopy.get_rect().width:
        sammx = -1
        sammy = 0
    
    
    if posx==0 and posy>=Y-snoopy.get_rect().height:
        sammx=0
        sammy=1
        sammy=-sammy 
    posx+=sammx 
    posy+=sammy
    ekraan.blit(snoopy,(posx,posy))

def teine():
    global posx,posy
    if posx>X-snoopy.get_rect().width or posx<0:
        sammx=-sammx
    if posy>X-snoopy.get_rect().height or posy<0:
        sammy=-sammy 
    if posy<0:
        posy=0
    elif posy>Y-snoopy.get_rect().height:
        posy=Y-snoopy.get_rect().height

    
    if random.randint(0, 20) == 0:
        sammy = random.choice([-1, -15])

    posx+=sammx 
    posy+=sammy
    ekraan.blit(snoopy,(posx,posy)) 

def kolmas(): 
    global posx,posy 
    if posx==0 and posy==0:
        sammx=1
        sammy=0
    if posx==X-snoopy.get_rect().width and posy<=Y-snoopy.get_rect().height:
        sammx=0
        sammy=1
    if posx<=X-snoopy.get_rect().width and posy==Y-snoopy.get_rect().height:
        sammx=1
        sammy=0
        sammx=-sammx
    
    
    if posx==0 and posy>=Y-snoopy.get_rect().height:
        sammx=0
        sammy=1
        sammy=-sammy 
    posx+=sammx 
    posy+=sammy
    ekraan.blit(snoopy,(posx,posy))

pygame.init() 
#värvid
kollane=[255,255,10] 
punane=[255,0,0] 
hall=[200,200,200] 
roosa=[255,150,255] 
roheline=[100,255,100] 
#ekraani suurus 
X=640 
Y=480 
ekraan=pygame.display.set_mode([X,Y]) 
pygame.display.set_caption("animatsion") 
ekraan.fill(roheline) 
kell=pygame.time.Clock() 
snoopy=pygame.image.load("snoopy.png") 
posx=X-snoopy.get_rect().width
posy=Y-snoopy.get_rect().height 
lõpp=False 
sammx = 2  
sammy = 0
while not lõpp:
    kell.tick(60) 
    events = pygame.event.get() 
    for i in events: 
        if i.type == pygame.QUIT: 
            sys.exit() 
        if random.randint(esimene,teine,kolmas):
            break 
"""sammx = -2  
sammy = 0
while not lõpp:
    kell.tick(60) 
    events = pygame.event.get() 
    for i in events: 
        if i.type == pygame.QUIT: 
            sys.exit() 

   if posx == 0 and posy == 0:
        sammx = 0
        sammy = 1
    if posx == 0 and posy >= Y - snoopy.get_rect().width:
        sammx = 1
        sammy = 0
    if posx <= X - snoopy.get_rect().width and posy == Y - snoopy.get_rect().height:
        sammx = 0
        sammy = -1
    if posx >= X - snoopy.get_rect().width and posy <= Y - snoopy.get_rect().width:
        sammx = -1
        sammy = 0
    
    
    if posx==0 and posy>=Y-snoopy.get_rect().height:
        sammx=0
        sammy=1
        sammy=-sammy 
    posx+=sammx 
    posy+=sammy
    ekraan.blit(snoopy,(posx,posy))
   
    pygame.display.flip() 
    ekraan.fill(roheline)
    pygame.quit"""




"""sammx=2 
sammy=0
while not lõpp:
    kell.tick(60) 
    events=pygame.event.get() 
    for i in pygame.event.get(): 
        if i.type==pygame.QUIT(): 
            sys.exit() 
     
    if posx>X-snoopy.get_rect().width or posx<0:
        sammx=-sammx
    if posy>X-snoopy.get_rect().height or posy<0:
        sammy=-sammy 
    if posy<0:
        posy=0
    elif posy>Y-snoopy.get_rect().height:
        posy=Y-snoopy.get_rect().height

    
    if random.randint(0, 20) == 0:
        sammy = random.choice([-1, -15])

    posx+=sammx 
    posy+=sammy
    ekraan.blit(snoopy,(posx,posy))

    pygame.display.flip() 
    ekraan.fill(roheline)
    pygame.quit"""


"""sammx=2 
sammy=0
while not lõpp:
    kell.tick(60) 
    events=pygame.event.get() 
    for i in pygame.event.get(): 
        if i.type==pygame.QUIT(): 
            sys.exit() 
    if posx==0 and posy==0:
        sammx=1
        sammy=0
    if posx==X-snoopy.get_rect().width and posy<=Y-snoopy.get_rect().height:
        sammx=0
        sammy=1
    if posx<=X-snoopy.get_rect().width and posy==Y-snoopy.get_rect().height:
        sammx=1
        sammy=0
        sammx=-sammx
    
    
    if posx==0 and posy>=Y-snoopy.get_rect().height:
        sammx=0
        sammy=1
        sammy=-sammy 
    posx+=sammx 
    posy+=sammy
    ekraan.blit(snoopy,(posx,posy))
   
    pygame.display.flip() 
    ekraan.fill(roheline)
    pygame.quit"""