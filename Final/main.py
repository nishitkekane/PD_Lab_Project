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


def main_menu():
    while True:
        win.blit(bg, (0, 0))
        mouseX, mouseY = pg.mouse.get_pos()

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


def options():
    running = True
    while running:
        win.fill((0, 0, 0))
        drawText("OPTIONS Page", font, (255, 255, 255), win, 20, 20)
        # mainMenuText = font.render("Main Menu", 1, (255, 255, 255))
        # win.blit(mainMenuText, (width / 2 - mainMenuText.get_width() / 2, 200))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pg.display.update()
        mainClock.tick(FPS)


main_menu()
