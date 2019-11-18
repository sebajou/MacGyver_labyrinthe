#!/usr/bin/python3
# -*-coding:Utf-8 -*

class MacGyver:
    """
    This class allows positionment of MacGyver
    """
    def loadMacGyver(self, rack, y,x):
        """Load the initial position of Mac Gyver"""
        rack[y][x] = "X"
        return rack, y, x

    def move(self, direction, rack, y, x):
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

    def gather(self, count, rack, y, x, y_artA, x_artA, y_artT, x_artT, y_artE, x_artE):
        """determine if an artefact is gather and count the number of gather artefact"""
        if (y == y_artA and x == x_artA): 
            count = count + 1
            y_artA = None
            x_artA = None
            print("\n\nYou gather {0} artefact(s)\n". format(count))
        elif (y == y_artT and x == x_artT): 
            count = count + 1
            y_artT = None
            x_artT = None
            print("\n\nYou gather {0} artefact(s)\n". format(count))
        elif (y == y_artE and x == x_artE): 
            count = count + 1
            y_artE = None
            x_artE = None
            print("\n\nYou gather {0} artefact(s)\n". format(count))
        else: 
            pass
        return count, y_artA, x_artA, y_artT, x_artT, y_artE, x_artE
