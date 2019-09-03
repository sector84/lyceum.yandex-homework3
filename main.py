import pygame

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)


def draw():
    red = pygame.Color('red')
    points = [(15, 15+90), (280, 15+135)]
    pygame.draw.rect(screen, red, points, 0)


if __name__ == '__main__':
    draw()

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()