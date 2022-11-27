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
            self.jogadores.vetorUnitario1[0] = -1
        elif pg.key.get_pressed()[pg.K_d]:
            self.jogadores.vetorUnitario1[0] = 1
        else:
            self.jogadores.vetorUnitario1[0] = 0
        if pg.key.get_pressed()[pg.K_w]:
            self.jogadores.vetorUnitario1[1] = -1
        elif pg.key.get_pressed()[pg.K_s]:
            self.jogadores.vetorUnitario1[1] = 1
        else:
            self.jogadores.vetorUnitario1[1] = 0

        # Jogador 2
        if pg.key.get_pressed()[pg.K_j]:
            self.jogadores.vetorUnitario2[0] = -1
        elif pg.key.get_pressed()[pg.K_l]:
            self.jogadores.vetorUnitario2[0] = 1
        else:
            self.jogadores.vetorUnitario2[0] = 0
        if pg.key.get_pressed()[pg.K_i]:
            self.jogadores.vetorUnitario2[1] = -1
        elif pg.key.get_pressed()[pg.K_k]:
            self.jogadores.vetorUnitario2[1] = 1
        else:
            self.jogadores.vetorUnitario2[1] = 0

    def atualiza_estado(self):
        self.jogadores.mover1()
        self.jogadores.mover2()
        self.jogadores.atualiza_posicao()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.jogadores.desenha(self.tela, pg.time.get_ticks())
        pg.display.flip()