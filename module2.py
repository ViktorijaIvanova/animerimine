

import pygame
import sys

pygame.init()

# цвета
yellow = [255, 255, 10]
red = [255, 0, 0]
gray = [200, 200, 200]
pink = [255, 150, 255]
roheline = [100, 255, 100]

# размеры экрана
X = 640
Y = 480
ekraan = pygame.display.set_mode([X, Y])
pygame.display.set_caption("animation")
ekraan.fill(roheline  )
kell = pygame.time.Clock()
snoopy = pygame.image.load("snoopy.png")
pos_x = X - snoopy.get_rect().width
pos_y = Y - snoopy.get_rect().height
lõpp = False

def animat(sammx,sammy,posx,posy):
    global pos_x, pos_y
    while not lõpp:
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
    kell.tick(60)
    events = pygame.event.get()
    for i in events:
        if i.type == pygame.QUIT:
                sys.exit()

        ekraan.blit(snoopy, (pos_x, pos_y))

        pygame.display.flip()
        ekraan.fill(roheline)

def animate_bouncing():
    pos_x = X // 2
    pos_y = Y - snoopy.get_rect().height
    sammx = 2  
    sammy = 2
    while not lõpp:
        pos_x += sammx
        pos_y += sammy
        if pos_x > X - snoopy.get_rect().width or pos_x < 0:
            sammx = -sammx
        if pos_y > Y - snoopy.get_rect().height or pos_y < 0:
            sammy = -sammy

        ekraan.fill(roheline)
        ekraan.blit(snoopy, (pos_x, pos_y))
        pygame.display.flip()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()

def animate(sammx, sammy):
    global pos_x, pos_y
    while not lõpp:
        pos_x += sammx
        pos_y += sammy
        if pos_x > X - snoopy.get_rect().width or pos_x < 0:
            sammx = -sammx
        if pos_y > Y - snoopy.get_rect().height or pos_y < 0:
            sammy = -sammy
        kell.tick(60)
        events = pygame.event.get()
        for i in events:
            if i.type == pygame.QUIT:
                sys.exit()

        ekraan.blit(snoopy, (pos_x, pos_y))

        pygame.display.flip()
        ekraan.fill(roheline)
while True:
    print("1 - clockwise")
    print("2 - bouncing")
    print("3 - counterclockwise")
    valik= input("Sisesta number: ")
    if valik == "1":
        sammx=2
        sammy=0
        animat()
    elif valik == "2":
        animate_bouncing()
    elif valik == "3":
        sammx = 2
        sammy = 2
        animate(sammx,sammy)
    else:
        print("Invalid choice, try again!")
