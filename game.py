import pygame as pg
import os
import time
import random
from Laser import Laser
from utilities import *
from Ship import Ship
from Player import Player
from Enemy import Enemy

pg.init()
pg.font.init()

# Window
pg.display.set_mode((width, height))
pg.display.set_caption("Alien Invasion")


def game():
    def redraw_window():
        win.blit(bg, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
        for enemy in enemies:
            enemy.draw()

        player.draw()
        win.blit(lives_label, (10, 10))
        win.blit(level_label, (width - level_label.get_width() - 10, 10))
        if lost:
            win.blit(lost_label, (width / 2 - lost_label.get_width() / 2, 350))

        player.healthbar()
        pg.display.update()

    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    level = 0
    lives = 5

    run = True
    FPS = 40
    lost = False

    enemies = []
    wave_length = 0
    lost_count = 0

    laser_vel = 15
    player_vel = 15
    enemy_vel = 4

    player = Player(325, 600)
    clock = pg.time.Clock()

    main_font = pg.font.Font("Assets/Fonts/Alpharush.ttf", 25)
    lost_font = pg.font.Font("Assets/Fonts/Alpharush.ttf", 50)

    while run:
        clock.tick(FPS)
        redraw_window()

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
            wave_length += 5

            for i in range(wave_length):
                enemy = Enemy(
                    random.randrange(50, width - 100),
                    random.randrange(-1500, -100),
                    random.choice(["red", "blue", "green"]),
                )
                enemies.append(enemy)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quitGame()
            if keys[pg.K_ESCAPE]:
                quitGame()

        # Movement of player
        keys = pg.key.get_pressed()
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
