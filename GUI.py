import pygame
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
from Predict import Predictions

pygame.init()

# Dimensions of Window
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 500

p = Predictions()

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
radius = 13
positions = []
model = load_model('model.h5')
rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_WIDTH)
canvas = window.subsurface(rect)


def draw():
    pygame.draw.line(window, white, (0, WINDOW_WIDTH), (WINDOW_WIDTH, WINDOW_WIDTH), 2)
    for p in positions:
        pygame.draw.circle(window, white, p, radius)


def eval():
    img = image.load_img('predict.jpg', target_size=(28, 28))
    img = image.img_to_array(img)
    x = np.expand_dims(img, axis=0)
    images = np.vstack([x])


def main():
    run = True
    reset = False
    predict = False
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                global positions
                pos = pygame.mouse.get_pos()
                if pos[1] < WINDOW_WIDTH:
                    positions.append(pos)

            if event.type == pygame.KEYDOWN:
                e = event.key
                reset = (e == pygame.K_r)
                predict = (e == pygame.K_p)

        if predict:
            pygame.image.save(canvas, 'predict.jpg')
            print(p.evaluate('predict.jpg'))
            predict = False

        if reset:
            positions.clear()
            reset = False

        window.fill(black)
        draw()
        pygame.display.update()


main()
