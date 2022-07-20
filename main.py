import math
import random

import pygame
from pygame import mixer

# Initializing of game:
pygame.init()

# The screen:
RandX = 700
RandY = 620
screen = pygame.display.set_mode((RandX, RandY))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Background:
Background = pygame.image.load("Background3.jpg")
Background = pygame.transform.scale(Background, (RandX, RandY))
mixer.music.load("background.wav")
mixer.music.play(-1)
bullet_sound = mixer.Sound("laser.wav")



# Player:
playerIMG = pygame.image.load("spaceship.png")
playerIMG = pygame.transform.scale(playerIMG, (50, 50))
playerX = 320
playerY = 500
player_speed = 0.175
playerX_change = 0

player_HP = 3

# lasers:
lasers_power = 2

lasersIMG = pygame.image.load("minus.png")
lasersIMG = pygame.transform.rotate(lasersIMG, 90)
lasersIMG = pygame.transform.scale(lasersIMG, (50, 50))
lasersX = playerX - 20
lasersY = 500
lasers_speed = 0.5
lasersY_change = lasers_speed

lasers2IMG = pygame.image.load("minus.png")
lasers2IMG = pygame.transform.rotate(lasersIMG, 90)
lasers2IMG = pygame.transform.scale(lasersIMG, (50, 50))
lasers2X = playerX - 10
lasers2Y = 500
lasers2_speed = 0.5
lasers2Y_change = lasers_speed

lasers3IMG = pygame.image.load("minus.png")
lasers3IMG = pygame.transform.rotate(lasersIMG, 90)
lasers3IMG = pygame.transform.scale(lasersIMG, (50, 50))
lasers3X = playerX + 10
lasers3Y = 500
lasers3_speed = 0.5
lasers3Y_change = lasers_speed

lasers4IMG = pygame.image.load("minus.png")
lasers4IMG = pygame.transform.rotate(lasersIMG, 90)
lasers4IMG = pygame.transform.scale(lasersIMG, (50, 50))
lasers4X = playerX + 20
lasers4Y = 500
lasers4_speed = 0.5
lasers4Y_change = lasers_speed

lasers5IMG = pygame.image.load("minus.png")
lasers5IMG = pygame.transform.rotate(lasers5IMG, 90)
lasers5IMG = pygame.transform.scale(lasers5IMG, (50, 50))
lasers5X = playerX - 20
lasers5Y = 500
lasers5_speed = 0.5
lasers5Y_change = lasers_speed

lasers6IMG = pygame.image.load("minus.png")
lasers6IMG = pygame.transform.rotate(lasers6IMG, 90)
lasers6IMG = pygame.transform.scale(lasers6IMG, (50, 50))
lasers6X = playerX - 10
lasers6Y = 500
lasers6_speed = 0.5
lasers6Y_change = lasers_speed

lasers7IMG = pygame.image.load("minus.png")
lasers7IMG = pygame.transform.rotate(lasers7IMG, 90)
lasers7IMG = pygame.transform.scale(lasers7IMG, (50, 50))
lasers7X = playerX + 10
lasers7Y = 500
lasers7_speed = 0.5
lasers7Y_change = lasers_speed

lasers8IMG = pygame.image.load("minus.png")
lasers8IMG = pygame.transform.rotate(lasers8IMG, 90)
lasers8IMG = pygame.transform.scale(lasers8IMG, (50, 50))
lasers8X = playerX + 20
lasers8Y = 500
lasers8_speed = 0.5
lasers8Y_change = lasers_speed

start = False

# Upgrades:
upgradesIMG = []
upgradesIMGX = []
upgradesIMGY = []
upgradesIMGY_change = []
player_speedIMG = pygame.image.load("hedgehog.png")
player_speedIMG = pygame.transform.scale(player_speedIMG, (50, 50))
upgradesIMGX_player_speed = 100
upgradesIMG.append(player_speedIMG)
upgradesIMGX.append(upgradesIMGX_player_speed)
upgradesIMGY.append(-50)
upgradesIMGY_change.append(0)
player_PowerIMG = pygame.image.load("muscle.png")
player_PowerIMG = pygame.transform.scale(player_PowerIMG, (50, 50))
upgradesIMGX_player_power = 325
upgradesIMG.append(player_PowerIMG)
upgradesIMGX.append(upgradesIMGX_player_power)
upgradesIMGY.append(-50)
upgradesIMGY_change.append(0)
bullet_speedIMG = pygame.image.load("bullets.png")
bullet_speedIMG = pygame.transform.scale(bullet_speedIMG, (50, 50))
upgradesIMGX_bullet_speed = 550
black_rgb = (0, 0, 0)
white_rgb = (255, 255, 255)
var = pygame.PixelArray(bullet_speedIMG)
var.replace(black_rgb, white_rgb)  # replaces all black in the picture to white
del var
upgradesIMG.append(bullet_speedIMG)
upgradesIMGX.append(upgradesIMGX_bullet_speed)
upgradesIMGY.append(-50)
upgradesIMGY_change.append(0)


