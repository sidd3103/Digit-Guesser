import pygame
from keras.models import load_model
import numpy as np
from keras.preprocessing import image

pygame.init()
# Dimensions of Window
WINDOW_HEIGHT = 650
WINDOW_WIDTH = 500
# Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
# Font
text_font = pygame.font.SysFont('comicsans', 35)
# Convolutional model
model = load_model('model.h5')


class Guesser:
    def __init__(self, width, height):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Digit Guesser')
        self.radius = 16
        rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_WIDTH)
        self.canvas = self.window.subsurface(rect)
        self.positions = []

    @staticmethod
    def eval():
        img = image.load_img('predict.jpg', target_size=(28, 28), color_mode='grayscale')
        img = image.img_to_array(img)
        img = img.astype('float32') / 255
        img = np.expand_dims(img, axis=0)
        p = model.predict(img)
        return np.argmax(p)

    def instructions(self, number):
        m1 = text_font.render("Press R to reset", True, black)
        self.window.blit(m1, (10, 510))
        m2 = text_font.render("Press P to predict", True, black)
        self.window.blit(m2, (10, 540))

        if number != -1:
            m3 = text_font.render("The digit drawn is (might be)  " + str(number), True, red)
            self.window.blit(m3, (10, 580))

    def update(self, number):
        self.window.fill(white)
        self.canvas.fill(black)
        self.draw()
        self.instructions(number)
        pygame.display.update()

    def draw(self):
        for pos in self.positions:
            pygame.draw.circle(self.canvas, white, pos, self.radius)

    def start(self):
        run = True
        reset = False
        predict = False
        number = -1
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    self.positions.append(pos)

                if event.type == pygame.KEYDOWN:
                    reset = (event.key == pygame.K_r)
                    predict = (event.key == pygame.K_p)

            if predict:
                pygame.image.save(self.canvas, 'predict.jpg')
                number = Guesser.eval()
                predict = False

            if reset:
                reset = False
                number = -1
                self.positions.clear()

            self.update(number)


g = Guesser(WINDOW_WIDTH, WINDOW_HEIGHT)
g.start()
pygame.quit()
