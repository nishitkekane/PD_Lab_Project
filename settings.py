import pygame

class Settings:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screenWidth = 1920
        self.screenHeight = 1080
        self.bgColour = (77,77,99)

        self.sound= True

        self.maxShip = 3

        self.maxBullets = 5
        self.maxSuperBullets = 1
        
        self.speedupGameplayScale = 1.2
        self.scoreSpeedupGameplayFactor = 1.5

        self.shipSpeedFactor = 10.0
        self.bulletSpeedFactor = 12.0
        self.superBulletSpeedFactor = 15.0
        
        self.AlienHitPointsByBullet = 100
        self.AlienHitPointsBySuperBullet = 50
        
        def increaseSpeed(self):
            self.shipSpeedUpFactor *= self.speedupGameplayScale
            self.bulletSpeedFactor *= self.speedupGameplayScale
            self.superBulletSpeedFactor *= self.speedupGameplayScale
            self.AlienHitPointsByBullet *= self.speedupGameplayScale
            self.AlienHitPointsBySuperBullet *= self.speedupGameplayScale

    def play_sound_effect(self, effect):
        if effect == "shootBullet":
            self.shootBullet = pygame.mixer.Sound("Assets/Audio/GunShot.mp3")
            self.shootBullet.set_volume(0.5)
            self.shootBullet.play()
        elif effect == "shootSuperBullet":
            self.shootSuperBullet_volume = pygame.mixer.Sound("Assets/Audio/GunShot.mp3")
            self.shootSuperBullet_volume(0.5)
            self.shootSuperBullet.play()
        elif effect == "explosion":
            self.explosion = pygame.mixer.Sound("Assets/Audio/Explosion.mp3")
            self.explosion.set_volume(0.5)
            self.explosion.play()
        elif effect == "button":
            self.button = pygame.mixer.Sound("Assets/Audio/Button.mp3")
            self.button.set_volume(0.5)
            self.button.play()
        elif effect == "nextLevel":
            self.nextLevel = pygame.mixer.Sound("Assets/Audio/Button.mp3")
            self.nextLevel.set_volume(0.5)
            self.nextLevel.play()
        elif effect == "crash":
            self.crash = pygame.mixer.Sound("Assets/Audio/Crash.wav")
            self.crash.set_volume(0.5)
            self.crash.play()
