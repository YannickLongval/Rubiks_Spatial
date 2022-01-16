import pygame
import time
import os
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN
from cube import Cube
pygame.font.init()

#button sizes
ARROW_BUTTON_SIZE = (45, 45)

#load in images
ARROW_IMAGE = pygame.image.load(os.path.join('img/Arrow.png'))
ARROW_TURN_IMAGE = pygame.image.load(os.path.join("img/Arrow_Turn.png"))
ARROW_TURN = pygame.transform.scale(ARROW_TURN_IMAGE, ARROW_BUTTON_SIZE)
ARROW_UP = pygame.transform.scale(ARROW_IMAGE, ARROW_BUTTON_SIZE)
ARROW_RIGHT = pygame.transform.rotate(ARROW_UP, 270)
ARROW_LEFT = pygame.transform.rotate(ARROW_UP, 90)
ARROW_DOWN = pygame.transform.rotate(ARROW_UP, 180)

# Locations of arrows and action if pressed
buttons = {
    (229, 13): "LU",
    (329, 13): "RU",
    (229, 690): "LD",
    (329, 690): "RD",
    (19, 225): "BL",
    (19, 325): "FL",
    (539, 225): "BR",
    (539, 325): "FR",
    (384, 170): "UL",
    (174, 170): "UR",
    (384, 480): "DR",
    (174, 480): "DL"
}

#font imports
TEXT_FONT = pygame.font.SysFont('comicsans', 80)
SMALL_TEXT = pygame.font.SysFont('comicsans', 40)

cube = Cube()

WIDTH, HEIGHT = 600, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (40, 45, 50)

def draw_menu_window():
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100))
    WIN.blit(TEXT_FONT.render('START', 1, (255, 255, 255)), (WIDTH // 2 - 90, HEIGHT // 2 - 25))
    WIN.blit(TEXT_FONT.render("RUBIK'S SPATIAL", 1, (255, 255, 255)), (WIDTH // 2 - 220, 100))
    pygame.display.update()
    
def draw_pause_window():
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 190, HEIGHT // 2 - 225, 400, 100))
    WIN.blit(TEXT_FONT.render('RESUME', 1, (255, 255, 255)), (WIDTH // 2 - 120, HEIGHT // 2 - 200))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 190, HEIGHT // 2 - 25, 400, 100))
    WIN.blit(TEXT_FONT.render('MAIN MENU', 1, (255, 255, 255)), (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.update()

def draw_win_window():
    WIN.fill(BACKGROUND)
    WIN.blit(TEXT_FONT.render('YOU WIN', 1, (255, 255, 255)), (WIDTH // 2 - 120, 50))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 190, HEIGHT // 2 - 225, 400, 100))
    WIN.blit(TEXT_FONT.render('RESTART', 1, (255, 255, 255)), (WIDTH // 2 - 120, HEIGHT // 2 - 200))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH // 2 - 190, HEIGHT // 2 - 25, 400, 100))
    WIN.blit(TEXT_FONT.render('MAIN MENU', 1, (255, 255, 255)), (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.update()

def draw_game_window():
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
    WIN.blit(ARROW_TURN, (384, 480))
    WIN.blit(pygame.transform.flip(ARROW_TURN, True, False), (174, 480))
    pygame.draw.rect(WIN, (255, 0, 0), pygame.Rect(WIDTH - 130, 20, 110, 50))
    WIN.blit(SMALL_TEXT.render('PAUSE', 1, (255, 255, 255)), (WIDTH - 120, 30))
    pygame.display.update()

def main():
    state = 'menu'
    run = True
    while run:

        #shows menu screen until start button is pressed
        if state == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 100 <= mouse[0] <= WIDTH // 2 + 100 and HEIGHT // 2 - 50 <= mouse[1] <= HEIGHT // 2 + 50:
                        state = 'play'
                        cube.scramble()
            mouse = pygame.mouse.get_pos()
            draw_menu_window()

        #screen with cube that player can rotate with arrows
        elif state == "play":
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in buttons:
                        if item[0] <= mouse[0] <= item[0] + ARROW_BUTTON_SIZE[0] and item[1] <= mouse[1] <= item[1] + ARROW_BUTTON_SIZE[1]:
                            cube.turn(buttons[item])
                    if WIDTH - 130 <= mouse[0] <= WIDTH - 20 and 20 <= mouse[1] <= 70:
                        state = "pause"
            mouse = pygame.mouse.get_pos()

            if cube.is_solved():
                state = "win"
                        
            draw_game_window()

        #pause screen has resume and main menu buttons, to either return to game or go to menu screen
        elif state == 'pause':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 190 <= mouse[0] <= WIDTH // 2 + 210 and HEIGHT // 2 - 225 <= mouse[1] <= HEIGHT // 2 - 125:
                        state = 'play'
                    elif WIDTH // 2 - 190 <= mouse[0] <= WIDTH // 2 + 210 and HEIGHT // 2 - 25 <= mouse[1] <= HEIGHT // 2 + 75:
                        state = 'menu'
            mouse = pygame.mouse.get_pos()

            draw_pause_window()

        #win screen when player completes cube
        elif state == 'win':
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 190 <= mouse[0] <= WIDTH // 2 + 210 and HEIGHT // 2 - 225 <= mouse[1] <= HEIGHT // 2 - 125:
                        cube.scramble()
                        state = 'play'
                    elif WIDTH // 2 - 190 <= mouse[0] <= WIDTH // 2 + 210 and HEIGHT // 2 - 25 <= mouse[1] <= HEIGHT // 2 + 75:
                        state = 'menu'
            mouse = pygame.mouse.get_pos()

            draw_win_window()


if __name__ == "__main__":
    main()