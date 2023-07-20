import pygame
import player
import enemy
import bullet
import random

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

window = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('favicon.ico')
pygame.display.set_icon(icon)

# constants
white = (255, 255, 255)
black = (0, 0, 0)

# Return true if the two given lines cross one another, false otherwise
def LinesIntersect(lineA, lineB):
    result = False
    return result

# Return true if the two given objects have collided with one another, false otherwise.
def ObjectsCollide(objA, objB):
    result = False
    return result


def main():

    # Create player.
    playerObj = player.Player(400, 500, white, WINDOW_WIDTH, WINDOW_HEIGHT, window)

    # Create list of enemies that exist.
    enemyList = enemy.SpawnEnemy(3, WINDOW_WIDTH, WINDOW_HEIGHT, window, white)

    # Create list of bullets that have been fired.
    bulletList = []

    # game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                raise SystemExit

            # when key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    playerObj.SetVertDirection(-1)
                if event.key == pygame.K_a:
                    playerObj.SetHorizDirection(-1)
                if event.key == pygame.K_s:
                    playerObj.SetVertDirection(1)
                if event.key == pygame.K_d:
                    playerObj.SetHorizDirection(1)
                if event.key == pygame.K_SPACE:
                    newBullet = bullet.SpawnBullet(playerObj.x, playerObj.y-20, white, WINDOW_WIDTH,WINDOW_HEIGHT,window)
                    bulletList.append(newBullet)
                if event.key == pygame.K_r: # restart
                    main() # where does the previously allocated memory go?
            
            # when key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    if playerObj.vertDirection == -1:
                        playerObj.SetVertDirection(0)
                if event.key == pygame.K_a:
                    if playerObj.horizDirection == -1:
                        playerObj.SetHorizDirection(0)
                if event.key == pygame.K_s:
                    if playerObj.vertDirection == 1:
                        playerObj.SetVertDirection(0)
                if event.key == pygame.K_d:
                    if playerObj.horizDirection == 1:
                        playerObj.SetHorizDirection(0)

        # Logic updates
        playerObj.Update()
        
        for e in enemyList:
            e.Update()

        updateIndex = 0
        for b in bulletList:
            b.Update()

            # check if bullet has gone past top of screen
            outOfBounds = b.IsOutOfBounds()
            if outOfBounds:
                del bulletList[updateIndex] # remove object from list
                continue                    # go to next iteration of for loop
            updateIndex = updateIndex + 1

        # Check collisions

        # Player collisions

        # Bullet collisions
    
        # Graphical updates
            
        # background color
        window.fill(black)

        # update the entire display
        playerObj.Draw()

        for e in enemyList:
            e.Draw()

        for b in bulletList:
            b.Draw()
            
        pygame.display.flip()

main()

