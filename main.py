import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    green = pygame.Color('green')
    points = [(10, 10), (15, 280)]
    pygame.draw.rect(screen, green, points, 0)
    white = pygame.Color('white')
    points = [(15, 15), (280, 45)]
    pygame.draw.rect(screen, white, points, 0)
    blue = pygame.Color('blue')
    points = [(15, 15+45), (280, 45)]
    pygame.draw.rect(screen, blue, points, 0)


if __name__ == '__main__':
    draw()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()