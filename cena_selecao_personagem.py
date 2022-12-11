import pygame as pg
import sys
from configs import*

class cenaSelecaoPersonagem:
    def __init__(self,tela):
        self.frameRate = pg.time.Clock()
        #CAPTURAR SUPERFÍCIE DA TELA
        self.tela = tela
        self.superficie_tela = pg.display.get_surface()
        self.fonte = pg.font.Font(None,40)
        self.retanguloJ1 = pg.rect.Rect(30,30,200,200)
        self.retanguloJ2 = pg.rect.Rect(Configs.LARGURA_TELA/2+30,30,200,200)
        self.rodando = True
        self.listaPersonagens = ['arqueiro','ladino','cavaleiro']
        self.selecionadoJ1 = 'arqueiro'
        self.selecionadoJ2 = 'arqueiro'
        self.i1 = 0
        self.i2 = 0
        self.sprites = []
        self.tempoMarcado = 0
        self.selecaoConcluida = [False,False]
        self.tempo = 0
        self.sprite_sheet_arqueiro = pg.image.load("sprites/arqueiro.png").convert_alpha()
        self.sprites_arqueiro = []
        self.sprite_sheet_cavaleiro = pg.image.load("sprites/cavaleiro.png").convert_alpha()
        self.sprites_cavaleiro = []
        self.sprite_sheet_ladino = pg.image.load("sprites/ladino.png").convert_alpha()
        self.sprites_ladino = []
        self.frame_atual = 3
        self.tempo_anterior = 0

        # sprites arqueiro
        contadorFrames = 0
        for _ in range(9):
            self.sprites_arqueiro.append(self.sprite_selecionado(self.sprite_sheet_arqueiro, contadorFrames, Configs.dimensoes_sprite['arqueiro']))
            contadorFrames += 1

        # sprites cavaleiro
        contadorFrames = 0
        for _ in range(9):
            self.sprites_cavaleiro.append(self.sprite_selecionado(self.sprite_sheet_cavaleiro, contadorFrames,Configs.dimensoes_sprite['cavaleiro']))
            contadorFrames += 1

        # sprites ladino
        contadorFrames = 0
        for _ in range(9):
            self.sprites_ladino.append(self.sprite_selecionado(self.sprite_sheet_ladino, contadorFrames,Configs.dimensoes_sprite['ladino']))
            contadorFrames += 1

    def sprite_selecionado(self, sheet, frame,dimensoes):
        imagem = pg.Surface(dimensoes).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem = pg.transform.scale(imagem, (dimensoes[0] * 3, dimensoes[1] * 3))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

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

        self.dicionario = {'arqueiro': self.sprites_arqueiro[self.frame_atual],'cavaleiro':self.sprites_cavaleiro[self.frame_atual],
        'ladino':self.sprites_ladino[self.frame_atual]}

        self.posicao_rect = [self.retanguloJ1.centerx- Configs.subracao_rect[self.selecionadoJ1][0] * 3, 
                             self.retanguloJ1.centery - Configs.subracao_rect[self.selecionadoJ1][1] * 3 + 40]

        self.superficie_tela.blit(self.dicionario[self.selecionadoJ1], self.posicao_rect)
        if pg.time.get_ticks() - self.tempo_anterior >= Configs.DURACAO_FRAME:
            self.frame_atual += 1

            if self.frame_atual == len(self.sprites_arqueiro):
                self.frame_atual = 0
            self.tempo_anterior = pg.time.get_ticks()

        self.posicao_rect = [self.retanguloJ2.centerx- Configs.subracao_rect[self.selecionadoJ2][0] * 3, 
                             self.retanguloJ2.centery - Configs.subracao_rect[self.selecionadoJ2][1] * 3 + 40]

        self.superficie_tela.blit(self.dicionario[self.selecionadoJ2], self.posicao_rect)
        if pg.time.get_ticks() - self.tempo_anterior >= Configs.DURACAO_FRAME:
            self.frame_atual += 1

            if self.frame_atual == len(self.sprites_arqueiro):
                self.frame_atual = 0
            self.tempo_anterior = pg.time.get_ticks()

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