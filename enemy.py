import pygame
import math
import random

def SpawnEnemy(number, window_Width, window_Height, window, color):
    enemyList = []
    for i in range(0, number):
        enemyX = random.randint(20, window_Width-20)
        enemyY = random.randint(20, window_Height/10)
        e = Enemy(enemyX, enemyY, color, window_Width, window_Height, window)
        e.SetHorizDirection(1)
        enemyList.append(e)
    return enemyList

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

        # Intended speed of the enemy
        self.maxSpeed = 0.3

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
            cy += 30

        # update position based on speed and direction
        cx += hDir * self.maxSpeed

        self.y = cy
        self.x = cx
        self.vertDirection = vDir
        self.horizDirection = hDir


    def Draw(self):
        self.UpdatePoints()
        pygame.draw.polygon(self.surface, self.color, self.points)

