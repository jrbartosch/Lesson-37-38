import math
import random
import pygame
scrnwidth = 800
scrnheight = 500
playerstartx = 370
playerstarty = 380
enemystartymin = 50
enemystartymax = 150
enemyspdx = 4
enemyspdy = 40
bulletspdy = 10
crashdist = 27
pygame.init()
screen = pygame.display.set_mode((scrnwidth, scrnheight))
pygame.display.set_caption('Space Invaders')
img = pygame.image.load('ufo.png')
pygame.display.set_icon(img)
playerimg = pygame.image.load('player.png')
playerx = playerstartx
playery = playerstarty
playerxchange = 0
enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
enemynum = 6
bg = pygame.image.load('bg.png')
for _i in range(enemynum):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, scrnwidth - 64))
    enemyy.append(random.randint(enemystartymin, enemystartymax))
    enemyxchange.append(enemyspdx)
    enemyychange.append(enemyspdy)
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = playerstarty
bulletxchange = 0
bulletychange = bulletspdy
bulletstate = 'ready'
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10
gameoverfont = pygame.font.Font('freesansbold.ttf', 64)
scoreval = 0
def show_score(x, y):
    score = font.render('Score:' + str(scoreval), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_txt():
    gameovertxt = gameoverfont.render('GAME OVER', True, (255, 255, 255))
    screen.blit(gameovertxt, (200, 250))
def player(x, y):
    screen.blit(playerimg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))
def fire_bullet(x, y):
    global bulletstate
    bulletstate = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))
def checkcrash(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety) ** 2)
    return distance < crashdist
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -5
            if event.key == pygame.K_RIGHT:
                playerxchange = 5
            if event.key == pygame.K_SPACE and bulletstate == 'ready':
                bulletx = playerx
                fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerxchange = 0
    playerx += playerxchange
    playerx = max(0, min(playerx, scrnwidth - 64))
    for i in range(enemynum):
        if enemyy[i] > 340:
            for j in range(enemynum):
                enemyy[j] = 2000
            game_over_txt()
            break
        enemyx[i] += enemyxchange[i]
        if enemyx[i] <= 0 or enemyx[i] >= scrnwidth - 64:
            enemyxchange[i] *= -1
            enemyy[i] += enemyychange[i]
        if checkcrash(enemyx[i], enemyy[i], bulletx, bullety):
            bullety = playerstarty
            bulletstate = 'ready'
            scoreval += 1
            enemyx[i] = random.randint(0, scrnwidth - 64)
            enemyy[i] = random.randint(enemystartymin, enemystartymax)
        enemy(enemyx[i], enemyy[i], i)
        if bullety <= 0:
            bullety = playerstarty
            bulletstate = 'ready'
        elif bulletstate == 'fire':
            fire_bullet(bulletx, bullety)
            bullety -= bulletychange
        player(playerx, playery)
        show_score(textx, texty)
        pygame.display.update()
pygame.quit()