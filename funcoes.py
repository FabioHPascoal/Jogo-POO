import sympy as sym
import pygame as pg
import math

class Funcoes:
    def __init__(self) -> None:
        pass

    def sprite_selecionado(self, sheet, frame, escala, dimensoes):
        imagem = pg.Surface((dimensoes[0], dimensoes[1])).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem = pg.transform.scale(imagem, (dimensoes[0] * escala, dimensoes[1] * escala))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem
 
    def velocidade_colisao(self, massa1, velocidade1, massa2, velocidade2):
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

    def velocidadeColisao(self, posicao1, posicao2, velocidade1, velocidade2, massa1, massa2):
        Vadicional1 = [0, 0]
        Vadicional2 = [0, 0]

        X1, Y1 = posicao1
        X2, Y2 = posicao2

        V1x, V1y = velocidade1
        V2x, V2y = velocidade2

        angulo1 = self.inclinacaoPontos(X2, Y2, X1, Y1) + math.pi
        angulo2 = self.inclinacaoPontos(X1, Y1, X2, Y2) + math.pi

        moduloVelocidade1 = ((V1x ** 2) + (V1y ** 2)) ** 0.5
        moduloVelocidade2 = ((V2x ** 2) + (V2y ** 2)) ** 0.5

        solucao = self.velocidade_colisao(massa1, int(moduloVelocidade1), massa2, int(moduloVelocidade2))

        Vadicional1[0] = int(abs(solucao[0] - moduloVelocidade1) * math.cos(angulo1)) 
        Vadicional1[1] = int(abs(solucao[0] - moduloVelocidade1) * math.sin(angulo1))
        Vadicional2[0] = int(abs(solucao[1] - moduloVelocidade2) * math.cos(angulo2)) 
        Vadicional2[1] = int(abs(solucao[1] - moduloVelocidade2) * math.sin(angulo2))
            
        return [Vadicional1, Vadicional2]

    def distancia_squared(self, X1, Y1, X2, Y2):
        distancia_squared = (X1 - X2) ** 2 + (Y1 - Y2) ** 2
        return distancia_squared

    def inclinacaoPontos(self, X1, Y1, X2, Y2):
        inclinacao = math.atan2(Y1 - Y2, X1 - X2)
        return inclinacao

    def inclinacaoSinCos(self, sin, cos):
        inclinacao = math.atan2(sin, cos)
        return inclinacao

    def sinal(self, valor):
        if valor > 0.1:
            return 1
        elif valor < -0.1:
            return -1
        else:
            return 0

    # def sinal(self, valor):
    #     if valor > 0:
    #         return 1
    #     elif valor < 0:
    #         return -1
    #     else:
    #         return 0
