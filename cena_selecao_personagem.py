import pygame as pg
import sys
from configs import*

class cenaSelecaoPersonagem:
    def __init__(self,tela):
        self.frameRate = pg.time.Clock()
        self.tela = tela
        #CAPTURAR SUPERFÍCIE DA TELA
        self.superficie_tela = pg.display.get_surface()
        self.fonte = pg.font.Font(None,40)
        self.retanguloJ1 = pg.rect.Rect(30,30,200,200)
        self.retanguloJ2 = pg.rect.Rect(Configs.LARGURA_TELA/2+30,30,200,200)
        self.rodando = True
        self.listaPersonagens = ['arqueiro','ladino','cavaleiro']
        self.selecionadoJ1 = 'classe'
        self.selecionadoJ2 = 'classe'
        self.i1 = 0
        self.i2 = 0
        self.sprites = []
        self.tempoMarcado = 0
        self.selecaoConcluida = [False,False]
        self.tempo = 0

    def desenharPainel(self):
        self.tela.fill(Configs.BRANCO)
        pg.draw.rect(self.tela,Configs.AZUL,self.retanguloJ1)
        pg.draw.rect(self.tela,Configs.AZUL,self.retanguloJ2)
        self.exibirPersonagens()
        pg.display.flip()
        
    def exibirPersonagens(self):
        infoJ1 = 'Classe: ' + str(self.selecionadoJ1)
        infoJ2 = 'Classe: ' + str(self.selecionadoJ2)
        superficie_tela = pg.display.get_surface()
        superficie_dadosJ1= self.fonte.render(str(infoJ1),True,Configs.PRETO)
        superficie_dadosJ2= self.fonte.render(str(infoJ2),True,Configs.PRETO)
        retangulo1 = superficie_dadosJ1.get_rect(topleft = (350,30))
        retangulo2 = superficie_dadosJ2.get_rect(topleft = (1000,30))
        superficie_tela.blit(superficie_dadosJ1,retangulo1)
        superficie_tela.blit(superficie_dadosJ2,retangulo2)

    def escolherPersonagem(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        if pg.time.get_ticks() - self.tempoMarcado >= 100:
            self.tempoMarcado = pg.time.get_ticks()

            # Jogador 1
            if pg.key.get_pressed()[pg.K_a]:
                self.i1 += 1
            if pg.key.get_pressed()[pg.K_d]:
                self.i1 -= 1

            if self.i1>2:
                self.i1 = 0
            elif self.i1< 0:
                self.i1 = 2

            self.selecionadoJ1 = self.listaPersonagens[self.i1]

            if pg.key.get_pressed()[pg.K_r]:
                self.selecaoConcluida[0] = True

            # Jogador 2
            if pg.key.get_pressed()[pg.K_l]:
                self.i2 += 1
            elif pg.key.get_pressed()[pg.K_j]:
                self.i2 -= 1

            if self.i2>2:
                self.i2 = 0
            elif self.i2< 0:
                self.i2 = 2

            self.selecionadoJ2 = self.listaPersonagens[self.i2]

            if pg.key.get_pressed()[pg.K_p]:
                self.selecaoConcluida[1] = True       

    def rodar(self):
        while(self.selecaoConcluida != [True,True]):
            self.desenharPainel()
            self.escolherPersonagem()
            self.tempo = pg.time.get_ticks()
            self.frameRate.tick(Configs.FRAME_RATE)