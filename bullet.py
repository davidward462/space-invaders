import pygame

def SpawnBullet(x, y, color, windowWidth, windowHeight, surface):
    newBullet = Bullet(x, y, color, windowWidth, windowHeight, surface)
    return newBullet

class Bullet:

    def __init__(self, x, y, color, windowWidth, windowHeight, surface):
        self.x = x
        self.y = y

        #self.length = 10
        #self.width = 5
        self.radius = 5
        self.collisionDistance = 5

        # surface details (for drawing and borders)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.surface = surface
        
        # Direction can be 0, -1, or 1
        # The enemy is moving downwards.
        self.vertDirection = -1 
        self.horizDirection = 0

        # Intended speed of the player
        self.maxSpeed = 1.2

        self.color = color

    def IsOutOfBounds(self):
        result = False
        cx = self.x
        cy = self.y
        if cy < 0:
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


