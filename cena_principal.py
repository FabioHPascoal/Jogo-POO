import sys
import pygame as pg

from jogadores import Jogadores
from configs import Configs

class CenaPrincipal:
    def __init__(self, tela):
        self.frameRate = pg.time.Clock()
        self.tempoCorrido = 0
        self.jogadores = Jogadores("saxao", "archer")
        self.tela = tela
        self.rodando = True

    def rodar(self):
        while self.rodando:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            self.frameRate.tick(Configs.FRAME_RATE)
            # print("")

    def tratamento_eventos(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Jogador 1
        if pg.key.get_pressed()[pg.K_a]:
            self.jogadores.direcao1.x = -1
        elif pg.key.get_pressed()[pg.K_d]:
            self.jogadores.direcao1.x = 1
        else:
            self.jogadores.direcao1.x = 0
        if pg.key.get_pressed()[pg.K_w]:
            self.jogadores.direcao1.y = -1
        elif pg.key.get_pressed()[pg.K_s]:
            self.jogadores.direcao1.y = 1
        else:
            self.jogadores.direcao1.y = 0

        # Jogador 2
        if pg.key.get_pressed()[pg.K_j]:
            self.jogadores.direcao2.x = -1
        elif pg.key.get_pressed()[pg.K_l]:
            self.jogadores.direcao2.x = 1
        else:
            self.jogadores.direcao2.x = 0
        if pg.key.get_pressed()[pg.K_i]:
            self.jogadores.direcao2.y = -1
        elif pg.key.get_pressed()[pg.K_k]:
            self.jogadores.direcao2.y = 1
        else:
            self.jogadores.direcao2.y = 0

    def atualiza_estado(self):
        self.jogadores.mover1()
        self.jogadores.mover2()
        self.jogadores.atualiza_posicao()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.jogadores.desenha(self.tela, pg.time.get_ticks())
        pg.display.flip()