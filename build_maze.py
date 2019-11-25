#!/usr/bin/python3
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from sys import exit
from constantes import *


def pygame_initialisation():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGTH, SCREEN_WIDTH))
    pygame.display.set_caption("Mac Gyver maze")
    screen.fill(COLOR_FONT)
    clock = pygame.time.Clock()
    return clock, screen


class MazeElements:
    """
    Mother class of Maze's elements (wall, floor, artefact, guard).
    During instantiation build an elements of Maze (wall, guard or floor).
    + Methdod "__init__" load the image of maze elements.
    + Method "loadAndPrint" create a surface for image to display.
    + Method "pygame_display" display the image.
    """
    def __init__(self):
        """Load the image of element"""
        self.element_image = \
            pygame.image.load("./assets/images/seringueO.png").convert_alpha()

    def loadAndPrint(self):
        """Create the surface for image display"""
        # Pygame print wall.
        element_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        element_surface.fill(COLOR_ELEMENT)
        # Load of wall image.

    def pygame_display(self, screen, position):
        """display the image on the screen"""
        screen.blit(self.element_image, position)
        pygame.display.flip()


class WallElements(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/wall.png").convert_alpha()


class FloorElements(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/floor.png").convert_alpha()


class GuardElements(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/guard.png").convert_alpha()


class AiguilleElements(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/aiguille.png").convert_alpha()


class EtherElements(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/ether.png").convert_alpha()


class TubeElements(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/tube.png").convert_alpha()


class PygameMacGyver(MazeElements):
    """
    This is a MazeElements daughter class.
    """
    def __init__(self):
        MazeElements.__init__(self)
        self.element_image = \
            pygame.image.load("./assets/images/MacGyver.png").convert_alpha()
