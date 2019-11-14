#!/usr/bin/python3
# -*-coding:Utf-8 -*

class MacGyver:
    """
    This class allows positionment of MacGyver
    """
    def loadMacGyver(rack, y,x):
        """Load the initial position of Mac Gyver"""
        rack[y][x] = "X"
        return rack, y, x

    def move(direction, rack, y, x):
        """allow MacGyver to move"""
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

        return rack, y, x