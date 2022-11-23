import pygame as pg
import sympy as sym
import math
from configs import Configs

class Jogadores:
    def __init__(self, classe_Jogador1, classe_Jogador2):
        self.classe_Jogador1 = classe_Jogador1
        self.raio1 = Configs.raio_personagem[self.classe_Jogador1]
        self.massa1 = Configs.massa_personagem[self.classe_Jogador1]
        self.vetorUnitario1 = [0, 0]
        self.velocidade1 = [0, 0]
        self.V1_adicional = [0, 0]
        self.posicao1 = (Configs.spawnX_1, Configs.spawnY_1)

        self.classe_Jogador2 = classe_Jogador2
        self.raio2 = Configs.raio_personagem[self.classe_Jogador2]
        self.massa2 = Configs.massa_personagem[self.classe_Jogador2]
        self.vetorUnitario2 = [0, 0]
        self.velocidade2 = [0, 0]
        self.V2_adicional = [0, 0]
        self.posicao2 = (Configs.spawnX_2, Configs.spawnY_2)

        Jogadores.velocidade_colisao(1, 1, 1, 1)

    def mover1(self):
        if self.vetorUnitario1[0] == self.vetorUnitario1[1] == 0:
            self.velocidade1 = [0,0]
        else:
            Vmodulo = Configs.velocidade_personagem[self.classe_Jogador1]  
            angulo = Jogadores.inclinacaoSinCos(self.vetorUnitario1[1], self.vetorUnitario1[0])
            self.velocidade1 = [int(Vmodulo * math.cos(angulo)), int(Vmodulo * math.sin(angulo))]
                
    def mover2(self):
        if self.vetorUnitario2[0] == self.vetorUnitario2[1] == 0:
            self.velocidade2 = [0,0]
        else:
            Vmodulo = Configs.velocidade_personagem[self.classe_Jogador1]  
            angulo = Jogadores.inclinacaoSinCos(self.vetorUnitario2[1], self.vetorUnitario2[0])
            self.velocidade2 = [int(Vmodulo * math.cos(angulo)), int(Vmodulo * math.sin(angulo))]

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
            self.V1_adicional[0] = int(V1x_adicional * Configs.desaceleracao)
        if abs(V1y_adicional) > 0:
            self.V1_adicional[1] = int(V1y_adicional * Configs.desaceleracao)
        if abs(V2x_adicional) > 0:
            self.V2_adicional[0] = int(V2x_adicional * Configs.desaceleracao)
        if abs(V2y_adicional) > 0:
            self.V2_adicional[1] = int(V2y_adicional * Configs.desaceleracao)

        novaVelocidade1 = [V1x + V1x_adicional, V1y + V1y_adicional]
        novaVelocidade2 = [V2x + V2x_adicional, V2y + V2y_adicional]

        novo_X1 = X1 + novaVelocidade1[0]
        novo_Y1 = Y1 + novaVelocidade1[1]
        novo_X2 = X2 + novaVelocidade2[0]
        novo_Y2 = Y2 + novaVelocidade2[1]

        distancia_squared = Jogadores.distancia_squared(novo_X1, novo_Y1, novo_X2, novo_Y2)
        angulo1 = Jogadores.inclinacaoPontos(X2, Y2, X1, Y1) + math.pi
        angulo2 = Jogadores.inclinacaoPontos(X1, Y1, X2, Y2) + math.pi
       
        #Não-colisão
        if distancia_squared >= (r1 + r2) ** 2:
            self.posicao1 = (novo_X1, novo_Y1)
            self.posicao2 = (novo_X2, novo_Y2)

        #Colisão
        elif distancia_squared < (r1 + r2) ** 2:
            moduloVelocidade1 = ((novaVelocidade1[0] ** 2) + (novaVelocidade1[1] ** 2)) ** 0.5
            moduloVelocidade2 = ((novaVelocidade2[0] ** 2) + (novaVelocidade2[1] ** 2)) ** 0.5

            solucao = Jogadores.velocidade_colisao(m1, int(moduloVelocidade1), m2, int(moduloVelocidade2))

            self.V1_adicional[0] = int(abs(solucao[0] - moduloVelocidade1) * math.cos(angulo1)) 
            self.V1_adicional[1] = int(abs(solucao[0] - moduloVelocidade1) * math.sin(angulo1))
            self.V2_adicional[0] = int(abs(solucao[1] - moduloVelocidade2) * math.cos(angulo2)) 
            self.V2_adicional[1] = int(abs(solucao[1] - moduloVelocidade2) * math.sin(angulo2))

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
    
    def inclinacaoPontos(X1, Y1, X2, Y2):
        inclinacao = math.atan2(Y1 - Y2, X1 - X2)
        return inclinacao

    def inclinacaoSinCos(sin, cos):
        inclinacao = math.atan2(sin, cos)
        return inclinacao

class Minion:
    pass