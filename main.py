import pygame as pg
import os
import time 
import random

pg.init()
pg.font.init()

#Window
width,height=750,750
win=pg.display.set_mode((width,height))

pg.display.set_mode((width,height))
pg.display.set_caption("Alien Invasion")

#Load images

#ships
red_ship=pg.image.load('pixel_ship_red_small.png')
blue_ship=pg.image.load('pixel_ship_blue_small.png')
green_ship=pg.image.load('pixel_ship_green_small.png')
yellow_ship=pg.image.load('pixel_ship_yellow.png')

#lasers
red_laser=pg.image.load('pixel_laser_red.png')
yellow_laser=pg.image.load('pixel_laser_yellow.png')
green_laser=pg.image.load('pixel_laser_green.png')
blue_laser=pg.image.load('pixel_laser_blue.png')

#background
bg=pg.transform.scale(pg.image.load('background-black.png'),(width,height))


class Laser:
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.mask=pg.mask.from_surface(self.img)
    
    def draw(self):
        win.blit(self.img,(self.x,self.y))
    
    def move(self,vel):
        self.y+=vel
        
    def off_Screen(self):
        return not(self.y<=height or self.y>=0)
    
    def collision(self,obj):
        return collide(self,obj)
    
    
#class Ship which shares common attributes between class Player and class Enemy
class Ship:
    COOLDOWN=15
    
    def __init__(self,x,y,health=100):
        self.x=x
        self.y=y
        self.health=health
        self.ship_img=None
        self.laser_img=None
        self.lasers=[]
        self.cool_counter=0
    
    def draw(self):
        win.blit(self.ship_img,(self.x,self.y))
        for laser in self.lasers:
            laser.draw()
            
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()
    
    def shoot(self):
        if self.cool_counter==0:
            laser=Laser(self.x,self.y,self.laser_img)
            self.lasers.append(laser)
            self.cool_counter=1
            
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
        if self.cool_counter>=self.COOLDOWN:
            self.cool_counter=0
        elif self.cool_counter>0:
            self.cool_counter+=1
            

#class Player is inherits from class Ship         
class Player(Ship):
    def __init__(self,x,y,health=100):
            super().__init__(x,y,health)
            self.ship_img=yellow_ship
            self.laser_img=yellow_laser
            self.mask=pg.mask.from_surface(self.ship_img)
            self.max_health=health
            
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_Screen():
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                
    def healthbar(self):
        pg.draw.rect(win, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pg.draw.rect(win, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

        
    
#class Enemy is inherits from class Ship
class  Enemy(Ship):
    COLOR_MAP={
        "red":(red_ship,red_laser),
        "green":(green_ship,green_laser),
        "blue":(blue_ship,blue_laser)
    }
    
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pg.mask.from_surface(self.ship_img)
        
    def move(self, vel):
        self.y += vel
                    
    def shoot(self):
        if self.cool_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1  
            
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
    
def main():
    
   
    def redraw_window():
        win.blit(bg,(0,0))
        lives_label=main_font.render(f"Lives: {lives}",1,(255,255,255))
        level_label=main_font.render(f"Level: {level}",1,(255,255,255))
        lost_label=lost_font.render("You Lost!!",1,(255,255,255))
        for enemy in enemies:
            enemy.draw()
        
        player.draw()
        win.blit(lives_label,(10,10))
        win.blit(level_label,(width-level_label.get_width()-10,10))
        if lost:
            win.blit(lost_label,(width/2-lost_label.get_width()/2,350))
        
        player.healthbar()
        pg.display.update()
       
    level=0
    lives=5
    
    run=True
    FPS=40
    lost=False
    
    enemies=[]
    wave_length=0
    lost_count=0
    
    laser_vel=15
    player_vel=15
    enemy_vel=4
    
    player=Player(325,600)  
    clock=pg.time.Clock()
    
    main_font=pg.font.SysFont('Comic Sans',25)
    lost_font=pg.font.SysFont('Comic Sans',50)
    
    while run:
        
        clock.tick(FPS)
        redraw_window()
            
        if lives<=0 or player.health<=0:
            lost=True
            lost_count+=1
                
        if lost:
            if lost_count>FPS*3:
                run=False
            else:
                continue
                
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, width-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
                
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                
        #Movement of player
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pg.K_RIGHT] and player.x + player_vel + player.get_width() < width: # right
            player.x += player_vel
        if keys[pg.K_UP] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pg.K_DOWN] and player.y + player_vel + player.get_height() + 15 < height: # down
            player.y += player_vel
        if keys[pg.K_SPACE]:
            player.shoot()
    
        #Movement of enemies
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y+enemy.get_height()<height and enemy.y+enemy.get_height()>0:
                enemy.move_lasers(laser_vel-5,player)
            
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
             
            if random.randrange(0,3*60)==1:
                enemy.shoot()
                
            if enemy.y+enemy.get_height()>height:
                lives=lives-1
                enemies.remove(enemy)
                
        player.move_lasers(-laser_vel,enemies)
            

            
def main_menu():
    title_font = pg.font.SysFont("comicsans", 45)
    run = True
    while run:
        win.blit(bg, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        win.blit(title_label, (width/2 - title_label.get_width()/2, 350))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                main()
    pg.quit()


main_menu()