import pygame as pg
from configs import Configs

pg.init()

fonte = pg.font.Font(None,30)

def debug(info, y = 10, x = 10):
    superficie_tela = pg.display.get_surface()
    superficie_debug = fonte.render(str(info),True,'White')
    retangulo_debug = superficie_debug.get_rect(topleft = (x,y))
    pg.draw.rect(superficie_tela,Configs.PRETO,retangulo_debug)
    superficie_tela.blit(superficie_debug,retangulo_debug)