# Aliens:
num_aliens = 1
alien_HP = 5
aliensX = []
aliensY = []
aliensX_change = []
aliensY_change = []
aliensIMG = []
aliens_HP = []
lege_lijst = []
volle_lijst = []
for i in range(num_aliens):
    lege_lijst.append(0)
    volle_lijst.append(1000)

for i in range(num_aliens):
    alienIMG = pygame.image.load("ufo.png")
    alienIMG = pygame.transform.scale(alienIMG, (50, 50))
    aliensIMG.append(alienIMG)
    black_rgb = (0, 0, 0)
    red_rgb = (255, 0, 0)
    var = pygame.PixelArray(alienIMG)
    var.replace(black_rgb, red_rgb)  # replaces all black in the picture to red
    del var

    aliensX.append(random.randint(0, 650))
    aliensY.append(random.randint(-100, -50))
    aliens_speed = 0.10
    aliensX_change.append(aliens_speed)
    aliensY_change.append(0)

    aliens_HP.append(alien_HP)
    level = 1

# Monster:
Monster_start = False
matterIMG = pygame.image.load("dark-matter.png")
matterIMG = pygame.transform.scale(matterIMG, (50, 50))
matter_speed = 0.35
matter_change = 0
matter_power = 1
matterX = 300
matterY = -20

score = 0
semi = 0

font = pygame.font.Font("freesansbold.ttf", 32)
tekstX = 10
tekstY = 10


def player(x, y):
    screen.blit(playerIMG, (x, y))


def laser(laser, x, y):
    screen.blit(laser, (x, y))


def collision(laserX, laserY, aliensX, aliensY):
    distance = math.sqrt(math.pow(aliensX - laserX, 2) + math.pow(aliensY - laserY, 2))
    if distance < 27:
        return True
    else:
        return False


def collision2(laserX, laserY, playerX, playerY):
    distance = math.sqrt(math.pow(playerX - laserX, 2) + math.pow(playerY - laserY, 2))
    if distance < 35:
        return True
    else:
        return False


def collision3(MonsterX, MonsterY, playerX, playerY):
    distance = math.sqrt(math.pow(playerX - MonsterX, 2) + math.pow(playerY - MonsterY, 2))
    if distance < 100:
        return True
    else:
        return False


def upgrades(x, y, k):
    screen.blit(upgradesIMG[k], (x, y))


def aliens(x, y, i):
    screen.blit(aliensIMG[i], (x, y))


def monster(x, y):
    screen.blit(MonsterIMG, (x, y))


def show_score(x, y):
    score2 = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score2, (x, y))


def show_hp(x, y):
    hp = font.render("HP: " + str(player_HP), True, (255, 255, 255))
    screen.blit(hp, (x, y))


def show_level(x, y):
    levels = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(levels, (x, y))


