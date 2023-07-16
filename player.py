import pygame
import math

class Player:

    def __init__(self, x, y, color, windowWidth, windowHeight, surface):
        # position on the screen
        self.x = x
        self.y = y

        # Dimensions
        self.width = 40
        self.height = 60
        
        # surface details (for drawing and borders)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.surface = surface
        
        # direction can be 0, -1, or 1
        self.vertDirection = 0
        self.horizDirection = 0

        # Intended speed of the player
        self.maxSpeed = 0.6

        # Current speed
        self.speed = 1

        self.color = color

        # corners of the polygon
        self.points = [(self.x, self.y-self.height/2), (self.x-self.width/2, self.y+self.height/2), (self.x+self.width/2, self.y+self.height/2)]
    
    def SetColor(self, color):
        self.color = color

    def SetVertDirection(self, dir):
        self.vertDirection = dir

    def SetHorizDirection(self, dir):
        self.horizDirection = dir

    def UpdateSpeed(self):
        a = self.horizDirection
        b = self.vertDirection

        # calculate length of hypoteneuse (actual speed)
        c = (a*a + b*b)**0.5
        if c != 0:
            self.speed = 1/c
        else:
            self.speed = 1

    # Move points based on new player position
    def UpdatePoints(self):
        self.points = [(self.x, self.y-self.height/2), (self.x-self.width/2, self.y+self.height/2), (self.x+self.width/2, self.y+self.height/2)]

    def BoundedX(self, cx):
        if cx < 1 + 10:
            cx = 1 + 10

        if cx > self.windowWidth - 10:
            cx = self.windowWidth - 10
        return cx

    def BoundedY(self, cy):
        if cy < 1 + 15:
            cy = 1 + 15

        if cy > self.windowHeight - 15:
            cy = self.windowHeight - 15
        return cy

    # Perform logical updates to player
    def Update(self):
        self.UpdateSpeed()

        cx = self.x
        cy = self.y
        vDir = self.vertDirection
        hDir = self.horizDirection

        # update position based on speed and direction
        cx += hDir * self.maxSpeed * self.speed
        cy += vDir * self.maxSpeed * self.speed

        # Keep new position within screen bounds
        cx = self.BoundedX(cx)
        cy = self.BoundedY(cy)

        self.x = cx
        self.y = cy

    def Draw(self):
        self.UpdatePoints()
        pygame.draw.polygon(self.surface, self.color, self.points)

