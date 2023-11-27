import pygame as pg
from utilities import height, width, win, explosionAudio


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pg.mask.from_surface(self.img)

    def draw(self):
        win.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_Screen(self):
        return not (self.y <= height or self.y >= 0)

    def collision(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None
