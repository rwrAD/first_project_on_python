from random import randint
import pygame as pg
import sys
 
W = 400
H = 400
WHITE = (255, 255, 255)
 
 
class Car(pg.sprite.Sprite):
    def __init__(self, x, filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(
            pg.image.load(filename), (70, 70))

        self.x = x
        self.rect = self.image.get_rect(
            center=(self.x, 0))
    def update(self):
        if self.rect.y < H:
            self.rect.y += 2
        else:
            self.rect.x = randint(1, W)
            self.rect.y = -70
 
 
sc = pg.display.set_mode((W, H))
 
# координата x будет случайна
ufos = pg.sprite.Group()
ufos.add(Car(randint(1,W), 'ufo.png'),
        Car(randint(1,W), 'ufo.png'),
        Car(randint(1,W), 'ufo.png'),
        Car(randint(1,W), 'ufo.png'),
        Car(randint(1,W), 'ufo.png'))


 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
 
    sc.fill(WHITE)
    
    ufos.draw(sc)

    pg.display.update()
    pg.time.delay(20)

    ufos.update()
 
    # машинка ездит сверху вниз
    

    