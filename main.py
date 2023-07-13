import pygame
import player
import enemy
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

def CreateEnemy(number, window_Width, window_Height, window):
    enemyList = []
    for i in range(0, number):
        enemyX = random.randint(20, window_Width-20)
        enemyY = random.randint(20, window_Height/10)
        enemy = enemy.Enemy(enemyX, enemyY, white, window_Width, window_Height, window)
        enemy.SetHorizDirection(1)
        enemyList.append(enemy)
    return enemyList

def main():

    # Create player
    thePlayer = player.Player(400, 500, white, WINDOW_WIDTH, WINDOW_HEIGHT, window)

    # Create enemies
    enemies = enemy.CreateEnemy(3, WINDOW_WIDTH, WINDOW_HEIGHT, window, white)

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
                    thePlayer.SetVertDirection(-1)
                if event.key == pygame.K_a:
                    thePlayer.SetHorizDirection(-1)
                if event.key == pygame.K_s:
                    thePlayer.SetVertDirection(1)
                if event.key == pygame.K_d:
                    thePlayer.SetHorizDirection(1)
                if event.key == pygame.K_r: # restart
                    main() # where does the previously allocated memory go?
            
            # when key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    thePlayer.SetVertDirection(0)
                if event.key == pygame.K_a:
                    thePlayer.SetHorizDirection(0)
                if event.key == pygame.K_s:
                    thePlayer.SetVertDirection(0)
                if event.key == pygame.K_d:
                    thePlayer.SetHorizDirection(0)

        # Logic updates
        thePlayer.Update()
        for e in enemies:
            e.Update()
    
        # Graphical updates
            
        # background color
        window.fill(black)

        # update the entire display
        thePlayer.Draw()
        for e in enemies:
            e.Draw()
            
        pygame.display.flip()

main()

