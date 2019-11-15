#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""
This is a game where you drive Mac Gyver out of a maze. 
"""

##############################################################################################
#=============================================================================================
#                           title: Mac Gyver maze
#=============================================================================================
#                           author: Sébastien Jourdan 
#                                    /-\
#                                   c° °>
#                                    \O/
#                           email: sebajou@gmail.com
#                           society: None
#                           Initial date: November 2019
#                           Version: v1
#                           History: None
#                           Comment: This program is a game where you drive Mac Gyver 
# out of a maze. 
##############################################################################################

#importation
from mac_gyver import *
from maze import*

def main():
    #instancition
    MG = MacGyver()
    TM = TheMaze()

    #load file maze_plan.txt in table of table (rack)
    oneMaze = TM.loadMaze()

    #setting up table of table wich contain the maze. 
    rack = TM.setTable(oneMaze)

    #load Mac Gyver (X) at the entrance of maze, rack[y][x]
    rack, y, x = MG.loadMacGyver(rack=rack, y=1, x=0)
    TM.print_maze(rack)

    #Alow to move Mac Gyver and control that Mac Gyver don't go trough the wall
    victory = False
    while not victory:
        #Out loop condition
        if  y==13 and x==14:
            victory = True
        else:
        #input keyboard
            direction = input("Wich direction you want to go? (upward u, downward n, left h, right j): ")
        
        #moving Mac Gyver
        rack, y, x = MG.move(direction, rack, y, x)

        #Print maze
        TM.print_maze(rack)
                

    #In case of victory
    TM.win(victory, rack)

if __name__ == '__main__':
    main()
