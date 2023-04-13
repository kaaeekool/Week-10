import pygame
from button import aButton


pygame.init()
#display
window = pygame.display.set_mode((800, 600))

#create a button instance 
BUTTONONE = aButton(window , 100, 100, 100, 50)
BUTTONTWO = aButton(window, 350, 100, 100, 50)

TheButtons = [BUTTONONE,BUTTONTWO]

#clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        for activebuttons in TheButtons:
            activebuttons.eventResponse(event)

    window.fill((47, 19, 92))
    for activebuttons in TheButtons:
        activebuttons.draw()
            

    pygame.display.update()
    clock.tick(60)