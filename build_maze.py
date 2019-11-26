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


def pygame_display(rack, screen):
    for y_maze in range(15):
        for x_maze in range(15):
            if rack[y_maze][x_maze] == "M":
                WE = WallElements()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = WE.loadAndPrint()
                WE.pygame_display(screen, position)
            elif rack[y_maze][x_maze] == "+":
                FE = FloorElements()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = FE.loadAndPrint()
                FE.pygame_display(screen, position)
            elif rack[y_maze][x_maze] == "A":
                AE = AiguilleElements()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = AE.loadAndPrint()
                AE.pygame_display(screen, position)
            elif rack[y_maze][x_maze] == "E":
                EE = EtherElements()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = EE.loadAndPrint()
                EE.pygame_display(screen, position)
            elif rack[y_maze][x_maze] == "T":
                TE = TubeElements()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = TE.loadAndPrint()
                TE.pygame_display(screen, position)
            elif rack[y_maze][x_maze] == "G":
                GE = GuardElements()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = GE.loadAndPrint()
                GE.pygame_display(screen, position)
            elif rack[y_maze][x_maze] == "X":
                MGE = PygameMacGyver()
                position = (ELEMENT_HEIGTH*x_maze, ELEMENT_WIDTH*y_maze)
                element_image = MGE.loadAndPrint()
                MGE.pygame_display(screen, position)


class MazeElements:
    """
    Mother class of Maze's elements (wall, floor, artefact, guard).
    During instantiation build an elements of Maze (wall, guard or floor).
    + Methdod "__init__" load the image of maze elements.
    + Method "loadAndPrint" create a surface for image to display.
    + Method "pygame_display" display the image.
        - Parameters: screen is the screen, position is position where display.
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
