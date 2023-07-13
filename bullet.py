import pygame

class Bullet:

    def __init__(self, x, y, windowWidth, windowHeight, color):
        self.x = x
        self.y = y

        #self.length = 10
        #self.width = 5
        self.radius = 5

        # surface details (for drawing and borders)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.surface = surface
        
        # Direction can be 0, -1, or 1
        # The enemy is moving downwards.
        self.vertDirection = 0
        self.horizDirection = 0

        # Intended speed of the player
        self.maxSpeed = 0.5

        self.color = color


    def Draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)



