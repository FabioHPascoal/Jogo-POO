import sympy as sym
import math

class Funcoes:
    def __init__(self) -> None:
        pass
 
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
        if valor > 0:
            return 1
        elif valor < 0:
            return -1
        else:
            return 0
