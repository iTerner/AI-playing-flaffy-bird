import pygame
import neat
import time
import os
import random
from const import WIN_HEIGHT, WIN_WIDTH, BASE_IMG, BG_IMG, BIRD_IMGS, PIPE_IMG, STAT_FONT

IMGS = BIRD_IMGS
MAX_ROTATION = 25
ROT_VEL = 20
ANIMATION_TIME = 5

# the numbers is physics calc


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2
        # in order to not moving down to fast
        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y += d
        if d < 0 or self.y < self.height + 50:
            if self.tilt < MAX_ROTATION:
                self.tilt = MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= ROT_VEL

    def draw(self, win):
        self.img_count += 1
        if self.img_count < ANIMATION_TIME:
            self.img = IMGS[0]
        elif self.img_count < ANIMATION_TIME * 2:
            self.img = IMGS[1]
        elif self.img_count < ANIMATION_TIME * 3:
            self.img = IMGS[2]
        elif self.img_count < ANIMATION_TIME * 4:
            self.img = IMGS[1]
        elif self.img_count < ANIMATION_TIME * 4 + 1:
            self.img = IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = IMGS[1]
            self.img_count = ANIMATION_TIME * 2

        roteted_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = roteted_image.get_rect(
            center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(roteted_image, new_rect.topleft)

    # in order to make the collition "beautiful"
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
