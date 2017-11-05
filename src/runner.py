import pygame

def run_game():
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)


    print(pygame.joystick.get_init())
    print(pygame.joystick.get_count())

    cont = pygame.joystick.Joystick(1)
    cont.init()
    print(cont.get_name())
    print(cont.get_numbuttons())
    print(cont.get_numballs())

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
            if event.type == pygame.JOYBUTTONDOWN:
                print("done")
        pressed = pygame.key.get_pressed()
        if cont.get_button(1):
            print("button 1 was pressed")
        if cont.get_button(2):
            print("button 2 was pressed")
        if cont.get_button(3):
            print("button 3 was pressed")
        if cont.get_button(4):
            print("button 4 was pressed")
        if cont.get_button(5):
            print("button 5 was pressed")
        if cont.get_button(6):
            print("button 6 was pressed")
        if cont.get_button(7):
            print("button 7 was pressed")
        if cont.get_button(8):
            print("button 8 was pressed")
        if cont.get_button(9):
            print("button 9 was pressed")
        if cont.get_button(10):
            print("button 10 was pressed")
        if cont.get_button(11):
            print("button 11 was pressed")
        if cont.get_button(12):
            print("button 12 was pressed")
        if cont.get_button(13):
            print("button 13 was pressed")
        if cont.get_button(14):
            print("button 14 was pressed")
        if cont.get_button(15):
            print("button 15 was pressed")
        if cont.get_button(0):
            print("button 0 was pressed")


        if pressed[pygame.K_UP] and y > 0: y -= 4
        if pressed[pygame.K_DOWN] and y < 560: y += 4

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