running = True
while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Colors:
    screen.fill((0, 0, 40))
    screen.blit(Background, (0, 0))

    # Speler:
    if playerX <= 0:
        playerX = 0
    if playerX >= RandX - 50:
        playerX = RandX - 50
    playerX += playerX_change
    player(playerX, playerY)

    # Monster:
    if level == 10:
        if MonsterX <= 0:
            MonsterX_change *= -1
            MonsterY += 50
        if MonsterX >= RandX - 50:
            MonsterX_change *= -1
            MonsterY += 50
        MonsterX += MonsterX_change
        matter_change = matter_speed
        if MonsterX_change > 0:
            matterX += matter_change / 8
        elif MonsterX_change < 0:
            matterX -= matter_change / 8
        matterY += matter_change
        laser(matterIMG, matterX, matterY)
        monster(MonsterX, MonsterY)

        if matterY >= RandY:
            matterY = MonsterY + 30
            matterX = MonsterX

    # laser:
    lasersY_change = lasers_speed
    lasers2Y_change = lasers_speed
    lasers3Y_change = lasers_speed
    lasers4Y_change = lasers_speed
    lasers5Y_change = lasers_speed
    lasers6Y_change = lasers_speed
    lasers7Y_change = lasers_speed
    lasers8Y_change = lasers_speed

    lasersY -= lasersY_change
    laser(lasersIMG, lasersX, lasersY)

    lasers2Y -= lasers2Y_change
    laser(lasers2IMG, lasers2X, lasers2Y)

    lasers3Y -= lasers3Y_change
    laser(lasers3IMG, lasers3X, lasers3Y)

    lasers4Y -= lasers4Y_change
    laser(lasers4IMG, lasers4X, lasers4Y)

    if start is True:
        lasers5Y -= lasers5Y_change
        laser(lasers5IMG, lasers5X, lasers5Y)

        lasers6Y -= lasers6Y_change
        laser(lasers6IMG, lasers6X, lasers6Y)

        lasers7Y -= lasers7Y_change
        laser(lasers7IMG, lasers7X, lasers7Y)

        lasers8Y -= lasers8Y_change
        laser(lasers8IMG, lasers8X, lasers8Y)

    for i in range(num_aliens):
        # Aliens:
        if aliensX[i] <= 0:
            aliensX_change[i] *= -1
            aliensY[i] += 30
        if aliensX[i] >= RandX - 50:
            aliensX_change[i] *= -1
            aliensY[i] += 30
        aliensX[i] += aliensX_change[i]
        aliensY[i] += aliensY_change[i]
        aliens(aliensX[i], aliensY[i], i)

        if aliensY[i] >= RandY:
            aliensX[i] = 1000
            aliensX_change[i] = 0
            aliensY_change[i] = 0

        if lasersY <= 0:
            lasersX = playerX - 20
            lasersY = 500
            bullet_sound.play()

        if lasers2Y <= 0:
            lasers2X = playerX - 10
            lasers2Y = 490
            bullet_sound.play()

        if lasers3Y <= 0:
            lasers3X = playerX + 10
            lasers3Y = 490
            bullet_sound.play()

        if lasers4Y <= 0:
            lasers4X = playerX + 20
            lasers4Y = 500
            bullet_sound.play()

        if lasers5Y <= 0:
            lasers5X = playerX - 20
            lasers5Y = 500
            bullet_sound.play()

        if lasers6Y <= 0:
            lasers6X = playerX - 10
            lasers6Y = 490
            bullet_sound.play()

        if lasers7Y <= 0:
            lasers7X = playerX + 10
            lasers7Y = 490
            bullet_sound.play()

        if lasers8Y <= 0:
            lasers8X = playerX + 20
            lasers8Y = 500
            bullet_sound.play()

        if collision(lasersX, lasersY, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasersX = playerX - 20
            lasersY = 500
            score += lasers_power

        if collision(lasers2X, lasers2Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers2X = playerX - 10
            lasers2Y = 500
            score += lasers_power

        if collision(lasers3X, lasers3Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers3X = playerX + 10
            lasers3Y = 500
            score += lasers_power

        if collision(lasers4X, lasers4Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers4X = playerX + 20
            lasers4Y = 500
            score += lasers_power

        if collision(lasers5X, lasers5Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers5X = playerX - 20
            lasers5Y = 500
            score += lasers_power

        if collision(lasers6X, lasers6Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers6X = playerX - 10
            lasers6Y = 500
            score += lasers_power

        if collision(lasers7X, lasers7Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers7X = playerX + 10
            lasers7Y = 500
            score += lasers_power

        if collision(lasers8X, lasers8Y, aliensX[i], aliensY[i]):
            aliens_HP[i] -= lasers_power
            lasers8X = playerX + 20
            lasers8Y = 500
            score += lasers_power

        if collision2(playerX, playerY, aliensX[i], aliensY[i]):
            player_HP -= 1
            aliensX[i] = 1000
            aliensY_change[i] = 0
            aliensX_change[i] = 0

        if aliens_HP[i] <= 0:
            aliensX[i] = 1000
            aliensX_change[i] = 0
            aliensY_change[i] = 0
            aliens_HP[i] = 0

    if level >= 10:
        # Monster Vecht:
        if collision3(lasersX, lasersY, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasersX = playerX - 20
            lasersY = 500
            score += lasers_power

        if collision3(lasers2X, lasers2Y, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasers2X = playerX - 10
            lasers2Y = 500
            score += lasers_power

        if collision3(lasers3X, lasers3Y, MonsterX, MonsterX):
            Monster_HP -= lasers_power
            lasers3X = playerX + 10
            lasers3Y = 500
            score += lasers_power

        if collision3(lasers4X, lasers4Y, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasers4X = playerX + 20
            lasers4Y = 500
            score += lasers_power

        if collision3(lasers5X, lasers5Y, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasers5X = playerX - 20
            lasers5Y = 500
            score += lasers_power

        if collision3(lasers6X, lasers6Y, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasers6X = playerX - 10
            lasers6Y = 500
            score += lasers_power

        if collision3(lasers7X, lasers7Y, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasers7X = playerX + 10
            lasers7Y = 500
            score += lasers_power

        if collision3(lasers8X, lasers8Y, MonsterX, MonsterY):
            Monster_HP -= lasers_power
            lasers8X = playerX + 20
            lasers8Y = 500
            score += lasers_power

        if collision2(playerX, playerY, matterX, matterY):
            player_HP -= 1
            matterX = MonsterX
            matterY = MonsterY

        if collision3(playerX, playerY, MonsterX, MonsterY):
            player_HP -= 100

        if Monster_HP <= 0:
            MonsterX = 1000
            MonsterX_change = 0

    if lasersY <= 250:
        start = True
    # Score:
    show_score(tekstX, tekstY)

    # HP:
    show_hp(580, 550)

    # Level:
    show_level(20, 550)

    # Upgrades:
    for m in range(len(upgradesIMG)):
        upgradesIMGY[m] += upgradesIMGY_change[m]
        upgrades(upgradesIMGX[m], upgradesIMGY[m], m)
        if collision2(upgradesIMGX[m], upgradesIMGY[m], playerX, playerY) is True:
            if upgradesIMG[m] == bullet_speedIMG:
                lasers_speed += 0.2
                lasers2_speed += 0.2
                upgradesIMGY[m] = -50
                upgradesIMGY_change[m] = 0
            if upgradesIMG[m] == player_speedIMG:
                player_speed += 0.1
                upgradesIMGY[m] = -50
                upgradesIMGY_change[m] = 0
            if upgradesIMG[m] == player_PowerIMG:
                lasers_power += 1
                upgradesIMGY[m] = -50
                upgradesIMGY_change[m] = 0
        if upgradesIMGY[m] >= RandY:
            upgradesIMGY[m] = -50
            upgradesIMGY_change[m] = 0

    if (aliens_HP == lege_lijst or aliensX == volle_lijst) and Monster_start is False:
        # Player:
        level += 1
        for p in range(len(upgradesIMG)):
            upgradesIMGY_change[p] += 0.16

        # Aliens:
        if level <= 9:
            if num_aliens <= 8:
                num_aliens += 1
            else:
                alien_HP += 5
            aliens_speed += 0.1
            alien_HP += 5
            aliensX = []
            aliensY = []
            aliensX_change = []
            aliensY_change = []
            aliensIMG = []
            aliens_HP = []
            lege_lijst = []
            volle_lijst = []
            for i in range(num_aliens):
                lege_lijst.append(0)
                volle_lijst.append(1000)

            for i in range(num_aliens):
                alienIMG = pygame.image.load("ufo.png")
                alienIMG = pygame.transform.scale(alienIMG, (50, 50))
                aliensIMG.append(alienIMG)
                black_rgb = (0, 0, 0)
                red_rgb = (255, 0, 0)
                var = pygame.PixelArray(alienIMG)
                var.replace(black_rgb, red_rgb)  # replaces all black in the picture to red
                del var

                aliensX.append(random.randint(0, 650))
                aliensY.append(random.randint(-150, -50))
                aliensX_change.append(aliens_speed)
                aliensY_change.append(0)

                aliens_HP.append(alien_HP)
        else:
            MonsterIMG = pygame.image.load("monster.png")
            MonsterIMG = pygame.transform.scale(MonsterIMG, (150, 150))
            black_rgb = (0, 0, 0)
            red_rgb = (255, 0, 0)
            var = pygame.PixelArray(MonsterIMG)
            var.replace(black_rgb, red_rgb)  # replaces all black in the picture to red
            del var

            MonsterX = 300
            MonsterY = -100
            Monster_speed = 0.2
            MonsterX_change = Monster_speed
            MonsterY_change = 0
            Monster_HP = 2000
            Monster_start = True

    if player_HP <= 0:
        einde = font.render("You Died", True, (255, 255, 255))
        screen.blit(einde, (260, 300))
        einde2 = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(einde2, (260, 350))
        for i in range(num_aliens):
            aliensX_change[i] = 0
            player_speed = 0
            lasers_speed = 0

    if level == 10 and Monster_HP <= 0:
        einde = font.render("You Won", True, (255, 255, 255))
        screen.blit(einde, (260, 300))
        einde2 = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(einde2, (260, 350))
        player_speed = 0
        lasersX = -100
        lasers2X = -100
        lasers3X = -100
        lasers4X = -100
        lasers5X = -100
        lasers6X = -100
        lasers7X = -100
        lasers8X = -100
        lasers_speed = 0


    pygame.display.update()

