import sys
import pygame as pg

from personagens import Personagem1
from configs import Configs

class CenaPrincipal:
    def __init__(self, tela):
        self.tela = tela

        spawnX_1 = Configs.LARGURA_TELA // 2 - Configs.LARGURA_PERSONAGEM
        spawnY_1 = Configs.ALTURA_TELA // 2 - Configs.ALTURA_PERSONAGEM
        
        self.personagem1 = Personagem1(posicao = (spawnX_1, spawnY_1))

        self.rodando = True

    def rodar(self):
        while self.rodando:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()

    def tratamento_eventos(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Personagem 1
        if pg.key.get_pressed()[pg.K_w]:
            self.personagem1.mover_para_cima()
            print("W")
        elif pg.key.get_pressed()[pg.K_s]:
            self.personagem1.mover_para_baixo()
            print("S")
        else:
            self.personagem1.pararY()
        if pg.key.get_pressed()[pg.K_a]:
            self.personagem1.mover_para_esquerda()
            print("A")
        elif pg.key.get_pressed()[pg.K_d]:
            self.personagem1.mover_para_direita()
            print("D")
        else:
            self.personagem1.pararX()

    def atualiza_estado(self):
        self.personagem1.atualizar_posicao()

    def desenha(self):
        self.tela.fill((255, 255, 255))
        self.personagem1.desenha(self.tela)
        pg.display.flip()