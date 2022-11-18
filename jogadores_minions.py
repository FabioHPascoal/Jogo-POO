import pygame as pg
import sympy as sym
import math
from configs import Configs

class Jogadores:
    def __init__(self, classe_Jogador1, classe_Jogador2):
        self.classe_Jogador1 = classe_Jogador1
        self.raio1 = Configs.raio_personagem[self.classe_Jogador1]
        self.massa1 = Configs.massa_personagem[self.classe_Jogador1]
        self.velocidade1 = [0, 0]
        self.V1_adicional = [0, 0]
        self.posicao1 = (Configs.spawnX_1, Configs.spawnY_1)

        self.classe_Jogador2 = classe_Jogador2
        self.raio2 = Configs.raio_personagem[self.classe_Jogador2]
        self.massa2 = Configs.massa_personagem[self.classe_Jogador2]
        self.velocidade2 = [0, 0]
        self.V2_adicional = [0, 0]
        self.posicao2 = (Configs.spawnX_2, Configs.spawnY_2)

        Jogadores.velocidade_colisao(self.massa1, self.velocidade1[0], self.massa2, self.velocidade2[0])

    def moverX1(self, angulo):
        self.velocidade1[0] = int(Configs.velocidade_personagem[self.classe_Jogador1] * math.cos(angulo))
    def moverY1(self, angulo):
        self.velocidade1[1] = int(Configs.velocidade_personagem[self.classe_Jogador1] * math.sin(angulo)) * -1
    def pararX1(self):
        self.velocidade1[0] = 0
    def pararY1(self):
        self.velocidade1[1] = 0

    def moverX2(self, angulo):
        self.velocidade2[0] = int(Configs.velocidade_personagem[self.classe_Jogador2] * math.cos(angulo))
    def moverY2(self, angulo):
        self.velocidade2[1] = int(Configs.velocidade_personagem[self.classe_Jogador2] * math.sin(angulo)) * -1
    def pararX2(self):
        self.velocidade2[0] = 0
    def pararY2(self):
        self.velocidade2[1] = 0

    def atualiza_posicao(self):      
        
        X1, Y1 = self.posicao1
        X2, Y2 = self.posicao2
        
        r1 = self.raio1
        r2 = self.raio2

        if abs(self.V1_adicional[0]) > 0:
            self.V1_adicional[0] = int(self.V1_adicional[0] * 0.7)
        if abs(self.V1_adicional[1]) > 0:
            self.V1_adicional[1] = int(self.V1_adicional[1] * 0.7)
        if abs(self.V2_adicional[0]) > 0:
            self.V2_adicional[0] = int(self.V2_adicional[0] * 0.7)
        if abs(self.V2_adicional[1]) > 0:
            self.V2_adicional[1] = int(self.V2_adicional[1] * 0.7)
      
        novo_X1 = X1 + self.velocidade1[0] + self.V1_adicional[0]
        novo_Y1 = Y1 + self.velocidade1[1] + self.V1_adicional[1]
        novo_X2 = X2 + self.velocidade2[0] + self.V2_adicional[0]
        novo_Y2 = Y2 + self.velocidade2[1] + self.V2_adicional[1]

        distancia_squared = Jogadores.distancia_squared(novo_X1, novo_Y1, novo_X2, novo_Y2)
       
        if distancia_squared >= (r1 + r2) ** 2:
            self.posicao1 = (novo_X1, novo_Y1)
            self.posicao2 = (novo_X2, novo_Y2)

        elif distancia_squared < ((r1 + r2) ** 2):
            inclinacao = Jogadores.inclinacao(X1, Y1, X2, Y2)

            vX_adicional = Jogadores.velocidade_colisao(self.massa1, self.velocidade1[0], self.massa2, self.velocidade2[0])
            vY_adicional = Jogadores.velocidade_colisao(self.massa1, self.velocidade1[1], self.massa2, self.velocidade2[1])
          
            self.V1_adicional = [int(vX_adicional[0]), int(vY_adicional[0])]
            self.V2_adicional = [int(vX_adicional[1]), int(vY_adicional[1])]

    def desenha(self, tela):
        cor1 = Configs.cor_personagem[self.classe_Jogador1]
        X1, Y1 = self.posicao1
        r1 = Configs.raio_personagem[self.classe_Jogador1]
        pg.draw.circle(tela, cor1, (X1, Y1), r1)

        cor2 = Configs.cor_personagem[self.classe_Jogador2]
        X2, Y2 = self.posicao2
        r2 = Configs.raio_personagem[self.classe_Jogador2]
        pg.draw.circle(tela, cor2, (X2, Y2), r2)

    def tempoCorrido(self, tempoCorrido):
        print(tempoCorrido)

    def velocidade_colisao(massa1, velocidade1, massa2, velocidade2):
        Qmvi = massa1 * velocidade1 + massa2 * velocidade2
        Eci = (massa1 * velocidade1 ** 2)/2 + (massa2 * velocidade2 ** 2)/2
        
        velocidade1Final, velocidade2Final = sym.symbols('velocidade1Final,velocidade2Final')
        eq2 = sym.Eq(massa1 * velocidade1Final + massa2 * velocidade2Final, Qmvi)
        eq1 = sym.Eq(massa1 * velocidade1Final ** 2 + massa2 * velocidade2Final ** 2, (2 * Eci))

        resultado = sym.solve([eq1,eq2],(velocidade1Final, velocidade2Final))

        if len(resultado) == 1:
            solucao_correta = [resultado[0][0] - velocidade1, resultado[0][1] - velocidade2]
        elif abs(velocidade1) == abs(resultado[0][0]):
            solucao_correta = [resultado[1][0] - velocidade1, resultado[1][1] - velocidade2]
        elif abs(velocidade1) == abs(resultado[1][0]):
            solucao_correta = [resultado[0][0] - velocidade1, resultado[0][1] - velocidade2]

        return solucao_correta

    def distancia_squared(x1, y1, x2, y2):
        distancia_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distancia_squared
    
    def inclinacao(x1, y1, x2, y2):
        if x1 - x2 == 0:
            return math.pi/2
        else:
            inclinacao = math.atan((y1 - y2)/(x1 - x2))
            return inclinacao

    def sinal(valor):
        if valor > 0:
            return 1
        elif valor < 0:
            return -1
        else:
            return 0

class Ataques:
    pass

class Minion:
    pass