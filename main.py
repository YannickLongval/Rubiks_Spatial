import pygame
import time
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
colours = [GREEN, WHITE, BLUE, YELLOW, RED, ORANGE]
cube = np.empty((6, 3, 3, 3))

ARROW_IMAGE = pygame.image.load(os.path.join('img/Arrow.png'))
ARROW_TURN_IMAGE = pygame.image.load(os.path.join("img/Arrow_Turn.png"))
ARROW_TURN = pygame.transform.scale(ARROW_TURN_IMAGE, (45, 45))
ARROW_UP = pygame.transform.scale(ARROW_IMAGE, (45, 45))
ARROW_RIGHT = pygame.transform.rotate(ARROW_UP, 270)
ARROW_LEFT = pygame.transform.rotate(ARROW_UP, 90)
ARROW_DOWN = pygame.transform.rotate(ARROW_UP, 180)


for index, colour in enumerate(colours):
    cube[index] =  np.full((3, 3, 3), colour)

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (40, 45, 50)

def turn(dir):
    if dir == "LU":
        temp = np.copy(cube[0][0])
        cube[0][0], cube[1][0], cube[2][0], cube[3][0] = cube[1][0], cube[2][0], cube[3][0], temp
        cube[4] = np.rot90(cube[4], 3)
    elif dir == "LD":
        temp = np.copy(cube[3][0])
        cube[3][0], cube[2][0], cube[1][0], cube[0][0] = cube[2][0], cube[1][0], cube[0][0], temp
        cube[4] = np.rot90(cube[4])
    elif dir == "RU":
        temp = np.copy(cube[0][2])
        cube[0][2], cube[1][2], cube[2][2], cube[3][2] = cube[1][2], cube[2][2], cube[3][2], temp
        cube[5] = np.rot90(cube[5])
    elif dir == "RD":
        temp = np.copy(cube[3][2])
        cube[3][2], cube[2][2], cube[1][2], cube[0][2] = cube[2][2], cube[1][2], cube[0][2], temp
        cube[5] = np.rot90(cube[5], 3)
    elif dir == "UR":
        temp = np.copy(np.flip(cube[2][:, 0], 0))
        cube[2][:, 0], cube[4][2], cube[0][:, 2], cube[5][0] = cube[4][2], np.flip(cube[0][:, 2], 0), cube[5][0], temp
        cube[1] = np.rot90(cube[1], 3)
    elif dir == "UL":
        temp = np.copy(cube[2][:, 0])
        cube[2][:, 0], cube[5][0], cube[0][:, 2], cube[4][2] = np.flip(cube[5][0], 0), cube[0][:, 2], np.flip(cube[4][2], 0), temp
        cube[1] = np.rot90(cube[1])
    elif dir == "DR":
        temp = np.copy(np.flip(cube[2][:, 2], 0))
        cube[2][:, 2], cube[4][0], cube[0][:, 0], cube[5][2] = cube[4][0], np.flip(cube[0][:, 0], 0), cube[5][2], temp
        cube[3] = np.rot90(cube[3])
    elif dir == "DL":
        temp = np.copy(cube[2][:, 2])
        cube[2][:, 2], cube[5][2], cube[0][:, 0], cube[4][0] = np.flip(cube[5][2], 0), cube[0][:, 0], np.flip(cube[4][0], 0), temp
        cube[3] = np.rot90(cube[3], 3)
    elif dir == "FR":
        temp = np.copy(cube[1][:, 2])
        cube[1][:, 2], cube[4][:, 2], cube[3][:, 0], cube[5][:, 2] = cube[4][:, 2], np.flip(cube[3][:, 0], 0), np.flip(cube[5][:, 2], 0), temp
        cube[2] = np.rot90(cube[2])
    elif dir == "FL":
        temp = np.copy(cube[1][:, 2])
        cube[1][:, 2], cube[5][:, 2], cube[3][:, 0], cube[4][:, 2] = cube[5][:, 2], np.flip(cube[3][:, 0], 0), np.flip(cube[4][:, 2], 0), temp
        cube[2] = np.rot90(cube[2], 3)
    elif dir == "BR":
        temp = np.copy(cube[1][:, 0])
        cube[1][:, 0], cube[4][:, 0], cube[3][:, 2], cube[5][:, 0] = cube[4][:, 0], np.flip(cube[3][:, 2], 0), np.flip(cube[5][:, 0], 0), temp
        cube[0] = np.rot90(cube[0], 3)
    elif dir == "BL":
        temp = np.copy(cube[1][:, 0])
        cube[1][:, 0], cube[5][:, 0], cube[3][:, 2], cube[4][:, 0] = cube[5][:, 0], np.flip(cube[3][:, 2], 0), np.flip(cube[4][:, 0], 0), temp
        cube[0] = np.rot90(cube[0])
def draw_window():
    WIN.fill(BACKGROUND)
    for i in range(4):
        for j in range(len(cube[i])):
            for k in range(len(cube[i][j])):
                pygame.draw.rect(WIN, cube[i][j][k], pygame.Rect(50*j + 229, 50*k + 155*i + 70, 45, 45))
    for i in range(2):
        for j in range(len(cube[i])):
            for k in range(len(cube[i][j])):
                pygame.draw.rect(WIN, cube[i + 4][j][k], pygame.Rect(50*j + 310*i + 74, 50*k + 225, 45, 45))
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
                    turn("LU")
                elif 329 <= mouse[0] <= 329 + 45 and 13 <= mouse[1] <= 13 + 45:
                    turn("RU") 
                elif 229 <= mouse[0] <= 229 + 45 and 690 <= mouse[1] <= 690 + 45:
                    turn("LD")
                elif 329 <= mouse[0] <= 329 + 45 and 690 <= mouse[1] <= 690 + 45:
                    turn("RD")
                elif 19 <= mouse[0] <= 19 + 45 and 225 <= mouse[1] <= 225 + 45:
                    turn("BL")
                elif 19 <= mouse[0] <= 19 + 45 and 325 <= mouse[1] <= 325 + 45:
                    turn("FL")
                elif 539 <= mouse[0] <= 539 + 45 and 225 <= mouse[1] <= 225 + 45:
                    turn("BR")
                elif 539 <= mouse[0] <= 539 + 45 and 325 <= mouse[1] <= 325 + 45:
                    turn("FR")
                elif 384 <= mouse[0] <= 384 + 45 and 170 <= mouse[1] <= 170 + 45:
                    turn("UL")
                elif 174 <= mouse[0] <= 174 + 45 and 170 <= mouse[1] <= 170 + 45:
                    turn("UR")
                elif 384 <= mouse[0] <= 384 + 45 and 480 <= mouse[1] <= 480 + 45:
                    turn("DR")
                elif 174 <= mouse[0] <= 174 + 45 and 480 <= mouse[1] <= 480 + 45:
                    turn("DL")
        mouse = pygame.mouse.get_pos()
                    
        draw_window()


if __name__ == "__main__":
    main()