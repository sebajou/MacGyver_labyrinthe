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


def main():
    """Function of general game cook."""
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

    # Print the maze.
    TM.print_maze(rack)

    # Loop for run the game and pick up instruction.
    guard = False
    count = 0
    victory = False
    die = False

    while not victory:
        # Input keyboard.
        direction = input("Wich direction you want to go? \
            (upward u, downward n, left h, right j): ")

        # Moving Mac Gyver.
        rack, y, x = MG.move(direction, rack, y, x)

        # Print maze.
        TM.print_maze(rack)

        # Counter of artefacts.
        count, y_artA, x_artA, y_artT, x_artT, y_artE, x_artE \
            = MG.gather(
                count=count, rack=rack, y=y, x=x,
                y_artA=y_artA, x_artA=x_artA,
                y_artT=y_artT, x_artT=x_artT,
                y_artE=y_artE, x_artE=x_artE
                )

        # Determin if Mac Gyver are at Guard position ?
        guard = TM.exit(y, x)

        # Out loop condition.
        if guard and count == 3:
            victory = True
        elif guard and (count != 3):
            die = True
            break
        else:
            pass

    # At exit, die or victory.
    TM.win(victory, die, rack)


# Execute "main" funciton like main code.
if __name__ == '__main__':
    main()
