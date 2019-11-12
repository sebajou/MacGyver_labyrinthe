#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""
This program are a play where you drive Mac Gyver out of a maze. 
"""

##############################################################################################
#               authors: Sébastien Jourdan  
#               title: Mac Gyver maze
##############################################################################################

#load file maze_plan.txt in table of table (rack)
maze = open("maze_plan.txt", "r")

maze = maze.read()
maze = maze.split("\n")
rack = []

for line in maze:
    list_line = []
    for caractere in line: 
        list_line.append(caractere)
    rack.append(list_line)

rack
#maze.close()

#load Mac Gyver (X) at the entrance of maze, rack[y][x]
y=1
x=0
rack[y][x] = "X"
print(rack)
#Alow to move Mac Gyver and control that Mac Gyver don't go trough the wall

while not (y==13 and x==14):

    direction = input("Wich direction you want to go? (upward u, downward n, left h, right j): ")
    
    if direction == "u": 
        rack[y][x] = "+"
        if (y-1<0 or rack[y-1][x]=="M"):
            rack[y][x] = "X"
        else:
            y=y-1
            rack[y][x] = "X"
        #move upward
    elif direction == "n":
        rack[y][x] = "+"
        if (y+1>14 or rack[y+1][x]=="M"):
            rack[y][x] = "X"
        else:
            y=y+1
            rack[y][x] = "X"
        #move downward
    elif direction == "h":
        rack[y][x] = "+"
        if (x-1<0 or rack[y][x-1]=="M"):
            rack[y][x] = "X"
        else:
            x=x-1
            rack[y][x] = "X"
        #move left
    elif direction == "j":
        rack[y][x] = "+"
        if (x+1>14 or rack[y][x+1]=="M"):
            rack[y][x] = "X"
        else:
            x=x+1
            rack[y][x] = "X"
        #move right
    else:
        pass
    print(rack)

if (y==13 and x==14):
    print(rack)
    for i in range(0,14):
                print("You win !")
