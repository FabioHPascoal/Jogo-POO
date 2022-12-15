import pygame as pg
from configs import Configs

pg.init()

fonte = pg.font.Font(None,40)

class HUD:
    def __init__(self, vitalidadeJ1, vitalidadeJ2):
        self.superficie_tela = pg.display.get_surface()
        self.vitalidadeJ1 = vitalidadeJ1
        self.vitalidadeJ2 = vitalidadeJ2

        self.coracoesJ1 = []
        self.coracoesJ2 = []

        for vidas in range(self.vitalidadeJ1):
            self.coracoesJ1.append(Coracoes((30 + 64 * vidas, 30)))

        for vidas in range(self.vitalidadeJ2):
            self.coracoesJ2.append(Coracoes((936 + 64 * vidas, 30)))

    def exibirHUD(self, vidasJ1, vidasJ2,cronometro, y = 20, x = Configs.LARGURA_TELA/2):
        self.superficie_cronometro = fonte.render(str(cronometro), True,'White')
        self.retangulo_cronometro = self.superficie_cronometro.get_rect(center = (x,y))
        self.superficie_tela.blit(self.superficie_cronometro, self.retangulo_cronometro)

        self.atualizarCoracoes(vidasJ1,vidasJ2)

        for vidas in self.coracoesJ1:
            self.superficie_tela.blit(vidas.image, vidas.rect)
        for vidas in self.coracoesJ2:
            self.superficie_tela.blit(vidas.image, vidas.rect)

    def atualizarCoracoes(self, vidasJ1, vidasJ2):
        if self.vitalidadeJ1 < vidasJ1:
            self.coracoesJ1.append(Coracoes((30 + 64 * (vidasJ1-1), 30)))
            self.vitalidadeJ1 += 1
        elif self.vitalidadeJ1 > vidasJ1 and len(self.coracoesJ1) > 0:
            self.coracoesJ1.pop()
            self.vitalidadeJ1 -= 1

        if self.vitalidadeJ2 < vidasJ2:
            self.coracoesJ2.append(Coracoes((936 + 64 * (vidasJ2-1), 30)))
            self.vitalidadeJ2 += 1
        elif self.vitalidadeJ2 > vidasJ2 and len(self.coracoesJ2) > 0:
            self.coracoesJ2.pop()
            self.vitalidadeJ2 -= 1

class Coracoes:
    def __init__(self, posicao):
        self.image = pg.image.load("sprites/coracao.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)