
import pygame as pg
from configs import*

class Minion(pg.sprite.Sprite):
    def __init__(self,posicao,classe,grupos_sprites,grupos_obstaculos):
        super().__init__(grupos_sprites)
        self.classe = classe
        self.image = pg.image.load('minion.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)
        self.velocidade = 1
        self.sprites_obstaculos = grupos_obstaculos
        self.sprites_minions = grupos_sprites

    def movimento(self,posicao1,posicao2):
        self.distancia1 = (posicao1[0] - self.rect.x)**2 + (posicao1[1] - self.rect.y)**2
        self.distancia2 = (posicao2[0] - self.rect.x)**2 + (posicao2[1] - self.rect.y)**2

        if self.distancia1 < self.distancia2:
            if posicao1[0] > self.rect.right:
                self.rect.x += self.velocidade
            else:
                self.rect.x -= self.velocidade
            self.colisao('horizontal')
            if posicao1[1] > self.rect.bottom:
                self.rect.y += self.velocidade
            else:
                self.rect.y -= self.velocidade
            self.colisao('vertical')

        else:
            if posicao2[0] > self.rect.right:
                self.rect.x += self.velocidade
            else:
                self.rect.x -= self.velocidade
            self.colisao('horizontal')
            if posicao2[1] > self.rect.bottom:
                self.rect.y += self.velocidade
            else:
                self.rect.y -= self.velocidade
            self.colisao('vertical')

        self.correcaoSairDoMapa()

    def colisao(self,direcao):
        colisaoEntreMinions = 0
        if direcao ==  'horizontal':
            for sprite in self.sprites_obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.rect.left < sprite.rect.left:
                        self.rect.right = sprite.rect.left
                    else:
                        self.rect.left = sprite.rect.right
            for sprite in self.sprites_minions:
                if sprite.rect.colliderect(self.rect):
                    colisaoEntreMinions += 1
                    if colisaoEntreMinions > 1:
                        if self.rect.left < sprite.rect.left:
                            self.rect.right = sprite.rect.left
                        else:
                            self.rect.left = sprite.rect.right
   

        if direcao ==  'vertical':
            for sprite in self.sprites_obstaculos:
                if sprite.rect.colliderect(self.rect):
                    if self.rect.top < sprite.rect.top:
                        self.rect.bottom = sprite.rect.top
                    else:
                        self.rect.top = sprite.rect.bottom

            for sprite in self.sprites_minions:
                if sprite.rect.colliderect(self.rect):
                    colisaoEntreMinions += 1
                    if colisaoEntreMinions > 1:
                        if self.rect.top < sprite.rect.top:
                            self.rect.bottom = sprite.rect.top
                        else:
                            self.rect.top = sprite.rect.bottom

    def correcaoSairDoMapa(self):
        if self.rect.left < Configs.BLOCOS_TAMANHO:
            self.rect.left = Configs.BLOCOS_TAMANHO
        if self.rect.right > Configs.LARGURA_TELA - Configs.BLOCOS_TAMANHO:
            self.rect.right = Configs.LARGURA_TELA - Configs.BLOCOS_TAMANHO
        if self.rect.top < Configs.BLOCOS_TAMANHO:
            self.rect.top = Configs.BLOCOS_TAMANHO
        if self.rect.bottom > Configs.ALTURA_TELA - Configs.BLOCOS_TAMANHO:
            self.rect.bottom = Configs.ALTURA_TELA - Configs.BLOCOS_TAMANHO