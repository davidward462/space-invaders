import pygame
import math
import player
import enemy
import bullet
import random

pygame.init()
pygame.font.init()

debug = False

# For debugging
if debug:
    print(f"pygame initialized = {pygame.get_init()}")
    print(f"fonts initialized = {pygame.font.get_init()}")

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800

window = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('favicon.ico')
pygame.display.set_icon(icon)

# constants
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)

# Return true if the two given lines cross one another, false otherwise
def LinesIntersect(lineA, lineB):
    result = False
    return result

# Return true if the two given objects have collided with one another, false otherwise.
# TODO: make this use the points from the objects.
def ObjectsCollide(objA, objB):
    result = False
    Ax = objA.x
    Ay = objA.y
    Bx = objB.x
    By = objB.y

    # distance between object positions
    a = Ax - Bx
    b = Ay - By 
    inner = (a**2) + (b**2)
    distance = math.sqrt(inner)

    radiusA = objA.collisionDistance
    radiusB = objB.collisionDistance

    radiusSum = radiusA + radiusB

    if radiusSum >= distance:
        result = True
    else:
        return False

    return result

def CloseProgram():
    pygame.font.quit()
    pygame.quit()
    raise SystemExit


def main():

    # Create player.
    playerObj = player.Player(400, 500, white, WINDOW_WIDTH, WINDOW_HEIGHT, window)
    playerWin = False

    # Create list of enemies that exist.
    enemyList = enemy.SpawnEnemy(5, WINDOW_WIDTH, WINDOW_HEIGHT, window, white)

    # Create list of bullets that have been fired.
    bulletList = []

    # Create font that displays on player death
    deathFont = pygame.font.SysFont('freesansbold', 32)

    # Create font that displays when player wins
    winFont = pygame.font.SysFont('freesansbold', 32)

    # Create text surface object
    deathText = deathFont.render('You died.', True, white, black)

    # Create text surface object
    winText = winFont.render('You win!', True, white, black)

    deathTextRec = deathText.get_rect()
    deathTextRec.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    winTextRect = winText.get_rect()
    winTextRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # game loop
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                CloseProgram()

            # when key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # restart
                    main() # where does the previously allocated memory go?
                if event.key == pygame.K_ESCAPE:
                    run = False
                    CloseProgram()
                if playerObj.isAlive: # player control
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

        # Check collisions
        itemIndex = 0

        # Enemy collisions
        for e in enemyList:

            if ObjectsCollide(playerObj, e):
                playerObj.isAlive = False

            # if enemy collides with bullet
            for b in bulletList:
                if ObjectsCollide(e, b):
                    del enemyList[itemIndex]
                    continue
            itemIndex = itemIndex + 1

        # Bullet collisions
        itemIndex = 0
        for b in bulletList:
            b.Update()

            # check if bullet has gone past top of screen
            outOfBounds = b.IsOutOfBounds()
            if outOfBounds:
                del bulletList[itemIndex] # remove object from list
                continue                    # go to next iteration of for loop
            itemIndex = itemIndex + 1

        # Player wins if all enemies are destroyed
        if len(enemyList) == 0:
            playerWin = True
    
        # Graphical updates
            
        # background color
        window.fill(black)

        # update the entire display
        playerObj.Draw()

        # Draw all enemies
        for e in enemyList:
            e.Draw()

        # Draw all bullets
        for b in bulletList:
            b.Draw()
            
        if not playerObj.isAlive:
            # If player is dead, copy text surface to display surface
            window.blit(deathText, deathTextRec)

        if playerWin:
            # If player wins, copy text surface to display surface
            window.blit(winText, winTextRect)

        # Update display
        pygame.display.flip()

main()

