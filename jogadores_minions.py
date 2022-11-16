import pygame as pg
from scipy.optimize import fsolve
import sympy as sym
import math
from configs import Configs

class Jogador:
    def __init__(self, classe_jogador, posicao):
        self.classe_jogador = classe_jogador
        self.raio = Configs.raio_personagem[self.classe_jogador]
        self.massa = Configs.massa_personagem[self.classe_jogador]
        self.velocidade = [0, 0]
        self.posicao = posicao
        self.colidiu = False
    
    def moverX(self, angulo):
        self.velocidade[0] = int(Configs.velocidade_personagem[self.classe_jogador] * math.cos(angulo))

    def moverY(self, angulo):
        self.velocidade[1] = int(Configs.velocidade_personagem[self.classe_jogador] * math.sin(angulo)) * -1

    def pararX(self):
        self.velocidade[0] = 0

    def pararY(self):
        self.velocidade[1] = 0

    def atualiza_posicao(self, posicao_oponente, raio_oponente): 
        self.posicao_oponente = posicao_oponente
        self.raio_oponente = raio_oponente
        
        x, y = self.posicao
        x2, y2 = self.posicao_oponente
        
        r = self.raio
        r2 = self.raio_oponente
      
        novo_x = x + self.velocidade[0]
        novo_y = y + self.velocidade[1]

        distancia_squared = Jogador.distancia_squared(novo_x, novo_y, x2, y2)
       
        if distancia_squared >= (r + r2) ** 2:
            self.posicao = (novo_x, novo_y)
            self.colidiu = False

        elif distancia_squared < (r + r2) ** 2:
            self.colidiu = True
    
        return self.posicao

    def posicao_caso_colidiu(self, novaPosicao, novaPosicao_oponente, velocidade_oponente, massa_oponente):
        x, y = self.posicao
        x2, y2 = self.posicao_oponente

        r = Configs.raio_personagem[self.classe_jogador]
        r2 = self.raio_oponente

        V1x, V1y = self.velocidade
        V2x, V2y = velocidade_oponente

        m = self.massa
        m2 = massa_oponente

        novo_x, novo_y = novaPosicao
        novo_x2, novo_y2 = novaPosicao_oponente

        if self.colidiu:
            
            self.velocidade[0] = Jogador.velocidade_colisao(m, V1x, m2, V2x)
            self.velocidade[1] = Jogador.velocidade_colisao(m, V1y, m2, V2y)

            for i in range(1, abs(self.velocidade[0])):
                novo_x = x + i * Jogador.sinal(self.velocidade[0])
                nova_distancia = Jogador.distancia_squared(novo_x, y, novo_x2, y2)
                if nova_distancia < (r + r2) ** 2:
                    break
                self.posicao = (novo_x, y)
            x = novo_x
            
            for i in range(1, abs(self.velocidade[1])):
                novo_y = y + i * Jogador.sinal(self.velocidade[1])
                nova_distancia = Jogador.distancia_squared(x, novo_y, x2, novo_y2)
                if nova_distancia < (r + r2) ** 2:
                    break
                self.posicao = (x, novo_y)
            y = novo_y

    def desenha(self, tela):
        cor = Configs.cor_personagem[self.classe_jogador]
        x, y = self.posicao
        r = Configs.raio_personagem[self.classe_jogador]
        pg.draw.circle(tela, cor, (x, y), r)

    def velocidade_colisao(massa1, velocidade1, massa2, velocidade2):
        Qmvi = massa1 * velocidade1 + massa2 * velocidade2
        Eci = (massa1 * velocidade1 ** 2)/2 + (massa2 * velocidade2 ** 2)/2
        
        velocidade1Final, velocidade2Final = sym.symbols('velocidade1Final,velocidade2Final')
        eq2 = sym.Eq(massa1 * velocidade1Final + massa2 * velocidade2Final, Qmvi)
        eq1 = sym.Eq(massa1 * velocidade1Final ** 2 + massa2 * velocidade2Final ** 2, (2 * Eci))

        resultado = sym.solve([eq1,eq2],(velocidade1Final, velocidade2Final))
        print(resultado)
        return int(resultado[0][0])

    def distancia_squared(x1, y1, x2, y2):
        distancia_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distancia_squared
    
    def inclinacao(x1, y1, x2, y2):
        if x1 - x2 == 0:
            return math.pi/2
        else:
            inclinacao = math.atan((y1 - y2)/(x1 - x2))
            return inclinacao

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