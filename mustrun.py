import pgzrun
import pygame
import pygame.freetype
import random
import time
import sys

WIDTH = 1000
HEIGHT = 600

max_width = WIDTH - 30
min_width = 30
max_height = HEIGHT - 50
min_height = 150

apple = Actor('apple')
apple.pos = 300,300

runner = Actor('dancer-start')
runner.pos = 30,560

def draw():
    screen.fill((30, 30, 30))
    runner.draw()
    apple.draw()

def draw_text(text):
    font = pygame.font.SysFont("arial", 25)
    y_pos = x_pos = 5
    text = font.render(text, 10, (255, 255, 255))
    screen.blit(text, (x_pos, y_pos))
    pygame.display.update()
    time.sleep(0.1)
    
def update():
    keys = pygame.key.get_pressed()  #
    if keys[pygame.K_RIGHT]:  #
        if runner.x > max_width:
            runner.x = max_width
        else:
            runner.left += 5
    if keys[pygame.K_LEFT]:  #
        if runner.x < min_width:
            runner.x = min_width
        else:
            runner.left -= 5
    if keys[pygame.K_UP]:  #
        if runner.y < min_height:
            runner.y = min_height
        else:
            runner.y -= 5
            print (runner.y)
    if keys[pygame.K_DOWN]:  #
        if runner.y > max_height:
            runner.y = max_height
        else:
            runner.y += 5
    if runner.collidepoint(apple.pos):
        apple.pos = random.randint(min_width,max_width),random.randint(min_height,max_height)
        apple.draw()
        draw_text("Hallo")
    if keys[pygame.K_ESCAPE]:
        quit()

pgzrun.go()