import pygame as pg
import math
from configs import Configs

class Jogador:
    def __init__(self, classe_jogador, posicao):
        self.posicao = posicao
        self.velocidade = [0, 0]
        self.classe_jogador = classe_jogador
    
    def moverX(self, angulo):
        self.velocidade[0] = int(Configs.velocidade_personagem[self.classe_jogador] * math.cos(angulo))

    def moverY(self, angulo):
        self.velocidade[1] = int(Configs.velocidade_personagem[self.classe_jogador] * math.sin(angulo)) * -1

    def pararX(self):
        self.velocidade[0] = 0

    def pararY(self):
        self.velocidade[1] = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        novo_x = x + self.velocidade[0]
        novo_y = y + self.velocidade[1]
        r = Configs.raio_personagem[self.classe_jogador]
        
        if  (novo_x + r >= 0) and (novo_x + r <= Configs.LARGURA_TELA)\
        and (novo_x - r >= 0) and (novo_x - r <= Configs.LARGURA_TELA):
            self.posicao = (novo_x, y)
            x = novo_x

        if  (novo_y + r >= 0) and (novo_y + r <= Configs.ALTURA_TELA)\
        and (novo_y - r >= 0) and (novo_y - r <= Configs.ALTURA_TELA):
            self.posicao = (x, novo_y)
            y = novo_y

    def desenha(self, tela):
        cor = Configs.cor_personagem[self.classe_jogador]
        x, y = self.posicao
        r = Configs.raio_personagem[self.classe_jogador]
        pg.draw.circle(tela, cor, (x, y), r)

class Ataques:
    pass
class Minion:
    pass