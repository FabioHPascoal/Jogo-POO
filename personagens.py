import pygame as pg
from configs import Configs

class Personagem1:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = [0, 0]
        self.x2 = 0
    
    def mover_para_cima(self):
        self.velocidade[1] = -Configs.VELOCIDADE_PERSONAGEM

    def mover_para_baixo(self):
        self.velocidade[1] = Configs.VELOCIDADE_PERSONAGEM 
    
    def mover_para_esquerda(self):
        self.velocidade[0] = -Configs.VELOCIDADE_PERSONAGEM 
   
    def mover_para_direita(self):
        self.velocidade[0] = Configs.VELOCIDADE_PERSONAGEM

    def pararX(self):
        self.velocidade[0] = 0
        self.velocidade[1] = 0

    def pararY(self):
        self.velocidade[0] = 0
        self.velocidade[1] = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        novo_x = x + self.velocidade[0]
        novo_y = y + self.velocidade[1]

        if (novo_y >= 0) and ((novo_y + Configs.ALTURA_PERSONAGEM) <= Configs.ALTURA_TELA):
            self.posicao = (x, novo_y)
   
        if (novo_x >= 0) and ((novo_x + Configs.LARGURA_PERSONAGEM) <= Configs.LARGURA_TELA):
            self.posicao = (novo_x, y)

    def desenha(self, tela):
        x = self.posicao[0]
        y = self.posicao[1]
        l = Configs.LARGURA_PERSONAGEM
        a = Configs.ALTURA_PERSONAGEM
        pg.draw.rect(tela, Configs.COR_PERSONAGEM, pg.rect.Rect(x, y, l, a))