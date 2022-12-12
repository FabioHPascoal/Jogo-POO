import pygame as pg
from funcoes import Funcoes
from configs import Configs

class Espadada(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.tempoSurgimento = pg.time.get_ticks()
        self.projetil = False
        self.duracao = 700
        self.direcao = direcao
        self.posicao = posicao
        self.velocidade = 0
        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.x += self.velocidade * self.direcaoX
        self.rect.y += self.velocidade * self.direcaoY
        self.tempoExistente = pg.time.get_ticks() - self.tempoSurgimento
        if self.tempoExistente > self.duracao:
            self.kill()

class Flecha(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.tempoSurgimento = pg.time.get_ticks()
        self.projetil = True
        self.duracao = 5000
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
        self.tempoExistente = pg.time.get_ticks() - self.tempoSurgimento
        if self.tempoExistente > self.duracao:
            self.kill()

class Fire_floor(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.tempoSurgimento = pg.time.get_ticks()
        self.projetil = False
        self.duracao = 5000
        self.direcao = direcao
        self.posicao = [posicao[0] + Funcoes.sinal(self, direcao[0]) * 150, posicao[1] + Funcoes.sinal(self, direcao[1]) * 150]
        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.tempoExistente = pg.time.get_ticks() - self.tempoSurgimento
        if self.tempoExistente > self.duracao:
            self.kill()