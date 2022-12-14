import pygame as pg
from funcoes import Funcoes
from configs import Configs

class Espadada(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.tempoSurgimento = pg.time.get_ticks()
        self.projetil = False
        self.duracao = 250
        self.direcao = direcao
        self.posicao = posicao
        self.velocidade = 0
        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.centerx += self.velocidade * self.direcaoX
        self.rect.centery += self.velocidade * self.direcaoY
        self.tempoExistente = pg.time.get_ticks() - self.tempoSurgimento
        if self.tempoExistente > self.duracao:
            self.kill()

class Flecha(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.projetil = True
        self.direcao = direcao
        self.posicao = posicao
        self.velocidade = Configs.velocidade_projeteis["flecha"]
        self.image = image
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = self.posicao)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.centerx += self.velocidade * self.direcaoX
        self.rect.centery += self.velocidade * self.direcaoY

class Facada(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.tempoSurgimento = pg.time.get_ticks()
        self.projetil = True
        self.duracao = 200
        self.direcao = direcao
        self.posicao = posicao
        self.velocidade = Configs.velocidade_projeteis["facada"]
        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.centerx += self.velocidade * self.direcaoX
        self.rect.centery += self.velocidade * self.direcaoY
        self.tempoExistente = pg.time.get_ticks() - self.tempoSurgimento
        if self.tempoExistente > self.duracao:
            self.kill()

class Fireball(pg.sprite.Sprite):
    def __init__(self, posicao, direcao, image):
        super().__init__()
        self.projetil = True
        self.direcao = direcao
        self.posicao = posicao
        self.velocidade = Configs.velocidade_projeteis["fireball"]
        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)

        self.direcaoX = Funcoes.sinal(self, self.direcao[0])
        self.direcaoY = Funcoes.sinal(self, self.direcao[1])
 
    def update(self):
        self.rect.centerx += self.velocidade * self.direcaoX
        self.rect.centery += self.velocidade * self.direcaoY

class Fire_floor(pg.sprite.Sprite):
    def __init__(self, posicao, image):
        super().__init__()
        self.tempoSurgimento = pg.time.get_ticks()
        self.projetil = False
        self.duracao = 5000
        self.posicao = posicao
        self.image = image
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)
 
    def update(self):
        self.tempoExistente = pg.time.get_ticks() - self.tempoSurgimento
        if self.tempoExistente > self.duracao:
            self.kill()