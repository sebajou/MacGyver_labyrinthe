#!/usr/bin/python3
# -*-coding:Utf-8 -* *


class MacGyver:
    """
    This class allows positionment of MacGyver.
    + Methode "loadMacGyver" write an X at Mac Gyver position
    in table containing the maze.
        - Parameter: table containing the maze "rack",
        position of Mac Gyver "y" and "x".
        - Return the "rack", "y", and "x".
    + Methode "move" allow movement of Mac Gyver from instruction.
        - Parameter:
        If "direction" correspond to allowed instruction (u, n, h or j),
        and if the envisaged movement not correspond to a forbiden movement
        (wall "M", entry "E" or guard position "G")
        Mac Gyver "X" are erase from precedent position
        and write in the new one.
        "rack" is the table wich contain the maze.
        "y", "x" are the position of Mac Gyver.
        - Return: The rack and Mac Gyver position.
    + Methode "gather": Determine if an artefact is gather
    and count the number of gather artefact.
        - Parameter:
        "count" a counter of gather arteffact number.
        "y" and "x" Mac Gyver position.
        "y_artA", "x_artA", "y_artT", "x_artT", "y_artE" and "x_artE"
        the position of artefacts.
        - Return: the counter and artefacts position.
    """
    def loadMacGyver(self, rack, y, x):
        """Load the initial position of Mac Gyver."""
        rack[y][x] = "X"
        return rack, y, x

    def move(self, direction, rack, y, x):
        """Allow MacGyver to move."""
        # move upward
        if direction == "u":
            rack[y][x] = "+"
            if (y-1 < 0 or rack[y-1][x] == "M"):
                rack[y][x] = "X"
            else:
                y = y-1
                rack[y][x] = "X"
        # move downward
        elif direction == "n":
            rack[y][x] = "+"
            if (y+1 > 14 or rack[y+1][x] == "M"):
                rack[y][x] = "X"
            else:
                y = y+1
                rack[y][x] = "X"
        # move left
        elif direction == "h":
            rack[y][x] = "+"
            if (x-1 < 0 or rack[y][x-1] == "M"):
                rack[y][x] = "X"
            else:
                x = x-1
                rack[y][x] = "X"
        # move right
        elif direction == "j":
            rack[y][x] = "+"
            if (x+1 > 14 or rack[y][x+1] == "M"):
                rack[y][x] = "X"
            else:
                x = x+1
                rack[y][x] = "X"
        # unapropriate keyboard
        else:
            pass

        return rack, y, x

    def gather(
        self, count, rack, y, x, y_artA, x_artA, y_artT, x_artT, y_artE, x_artE
            ):
        """
        Determine if an artefact is gather
        and count the number of gather artefact.
        """
        if (y == y_artA and x == x_artA):
            count = count + 1
            y_artA = None
            x_artA = None
            # myfont = pygame.font.Font("./assets/fonts/free.ttf", 100)
            # label = myfont.render(
            # "You gather 1 artefacts !", 1, COLOR_YELLOW
            # )
            # screen.blit(label, (10, 10))
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
