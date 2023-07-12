import pygame
import entities
import random

pygame.init()

window_Height = 600
window_Width = 800

window = pygame.display.set_mode( (window_Width, window_Height) )

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
        enemy = entities.Enemy(enemyX, enemyY, white, window_Width, window_Height, window)
        enemy.SetHorizDirection(1)
        enemyList.append(enemy)
    return enemyList

def main():

    # Create player
    player = entities.Player(400, 500, white, window_Width, window_Height, window)

    # Create enemies
    enemies = CreateEnemy(3, window_Width, window_Height, window)

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
                    player.SetVertDirection(-1)
                if event.key == pygame.K_a:
                    player.SetHorizDirection(-1)
                if event.key == pygame.K_s:
                    player.SetVertDirection(1)
                if event.key == pygame.K_d:
                    player.SetHorizDirection(1)
                if event.key == pygame.K_r: # restart
                    main() # where does the previously allocated memory go?
            
            # when key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.SetVertDirection(0)
                if event.key == pygame.K_a:
                    player.SetHorizDirection(0)
                if event.key == pygame.K_s:
                    player.SetVertDirection(0)
                if event.key == pygame.K_d:
                    player.SetHorizDirection(0)

        # Logic updates
        player.Update()
        for enemy in enemies:
            enemy.Update()
    
        # Graphical updates
            
        # background color
        window.fill(black)

        # update the entire display
        player.Draw()
        for enemy in enemies:
            enemy.Draw()
            
        pygame.display.flip()

main()

