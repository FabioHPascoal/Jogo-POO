import pygame as pg
from configs import Configs

class Jogador:
    def __init__(self, classe_jogador, posicao):
        self.posicao = posicao
        self.velocidade = [0, 0]
        self.classe_jogador = classe_jogador
    
    def mover_para_cima(self):
        self.velocidade[1] = -Configs.velocidade_personagem[self.classe_jogador]

    def mover_para_baixo(self):
        self.velocidade[1] = Configs.velocidade_personagem[self.classe_jogador]
    
    def mover_para_esquerda(self):
        self.velocidade[0] = -Configs.velocidade_personagem[self.classe_jogador]
   
    def mover_para_direita(self):
        self.velocidade[0] = Configs.velocidade_personagem[self.classe_jogador]

    def pararX(self):
        self.velocidade[0] = 0

    def pararY(self):
        self.velocidade[1] = 0

    def atualizar_posicao(self):
        x, y = self.posicao
        novo_x = x + self.velocidade[0]
        novo_y = y + self.velocidade[1]
        l = Configs.dimensoes_personagem[self.classe_jogador][0]
        a = Configs.dimensoes_personagem[self.classe_jogador][1]

        if (novo_x >= 0) and ((novo_x + l) <= Configs.LARGURA_TELA):
            self.posicao = (novo_x, y)
            x = novo_x

        if (novo_y >= 0) and ((novo_y + a) <= Configs.ALTURA_TELA):
            self.posicao = (x, novo_y)
            y = novo_y

    def desenha(self, tela):
        cor = Configs.cor_personagem[self.classe_jogador]
        x = self.posicao[0]
        y = self.posicao[1]
        l = Configs.dimensoes_personagem[self.classe_jogador][0]
        a = Configs.dimensoes_personagem[self.classe_jogador][1]
        pg.draw.rect(tela, cor, pg.rect.Rect(x, y, l, a))