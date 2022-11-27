import pygame as pg
import sympy as sym
import math
from configs import Configs

class Jogadores:
    def __init__(self, classe_Jogador1, classe_Jogador2):
        self.raio = Configs.raio_personagem
        self.escala = Configs.ESCALA
        Jogadores.velocidade_colisao(1, 1, 1, 1)
      
        #Jogador 1
        self.classe_Jogador1 = classe_Jogador1
        self.posicao1 = (Configs.spawnX_1, Configs.spawnY_1)
        self.massa1 = Configs.massa_personagem[self.classe_Jogador1]
        largura1, altura1 = Configs.dimensoes_personagem[self.classe_Jogador1]
        self.vetorUnitario1 = [0, 0]
        self.V1_adicional = [0, 0]
        
        self.animacao_atual1 = 3
        self.frame_atual1 = 0
        self.tempo_anterior1 = pg.time.get_ticks()
        self.sprites1 = [] #[[E], [D], [C], [B], [CE], [CD], [BE], [BD]]
        sprite_sheet1 = pg.image.load(f"sprites/{self.classe_Jogador1}.png").convert_alpha()

        #Forma uma lista de listas do tipo [movimento sendo executado][frame do movimento]
        contadorFrames = 0
        for i in range(len(Configs.frames_por_animacao1)):
            lista_temporaria = []
            for _ in range(Configs.frames_por_animacao1[i]):
                lista_temporaria.append(Jogadores.sprite_selecionado(sprite_sheet1, contadorFrames, largura1, altura1, self.escala))
                contadorFrames += 1
            self.sprites1.append(lista_temporaria)
        contadorFrames = 0

        #Jogador 2
        self.classe_Jogador2 = classe_Jogador2
        self.massa2 = Configs.massa_personagem[self.classe_Jogador2]
        self.vetorUnitario2 = [0, 0]
        self.V2_adicional = [0, 0]
        self.animacao_atual2 = 3
        self.frame_atual2 = 0
        self.tempo_anterior2 = pg.time.get_ticks()
        self.posicao2 = (Configs.spawnX_2, Configs.spawnY_2)


    def mover1(self):
        if self.vetorUnitario1[0] == self.vetorUnitario1[1] == 0:
            self.velocidade1 = [0,0]
            self.andando1 = False
            self.frame_atual1 = 0

        else:
            Vmodulo = Configs.velocidade_personagem[self.classe_Jogador1]  
            angulo = Jogadores.inclinacaoSinCos(self.vetorUnitario1[1], self.vetorUnitario1[0])
            self.velocidade1 = [int(Vmodulo * math.cos(angulo)), int(Vmodulo * math.sin(angulo))]
            self.animacao_atual1 = Configs.seleciona_animacoes[self.vetorUnitario1[0], self.vetorUnitario1[1]]
            self.andando1 = True
                
    def mover2(self):
        if self.vetorUnitario2[0] == self.vetorUnitario2[1] == 0:
            self.velocidade2 = [0,0]
            self.andando2 = False
            self.frame_atual2 = 0
        else:
            Vmodulo = Configs.velocidade_personagem[self.classe_Jogador1]  
            angulo = Jogadores.inclinacaoSinCos(self.vetorUnitario2[1], self.vetorUnitario2[0])
            self.velocidade2 = [int(Vmodulo * math.cos(angulo)), int(Vmodulo * math.sin(angulo))]
            self.animacao_atual2 = Configs.seleciona_animacoes[self.vetorUnitario2[0], self.vetorUnitario2[1]]
            self.andando2 = True

    def atualiza_posicao(self):      
        
        X1, Y1 = self.posicao1
        X2, Y2 = self.posicao2
        
        V1x, V1y = self.velocidade1
        V2x, V2y = self.velocidade2

        V1x_adicional, V1y_adicional = self.V1_adicional
        V2x_adicional, V2y_adicional = self.V2_adicional
        
        r = self.raio

        m1 = self.massa1
        m2 = self.massa2

        # Desaceleração
        if V1x_adicional != 0:
            self.V1_adicional[0] -= Configs.desaceleracao * Jogadores.sinal(V1x_adicional)
        if V1y_adicional != 0:
            self.V1_adicional[1] -= Configs.desaceleracao * Jogadores.sinal(V1y_adicional)
        if V2x_adicional != 0:
            self.V2_adicional[0] -= Configs.desaceleracao * Jogadores.sinal(V2x_adicional)
        if V2y_adicional != 0:
            self.V2_adicional[1] -= Configs.desaceleracao * Jogadores.sinal(V2y_adicional)

        novaVelocidade1 = [V1x + V1x_adicional, V1y + V1y_adicional]
        novaVelocidade2 = [V2x + V2x_adicional, V2y + V2y_adicional]

        novo_X1 = X1 + novaVelocidade1[0]
        novo_Y1 = Y1 + novaVelocidade1[1]
        novo_X2 = X2 + novaVelocidade2[0]
        novo_Y2 = Y2 + novaVelocidade2[1]

        distancia_squared = Jogadores.distancia_squared(novo_X1, novo_Y1, novo_X2, novo_Y2)
       
        #Não-colisão
        if distancia_squared >= (2 * r) ** 2:
            self.posicao1 = (novo_X1, novo_Y1)
            self.posicao2 = (novo_X2, novo_Y2)

        #Colisão
        elif distancia_squared < (2 * r) ** 2:
            moduloVelocidade1 = ((V1x ** 2) + (V1y ** 2)) ** 0.5
            moduloVelocidade2 = ((V2x ** 2) + (V2y ** 2)) ** 0.5

            solucao = Jogadores.velocidade_colisao(m1, int(moduloVelocidade1), m2, int(moduloVelocidade2))

            angulo1 = Jogadores.inclinacaoPontos(X2, Y2, X1, Y1) + math.pi
            angulo2 = Jogadores.inclinacaoPontos(X1, Y1, X2, Y2) + math.pi

            self.V1_adicional[0] += int(abs(solucao[0] - moduloVelocidade1) * math.cos(angulo1)) 
            self.V1_adicional[1] += int(abs(solucao[0] - moduloVelocidade1) * math.sin(angulo1))
            self.V2_adicional[0] += int(abs(solucao[1] - moduloVelocidade2) * math.cos(angulo2)) 
            self.V2_adicional[1] += int(abs(solucao[1] - moduloVelocidade2) * math.sin(angulo2))
    
    def sprite_selecionado(sheet, frame, largura, altura, escala):
        imagem = pg.Surface((largura, altura)).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * largura, 0, largura, altura))
        imagem = pg.transform.scale(imagem, (largura * escala, altura * escala))
        imagem.set_colorkey((0, 0, 0, 0))

        return imagem
    
    def desenha(self, tela, tempoAtual):
        self.posicao1_rect = [self.posicao1[0] - 16 * self.escala, self.posicao1[1] - 24 * self.escala]
        self.posicao2_rect = [self.posicao2[0] - 16 * self.escala, self.posicao2[1] - 24 * self.escala]
        
        if self.posicao1_rect[1] < self.posicao2_rect[1]:
            tela.blit(self.sprites1[self.animacao_atual1][self.frame_atual1], self.posicao1_rect)
            if tempoAtual - self.tempo_anterior1 >= Configs.DURACAO_FRAME and self.andando1:
                self.frame_atual1 += 1
                if self.frame_atual1 == len(self.sprites1[self.animacao_atual1]):
                    self.frame_atual1 = 0
                self.tempo_anterior1 = tempoAtual
                
            tela.blit(self.sprites1[self.animacao_atual2][self.frame_atual2], self.posicao2_rect)
            if tempoAtual - self.tempo_anterior2 >= Configs.DURACAO_FRAME and self.andando2:
                self.frame_atual2 += 1
                if self.frame_atual2 == len(self.sprites1[self.animacao_atual2]):
                    self.frame_atual2 = 0
                self.tempo_anterior2 = tempoAtual

        else:
            tela.blit(self.sprites1[self.animacao_atual2][self.frame_atual2], self.posicao2_rect)
            if tempoAtual - self.tempo_anterior2 >= Configs.DURACAO_FRAME and self.andando2:
                self.frame_atual2 += 1
                if self.frame_atual2 == len(self.sprites1[self.animacao_atual2]):
                    self.frame_atual2 = 0
                self.tempo_anterior2 = tempoAtual

            tela.blit(self.sprites1[self.animacao_atual1][self.frame_atual1], self.posicao1_rect)
            if tempoAtual - self.tempo_anterior1 >= Configs.DURACAO_FRAME and self.andando1:
                self.frame_atual1 += 1
                if self.frame_atual1 == len(self.sprites1[self.animacao_atual1]):
                    self.frame_atual1 = 0
                self.tempo_anterior1 = tempoAtual     

        # cor1 = Configs.cor_personagem[self.classe_Jogador1]
        # r1 = self.raio
        # pg.draw.circle(tela, cor1, self.posicao1, r1)

        # cor2 = Configs.cor_personagem[self.classe_Jogador2]
        # r2 = self.raio
        # pg.draw.circle(tela, cor2, self.posicao2, r2)
  
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

    def sinal(valor):
        if valor > 0:
            return 1
        elif valor < 0:
            return -1
        else:
            return 0