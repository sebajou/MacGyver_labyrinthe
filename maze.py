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

#usefull function
def print_maze(rack):
    """Pretty print of maze"""
    for j in range(15):
        print("\n", end='')
        for i in range(15):
            print(rack[j][i], end=' ')

def win(victory):
    """in case of victory"""
    if victory:
        print_maze(rack)
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

def loadMacGyver(y,x):
    """Load the initial position of Mac Gyver"""
    rack[y][x] = "X"
    return rack, y, x

def move(direction, rack):
    """allow MacGyver to move"""
    global y
    global x
    #move upward    
    if direction == "u": 
        rack[y][x] = "+"
        if (y-1<0 or rack[y-1][x]=="M"):
            rack[y][x] = "X"
        else:
            y=y-1
            rack[y][x] = "X"
    #move downward
    elif direction == "n":
        rack[y][x] = "+"
        if (y+1>14 or rack[y+1][x]=="M"):
            rack[y][x] = "X"
        else:
            y=y+1
            rack[y][x] = "X"
    #move left
    elif direction == "h":
        rack[y][x] = "+"
        if (x-1<0 or rack[y][x-1]=="M"):
            rack[y][x] = "X"
        else:
            x=x-1
            rack[y][x] = "X"
    #move right
    elif direction == "j":
        rack[y][x] = "+"
        if (x+1>14 or rack[y][x+1]=="M"):
            rack[y][x] = "X"
        else:
            x=x+1
            rack[y][x] = "X"
    #unapropriate keyboard
    else:
        pass

    return rack

#load file maze_plan.txt in table of table (rack)
maze = loadMaze()

#setting up table of table wich contain the maze. 
rack = setTable(maze)

#load Mac Gyver (X) at the entrance of maze, rack[y][x]
rack, y, x = loadMacGyver(y=1,x=0)
print_maze(rack)

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
    rack = move(direction, rack)

    #Print maze
    print_maze(rack)
            

#In case of victory
win(victory)