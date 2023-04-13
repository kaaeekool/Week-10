#button class
import pygame
#from baseShape import Shape
pygame.init()

class aButton:
    def __init__(self, bScreen, x = 0, y = 0, w = 10, h = 20):
        #window display
        self.bScreen = bScreen

        #x and y coordinate
        self.x = x
        self.y = y

        #width and length of the button
        self.width = w
        self.length = h

        #rect object to store coordinates of the button
        self.coordinates = pygame.Rect(x, y, w, h)

        #three RGB codes attributes for the states of the button
        self.default = (191, 64, 191)
        self.hover = (58, 144, 255)
        self.click = (12, 45, 129)

        #current state of the button
        self.state = 'default'

    #draw() method
    def draw(self):        
        #for event in pygame.event.get():
        if self.state == 'default':
            pygame.draw.rect(self.bScreen, self.default, self.coordinates)

        elif self.state == 'hover':
            pygame.draw.rect(self.bScreen, self.hover, self.coordinates)

        elif self.state == 'click':
            pygame.draw.rect(self.bScreen, self.click, self.coordinates)

    def eventResponse(self, eventObject):
     # Check if the event has something to do with the mouse moving or clicking, if not, just return to exit the function
        
     # Otherwise, check if the mouse position is within the area of the button. We can check this with collidePoint() in pygame
        #myRectObject.collidepoint(eventObject.pos) # will check the position of the mouse event and the inner area of any rect object

          # If the mouse is within the button, Check if the event.type is a mouseup (MOUSEBUTTONUP) or mousedown (MOUSEBUTTONDOWN)
               # use this to change the state of the button
        if eventObject.type == pygame.MOUSEMOTION or eventObject.type == pygame.MOUSEBUTTONDOWN or eventObject.type == pygame.MOUSEBUTTONUP:
            if self.coordinates.collidepoint(eventObject.pos):
                if eventObject.type == pygame.MOUSEMOTION:
                    self.state = 'hover'
                elif eventObject.type == pygame.MOUSEBUTTONDOWN:
                    self.state = 'clicked'
                elif eventObject.type == pygame.MOUSEBUTTONUP:
                    self.state = 'hover'
        
        else:
            self.state = 'default'