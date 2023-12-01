import pygame as pg
import sys

# Initialize Font
pg.font.init()
pg.mixer.init()

# Font
font = pg.font.Font("Assets/Fonts/Valorax-lg25V.otf", 44)
main_font = pg.font.Font("Assets/Fonts/Alpharush.ttf", 25)
lost_font = pg.font.Font("Assets/Fonts/Alpharush.ttf", 50)

# Window
width, height = 750, 750
win = pg.display.set_mode((width, height))

# Background
bg = pg.transform.scale(
    pg.image.load("Assets/Images/background-black.png"), (width, height)
)

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
red_ship = pg.image.load("Assets/Images/pixel_ship_red_small.png")
blue_ship = pg.image.load("Assets/Images/pixel_ship_blue_small.png")
green_ship = pg.image.load("Assets/Images/pixel_ship_green_small.png")
yellow_ship = pg.image.load("Assets/Images/pixel_ship_yellow.png")

# lasers
red_laser = pg.image.load("Assets/Images/pixel_laser_red.png")
yellow_laser = pg.image.load("Assets/Images/pixel_laser_yellow.png")
green_laser = pg.image.load("Assets/Images/pixel_laser_green.png")
blue_laser = pg.image.load("Assets/Images/pixel_laser_blue.png")

# Load Audio files
buttonAudio = pg.mixer.Sound("Assets/Audio/Button.wav")
explosionAudio = pg.mixer.Sound("Assets/Audio/Explosion.mp3")
gunshotAudio = pg.mixer.Sound("Assets/Audio/LaserShot.mp3")
backgroundAudio = pg.mixer.Sound(
    "Assets/Audio/Space shooter galaxy attack Background Music.mp3"
)


# Game Functions
def quitGame():
    run = False
    pg.quit()
    sys.exit(0)
