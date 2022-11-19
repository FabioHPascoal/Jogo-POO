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

        Jogadores.velocidade_colisao(1, 1, 1, 1)

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
        
        V1x, V1y = self.velocidade1
        V2x, V2y = self.velocidade2

        V1x_adicional, V1y_adicional = self.V1_adicional
        V2x_adicional, V2y_adicional = self.V2_adicional
        
        r1 = self.raio1
        r2 = self.raio2

        m1 = self.massa1
        m2 = self.massa2

        #Desaceleração
        if abs(V1x_adicional) > 0:
            self.V1_adicional[0] = int(V1x_adicional * 0.4)
        if abs(V1y_adicional) > 0:
            self.V1_adicional[1] = int(V1y_adicional * 0.4)
        if abs(V2x_adicional) > 0:
            self.V2_adicional[0] = int(V2x_adicional * 0.4)
        if abs(V2y_adicional) > 0:
            self.V2_adicional[1] = int(V2y_adicional * 0.4)

        novaVelocidade1 = [V1x + V1x_adicional, V1y + V1y_adicional]
        novaVelocidade2 = [V2x + V2x_adicional, V2y + V2y_adicional]

        novo_X1 = X1 + novaVelocidade1[0]
        novo_Y1 = Y1 + novaVelocidade1[1]
        novo_X2 = X2 + novaVelocidade2[0]
        novo_Y2 = Y2 + novaVelocidade2[1]

        distancia_squared = Jogadores.distancia_squared(novo_X1, novo_Y1, novo_X2, novo_Y2)
       
        #Não-colisão
        if distancia_squared >= (r1 + r2) ** 2:
            self.posicao1 = (novo_X1, novo_Y1)
            self.posicao2 = (novo_X2, novo_Y2)

        #Colisão
        elif distancia_squared < ((r1 + r2) ** 2):
            print("colidiu")
            
            inclinacao = int(Jogadores.inclinacao(X1, Y1, X2, Y2))

            solucaoX = Jogadores.velocidade_colisao(m1, novaVelocidade1[0], m2, novaVelocidade2[0])
            solucaoY = Jogadores.velocidade_colisao(m1, novaVelocidade1[1], m2, novaVelocidade2[1])

            self.V1_adicional = [int(solucaoX[0] - novaVelocidade1[0]), int(solucaoY[0] - novaVelocidade1[1])]
            self.V2_adicional = [int(solucaoX[1] - novaVelocidade2[0]), int(solucaoY[1] - novaVelocidade2[1])]

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
        EciX2 = massa1 * velocidade1 ** 2 + massa2 * velocidade2 ** 2
        
        velocidade1Final, velocidade2Final = sym.symbols('velocidade1Final,velocidade2Final')
        eq2 = sym.Eq(massa1 * velocidade1Final + massa2 * velocidade2Final, Qmvi)
        eq1 = sym.Eq(massa1 * velocidade1Final ** 2 + massa2 * velocidade2Final ** 2, EciX2)

        resultado = sym.solve([eq1,eq2],(velocidade1Final, velocidade2Final))

        if len(resultado) == 1:
            solucao = resultado[0]
        elif velocidade1 == resultado[0][0]:
            solucao = resultado[1]
        else:
            solucao = resultado[0]
            
        return solucao

    def distancia_squared(X1, Y1, X2, Y2):
        distancia_squared = (X1 - X2) ** 2 + (Y1 - Y2) ** 2
        return distancia_squared
    
    def inclinacao(X1, Y1, X2, Y2):
        if X1 - X2 == 0:
            return math.pi/2
        else:
            inclinacao = math.atan((Y1 - Y2)/(X1 - X2))
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