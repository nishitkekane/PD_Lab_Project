import pygame as pg
import os
import time
import random
from Laser import Laser
from utilities import *
from Ship import Ship
from Player import Player
from Enemy import Enemy

pause = False
background_music_playing = False


def pauseScreen():
    global pause
    paused = True

    overlay = pg.Surface((width, height))
    overlay.fill((0, 0, 0))

    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitGame()

            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                paused = False
                pause = False

        win.blit(overlay, (0, 0))

        # Pause Text
        pauseText = font.render("Paused", 1, (255, 255, 255))
        win.blit(pauseText, (width / 2 - pauseText.get_width() / 2, 25))

        # Create restart button
        restart_button = pg.Rect(width / 2 - 120 / 2, height / 2 - 50, 120, 40)
        pg.draw.rect(win, (0, 255, 0), restart_button)
        restart_label = main_font.render("Restart", 1, (255, 255, 255))
        win.blit(
            restart_label,
            (
                width / 2 - restart_label.get_width() / 2,
                height / 2 - 50 + 40 / 2 - restart_label.get_height() / 2,
            ),
        )

        # Create resume button
        resume_button = pg.Rect(width / 2 - 120 / 2, height / 2, 120, 40)
        pg.draw.rect(win, (0, 255, 0), resume_button)
        resume_label = main_font.render("Resume", 1, (255, 255, 255))
        win.blit(
            resume_label,
            (
                width / 2 - resume_label.get_width() / 2,
                height / 2 + 40 / 2 - resume_label.get_height() / 2,
            ),
        )

        # Create exit button
        exit_button = pg.Rect(width / 2 - 120 / 2, height / 2 + 50, 120, 40)
        pg.draw.rect(win, (255, 0, 0), exit_button)
        exit_label = main_font.render("Exit", 1, (255, 255, 255))
        win.blit(
            exit_label,
            (
                width / 2 - exit_label.get_width() / 2,
                height / 2 + 50 + 40 / 2 - exit_label.get_height() / 2,
            ),
        )

        pg.display.update()

        # Check for button clicks
        mouse_x, mouse_y = pg.mouse.get_pos()
        click, _, _ = pg.mouse.get_pressed()

        if restart_button.collidepoint(mouse_x, mouse_y) and click:
            pause = False
            paused = False
            game()

        if resume_button.collidepoint(mouse_x, mouse_y) and click:
            paused = False
            pause = False

        if exit_button.collidepoint(mouse_x, mouse_y) and click:
            quitGame()


def game():
    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    level = 0
    lives = 1

    run = True
    lost = False
    global pause
    enemies = []
    wave_length = 0
    lost_count = 0
    global background_music_playing
    if background_music_playing:
        backgroundAudio.stop()
        background_music_playing = False

    # Start background audio again
    backgroundAudio.play()
    background_music_playing = True

    laser_vel = 15
    player_vel = 15
    enemy_vel = 4

    player = Player(325, 600)
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        win.blit(bg, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
        # scoreLabel = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        for enemy in enemies:
            enemy.draw()

        player.draw()
        win.blit(lives_label, (10, 10))
        win.blit(level_label, (width - level_label.get_width() - 10, 10))
        # win.blit(scoreLabel, (width / 2, 10))
        player.healthbar()
        mouseX, mouseY = pg.mouse.get_pos()
        if lost:
            win.fill((0, 0, 255))
            PlayAgainButton = pg.Rect(width / 2 - 160, height / 2 - 40, 320, 80)
            pg.draw.rect(win, (255, 0, 0), PlayAgainButton)
            win.blit(
                lost_label,
                (
                    width / 2 - lost_label.get_width() / 2,
                    height / 2 - lost_label.get_height() / 2,
                ),
            )
            pg.display.update()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 2

            for i in range(wave_length):
                enemy = Enemy(
                    random.randrange(50, width - 100),
                    random.randrange(-1500, -100),
                    random.choice(["red", "blue", "green"]),
                )
                enemies.append(enemy)

        if not pause:
            pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitGame()

            keys = pg.key.get_pressed()

            if keys[pg.K_ESCAPE]:
                if pause:
                    pause = False
                else:
                    pause = True
                    pauseScreen()

        # Movement of player
        keys = pg.key.get_pressed()
        if not pause:
            if (keys[pg.K_LEFT] or keys[pg.K_a]) and player.x - player_vel > 0:  # left
                player.x -= player_vel
            if (
                keys[pg.K_RIGHT] or keys[pg.K_d]
            ) and player.x + player_vel + player.get_width() < width:  # right
                player.x += player_vel
            if (keys[pg.K_UP] or keys[pg.K_w]) and player.y - player_vel > 0:  # up
                player.y -= player_vel
            if (
                keys[pg.K_DOWN] or keys[pg.K_s]
            ) and player.y + player_vel + player.get_height() + 15 < height:  # down
                player.y += player_vel
            if keys[pg.K_SPACE]:
                player.shoot()

        # Movement of enemies
        for enemy in enemies[:]:
            if not pause:
                enemy.move(enemy_vel)
                if (
                    enemy.y + enemy.get_height() < height
                    and enemy.y + enemy.get_height() > 0
                ):
                    enemy.move_lasers(laser_vel - 5, player)

                if collide(enemy, player):
                    explosionAudio.play()
                    player.health -= 10
                    enemies.remove(enemy)

                if random.randrange(0, 3 * 60) == 1:
                    enemy.shoot()

                if enemy.y + enemy.get_height() > height:
                    lives = lives - 1
                    enemies.remove(enemy)

                player.move_lasers(-laser_vel, enemies)
        pg.display.update()
