# Load images
import pygame as pg


# Window
width, height = 750, 750
win = pg.display.set_mode((width, height))

pg.display.set_mode((width, height))
pg.display.set_caption("Alien Invasion")

# ships
red_ship = pg.image.load("Assets/Images/pixel_ship_red_small.png")
blue_ship = pg.image.load("Assets/Images/pixel_ship_blue_small.png")
green_ship = pg.image.load("Assets/Images/pixel_ship_green_small.png")
yellow_ship = pg.image.load("Assets/Images/pixel_ship_yellow.png")

# lasers
red_laser = pg.image.load("Assets/Images/pixel_laser_red.png")
yellow_laser = pg.image.load("Assets/Images/pixel_laser_yellow.png")
green_laser = pg.image.load("Assets/Images/pixel_laser_green.png")
blue_laser = pg.image.load("Assets/Images/pixel_laser_blue.png")
