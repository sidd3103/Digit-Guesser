import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
window = pygame.display.set_mode((200, 200))
radius = 5
positions = []


def draw():
    for p in positions:
        pygame.draw.circle(window, black, p, radius)

def main():
    run = True
    reset = False
    while run:
        window.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    global positions
                    positions.append(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset = True

        if reset:
            positions.clear()

        window.fill(white)
        if reset:
            reset = False
        else:
            draw()

        pygame.display.update()


main()
