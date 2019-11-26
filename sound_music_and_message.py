#!/usr/bin/python3
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from constantes import *


class Sound_and_message():
    """
    Class wich control display message on screen and sound.
    + Method "victory", display message for victory on screen.
    + Method "death", display message after death on screen.
    + Method "gather_message", display message after gather an objet
    and count the number of gathered message.
    """
    def victory(self, screen):
        # Print a message for the winner.
        self.myfont = pygame.font.Font("./assets/fonts/free.ttf", 40)
        label = self.myfont.render("You win !", 1, COLOR_BLUE)
        screen.blit(label, (10, 10))
        pygame.display.flip()
        # Sound of the winner.
        pygame.mixer.music.stop()
        son_winner = pygame.mixer.Sound("./assets/sounds/winner.wav")
        son_winner.set_volume(0.5)
        son_winner.play(loops=0)
        # Stop the game, time to play the sound.
        self.length = int(round((son_winner.get_length())*1000.0))
        pygame.time.delay(self.length)

    def death(self, screen):
        # Print a message for the loser.
        self.myfont = pygame.font.Font("./assets/fonts/free.ttf", 20)
        label = self.myfont.render(
            "You die with a slow, painful death.", 1, COLOR_BLUE
            )
        screen.blit(label, (10, 10))
        pygame.display.flip()
        # Sound of death.
        pygame.mixer.music.stop()
        son_death = pygame.mixer.Sound("./assets/sounds/death.ogg")
        son_death.set_volume(0.5)
        son_death.play(loops=0)
        # Stop the game, time to play the sound.
        self.length = int(round((son_death.get_length())*1000.0))
        pygame.time.delay(self.length)

    def gather_message(self, count, screen):
        # Print a message after gather artefact.
        self.myfont = pygame.font.Font("./assets/fonts/free.ttf", 40)
        self.message = ("You gather {0} artefact(s)". format(count))
        label = self.myfont.render(
            self.message, 1, COLOR_BLUE
            )
        screen.blit(label, (10, 10))
        pygame.display.flip()
        pygame.time.delay(1000)
