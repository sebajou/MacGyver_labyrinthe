#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""
This is a game where you drive Mac Gyver out of a maze.
"""

###############################################################################
# =============================================================================
#                           title: Mac Gyver Maze
# =============================================================================
#                           author: Sébastien Jourdan
#                                    /-\
#                                   c°,°>
#                                    \O/
#                           email: sebajou@gmail.com
#                           society: None
#                           Initial date: November 2019
#                           Version: v1
#                           History: None
#                           Comment: This program is a game
# where you drive Mac Gyver out of a maze.
###############################################################################

# Importation.
from mac_gyver import *
from maze import*
import artefacts
from sound_music_and_message import *
from sys import exit
from constantes import *
from build_maze import *
import pygame
from pygame.locals import *


def main():
    """Function of general game cook."""

    # Pygame initialisation and display setting.
    clock, screen = pygame_initialisation()

    # Instancition.
    ME = MazeElements()
    MG = MacGyver()
    TM = TheMaze()
    AA = artefacts.Aiguille()
    AT = artefacts.Tube()
    AE = artefacts.Ether()
    SD = Sound_and_message()

    # Load file maze_plan.txt in table of table (rack).
    oneMaze = TM.loadMaze()

    # Setting up table of table wich contain the maze.
    rack = TM.setTable(oneMaze)

    # Load all artefacts.
    rack, y_artA, x_artA = AA.loadArtefact(rack=rack)
    rack, y_artT, x_artT = AT.loadArtefact(rack=rack)
    rack, y_artE, x_artE = AE.loadArtefact(rack=rack)

    # Load Mac Gyver (X) at the entrance of maze, rack[y][x].
    rack, y, x = MG.loadMacGyver(rack=rack, y=1, x=0)

    # Music
    SD.play_music()

    # Loop for run the game and pick up instruction.
    guard = False
    count = 0
    victory = False
    die = False
    running = True

    while running:
        # Pygame control FPS.
        delta_ms = clock.tick(FPS)

        # Pygame display maze elements according to build_maze module
        # and according to maze_plan.txt load in rack table.
        ME.pygame_maze_display(rack, screen)

        # variable initialisation.
        direction = None

        # Pygame lisen instruction.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                # Mac Gyver go down.
                if event.key == K_DOWN:
                    direction = "n"
                # Mac Gyver go up.
                if event.key == K_UP:
                    direction = "u"
                # Mac Gyver go right.
                if event.key == K_RIGHT:
                    direction = "j"
                # Mac Gyver go left.
                if event.key == K_LEFT:
                    direction = "h"

        # Moving Mac Gyver.
        rack, y, x = MG.move(direction, rack, y, x)

        # Counter of artefacts.
        count, y_artA, x_artA, y_artT, x_artT, y_artE, x_artE \
            = MG.gather(
                count=count, rack=rack, y=y, x=x,
                y_artA=y_artA, x_artA=x_artA,
                y_artT=y_artT, x_artT=x_artT,
                y_artE=y_artE, x_artE=x_artE,
                screen=screen
                )

        # Determin if Mac Gyver are at Guard position ?
        guard = TM.exit(y, x)

        # Out loop condition.
        if guard and count == 3:
            victory = True
            running = False
        elif guard and (count != 3):
            die = True
            running = False
        else:
            pass

    # At exit, die or victory.
    TM.win(victory, die, rack, screen)

    # Close Pygame and free ressources.
    pygame.quit()
    exit()

    return 0


# Execute "main" funciton like main code.
if __name__ == '__main__':
    main()
