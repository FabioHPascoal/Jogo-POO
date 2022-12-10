import pygame as pg
from configs import*

class Bloco(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/parede.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Grama(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/grama.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)