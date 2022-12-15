import pygame as pg
import sys
from configs import*

class cenaVitoria:
    def __init__(self,tela,vencedor:str)->None:
        self.rodando = True
        self.tela = tela
        self.vencedor1 = pg.image.load("sprites/vitoriaJ1.png")
        self.vencedor2 = pg.image.load("sprites/vitoriaJ2.png")
        self.vencedor = vencedor

    def desenharPainel(self)->None:
        self.tela.fill(Configs.BRANCO)
        if self.vencedor == "jogador1":
            self.tela.blit(self.vencedor1,(0,0))
        else:
            self.tela.blit(self.vencedor2,(0,0))
        pg.display.flip()

    def novaPartida(self)->None:
        eventos = pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_r:
                    self.rodando = False

    def rodar(self)->None:
        while(self.rodando):
            self.desenharPainel()
            self.novaPartida()