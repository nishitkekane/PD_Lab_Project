import pygame as pg
from Laser import Laser
from Ship import Ship
from utilities import red_laser, red_ship, green_laser, green_ship, blue_laser, blue_ship


# class Enemy is inherits from class Ship
class Enemy(Ship):
    COLOR_MAP = {
        "red": (red_ship, red_laser),
        "green": (green_ship, green_laser),
        "blue": (blue_ship, blue_laser),
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pg.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
