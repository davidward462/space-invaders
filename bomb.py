import pygame

def SpawnBomb(x, y, color, windowWidth, windowHeight, surface):
    newBomb = Bomb(x, y, color, windowWidth, windowHeight, surface)
    return newBomb

class Bomb:

    def __init__(self, x, y, color, windowWidth, windowHeight, surface):
        self.x = x
        self.y = y

        #self.length = 10
        #self.width = 5
        self.radius = 7
        self.collisionDistance = 7

        # surface details (for drawing and borders)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.surface = surface
        
        # Direction can be 0, -1, or 1
        self.vertDirection = 1 
        self.horizDirection = 0

        # Intended speed of the bomb
        self.maxSpeed = 0.5

        self.color = color

    def IsOutOfBounds(self):
        result = False
        cx = self.x
        cy = self.y
        if cy < windowHeight:
            result = True
        return result

    def Update(self):

        cx = self.x
        cy = self.y
        vDir = self.vertDirection
        hDir = self.horizDirection

        # update position based on speed and direction
        cx += hDir * self.maxSpeed
        cy += vDir * self.maxSpeed

        self.y = cy
        self.x = cx
        self.vertDirection = vDir
        self.horizDirection = hDir

    def Draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)


