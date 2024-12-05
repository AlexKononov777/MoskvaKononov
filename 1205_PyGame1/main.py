import random

import pygame

def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    txt = font.render("Q, niggers!",
                      True,
                      (100, 255, 100))
    coors_x = width // 2 - txt.get_width() // 2
    coord_y = height // 2 - txt.get_height() // 2
    txt_w = txt.get_width()
    txt_h = txt.get_height()
    screen.blit(txt, (coors_x, coord_y))
    pygame.draw.rect(screen, (0, 255, 0), (coors_x - 10, coord_y - 10, txt_w + 20, txt_h + 20), 1)


def draw2(screen):
    for i in range(1000):
        screen.fill(pygame.Color('red'),
                    (random.random() * width,
                    random.random() * height, 2, 2))




if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    draw(screen)

    # смена кадров
    pygame.display.flip()

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()