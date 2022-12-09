import pygame as pg
from funcoes import Funcoes
from configs import Configs

class Flecha(pg.sprite.Sprite):
    def __init__(self, direcao):
        super().__init__()
 
        self.direcao = direcao
        self.image = pg.Surface([4, 10])
        self.image.fill(Configs.PRETO)
        self.rect = self.image.get_rect()
        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.x += 3 * self.direcaoX
        self.rect.y += 3 * self.direcaoY
 