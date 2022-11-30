import pygame as pg
from configs import*

class Bloco(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load('parede.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)