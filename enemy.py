import pygame
import math

class Enemy:
    def __init__(self, x, y, color, windowWidth, windowHeight, surface):

        # position on the screen
        self.x = x
        self.y = y

        # Dimensions
        self.width = 60
        self.height = 40
        
        # surface details (for drawing and borders)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.surface = surface
        
        # Direction can be 0, -1, or 1
        # The enemy is moving downwards.
        self.vertDirection = 0
        self.horizDirection = 0

        # Intended speed of the player
        self.maxSpeed = 0.2

        self.color = color

        self.points = [(self.x+self.width/2, self.y+self.height/2), (self.x-self.width/2, self.y+self.height/2), (self.x-self.width/2, self.y-self.height/2), (self.x+self.width/2, self.y-self.height/2)]

    def UpdatePoints(self):
        self.points = [(self.x+self.width/2, self.y+self.height/2), (self.x-self.width/2, self.y+self.height/2), (self.x-self.width/2, self.y-self.height/2), (self.x+self.width/2, self.y-self.height/2)]

    def SetHorizDirection(self, dir):
        self.horizDirection = dir

    def Update(self):

        cx = self.x
        cy = self.y
        vDir = self.vertDirection
        hDir = self.horizDirection
        
        # check if enemy should bounce
        if cx < 0 or cx >= self.windowWidth:
            hDir *= -1
            cy += 20

        # update position based on speed and direction
        cx += hDir * self.maxSpeed

        self.y = cy
        self.x = cx
        self.vertDirection = vDir
        self.horizDirection = hDir


    def Draw(self):
        self.UpdatePoints()
        pygame.draw.polygon(self.surface, self.color, self.points)

