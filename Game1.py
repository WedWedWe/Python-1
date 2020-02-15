import pygame
import sys

        
pygame.init()

clock = pygame.time.Clock()
size = width,height = 600,400
speed = [0,0]
bgc = (255,255,255)
screen_full = False
angle = 90

screen = pygame.display.set_mode(size,pygame.RESIZABLE)

pygame.display.set_caption("Flyme")

air = pygame.image.load("enemy1.png")

position = air.get_rect()
position = pygame.Rect(100,100,53,47)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-3,0]
                air = pygame.transform.rotate(air,90)
            if event.key == pygame.K_RIGHT:
                speed = [3,0]
                air = pygame.transform.rotate(air,270)
            if event.key == pygame.K_UP:
                speed = [0,-3]
                air = pygame.transform.rotate(air,180)
            if event.key == pygame.K_DOWN:
                speed = [0,3]
                air = pygame.transform.rotate(air,360)
            if event.key == pygame.K_SPACE:
                air = pygame.transform.rotate(air,90) 
            if event.key == pygame.K_F11:
                screen_full = not screen_full
                if screen_full:
                    screen = pygame.display.set_mode(pygame.display.list_modes()[1],pygame.FULLSCREEN | pygame.HWSURFACE)
                    width = pygame.display.list_modes()[1][0]
                    height = pygame.display.list_modes()[1][1]
                else:
                    screen = pygame.display.set_mode(size)
                    width = 600
                    height = 400
                
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            width,height=size
            print(size)
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)

            
    position = position.move(speed)
    #print(pygame.display.list_modes()[1])
    #if position.left<0:
    #air = pygame.transform.rotate(air,2)

    if position.left<0:
        if speed[0]<0:
            air = pygame.transform.rotate(air,180)
        speed[0]=-speed[0]
        
    if position.right>width:
        if speed[0]>0:
            air = pygame.transform.rotate(air,180)
        speed[0]=-speed[0]
        
    if position.bottom>height:
        if speed[1]>0:
            air = pygame.transform.rotate(air,180)
        speed[1]=-speed[1]
        
    if position.top<0:
        if speed[1]<0:
            air = pygame.transform.rotate(air,180)
        speed[1]=-speed[1]
        
    screen.fill(bgc)
    
    screen.blit(air,position)
    
    pygame.display.flip()
    
    #pygame.time.delay(10)
    clock.tick(100)
