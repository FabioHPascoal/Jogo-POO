import pygame as pg
from configs import Configs

pg.init()

fonte = pg.font.Font(None,30)

def placar(info1,info2, y = 10, x = Configs.LARGURA_TELA/2):
    info = str(info1)+' '+str(info2)
    superficie_tela = pg.display.get_surface()
    superficie_placar = fonte.render(str(info),True,'White')
    retangulo_placar = superficie_placar.get_rect(topleft = (x,y))
    pg.draw.rect(superficie_tela,Configs.PRETO,retangulo_placar)
    superficie_tela.blit(superficie_placar,retangulo_placar)