import numpy as np
import random

#colour imports
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#list of colour order (top, front, bottom, back, left, right)
colours = [GREEN, WHITE, BLUE, YELLOW, RED, ORANGE]

class Cube():

    #creates solved rubiks cube
    def __init__(self):
        self.layout = np.empty((6, 3, 3, 3))

        for index, colour in enumerate(colours):
            self.layout[index] =  np.full((3, 3, 3), colour)

    #changes values in array based on how the cube is turned
    def turn(self, dir):
        if dir == "LU":
            temp = np.copy(self.layout[0][0])
            self.layout[0][0], self.layout[1][0], self.layout[2][0], self.layout[3][0] = self.layout[1][0], self.layout[2][0], self.layout[3][0], temp
            self.layout[4] = np.rot90(self.layout[4], 3)
        elif dir == "LD":
            temp = np.copy(self.layout[3][0])
            self.layout[3][0], self.layout[2][0], self.layout[1][0], self.layout[0][0] = self.layout[2][0], self.layout[1][0], self.layout[0][0], temp
            self.layout[4] = np.rot90(self.layout[4])
        elif dir == "RU":
            temp = np.copy(self.layout[0][2])
            self.layout[0][2], self.layout[1][2], self.layout[2][2], self.layout[3][2] = self.layout[1][2], self.layout[2][2], self.layout[3][2], temp
            self.layout[5] = np.rot90(self.layout[5])
        elif dir == "RD":
            temp = np.copy(self.layout[3][2])
            self.layout[3][2], self.layout[2][2], self.layout[1][2], self.layout[0][2] = self.layout[2][2], self.layout[1][2], self.layout[0][2], temp
            self.layout[5] = np.rot90(self.layout[5], 3)
        elif dir == "UR":
            temp = np.copy(np.flip(self.layout[2][:, 0], 0))
            self.layout[2][:, 0], self.layout[4][2], self.layout[0][:, 2], self.layout[5][0] = self.layout[4][2], np.flip(self.layout[0][:, 2], 0), self.layout[5][0], temp
            self.layout[1] = np.rot90(self.layout[1], 3)
        elif dir == "UL":
            temp = np.copy(self.layout[2][:, 0])
            self.layout[2][:, 0], self.layout[5][0], self.layout[0][:, 2], self.layout[4][2] = np.flip(self.layout[5][0], 0), self.layout[0][:, 2], np.flip(self.layout[4][2], 0), temp
            self.layout[1] = np.rot90(self.layout[1])
        elif dir == "DR":
            temp = np.copy(np.flip(self.layout[2][:, 2], 0))
            self.layout[2][:, 2], self.layout[4][0], self.layout[0][:, 0], self.layout[5][2] = self.layout[4][0], np.flip(self.layout[0][:, 0], 0), self.layout[5][2], temp
            self.layout[3] = np.rot90(self.layout[3])
        elif dir == "DL":
            temp = np.copy(self.layout[2][:, 2])
            self.layout[2][:, 2], self.layout[5][2], self.layout[0][:, 0], self.layout[4][0] = np.flip(self.layout[5][2], 0), self.layout[0][:, 0], np.flip(self.layout[4][0], 0), temp
            self.layout[3] = np.rot90(self.layout[3], 3)
        elif dir == "FR":
            temp = np.copy(self.layout[1][:, 2])
            self.layout[1][:, 2], self.layout[4][:, 2], self.layout[3][:, 0], self.layout[5][:, 2] = self.layout[4][:, 2], np.flip(self.layout[3][:, 0], 0), np.flip(self.layout[5][:, 2], 0), temp
            self.layout[2] = np.rot90(self.layout[2])
        elif dir == "FL":
            temp = np.copy(self.layout[1][:, 2])
            self.layout[1][:, 2], self.layout[5][:, 2], self.layout[3][:, 0], self.layout[4][:, 2] = self.layout[5][:, 2], np.flip(self.layout[3][:, 0], 0), np.flip(self.layout[4][:, 2], 0), temp
            self.layout[2] = np.rot90(self.layout[2], 3)
        elif dir == "BR":
            temp = np.copy(self.layout[1][:, 0])
            self.layout[1][:, 0], self.layout[4][:, 0], self.layout[3][:, 2], self.layout[5][:, 0] = self.layout[4][:, 0], np.flip(self.layout[3][:, 2], 0), np.flip(self.layout[5][:, 0], 0), temp
            self.layout[0] = np.rot90(self.layout[0], 3)
        elif dir == "BL":
            temp = np.copy(self.layout[1][:, 0])
            self.layout[1][:, 0], self.layout[5][:, 0], self.layout[3][:, 2], self.layout[4][:, 0] = self.layout[5][:, 0], np.flip(self.layout[3][:, 2], 0), np.flip(self.layout[4][:, 0], 0), temp
            self.layout[0] = np.rot90(self.layout[0])

    #randomly does <turns> turns, essentially scrambling the cube
    def scramble(self, turns = 50):
        moves = ['LU', 'LD', 'RU', 'RD', 'UR', 'UL', 'DR', 'DL', 'FR', 'FL', 'BR', 'BL']
        for i in range(turns):
            self.turn(random.choice(moves))

    def compare_colours(self, s1, s2):
        for i in range(3):
            if s1[i] != s2[i]:
                return False
        return True
    
    #Checks that all faces have a solid colour, signifying a solved cube
    def is_solved(self):
        for face in self.layout:
            for row in face:
                if not self.compare_colours(row[0], row[1]) or not self.compare_colours(row[1], row[2]):
                    return False
        return True