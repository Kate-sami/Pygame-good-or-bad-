import pygame as pg
pg.init()
img = pg.image.load('input.jpg')
W, H = img.get_width(), img.get_height()
sc = pg. display.set_mode((W, H))
for x in range(W):
    for y in range(H):
        col = img.get_at((x, y))
        sc.set_at((x, y), (255-col[0] , 255-col[1] , 255-col[2]))
pg.image.save(sc, 'output.png')
pg.quit()