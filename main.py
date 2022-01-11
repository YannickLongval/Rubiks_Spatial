import pygame
import time
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
from cube import Cube

ARROW_IMAGE = pygame.image.load(os.path.join('img/Arrow.png'))
ARROW_TURN_IMAGE = pygame.image.load(os.path.join("img/Arrow_Turn.png"))
ARROW_TURN = pygame.transform.scale(ARROW_TURN_IMAGE, (45, 45))
ARROW_UP = pygame.transform.scale(ARROW_IMAGE, (45, 45))
ARROW_RIGHT = pygame.transform.rotate(ARROW_UP, 270)
ARROW_LEFT = pygame.transform.rotate(ARROW_UP, 90)
ARROW_DOWN = pygame.transform.rotate(ARROW_UP, 180)

cube = Cube()

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (40, 45, 50)
    
def draw_window():
    WIN.fill(BACKGROUND)
    for i in range(4):
        for j in range(len(cube.layout[i])):
            for k in range(len(cube.layout[i][j])):
                pygame.draw.rect(WIN, cube.layout[i][j][k], pygame.Rect(50*j + 229, 50*k + 155*i + 70, 45, 45))
    for i in range(2):
        for j in range(len(cube.layout[i])):
            for k in range(len(cube.layout[i][j])):
                pygame.draw.rect(WIN, cube.layout[i + 4][j][k], pygame.Rect(50*j + 310*i + 74, 50*k + 225, 45, 45))
    WIN.blit(ARROW_UP, (229, 13))
    WIN.blit(ARROW_UP, (329, 13))
    WIN.blit(ARROW_RIGHT, (539, 225))
    WIN.blit(ARROW_RIGHT, (539, 325))
    WIN.blit(ARROW_DOWN, (229, 690))
    WIN.blit(ARROW_DOWN, (329, 690))
    WIN.blit(ARROW_LEFT, (19, 225))
    WIN.blit(ARROW_LEFT, (19, 325))
    WIN.blit(ARROW_TURN, (384, 170))
    WIN.blit(pygame.transform.flip(ARROW_TURN, True, False), (174, 170))
    WIN.blit(pygame.transform.flip(ARROW_TURN, False, True), (384, 480))
    WIN.blit(pygame.transform.flip(ARROW_TURN, True, True), (174, 480))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 229 <= mouse[0] <= 229 + 45 and 13 <= mouse[1] <= 13 + 45:
                    cube.turn("LU")
                elif 329 <= mouse[0] <= 329 + 45 and 13 <= mouse[1] <= 13 + 45:
                    cube.turn("RU") 
                elif 229 <= mouse[0] <= 229 + 45 and 690 <= mouse[1] <= 690 + 45:
                    cube.turn("LD")
                elif 329 <= mouse[0] <= 329 + 45 and 690 <= mouse[1] <= 690 + 45:
                    cube.turn("RD")
                elif 19 <= mouse[0] <= 19 + 45 and 225 <= mouse[1] <= 225 + 45:
                    cube.turn("BL")
                elif 19 <= mouse[0] <= 19 + 45 and 325 <= mouse[1] <= 325 + 45:
                    cube.turn("FL")
                elif 539 <= mouse[0] <= 539 + 45 and 225 <= mouse[1] <= 225 + 45:
                    cube.turn("BR")
                elif 539 <= mouse[0] <= 539 + 45 and 325 <= mouse[1] <= 325 + 45:
                    cube.turn("FR")
                elif 384 <= mouse[0] <= 384 + 45 and 170 <= mouse[1] <= 170 + 45:
                    cube.turn("UL")
                elif 174 <= mouse[0] <= 174 + 45 and 170 <= mouse[1] <= 170 + 45:
                    cube.turn("UR")
                elif 384 <= mouse[0] <= 384 + 45 and 480 <= mouse[1] <= 480 + 45:
                    cube.turn("DR")
                elif 174 <= mouse[0] <= 174 + 45 and 480 <= mouse[1] <= 480 + 45:
                    cube.turn("DL")
        mouse = pygame.mouse.get_pos()
                    
        draw_window()


if __name__ == "__main__":
    main()