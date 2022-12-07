
import pygame as pg

class Minion(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites,grupos_obstaculos):
        super().__init__(grupos_sprites)
        self.image = pg.image.load('minion.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)
        self.velocidade = 2
        self.sprites_obstaculos = grupos_obstaculos

    def movimento(self,posicao1,posicao2):
        self.distancia1 = (posicao1[0]**2+posicao1[1]**2)**0.5
        self.distancia2 = (posicao2[0]**2+posicao2[1]**2)**0.5
        if self.distancia1 < self.distancia2:
            if posicao1[0] > self.rect.x:
                self.rect.x += self.velocidade
            else:
                self.rect.x -= self.velocidade
            if posicao1[1] > self.rect.y:
                self.rect.y += self.velocidade
            else:
                self.rect.y -= self.velocidade
        else:
            if posicao2[0] > self.rect.x:
                self.rect.x += self.velocidade
            else:
                self.rect.x -= self.velocidade
            if posicao2[1] > self.rect.y:
                self.rect.y += self.velocidade
            else:
                self.rect.y -= self.velocidade
        self.colisao('horizontal')
        self.colisao('vertical')

    def colisao(self,direcao):
            if direcao ==  'horizontal':
                for sprite in self.sprites_obstaculos:
                    if sprite.rect.colliderect(self.rect):
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