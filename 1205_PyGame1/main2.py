import pygame, sys

n = data = list(map(str.strip, sys.stdin))
for i in n:
    i = i.split()
    if i[0] == int or i[1] == int:
        pygame.init()
        screen = pygame.display.set_mode((i[0], i[1]))
        pygame.display.set_caption('Крест')
        running = True
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, n[0], n[1]), 5)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("black")
            pygame.display.flip()
    else:
        print('Неправильный формат ввода')

pygame.quit()