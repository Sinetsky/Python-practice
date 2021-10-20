import pygame
import time

pygame.init()

pygame.mixer.music.load("Little Big - Hypnodancer.mp3")

animCount = 0
WIDTH, HEIGHT = 750, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))

frames = {
    1: pygame.image.load("frames/1.png"),
    2: pygame.image.load("frames/2.png"),
    3: pygame.image.load("frames/3.png"),
    4: pygame.image.load("frames/4.png"),
    5: pygame.image.load("frames/5.png"),
    6: pygame.image.load("frames/6.png"),
    7: pygame.image.load("frames/7.png"),
    8: pygame.image.load("frames/8.png"),
    9: pygame.image.load("frames/9.png"),
    10: pygame.image.load("frames/10.png")
}

def animation():
    global animCount
    animCount += 1
    if animCount == 10:
        animCount = 1
    time.sleep(0.12)

pygame.mixer.music.play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    animation()
    pygame.display.update()
    screen.blit(frames[animCount], (0, 0))

pygame.quit()