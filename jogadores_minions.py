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

    def atualizar_posicao(self, posicao_oponente, raio_oponente):
        self.posicao_oponente = posicao_oponente
        self.raio_oponente = raio_oponente
        
        x, y = self.posicao
        x2, y2 = self.posicao_oponente
        
        r = Configs.raio_personagem[self.classe_jogador]
        r2 = self.raio_oponente
      
        novo_x = x + self.velocidade[0]
        novo_y = y + self.velocidade[1]

        distancia = Jogador.distancia(novo_x, novo_y, x2, y2)
        
        if (distancia >= r + r2):
            self.posicao = (novo_x, y)
            x = novo_x

        # else:
        #     self.velocidade[0] = distancia - (r + r2)
        #     novo_x = x + self.velocidade[0]
        #     self.posicao = (novo_x, y)
        #     x = novo_x

        if (distancia >= r + r2):
            self.posicao = (x, novo_y)
            y = novo_y

        # else:
        #     self.velocidade[1] = distancia - (r + r2)
        #     novo_y = y + self.velocidade[1]
        #     self.posicao = (x, novo_y)
        #     y = novo_y

    def desenha(self, tela):
        cor = Configs.cor_personagem[self.classe_jogador]
        x, y = self.posicao
        r = Configs.raio_personagem[self.classe_jogador]
        pg.draw.circle(tela, cor, (x, y), r)

    def distancia(x1, y1, x2, y2):
        distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return int(distancia)

class Ataques:
    pass

class Minion:
    pass