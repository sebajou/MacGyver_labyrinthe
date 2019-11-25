#!/usr/bin/python3
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from constantes import *


class TheMaze:
    """
    This class allow print and control of the maze.
    + Methode "print_maze" realise a pretty commande line print.
        - The paramaters of this methode is the table wich contain the maze.
        - No return argument for this methode.
    + Methode "win" print a message in case of win or lose.
        - Parameter of this methode are boolean about victory
        or die of Mac Gyver.
    + Methode "setTable" load the maze inside a table of table.
    from object create with loadMaze() methode
    Parameter: the txt files containing the maze
    Return the table containing the maze ("rack")
    + Methode "loadMaze" load the maze from txt files.
    Parameter: None.
    Return: loaded maze.
    + Methode "exit": Control if Mac Gyver is at Guard position.
    Parameter: position of Mac Gyver.
    Return boolean wich confirm if Mac Gyver are at Guard position or not.
    """
    def print_maze(self, rack):
        """Pretty print of maze."""
        for j in range(15):
            print("\n", end='')
            for i in range(15):
                print(rack[j][i], end=' ')

    def win(self, victory, die, rack, screen):
        """In case of victory or die."""
        TM = TheMaze()
        if victory:
            # Print a message for the winner.
            myfont = pygame.font.Font("./assets/fonts/free.ttf", 40)
            label = myfont.render("You win !", 1, COLOR_YELLOW)
            screen.blit(label, (10, 10))
            pygame.display.flip()
            # Sound of the winner.
            pygame.mixer.music.stop()
            son_winner = pygame.mixer.Sound("./assets/sounds/winner.wav")
            son_winner.set_volume(0.5)
            son_winner.play(loops=0)
            # Stop the game, time to play the sound.
            length = int(round((son_winner.get_length())*1000.0))
            pygame.time.delay(length)
            for i in range(0, 24):
                print("You win !")
        elif die:
            # Print a message for the loser.
            myfont = pygame.font.Font("./assets/fonts/free.ttf", 40)
            label = myfont.render(
                "You die with a slow, painful death.", 1, COLOR_YELLOW
                )
            screen.blit(label, (10, 10))
            pygame.display.flip()
            # Sound of death.
            pygame.mixer.music.stop()
            son_death = pygame.mixer.Sound("./assets/sounds/death.ogg")
            son_death.set_volume(0.5)
            son_death.play(loops=0)
            # Stop the game, time to play the sound.
            length = int(round((son_death.get_length())*1000.0))
            pygame.time.delay(length)
            for i in range(0, 24):
                print("You die !")
            print("You die with a slow, painful death.")

    def setTable(self, maze):
        """Setting up table of table wich contain the maze."""
        rack = []
        for line in maze:
            list_line = []
            for caractere in line:
                list_line.append(caractere)
            rack.append(list_line)
        return rack

    def loadMaze(self):
        """Load file maze_plan.txt in table of table (rack)."""
        maze = open("maze_plan.txt", "r")
        maze = maze.read()
        maze = maze.split("\n")
        return maze

    def exit(self, y, x):
        """Control if Mac Gyver is at Guard position."""
        guard = False
        if y == 13 and x == 14:
            guard = True
        else:
            pass
        return guard
