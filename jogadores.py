import pygame as pg
import math
from configs import Configs
from funcoes import Funcoes

class Jogadores(pg.sprite.Sprite):
    def __init__(self,posicao,classe,grupos,sprites_obstaculos):
        super().__init__(grupos)
        self.raio = Configs.raio_personagem
        self.escala = Configs.ESCALA
        self.classe = classe
        self.posicao = posicao
        self.massa = Configs.massa_personagem[self.classe]
        self.largura, self.altura = Configs.dimensoes_personagem[self.classe]
        self.vetorUnitario = [0, 0]
        self.animacao_atual = 3
        self.frame_atual = 0
        self.tempo_anterior = pg.time.get_ticks()
        self.sprites = [] #[[E], [D], [C], [B], [CE], [CD], [BE], [BD]]
        self.image = pg.image.load(f"sprites/{self.classe}.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.sprites_obstaculos = sprites_obstaculos

        self.funcoes = Funcoes()

        #Forma uma lista de listas do tipo [movimento sendo executado][frame do movimento]
        contadorFrames = 0
        for i in range(len(Configs.frames_por_animacao1)):
            lista_temporaria = []
            for _ in range(Configs.frames_por_animacao1[i]):
                lista_temporaria.append(self.sprite_selecionado(self.image, contadorFrames, Configs.ESCALA))
                contadorFrames += 1
            self.sprites.append(lista_temporaria)
        contadorFrames = 0


    def sprite_selecionado(self,sheet, frame, escala):
        self.imagem = pg.Surface((self.largura, self.altura)).convert_alpha()
        self.imagem.blit(sheet, (0, 0), (frame * self.largura, 0, self.largura, self.altura))
        self.imagem = pg.transform.scale(self.imagem, (self.largura * escala, self.altura * escala))
        self.imagem.set_colorkey((0, 0, 0, 0))
        return self.imagem

    def mover(self):
        if self.vetorUnitario[0] == self.vetorUnitario[1] == 0:
            self.velocidade = [0,0]
            self.andando = False
            self.frame_atual = 0
        else:
            Vmodulo = Configs.velocidade_personagem[self.classe]  
            angulo = self.funcoes.inclinacaoSinCos(self.vetorUnitario[1], self.vetorUnitario[0])
            self.velocidade = [int(Vmodulo * math.cos(angulo)), int(Vmodulo * math.sin(angulo))]
            self.animacao_atual = Configs.seleciona_animacoes[self.vetorUnitario[0], self.vetorUnitario[1]]
            self.andando = True
            
    def desenha(self, tela, tempoAtual):
        self.posicao_rect = [self.posicao[0] - 16 * self.escala, self.posicao[1] - 24 * self.escala]
        tela.blit(self.sprites[self.animacao_atual][self.frame_atual], self.posicao_rect)
        if tempoAtual - self.tempo_anterior >= Configs.DURACAO_FRAME and self.andando:
            self.frame_atual += 1
            if self.frame_atual == len(self.sprites[self.animacao_atual]):
                self.frame_atual = 0
            self.tempo_anterior = tempoAtual
   

        # cor1 = Configs.cor_personagem[self.classe_Jogador1]
        # r1 = self.raio
        # pg.draw.circle(tela, cor1, self.posicao, r1)

        # cor2 = Configs.cor_personagem[self.classe_Jogador2]
        # r2 = self.raio
        # pg.draw.circle(tela, cor2, self.posicao2, r2)
        
class Jogador1(Jogadores):
    def __init__(self, posicao, classe, grupos, sprites_obstaculos):
        super().__init__(posicao, classe, grupos, sprites_obstaculos)
        
class Jogador2(Jogadores):
    def __init__(self, posicao, classe, grupos, sprites_obstaculos):
        super().__init__(posicao, classe, grupos, sprites_obstaculos)

class Interacoes():
    def __init__(self):
        self.funcoes = Funcoes()
        self.funcoes.velocidade_colisao(1, 1, 1, 1)
        self.Vadicional1 = [0, 0]
        self.Vadicional2 = [0, 0]

    def atualiza_posicao(self, posicao1, posicao2, velocidade1, velocidade2, massa1, massa2):      
        
        self.X1, self.Y1 = posicao1
        self.X2, self.Y2 = posicao2

        V1x, V1y = velocidade1
        V2x, V2y = velocidade2

        V1x_adicional, V1y_adicional = self.Vadicional1
        V2x_adicional, V2y_adicional = self.Vadicional2
        
        r = Configs.raio_personagem

        m1 = massa1
        m2 = massa2

        # Desaceleração
        if V1x_adicional != 0:
            self.Vadicional1[0] -= Configs.desaceleracao * self.funcoes.sinal(V1x_adicional)
        if V1y_adicional != 0:
            self.Vadicional1[1] -= Configs.desaceleracao * self.funcoes.sinal(V1y_adicional)
        if V2x_adicional != 0:
            self.Vadicional2[0] -= Configs.desaceleracao * self.funcoes.sinal(V2x_adicional)
        if V2y_adicional != 0:
            self.Vadicional2[1] -= Configs.desaceleracao * self.funcoes.sinal(V2y_adicional)

        novaVelocidade1 = [V1x + V1x_adicional, V1y + V1y_adicional]
        novaVelocidade2 = [V2x + V2x_adicional, V2y + V2y_adicional]

        novo_X1 = self.X1 + novaVelocidade1[0]
        novo_Y1 = self.Y1 + novaVelocidade1[1]
        novo_X2 = self.X2 + novaVelocidade2[0]
        novo_Y2 = self.Y2 + novaVelocidade2[1]
        distancia_squared = self.funcoes.distancia_squared(novo_X1, novo_Y1, novo_X2, novo_Y2)
       
        #Não-colisão
        if distancia_squared >= (2 * r) ** 2:
            return [novo_X1, novo_Y1], [novo_X2, novo_Y2]

        #Colisão
        else:
            moduloVelocidade1 = ((V1x ** 2) + (V1y ** 2)) ** 0.5
            moduloVelocidade2 = ((V2x ** 2) + (V2y ** 2)) ** 0.5

            solucao = self.funcoes.velocidade_colisao(m1, int(moduloVelocidade1), m2, int(moduloVelocidade2))
            angulo1 = math.pi + math.atan2(self.Y1 - self.Y2, self.X1 - self.X2)
            angulo2 = math.pi + math.atan2(self.Y2 - self.Y1, self.X2 - self.X1)

            self.Vadicional1[0] += int(abs(solucao[0] - moduloVelocidade1) * math.cos(angulo1)) 
            self.Vadicional1[1] += int(abs(solucao[0] - moduloVelocidade1) * math.sin(angulo1))
            self.Vadicional2[0] += int(abs(solucao[1] - moduloVelocidade2) * math.cos(angulo2)) 
            self.Vadicional2[1] += int(abs(solucao[1] - moduloVelocidade2) * math.sin(angulo2))
            
            return [self.X1, self.Y1], [self.X2, self.Y2]
