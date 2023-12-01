import pygame as pg
import sys

# Initialize Font
pg.font.init()
pg.mixer.init()

# Font
font = pg.font.Font("Assets/Fonts/Valorax.otf", 44)
font_small = pg.font.Font("Assets/Fonts/Valorax.otf", 25)
main_font = pg.font.Font("Assets/Fonts/Alpharush.ttf", 25)
lost_font = pg.font.Font("Assets/Fonts/Alpharush.ttf", 50)

# Window
width, height = 750, 750
win = pg.display.set_mode((width, height))

# Background
bg = pg.transform.scale(
    pg.image.load("Assets/Images/background-black.png"), (width, height)
)
bg_01 = pg.transform.scale(pg.image.load("Assets/Images/bg_01.png"), (width, height))

bg_02 = pg.transform.scale(pg.image.load("Assets/Images/bg_02.png"), (width, height))

# Display
FPS = 60
# pg.display.set_mode((width, height))
# pg.display.set_caption("Alien Invasion")


def drawText(text, font, color, surface, x, y):
    textObject = font.render(text, 1, color)
    textRectangle = textObject.get_rect()
    textRectangle.topleft = (x, y)
    surface.blit(textObject, textRectangle)


# Load images
# ships
red_ship = pg.image.load("Assets/Images/red_ship.png")
red_ship = pg.transform.scale(
    red_ship, (red_ship.get_width() * 0.6, red_ship.get_height() * 0.6)
)

blue_ship = pg.image.load("Assets/Images/blue_ship.png")
blue_ship = pg.transform.scale(
    blue_ship, (blue_ship.get_width() * 0.6, blue_ship.get_height() * 0.6)
)

green_ship = pg.image.load("Assets/Images/green_ship.png")
green_ship = pg.transform.scale(
    green_ship, (green_ship.get_width() * 0.6, green_ship.get_height() * 0.6)
)
yellow_ship = pg.image.load("Assets/Images/yellow_ship.png")
yellow_ship = pg.transform.scale(
    yellow_ship, (yellow_ship.get_width() * 0.9, yellow_ship.get_height() * 0.9)
)
# lasers
red_laser = pg.image.load("Assets/Images/pixel_laser_red.png")
yellow_laser = pg.image.load("Assets/Images/pixel_laser_yellow.png")
green_laser = pg.image.load("Assets/Images/pixel_laser_green.png")
blue_laser = pg.image.load("Assets/Images/pixel_laser_blue.png")

# Load Audio files
buttonAudio = pg.mixer.Sound("Assets/Audio/Button.wav")
explosionAudio = pg.mixer.Sound("Assets/Audio/Explosion.mp3")
gunshotAudio = pg.mixer.Sound("Assets/Audio/LaserShot.mp3")
backgroundAudio = pg.mixer.Sound("Assets/Audio/BackgroundMusic.mp3")


# Game Functions
def quitGame():
    run = False
    pg.quit()
    sys.exit(0)
