import pygame as pg
pg.init()
img = pg.image.load('input.jpg')
W, H = img.get_width(), img.get_height()
sc = pg. display.set_mode((W, H))
n = int(input())
t = 0
for x in range(W):
    for y in range(H):
        col = img.get_at((x, y))
        if col[0] == n :
            t += 1
pg.image.save(sc, 'output.png')
pg.quit()
print(t)