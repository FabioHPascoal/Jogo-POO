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

        distancia_squared = Jogador.distancia_squared(novo_x, novo_y, x2, y2)
        inclinacao = Jogador.inclinacao(novo_x, novo_y, x2, y2)
        
        if distancia_squared >= (r + r2) ** 2:
            self.posicao = (novo_x, novo_y)
        
        else:
            for i in range(1, abs(self.velocidade[0])):
                novo_x = x + i * Jogador.sinal(self.velocidade[0])
                nova_distancia = Jogador.distancia_squared(novo_x, y, x2, y2)
                if nova_distancia < (r + r2) ** 2:
                    break
                self.posicao = (novo_x, y)
            x = novo_x
            
            for i in range(1, abs(self.velocidade[1])):
                novo_y = y + i * Jogador.sinal(self.velocidade[1])
                nova_distancia = Jogador.distancia_squared(x, novo_y, x2, y2)
                if nova_distancia < (r + r2) ** 2:
                    break
                self.posicao = (x, novo_y)
            y = novo_y

    def desenha(self, tela):
        cor = Configs.cor_personagem[self.classe_jogador]
        x, y = self.posicao
        r = Configs.raio_personagem[self.classe_jogador]
        pg.draw.circle(tela, cor, (x, y), r)

    def distancia_squared(x1, y1, x2, y2):
        distancia = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distancia
    
    def inclinacao(x1, y1, x2, y2):
        if x1 - x2 == 0:
            return math.pi/2
        else:
            inclinacao = math.atan((y1 - y2)/(x1 - x2))
            return inclinacao

    def elementoSuperior():
        pass

    def sinal(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

class Ataques:
    pass

class Minion:
    pass