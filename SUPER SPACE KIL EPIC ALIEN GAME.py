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

# lasers1:
lasers_power = 2
lasers_speed = 0.5
lasers1_IMG = []
lasers1_X = []
lasers1_Y = []
startplaats1 = playerX - 20
for p in range(4):
    lasersIMG = pygame.image.load("minus.png")
    lasersIMG = pygame.transform.rotate(lasersIMG, 90)
    lasersIMG = pygame.transform.scale(lasersIMG, (50, 50))
    lasers1_IMG.append(lasersIMG)
    lasers1_X.append(startplaats1)
    lasers1_Y.append(500)
    startplaats1 += 10
    if startplaats1 == playerX:
        startplaats1 += 10

# lasers2:
lasers_power = 2
lasers_speed = 0.5
lasers2_IMG = []
lasers2_X = []
lasers2_Y = []
startplaats2 = playerX - 20
for p in range(4):
    lasersIMG = pygame.image.load("minus.png")
    lasersIMG = pygame.transform.rotate(lasersIMG, 90)
    lasersIMG = pygame.transform.scale(lasersIMG, (50, 50))
    lasers2_IMG.append(lasersIMG)
    lasers2_X.append(startplaats2)
    lasers2_Y.append(500)
    startplaats2 += 10
    if startplaats2 == playerX:
        startplaats2 += 10

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
alien_HP = 15
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


def laser(lasers, x, y):
    screen.blit(lasers, (x, y))


def collision(lasersX, lasersY, aliensX, aliensY):
    distance = math.sqrt(math.pow(aliensX - lasersX, 2) + math.pow(aliensY - lasersY, 2))
    if distance < 27:
        return True
    else:
        return False


def collision2(lasersX, lasersY, playerX, playerY):
    distance = math.sqrt(math.pow(playerX - lasersX, 2) + math.pow(playerY - lasersY, 2))
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
    for i in range(len(lasers1_Y)):
        lasers1_Y[i] -= lasers_speed
        laser(lasers1_IMG[i], lasers1_X[i], lasers1_Y[i])

    if start is True:
        for i in range(len(lasers2_Y)):
            lasers2_Y[i] -= lasers_speed
            laser(lasers2_IMG[i], lasers2_X[i], lasers2_Y[i])

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

        alle_lasers = 0
        alle_lasers2_semi = 0
        start_positie = playerX - 20
        for k in range(len(lasers1_Y)):
            if lasers1_Y[k] <= -50:
                alle_lasers += 1
                lasers1_X[k] = start_positie
                start_positie += 10
                if start_positie == playerX:
                    start_positie += 10
        for k in range(len(lasers2_Y)):
            if lasers2_Y[k] <= 220:
                alle_lasers2_semi += 1
        if alle_lasers == 4 and alle_lasers2_semi == 4:
            bullet_sound.play()
            for j in range(len(lasers1_Y)):
                if j == 0 or j == 3:
                    lasers1_Y[j] = 500
                else:
                    lasers1_Y[j] = 490

        alle_lasers2 = 0
        alle_lasers1_semi = 0
        start_positie = playerX - 20
        for k in range(len(lasers2_Y)):
            if lasers2_Y[k] <= -50:
                alle_lasers2 += 1
                lasers2_X[k] = start_positie
                start_positie += 10
                if start_positie == playerX:
                    start_positie += 10
        for k in range(len(lasers1_Y)):
            if lasers1_Y[k] <= 220:
                alle_lasers1_semi += 1
        if alle_lasers2 == 4 and alle_lasers1_semi == 4:
            bullet_sound.play()
            for j in range(len(lasers2_Y)):
                if j == 0 or j == 3:
                    lasers2_Y[j] = 500
                else:
                    lasers2_Y[j] = 490

        for s in range(len(lasers1_IMG)):
            if collision(lasers1_X[s], lasers1_Y[s], aliensX[i], aliensY[i]):
                aliens_HP[i] -= lasers_power
                lasers1_Y[s] = -1000
                score += lasers_power

        for t in range(len(lasers2_IMG)):
            if collision(lasers2_X[t], lasers2_Y[t], aliensX[i], aliensY[i]):
                aliens_HP[i] -= lasers_power
                lasers2_Y[t] = -1000
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
        for s in range(len(lasers1_IMG)):
            if collision3(lasers1_X[s], lasers1_Y[s], MonsterX, MonsterY):
                Monster_HP -= lasers_power
                lasers1_Y[s] = -1000
                score += lasers_power

        for t in range(len(lasers2_IMG)):
            if collision3(lasers2_X[t], lasers1_Y[t], MonsterX, MonsterY):
                Monster_HP -= lasers_power
                lasers2_Y[t] = -1000
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

    allemaal_semi = 0
    for m in range(len(lasers1_Y)):
        if lasers1_Y[m] <= 220:
            allemaal_semi += 1
    if allemaal_semi == 4:
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
            if num_aliens <= 6:
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
        for i in range(len(lasers1_X)):
            lasers1_X[i] = -100
        for i in range(len(lasers2_X)):
            lasers2_X[i] = -100
        lasers_speed = 0

    pygame.display.update()
