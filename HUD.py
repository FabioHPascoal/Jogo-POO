import pygame as pg
from configs import Configs

pg.init()

fonte = pg.font.Font(None,40)

def HUD(info1,info2,cronometro, y = 20, x = Configs.LARGURA_TELA/2):
    info = str(info1)+'         '+ str(cronometro) +'          '+str(info2)
    superficie_tela = pg.display.get_surface()
    superficie_HUD = fonte.render(str(info),True,'White')
    retangulo = superficie_HUD.get_rect(center = (x,y))
    superficie_tela.blit(superficie_HUD,retangulo)