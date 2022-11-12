import sys
import pygame as pg

from jogadores_minions import Jogador
from configs import Configs

class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela

        self.jogador1 = Jogador("warrior", posicao = (Configs.spawnX_1, Configs.spawnY_1))
        self.jogador2 = Jogador("archer", posicao = (Configs.spawnX_2, Configs.spawnY_2))
        
        self.rodando = True

    def rodar(self):
        framesPorSegundo = pg.time.Clock()
        while self.rodando:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            framesPorSegundo.tick(Configs.FPS)

    def tratamento_eventos(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Jogador 1
        if pg.key.get_pressed()[pg.K_a]:
            self.jogador1.moverX(Configs.angulo["esquerda"])
        elif pg.key.get_pressed()[pg.K_d]:
            self.jogador1.moverX(Configs.angulo["direita"])
        else:
            self.jogador1.pararX()
        if pg.key.get_pressed()[pg.K_w]:
            self.jogador1.moverY(Configs.angulo["cima"])
        elif pg.key.get_pressed()[pg.K_s]:
            self.jogador1.moverY(Configs.angulo["baixo"])
        else:
            self.jogador1.pararY()

        # Jogador 2
        if pg.key.get_pressed()[pg.K_j]:
            self.jogador2.moverX(Configs.angulo["esquerda"])
        elif pg.key.get_pressed()[pg.K_l]:
            self.jogador2.moverX(Configs.angulo["direita"])
        else:
            self.jogador2.pararX()
        if pg.key.get_pressed()[pg.K_i]:
            self.jogador2.moverY(Configs.angulo["cima"])
        elif pg.key.get_pressed()[pg.K_k]:
            self.jogador2.moverY(Configs.angulo["baixo"])
        else:
            self.jogador2.pararY()

    def atualiza_estado(self):
        self.jogador1.atualizar_posicao()
        self.jogador2.atualizar_posicao()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.jogador1.desenha(self.tela)
        self.jogador2.desenha(self.tela)
        pg.display.flip()

    def colisao_jogadores(self):
        pass