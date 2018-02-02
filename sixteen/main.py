#!/usr/bin/env python

# Game Sixteen in Python
# Target:
# Order the matrix like this:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15  0]]

import numpy as np
import time
import os

# Define game target
target = list(range(1, 16))
target = np.array(target + [0]).reshape(4,4)


class Game(object):
    def __init__(self):
        self.state = True

    def _init_pane(self):
        # Initialize game pane
        numbers = np.arange(16)
        np.random.shuffle(numbers)
        mat = numbers.reshape(4,4)
        self.mat = mat

    def start(self):
        # init pane
        self._init_pane()
        while (self.mat==target).sum()!=16:
            # Ask an input
            while True:
                os.system('clear')
                self.print_mat()
                print("      Input 'over' to end the game.")
                x = input("   Input the number you want to move: ")
                # Validate x input
                if x == 'over': break
                elif str.isdigit(x) and int(x)<16 and int(x)>0: break
            if x == 'over': break
            x = int(x)
            # Find x location
            location = np.where(self.mat == x)
            location = list(map(int, location))
            # If there is 0 in x's UP,DOWN,RIGHT,LEFT
            up = (max(location[0]-1, 0), location[1])
            down = (min(location[0]+1, 3), location[1])
            right = (location[0], min(location[1]+1, 3))
            left = (location[0], max(location[1]-1, 0))
            if self.mat[up] == 0:
                print('up is 0')
                # swap 0 and UP
                self.mat[location[0], location[1]] = 0
                self.mat[up] = x

            elif self.mat[down] == 0:
                print('down is 0')
                self.mat[location[0], location[1]] = 0
                self.mat[down] = x

            elif self.mat[right] == 0:
                print('right is 0')
                self.mat[location[0], location[1]] = 0
                self.mat[right] = x

            elif self.mat[left] == 0:
                print('left is 0')
                self.mat[location[0], location[1]] = 0
                self.mat[left] = x

        self.state = False
        # Game over
        self.show_gameover()

    def show_gameover(self):
        os.system('clear')
        self.print_mat()
        print("           ***GAME OVER***")
        cont = input("        Another game? (y/[n]): ") or 'n'
        if cont.lower().startswith('y'):
            # another game
            self.state = True

    def print_mat(self):
        print("\n")
        print("            ***SIXTEEN***")
        pattern = """
        #####################
        | {: >2} | {: >2} | {: >2} | {: >2} |
        #####################
        | {: >2} | {: >2} | {: >2} | {: >2} |
        #####################
        | {: >2} | {: >2} | {: >2} | {: >2} |
        #####################
        | {: >2} | {: >2} | {: >2} | {: >2} |
        #####################
"""
        print(pattern.format(*self.mat.ravel()).replace(' 0', '  '))

def main():
    game = Game()
    while game.state == True:
        game.start()


if __name__ == "__main__": 
    main()
