import sys
import pygame


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

    screen.blit(background, (0, 0))
    pygame.display.flip()

    first_click = True
    save_coords = (0, 0)
    while True:

        # wait for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # when left mouse button is pressed, capture position
        get_click = pygame.mouse.get_pressed()
        if get_click[0] > 0:
            if first_click:
                save_coords = pygame.mouse.get_pos()
                first_click = False
            else:
                pygame.draw.line(screen, (255, 255, 255),
                                 save_coords, pygame.mouse.get_pos())
                save_coords = pygame.mouse.get_pos()
            pygame.display.flip()

        # if the mouse buttons aren't pressed, we reset the start of the line
        else:
            save_coords = (0, 0)
            first_click = True


main()
