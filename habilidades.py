import pygame as pg
from funcoes import Funcoes
from configs import Configs

class Flecha(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
 
        self.direcao = direcao
        self.posicao = posicao
        self.velocidade = Configs.velocidade_projeteis["flecha"]

        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.x += self.velocidade * self.direcaoX
        self.rect.y += self.velocidade * self.direcaoY