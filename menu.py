import pygame as pg
from pygame.locals import *
import sys
from utilities import *
from game import game

pg.init()
mainClock = pg.time.Clock()


def main_menu():
    click = False

    while True:
        win.blit(bg, (0, 0))
        drawText(
            "Main Menu", font, (0, 0, 0), win, win.get_width() / 2, win.get_height() / 2
        )

        mouseX, mouseY = pg.mouse.get_pos()

        button_1 = pg.Rect(
            win.get_width() / 2 - 160, win.get_height() / 2 - 150, 320, 80
        )
        button_2 = pg.Rect(win.get_width() / 2 - 160, win.get_height() / 2, 320, 80)

        if button_1.collidepoint((mouseX, mouseY)) == True:
            if click == True:
                game()
        if button_2.collidepoint((mouseX, mouseY)) == True:
            if click == True:
                options()
        pg.draw.rect(win, (255, 0, 0), button_1)
        pg.draw.rect(win, (255, 0, 0), button_2)

        # writing text on top of button
        drawText(
            "PLAY",
            font,
            (255, 255, 255),
            win,
            win.get_width() / 2 - 160 + 88,
            win.get_height() / 2 - 150 + 19,
        )
        drawText(
            "OPTIONS",
            font,
            (255, 255, 255),
            win,
            win.get_width() / 2 - 160 + 49,
            win.get_height() / 2 + 19,
        )

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                buttonAudio.play()
                if event.button == 1:
                    click = True

        pg.display.update()
        mainClock.tick(FPS)


def options():
    running = True
    while running:
        win.fill((0, 0, 0))

        drawText("OPTIONS Page", font, (255, 255, 255), win, 20, 20)
        for event in pg.event.get():
            if event.type == QUIT:
                quitGame()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pg.display.update()
        mainClock.tick(FPS)


main_menu()
