#!/usr/bin/python3
# -*-coding:Utf-8 -*

from pygame_objets import *
import pygame
from pygame.locals import *
from sys import exit
from constantes import *


class MazeElements:
    """
    Mother class of Maze's elements.
    During instantiation build an elements of Maze (wall, guard or floor).
    + Methdod __init__, :
    """
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        wall_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        wall_surface.fill(COLOR_WALL)
        # wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        wall_image = pygame.image.load("./assets/images/wall.png")\
            .convert_alpha()
        return wall_image

    def pygame_display(self, screen, wall_image, position):
        screen.blit(wall_image, position)
        pygame.display.flip()


class WallElements(MazeElements):
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        wall_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        wall_surface.fill(COLOR_WALL)
        wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        wall_image = pygame.image.load("./assets/images/wall.png")\
            .convert_alpha()
        return wall_image, wall_rectangle


class FloorElements(MazeElements):
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        floor_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        floor_surface.fill(COLOR_WALL)
        # wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        floor_image = pygame.image.load("./assets/images/floor.png")\
            .convert_alpha()
        return floor_image

    def pygame_display(self, screen, floor_image, position):
        screen.blit(floor_image, position)
        pygame.display.flip()


class GuardElements(MazeElements):
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        aiguille_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        aiguille_surface.fill(COLOR_WALL)
        # wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        aiguille_image = pygame.image.load("./assets/images/guard.png")\
            .convert_alpha()
        return aiguille_image

    def pygame_display(self, screen, aiguille_image, position):
        screen.blit(aiguille_image, position)
        pygame.display.flip()


class AiguilleElements(MazeElements):
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        aiguille_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        aiguille_surface.fill(COLOR_WALL)
        # wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        aiguille_image = pygame.image.load("./assets/images/aiguille.png")\
            .convert_alpha()
        return aiguille_image

    def pygame_display(self, screen, aiguille_image, position):
        screen.blit(aiguille_image, position)
        pygame.display.flip()


class EtherElements(MazeElements):
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        ether_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        ether_surface.fill(COLOR_WALL)
        # wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        ether_image = pygame.image.load("./assets/images/ether.png")\
            .convert_alpha()
        return ether_image

    def pygame_display(self, screen, ether_image, position):
        screen.blit(ether_image, position)
        pygame.display.flip()


class TubeElements(MazeElements):
    def __init__(self):
        pass

    def loadAndPrint(self):
        # Pygame print wall.
        tube_surface = pygame.Surface((ELEMENT_HEIGTH, ELEMENT_WIDTH))
        tube_surface.fill(COLOR_WALL)
        # wall_rectangle = wall_surface.get_rect()
        # Load of wall image.
        tube_image = pygame.image.load("./assets/images/tube.png")\
            .convert_alpha()
        return tube_image

    def pygame_display(self, screen, tube_image, position):
        screen.blit(tube_image, position)
        pygame.display.flip()
