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
def show_score(x, y):
    score = font.render('Score:' + str(score), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_overtxt():
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
    screen.blit(bg, (0, 0))
    screen.blit(playerimg, (playerx, playery))
    for i in range(enemynum):
        screen.blit(enemyimg[i], (enemyx[i], enemyy[i]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()