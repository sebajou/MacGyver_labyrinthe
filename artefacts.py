#!/usr/bin/python3
# -*-coding:Utf-8 -*

import random

class Artefact:
    """
    This is a mother class of all artefact (aiguille, tube and ether). 
    """
    def __init__(self):
        self.artefact = "F"

    def loadArtefact(self, rack):
        #Load the initial position of artefact
        self.getPosi = False
        while not self.getPosi:
            y_art = random.randint(0,14)
            x_art = random.randint(0,14) 
            if rack[y_art][x_art] == "+":
                rack[y_art][x_art] = self.artefact
                self.getPosi = True
            else: 
                self.getPosi = False
        return rack, y_art , x_art

class Aiguille(Artefact):
    """
    This is a Artefact daughter class. 
    """
    def __init__(self):
        Artefact.__init__(self)
        self.artefact = "A"


class Tube(Artefact):
    """
    This is a Artefact daughter class. 
    """
    def __init__(self):
        Artefact.__init__(self)
        self.artefact = "T"

class Ether(Artefact):
    """
    This is a Artefact daughter class. 
    """
    def __init__(self):
        Artefact.__init__(self)
        self.artefact = "E"


