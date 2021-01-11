import pygame
import neat
import time
import os
import random
from const import WIN_HEIGHT, WIN_WIDTH, BASE_IMG, BG_IMG, BIRD_IMGS, PIPE_IMG, STAT_FONT

VEL = 5
WIDTH = BASE_IMG.get_width()


class Base:
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = WIDTH

    def move(self):
        """
        move floor so it looks like its scrolling
        :return: None
        """
        self.x1 -= VEL
        self.x2 -= VEL

        if self.x1 + WIDTH < 0:
            self.x1 = self.x2 + WIDTH

        if self.x2 + WIDTH < 0:
            self.x2 = self.x1 + WIDTH

    def draw(self, win):
        win.blit(BASE_IMG, (self.x1, self.y))
        win.blit(BASE_IMG, (self.x2, self.y))
