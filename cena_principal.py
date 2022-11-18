import sys
import pygame as pg

from jogadores_minions import Jogadores
from configs import Configs

class CenaPrincipal:
    def __init__(self, tela):
        self.frameRate = pg.time.Clock()
        self.tempoCorrido = 0
        self.jogadores = Jogadores("warrior", "archer")
        self.tela = tela
        self.rodando = True

    def rodar(self):
        while self.rodando:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            self.frameRate.tick(Configs.FrameRate)

    def tratamento_eventos(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Jogador 1
        if pg.key.get_pressed()[pg.K_a]:
            self.jogadores.moverX1(Configs.angulo["esquerda"])
        elif pg.key.get_pressed()[pg.K_d]:
            self.jogadores.moverX1(Configs.angulo["direita"])
        else:
            self.jogadores.pararX1()
        if pg.key.get_pressed()[pg.K_w]:
            self.jogadores.moverY1(Configs.angulo["cima"])
        elif pg.key.get_pressed()[pg.K_s]:
            self.jogadores.moverY1(Configs.angulo["baixo"])
        else:
            self.jogadores.pararY1()

        # Jogador 2
        if pg.key.get_pressed()[pg.K_j]:
            self.jogadores.moverX2(Configs.angulo["esquerda"])
        elif pg.key.get_pressed()[pg.K_l]:
            self.jogadores.moverX2(Configs.angulo["direita"])
        else:
            self.jogadores.pararX2()
        if pg.key.get_pressed()[pg.K_i]:
            self.jogadores.moverY2(Configs.angulo["cima"])
        elif pg.key.get_pressed()[pg.K_k]:
            self.jogadores.moverY2(Configs.angulo["baixo"])
        else:
            self.jogadores.pararY2()

    def atualiza_estado(self):
        self.jogadores.atualiza_posicao()
        # self.jogadores.tempoCorrido(self.frameRate.tick(Configs.FrameRate))

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.jogadores.desenha(self.tela)
        pg.display.flip()