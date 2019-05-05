import sys
import pygame
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description='Generate image from pixels or '
        'generate pixels from image.')
    parser.add_argument('-s', dest='size', type=int, default=100,
                        help='size in pixels x pixels (square)')
    parser.add_argument('filename')
    args = parser.parse_args()

    size = args.size
    filename = args.filename

    # default color - black
    black = 0, 0, 0

    # set up this screen
    pygame.init()

    screen = pygame.display.set_mode((size, size))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    # read bytes from file if it already exists
    pix_list = []
    if not os.path.exists(filename + '.txt'):
        with open(filename + ".txt", "wb") as f:
            for xx in range(0, size):
                for yy in range(0, size):
                    f.write(
                        bytes([screen.get_at((xx, yy))[0]]))
    with open(filename + ".txt", "rb") as f:
        byte = f.read(1)
        while byte != b"":
            byte = f.read(1)
            pixel = int.from_bytes(byte, "big")
            pix_list.append(pixel)

    if len(pix_list) != size * size:
        print("Bad file size")
        return
    else:
        for xx in range(0, size):
            for yy in range(0, size):
                color = pix_list[size * xx + yy]
                screen.set_at((xx, yy), (color, color, color, 255))

    pygame.display.flip()

    first_click = True
    save_coords = (0, 0)
    while True:

        # wait for exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(filename + ".txt", "wb") as f:
                    for xx in range(0, size):
                        for yy in range(0, size):
                            f.write(
                                bytes([screen.get_at((xx, yy))[0]]))
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
