from site import execsitecustomize
import pygame
import sys
import random

def yx():
    global sammx, sammy, posx, posy, X, snoopy
    if posx <= 0:
        sammx = 2
    if posy <= 0:
        sammy = 2
    if posx >= X - snoopy.get_rect().width:
        sammx = -2
    if posy >= Y - snoopy.get_rect().height:
        sammy = -2
    posx += sammx
    posy += sammy
    ekraan.blit(snoopy, (posx, posy))

def esimene():
    global sammx, sammy, posx, posy, X, Y, snoopy
    if posx == 0 and posy == 0:
        sammx = 0
        sammy = 2
    if posx == 0 and posy >= Y - snoopy.get_rect().height:
        sammx = 2
        sammy = 0
    if posx <= X - snoopy.get_rect().width and posy == Y - snoopy.get_rect().height:
        sammx = 0
        sammy = -2
    if posx >= X - snoopy.get_rect().width and posy <= Y - snoopy.get_rect().width:
        sammx = -2
        sammy = 0

    posx += sammx
    posy += sammy
    ekraan.blit(snoopy, (posx, posy))

def teine():
    global sammx, sammy, posx, posy, X, Y, snoopy
    if posx > X - snoopy.get_rect().width or posx < 0:
        sammx = -sammx
    if posy > Y - snoopy.get_rect().height or posy < 0:
        sammy = -sammy
    if posy < 0:
        posy = 0
    elif posy > Y - snoopy.get_rect().height:
        posy = Y - snoopy.get_rect().height

    if random.randint(0, 20) == 0:
        sammy = random.choice([-2, -15])

    posx += sammx
    posy += sammy
    ekraan.blit(snoopy, (posx, posy))

def kolmas():
    global sammx, sammy, posx, posy, X, Y, snoopy
    if posx == 0 and posy == 0:
        sammx = 2
        sammy = 0
    if posx == X - snoopy.get_rect().width and posy <= Y - snoopy.get_rect().height:
        sammx = 0
        sammy = 2
    if posx <= X - snoopy.get_rect().width and posy == Y - snoopy.get_rect().height:
        sammx = 2
        sammy = 0
        sammx = -sammx

    if posx == 0 and posy >= Y - snoopy.get_rect().height:
        sammx = 0
        sammy = 2
        sammy = -sammy
    posx += sammx
    posy += sammy
    ekraan.blit(snoopy, (posx, posy )) 

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

while True:
     print("1-päripäeva")
     print("2-erinevates suundades")
     print("3-vastupäeva")
     valik=input("Kirjuta number, mis teeb su tegevuse: ")
     if valik=="1":
        esimene()
        yx
        while not lõpp:
            kell.tick(60) 
            events = pygame.event.get() 
            for i in events: 
                if i.type == pygame.QUIT: 
                    sys.exit()
            
                ekraan.blit(snoopy,(posx,posy))
    
                pygame.display.flip() 
                ekraan.fill(roheline)
                pygame.quit
                break
     elif valik=="2":
                teine()
                while not lõpp:
                    kell.tick(60) 
                    events = pygame.event.get() 
                    for i in events: 
                        if i.type == pygame.QUIT: 
                            sys.exit()
            
                        ekraan.blit(snoopy,(posx,posy))
    
                        pygame.display.flip() 
                        ekraan.fill(roheline)
                        pygame.quit
                        break

     elif valik=="3":
                kolmas
       
                while not lõpp:
                    kell.tick(60) 
                    events = pygame.event.get() 
                    for i in events: 
                        if i.type == pygame.QUIT: 
                            sys.exit()
            
                        ekraan.blit(snoopy,(posx,posy))
    
                        pygame.display.flip() 
                        ekraan.fill(roheline)
                        pygame.quit
                        break
                else:
                    print("Sa valisid ebakorrektse väärtuse")
"""while True:
    
    if valik==1:
        esimene()
        valik = random.choice()
    
      
    while not lõpp:
        kell.tick(60) 
        events = pygame.event.get() 
        for i in events: 
            if i.type == pygame.QUIT: 
                sys.exit()
            
            ekraan.blit(snoopy,(posx,posy))
    
            pygame.display.flip() 
            ekraan.fill(roheline)
            pygame.quit
            break
    if valik==2:
        teine
        valik = random.choice()
    while not lõpp:
        kell.tick(60) 
        events = pygame.event.get() 
        for i in events: 
            if i.type == pygame.QUIT: 
                sys.exit()
            
            ekraan.blit(snoopy,(posx,posy))
    
            pygame.display.flip() 
            ekraan.fill(roheline)
            pygame.quit
            break
    if valik==3:
        kolmas
        valik = random.choice()
    while not lõpp:
        kell.tick(60) 
        events = pygame.event.get() 
        for i in events: 
            if i.type == pygame.QUIT: 
                sys.exit()
            
            ekraan.blit(snoopy,(posx,posy))
    
            pygame.display.flip() 
            ekraan.fill(roheline)
            pygame.quit
            break
#valik = random.choice(functions)
   # valik  """