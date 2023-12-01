import pygame as pg
from pygame.locals import *
import sys
from utilities import *
from game import game

pg.init()
mainClock = pg.time.Clock()

# Window
pg.display.set_mode((width, height))
pg.display.set_caption("Alien Invasion")

current_background = bg
volume = 0.5


def main_menu():
    while True:
        # Mouse Position
        mouseX, mouseY = pg.mouse.get_pos()

        win.blit(bg, (0, 0))

        titleText = font.render("Alien Invasion", 1, (125, 125, 255))
        win.blit(titleText, (width / 2 - titleText.get_width() / 2, 100))

        mainMenuText = font.render("Main Menu", 1, (255, 255, 255))
        win.blit(mainMenuText, (width / 2 - mainMenuText.get_width() / 2, 200))

        playButton = pg.Rect(width / 2 - 160, 335, 320, 80)
        optionsButton = pg.Rect(width / 2 - 160, 335 + 150, 320, 80)

        pg.draw.rect(win, (255, 0, 0), playButton)
        pg.draw.rect(win, (255, 0, 0), optionsButton)

        # writing text on top of button
        playText = font.render("Play", 1, (255, 255, 255))
        win.blit(playText, (width / 2 - playText.get_width() / 2, 350))

        optionsText = font.render("Options", 1, (255, 255, 255))
        win.blit(optionsText, (width / 2 - optionsText.get_width() / 2, 500))
        exitButton = pg.Rect(width / 2 - 75, 645, 150, 60)
        pg.draw.rect(win, (255, 0, 0), exitButton)

        exitButtonText = font.render("EXIT", 1, (255, 255, 255))
        win.blit(exitButtonText, (width / 2 - exitButtonText.get_width() / 2, 650))

        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                buttonAudio.play()
                if event.button == 1:
                    click = True

        if playButton.collidepoint((mouseX, mouseY)):
            if click:
                game()
        if optionsButton.collidepoint((mouseX, mouseY)):
            if click:
                options()
        if exitButton.collidepoint((mouseX, mouseY)):
            if click:
                pg.quit()
                sys.exit()

        pg.display.update()
        mainClock.tick(FPS)


def set_background(background_name):
    global current_background
    current_background = background_name


def options():
    global volume
    running = True
    click = False
    while running:
        # Mouse Position
        mouseX, mouseY = pg.mouse.get_pos()

        win.fill((0, 0, 0))
        # Options Text
        optionsText = font.render("Options", 1, (255, 255, 255))
        win.blit(optionsText, (width / 2 - optionsText.get_width() / 2, 25))

        # Back Button
        backText = font_small.render("Back", 1, (255, 255, 255))
        backButton = pg.Rect(
            25,
            35,
            backText.get_width() + 5,
            backText.get_height() + 5,
        )
        pg.draw.rect(win, (255, 0, 0), backButton)

        win.blit(backText, (25, 35))

        background_text = font_small.render(
            f"Background: {current_background}", 1, (255, 255, 255)
        )
        win.blit(background_text, (width / 2 - background_text.get_width() / 2, 100))

        for i, (name, image) in enumerate(backgrounds.items()):
            button_text = font_small.render(name, 1, (255, 255, 255))
            button_rect = pg.Rect(
                50,
                150 + i * 50,
                button_text.get_width() + 25,
                button_text.get_height() + 4,
            )
            pg.draw.rect(win, (255, 0, 0), button_rect)
            win.blit(button_text, (60, 155 + i * 50))

            if button_rect.collidepoint((mouseX, mouseY)) and click:
                set_background(name)

        # Volume slider
        volume_text = font.render(f"Volume: {int(volume * 100)}%", 1, (255, 255, 255))
        volume_text_x = width / 2 - volume_text.get_width() / 2
        win.blit(volume_text, (volume_text_x, 400))

        slider_bar_width = 300
        slider_bar_x = (width - slider_bar_width) / 2
        pg.draw.rect(win, (255, 0, 0), (slider_bar_x, 490, slider_bar_width, 20))
        pg.draw.rect(
            win, (0, 255, 0), (slider_bar_x, 490, int(volume * slider_bar_width), 20)
        )

        if pg.mouse.get_pressed()[0]:
            if (
                slider_bar_x <= mouseX <= slider_bar_x + slider_bar_width
                and 490 <= mouseY <= 510
            ):
                volume = (mouseX - slider_bar_x) / slider_bar_width
        backgroundAudio.set_volume(volume)
        buttonAudio.set_volume(volume)
        explosionAudio.set_volume(volume)
        gunshotAudio.set_volume(volume)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                buttonAudio.play()
                if event.button == 1:
                    click = True

        if backButton.collidepoint((mouseX, mouseY)):
            if click:
                running = False

        pg.display.update()
        mainClock.tick(FPS)


main_menu()
