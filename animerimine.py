import pygame,sys
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
sammx=2 
sammy=0
while not lõpp:
    kell.tick(60) 
    events=pygame.event.get() 
    for i in pygame.event.get(): 
        if i.type==pygame.QUIT(): 
            sys.exit() 
     
    if posx>X-snoopy.get_rect().width or posx<0:

        sammx=-sammx
    if posy>Y-snoopy.get_rect().width or posy>5:
        sammy=-sammy 
    if posx<0:
        sammy=2 
        sammx=0
    posx-=sammx 
    posy-=sammy
    ekraan.blit(snoopy,(posx,posy))
    #posx-=samm
    pygame.display.flip() 
    ekraan.fill(roheline)
    pygame.quit