import pygame as pg
from cena_principal import CenaPrincipal
from cena_selecao_personagem import cenaSelecaoPersonagem
from configs import Configs

class JogoPOO:
    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode((Configs.LARGURA_TELA, Configs.ALTURA_TELA))
        pg.display.set_caption('JOGO')
  
    def rodar(self):
        while True:
            escolher_personagem = cenaSelecaoPersonagem(self.tela)
            escolher_personagem.rodar()
            cena_principal = CenaPrincipal(self.tela,escolher_personagem.selecionadoJ1,escolher_personagem.selecionadoJ2,escolher_personagem.tempo)
            cena_principal.rodar()
