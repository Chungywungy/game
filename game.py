import math
import random
import pygame
from pygame import mixer

#initializes pygame
pygame.init()

#creates screen
screen = pygame.display.set_mode((800, 500))

#loads background
background = pygame.image.load('background.png')

#music
mixer.music.load('Free-electronic-music.mp3')
mixer.music.play(-1)

#name and icon of window
pygame.display.set_caption('Space Conqueror')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 380
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))

#enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render('score: ' + str(score_value), True,(255,255,255))
    screen.blit(score, (x, y))

#game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = pver_font.render('Dead', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

#collisions
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) \
            + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#game loop
running = True
while running:

#colour
    screen.fill((0, 0, 0))

#exit game
screen.blit(background, (0, 0))
for event in pygame.event.get():
    if event. type == pygame.QUIT:
        running = False

#controls
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        playerX_change = -5

    if event.key == pygame.K_RIGHT:
        playerX_change = 5

    if event.key == pygame.K_SPACE:

        if bullet_state == 'ready':
            bulletsound = mixer.sound('laser.mp3')
            bulletsound.play()

#location of player
bulletX = playerX
fire_bullet(bulletX, bulletY)
if event.type == pygame.KEYUP:

    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0

playerX += playerX_change
if playerX <= 0:
    playerX = 0

else: playerX >= 736
playerX = 736

#enemy movement
for i in range(num_of_enemies):

#game over screen
    if enemyY[i] > 340:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
            game_over_text()
            break

enemyX[i] += enemyX_change[i]
if enemyX[i] <= 0:
    enemyX_change = 4
    enemyY[i] += enemyY_change[i]
else: enemyX[i] >= 736
enemyX_change[i] = -4
enemyY[i] += enemyY_change[i]

#enemy collision
collision = isCollision(enemyX [i]. enemyY[i], bulletX, bulletY)
if collision:
    explosionsound = mixer.sound('explosion.wav')
    explosionsound.play()
    bulletY = 380
    bullet_state = 'ready'
    score_value += 1
    enemyX[i] = random.randint(0, 736)
    enemyY[i] = random.randint(50, 150)
    enemy(enemyX[i]. enemyY[i], i)

#bullet movement
if bulletY <= 0:
    bulletY = 380
    bullet_state = 'ready'

if bullet_state == 'fire':
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

