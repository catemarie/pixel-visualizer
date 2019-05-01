import sys
import pygame

# note: to set pixel 100, 100 to white:
# background.set_at((100, 100), (255, 255, 255))


def main():

    pygame.init()

    # default size - 100x100 px
    size = width, height = 500, 500

    # default color - black
    black = 0, 0, 0

    # set up this screen
    screen = pygame.display.set_mode(size)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)

    while True:

        # wait for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # when left mouse button is pressed, capture position
        get_click = pygame.mouse.get_pressed()
        if get_click[0] > 0:
            print(str(pygame.mouse.get_pos()))

        # update display
        screen.blit(background, (0, 0))
        pygame.display.flip()


main()
