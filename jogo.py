import pygame as pg
from cena_principal import CenaPrincipal
from configs import Configs

class JogoPOO:
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((Configs.LARGURA_TELA, Configs.ALTURA_TELA))

    def rodar(self):
        while True:
            cena_principal = CenaPrincipal(self.tela)
            cena_principal.rodar()