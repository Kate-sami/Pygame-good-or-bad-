import pygame as pg
pg.init()
img = pg.image.load('input.jpg')
W, H = img.get_width(), img.get_height()
sc = pg. display.set_mode((W, H))
for x in range(W):
    for y in range(H):
        col = img.get_at((x, y))
        my_color = (col[0]+col[1]+col[2]) / 3
        sc.set_at((x, y), (my_color, my_color, my_color ))
pg.image.save(sc, 'output.png')
pg.quit()