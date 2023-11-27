import pygame as pg
from utilities import win, gunshotAudio
from Laser import Laser


# class Ship which shares common attributes between class Player and class Enemy
class Ship:
    COOLDOWN = 15

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_counter = 0

    def draw(self):
        win.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw()

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def shoot(self):
        if self.cool_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_counter = 1
            gunshotAudio.play()

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_Screen():
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 8
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_counter >= self.COOLDOWN:
            self.cool_counter = 0
        elif self.cool_counter > 0:
            self.cool_counter += 1
