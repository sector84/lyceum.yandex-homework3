import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    white = pygame.Color('white')
    points = [(15, 15), (280, 15+45)]
    pygame.draw.rect(screen, white, points, 0)


if __name__ == '__main__':
    draw()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()