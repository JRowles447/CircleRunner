import pygame

def run_game():
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    screen = pygame.display.set_mode((800, 600))
    done = False
    is_blue = True
    x = 20
    y = 280

    #Font object for game over
    myfont = pygame.font.SysFont('Trebuchet', 70)


    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y > 0: y -= 4
        if pressed[pygame.K_DOWN] and y < 560: y += 4
        # if pressed[pygame.K_LEFT]: x -= 3
        # if pressed[pygame.K_RIGHT]: x += 3

        screen.fill(BLACK)

        pygame.draw.rect(screen, BLUE, (x, y, 40, 40))

        #Check if the player goes off the screen
        # if x >= 760 or y >= 560 or x <= 40 or y <=40:
        #     screen.fill(WHITE)
        #     textSurface = myfont.render('Game Over', False, RED)
        #     screen.blit(textSurface, (310,250))

        pygame.display.flip()
        clock.tick(60)



def main():
    run_game()

if __name__ == '__main__':
    main()