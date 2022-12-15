import pygame as pg
import sys
from configs import*

class cenaSelecaoPersonagem:
    def __init__(self,tela)->None:
        self.frameRate = pg.time.Clock()
        self.tela = tela
        self.superficie_tela = pg.display.get_surface()
        self.painel = pg.image.load('sprites/selecaoPersonagens.png')
        self.fonte = pg.font.SysFont('arialblack',25)
        self.fonteHistoria = pg.font.SysFont('arialblack',20)
        self.retanguloJ1 = pg.rect.Rect(100, 120, 200, 200)
        self.retanguloJ2 = pg.rect.Rect(Configs.LARGURA_TELA / 2 + 100, 120, 200, 200)
        self.rodando = True
        self.listaPersonagens = ['arqueiro','ladino','cavaleiro', 'mago']
        self.selecionadoJ1 = 'arqueiro'
        self.selecionadoJ2 = 'arqueiro'
        self.i1 = 0
        self.i2 = 0
        self.sprites = []
        self.tempoMarcado = 0
        self.selecaoConcluida = [False, False]
        self.tempo = 0
        self.frame_atual = 0
        self.tempo_anterior = 0
        self.marcador1 = Configs.AZUL
        self.marcador2 = Configs.AZUL
        
        self.sprite_sheet_arqueiro = pg.image.load("sprites/arqueiro.png").convert_alpha()
        self.sprites_arqueiro = []
        
        self.sprite_sheet_cavaleiro = pg.image.load("sprites/cavaleiro.png").convert_alpha()
        self.sprites_cavaleiro = []
       
        self.sprite_sheet_ladino = pg.image.load("sprites/ladino.png").convert_alpha()
        self.sprites_ladino = []

        self.sprite_sheet_mago = pg.image.load("sprites/mago.png").convert_alpha()
        self.sprites_mago = []

        # sprites arqueiro, cavaleiro e ladino
        contadorFrames = 1
        for _ in range(8):
            self.sprites_arqueiro.append(self.sprite_selecionado(self.sprite_sheet_arqueiro, contadorFrames, Configs.dimensoes_sprite['arqueiro']))
            self.sprites_cavaleiro.append(self.sprite_selecionado(self.sprite_sheet_cavaleiro, contadorFrames, Configs.dimensoes_sprite['cavaleiro']))
            self.sprites_ladino.append(self.sprite_selecionado(self.sprite_sheet_ladino, contadorFrames, Configs.dimensoes_sprite['ladino']))
            self.sprites_mago.append(self.sprite_selecionado(self.sprite_sheet_mago, contadorFrames, Configs.dimensoes_sprite['mago']))
            contadorFrames += 1

    def sprite_selecionado(self, sheet, frame:int, dimensoes):
        imagem = pg.Surface(dimensoes).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem = pg.transform.scale(imagem, (dimensoes[0] * 3, dimensoes[1] * 3))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

    def desenharPainel(self)->None:
        self.tela.fill(Configs.BRANCO)
        self.tela.blit(self.painel,(0,0))
        self.exibirPersonagens()

        pg.display.flip()

    def exibirPersonagens(self)->None:
        infoJ2 = 'Classe: ' + str(self.selecionadoJ2)
        superficie_tela = pg.display.get_surface()

        superficie_dadosJ1 = []
        superficie_dadosJ2 = []

        superficie_dadosJ1.append(self.fonte.render('Classe: ' + str(self.selecionadoJ1),True,Configs.CINZA))
        superficie_dadosJ1.append(self.fonte.render('Velocidade: '+  str(Configs.velocidade_personagem[self.selecionadoJ1]),True,Configs.CINZA))
        superficie_dadosJ1.append(self.fonte.render('vitalidade: '+ str(Configs.vitalidade[self.selecionadoJ1]),True,Configs.CINZA))
        historiaJ1 = (self.fonteHistoria.render(str(Configs.historia[self.selecionadoJ1][0]),True,Configs.CINZA_ESCURO),
        self.fonteHistoria.render(str(Configs.historia[self.selecionadoJ1][1]),True,Configs.CINZA_ESCURO))

        superficie_dadosJ2.append(self.fonte.render('Classe: ' + str(self.selecionadoJ2),True,Configs.CINZA))
        superficie_dadosJ2.append(self.fonte.render('Velocidade: '+  str(Configs.velocidade_personagem[self.selecionadoJ2]),True,Configs.CINZA))
        superficie_dadosJ2.append(self.fonte.render('vitalidade: '+ str(Configs.vitalidade[self.selecionadoJ2]),True,Configs.CINZA))
        historiaJ2 = (self.fonteHistoria.render(str(Configs.historia[self.selecionadoJ2][0]),True,Configs.CINZA_ESCURO),
        self.fonteHistoria.render(str(Configs.historia[self.selecionadoJ2][1]),True,Configs.CINZA_ESCURO))
        
        i = 0
        for dados in superficie_dadosJ1:
            superficie_tela.blit(dados, dados.get_rect(topleft = (330, 120 + i * 40)))
            i += 1

        i = 0
        for dados in superficie_dadosJ2:
            superficie_tela.blit(dados, dados.get_rect(topleft = (980, 120 + i * 40)))
            i += 1

        superficie_tela.blit(historiaJ1[0],(130,450))
        superficie_tela.blit(historiaJ2[0],(780,450))
        superficie_tela.blit(historiaJ1[1],(130,470))
        superficie_tela.blit(historiaJ2[1],(780,470))

        self.dicionario = {'arqueiro': self.sprites_arqueiro[self.frame_atual], 'cavaleiro':self.sprites_cavaleiro[self.frame_atual],
        'ladino':self.sprites_ladino[self.frame_atual], 'mago':self.sprites_mago[self.frame_atual]}

        self.posicao_rect = [self.retanguloJ1.centerx- Configs.subracao_rect[self.selecionadoJ1][0] * 3, 
                             self.retanguloJ1.centery - Configs.subracao_rect[self.selecionadoJ1][1] * 3 + 40]

        self.superficie_tela.blit(self.dicionario[self.selecionadoJ1], self.posicao_rect)
        if pg.time.get_ticks() - self.tempo_anterior >= Configs.DURACAO_FRAME:
            self.frame_atual += 1

            if self.frame_atual == len(self.sprites_arqueiro):
                self.frame_atual = 0
            self.tempo_anterior = pg.time.get_ticks()

        self.posicao_rect = [self.retanguloJ2.centerx - Configs.subracao_rect[self.selecionadoJ2][0] * 3, 
                             self.retanguloJ2.centery - Configs.subracao_rect[self.selecionadoJ2][1] * 3 + 40]

        self.superficie_tela.blit(self.dicionario[self.selecionadoJ2], self.posicao_rect)
        if pg.time.get_ticks() - self.tempo_anterior >= Configs.DURACAO_FRAME:
            self.frame_atual += 1

            if self.frame_atual == len(self.sprites_arqueiro):
                self.frame_atual = 0
            self.tempo_anterior = pg.time.get_ticks()

    def escolherPersonagem(self)->None:
        eventos = pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                #Jogador 1
                if self.selecaoConcluida[0] == False:
                    if evento.key == pg.K_a:
                        self.i1 += 1
                    if evento.key == pg.K_d:
                        self.i1 -= 1
                    if evento.key == pg.K_c:
                        self.selecaoConcluida[0] = True
                        self.marcador1 = Configs.VERMELHO

                #Jogador 2
                if self.selecaoConcluida[1] == False:
                    if evento.key == pg.K_j:
                        self.i2 += 1
                    if evento.key == pg.K_l:
                        self.i2 -= 1
                    if evento.key == pg.K_PERIOD:
                        self.selecaoConcluida[1] = True
                        self.marcador2 = Configs.VERMELHO

        if self.i1 > 3:
            self.i1 = 0
        elif self.i1 < 0:
            self.i1 = 3
        if self.i2> 3:
            self.i2 = 0
        elif self.i2 < 0:
            self.i2 = 3
      
        self.selecionadoJ1 = self.listaPersonagens[self.i1]
        self.selecionadoJ2 = self.listaPersonagens[self.i2]

    def rodar(self)->None:
        while(self.selecaoConcluida != [True, True]):
            self.desenharPainel()
            self.escolherPersonagem()
            self.frameRate.tick(Configs.FRAME_RATE)
            self.tempo = pg.time.get_ticks()