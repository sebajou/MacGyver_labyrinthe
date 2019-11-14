#!/usr/bin/python3
# -*-coding:Utf-8 -*

class TheMaze:
    """
    This class allow print and control of the maze. 
    """
    def print_maze(rack):
        """Pretty print of maze"""
        for j in range(15):
            print("\n", end='')
            for i in range(15):
                print(rack[j][i], end=' ')

    def win(victory, rack):
        """in case of victory"""
        if victory:
            TheMaze.print_maze(rack)
            for i in range(0,24):
                        print("You win !")

    def setTable(maze):
        """Setting up table of table wich contain the maze"""
        rack = []
        for line in maze:
            list_line = []
            for caractere in line: 
                list_line.append(caractere)
            rack.append(list_line)
        return rack

    def loadMaze():
        """load file maze_plan.txt in table of table (rack)"""
        maze = open("maze_plan.txt", "r")
        maze = maze.read()
        maze = maze.split("\n")
        return maze
