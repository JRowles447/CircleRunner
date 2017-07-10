import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    done = False
    is_blue = True
    x = 380
    y = 280

    #Font rendering
    myfont = pygame.font.SysFont('Comic Sans MS', 45)


    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        screen.fill((0, 0, 0))
        if is_blue:
            color = (0, 0, 255)
        else:
            color = (255, 0, 0)
        pygame.draw.circle(screen, color, (x,y), 40)

        if x >= 760 or y >= 560 or x <= 40 or y <=40:
            screen.fill((255, 255, 255))
            textSurface = myfont.render('Game Over', False, (0, 0, 0))
            screen.blit(textSurface, (310,250))

        pygame.display.flip()
        clock.tick(60)



def main():
    run_game()

if __name__ == '__main__':
    main()