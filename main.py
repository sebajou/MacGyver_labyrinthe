#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""
This is a game where you drive Mac Gyver out of a maze.
"""

###############################################################################
# =============================================================================
#                           title: Mac Gyver maze
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
import pygame
from pygame.locals import *
from sys import exit
from constantes import *
from build_maze import *


def main():
    """Function of general game cook."""

    # Pygame initialisation and display setting.
    clock, screen = pygame_initialisation()

    # Instancition.
    MG = MacGyver()
    TM = TheMaze()
    AA = artefacts.Aiguille()
    AT = artefacts.Tube()
    AE = artefacts.Ether()

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
        for y_maze in range(15):
            for x_maze in range(15):
                if rack[y_maze][x_maze] == "M":
                    WE = WallElements()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = WE.loadAndPrint()
                    WE.pygame_display(screen, position)
                elif rack[y_maze][x_maze] == "+":
                    FE = FloorElements()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = FE.loadAndPrint()
                    FE.pygame_display(screen, position)
                elif rack[y_maze][x_maze] == "A":
                    AE = AiguilleElements()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = AE.loadAndPrint()
                    AE.pygame_display(screen, position)
                elif rack[y_maze][x_maze] == "E":
                    EE = EtherElements()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = EE.loadAndPrint()
                    EE.pygame_display(screen, position)
                elif rack[y_maze][x_maze] == "T":
                    TE = TubeElements()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = TE.loadAndPrint()
                    TE.pygame_display(screen, position)
                elif rack[y_maze][x_maze] == "G":
                    GE = GuardElements()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = GE.loadAndPrint()
                    GE.pygame_display(screen, position)
                elif rack[y_maze][x_maze] == "X":
                    MGE = PygameMacGyver()
                    position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                    element_image = MGE.loadAndPrint()
                    MGE.pygame_display(screen, position)

        # Input keyboard.
        """direction = input("Wich direction you want to go? \
            (upward u, downward n, left h, right j): ")"""
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

        # myfont = pygame.font.Font("./assets/fonts/free.ttf", 200)
        # label = myfont.render("Test", 1, COLOR_YELLOW)
        # screen.blit(label, (10, 10))

        # Counter of artefacts.
        count, y_artA, x_artA, y_artT, x_artT, y_artE, x_artE \
            = MG.gather(
                count=count, rack=rack, y=y, x=x,
                y_artA=y_artA, x_artA=x_artA,
                y_artT=y_artT, x_artT=x_artT,
                y_artE=y_artE, x_artE=x_artE,
                )

        # Determin if Mac Gyver are at Guard position ?
        guard = TM.exit(y, x)

        # Out loop condition.
        if guard and count == 3:
            # pygame.time.delay(5000)
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
