import sys
import pygame as pg

from random import randint
from jogadores import*
from configs import Configs
from bloco import*
from minion import Minion
from placar import placar

class CenaPrincipal:
    def __init__(self, tela):
        self.frameRate = pg.time.Clock()
        self.tempoCorrido = 0
        self.tela = tela
        self.rodando = True
        self.tempoImunidade = 1000
        #CAPTURAR SUPERFÍCIE DA TELA
        self.superficie_tela = pg.display.get_surface()
       
        #GRUPOS DE SPRITES
        self.sprites_visiveis = pg.sprite.Group()
        self.sprites_obstaculos = pg.sprite.Group()
        self.sprites_minions = pg.sprite.Group()
        
        #Mapa com posição dos sprites
        self.interacoes = Interacoes()
        self.criar_mapa()

    def criar_mapa(self):
        for indice_linha,linha in enumerate(Configs.MAPA_FASE1):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna*Configs.BLOCOS_TAMANHO
                y = indice_linha*Configs.BLOCOS_TAMANHO
                if coluna == "4":
                    Bloco((x,y),[self.sprites_visiveis,self.sprites_obstaculos])
                if coluna == " ":
                    Grama((x,y),[self.sprites_visiveis])
                if coluna == "1":
                    Configs.spawnX_1 = x
                    Configs.spawnY_1 = y
                    Grama((x,y),[self.sprites_visiveis])
                    self.jogador1 = Jogador([Configs.spawnX_1,Configs.spawnY_1,],"cavaleiro",[],self.sprites_obstaculos,self.sprites_minions)
                if coluna == "2":
                    Configs.spawnX_2 = x
                    Configs.spawnY_2 = y
                    Grama((x,y),[self.sprites_visiveis])
                    self.jogador2 = Jogador([Configs.spawnX_2,Configs.spawnY_2,],'arqueiro',[],self.sprites_obstaculos,self.sprites_minions)

    def rodar(self):
        while self.rodando:
            self.gerarMinions()
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            self.frameRate.tick(Configs.FRAME_RATE)
            # print(self.jogador1.animacao_atual)

    def tratamento_eventos(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Jogador 1
        if self.jogador1.livre:
            if pg.key.get_pressed()[pg.K_c]:
                self.jogador1.ataqueBasico()

        if pg.key.get_pressed()[pg.K_a]:
            self.jogador1.vetorUnitario[0] = -1
            self.jogador1.direcao[0] = -1
        elif pg.key.get_pressed()[pg.K_d]:
            self.jogador1.vetorUnitario[0] = 1
            self.jogador1.direcao[0] = 1
        else:
            self.jogador1.vetorUnitario[0] = 0
    
        if pg.key.get_pressed()[pg.K_w]:
            self.jogador1.vetorUnitario[1] = -1
            self.jogador1.direcao[1] = -1
        elif pg.key.get_pressed()[pg.K_s]:
            self.jogador1.vetorUnitario[1] = 1
            self.jogador1.direcao[1] = 1
        else:
            self.jogador1.vetorUnitario[1] = 0

        # Jogador 2
        if self.jogador2.livre:
            if pg.key.get_pressed()[pg.K_PERIOD]:
                self.jogador2.ataqueBasico()
        
        if pg.key.get_pressed()[pg.K_j]:
            self.jogador2.vetorUnitario[0] = -1
            self.jogador2.direcao[0] = -1
        elif pg.key.get_pressed()[pg.K_l]:
            self.jogador2.vetorUnitario[0] = 1
            self.jogador2.direcao[0] = 1
        else:
            self.jogador2.vetorUnitario[0] = 0
     
        if pg.key.get_pressed()[pg.K_i]:
            self.jogador2.vetorUnitario[1] = -1
            self.jogador2.direcao[1] = -1
        elif pg.key.get_pressed()[pg.K_k]:
            self.jogador2.vetorUnitario[1] = 1
            self.jogador2.direcao[1] = 1
        else:
            self.jogador2.vetorUnitario[1] = 0

    def atualiza_estado(self):
        self.jogador1.mover()
        self.jogador1.posicao = self.jogador1.moverParteSolida(self.jogador1.posicao)
        self.jogador2.mover()
        self.jogador2.posicao = self.jogador2.moverParteSolida(self.jogador2.posicao)
        self.jogador1.posicao, self.jogador2.posicao = self.interacoes.atualiza_posicao(self.jogador1.posicao, 
                                                                                        self.jogador2.posicao, 
                                                                                        self.jogador1.velocidade, 
                                                                                        self.jogador2.velocidade, 
                                                                                        self.jogador1.massa, 
                                                                                        self.jogador2.massa)
        for minion in self.sprites_minions:
            minion.movimento(self.jogador1.posicao,self.jogador2.posicao)

    def desenha(self):
        self.tela.fill(Configs.BRANCO)
        self.sprites_visiveis.draw(self.superficie_tela)
        self.sprites_visiveis.update()
        self.sprites_minions.draw(self.superficie_tela)
        self.sprites_minions.update()
    
        if self.jogador1.posicao[1] < self.jogador2.posicao[1]:
            self.jogador1.desenha(self.tela, pg.time.get_ticks())
            self.jogador2.desenha(self.tela, pg.time.get_ticks())
            # pg.draw.rect(self.tela,Configs.BRANCO,self.jogador1.rect)
            # pg.draw.rect(self.tela,Configs.BRANCO,self.jogador2.rect)

        elif self.jogador1.posicao[1] >= self.jogador2.posicao[1]:
            self.jogador2.desenha(self.tela, pg.time.get_ticks())
            self.jogador1.desenha(self.tela, pg.time.get_ticks())
            # pg.draw.rect(self.tela,Configs.BRANCO,self.jogador1.rect)
            # pg.draw.rect(self.tela,Configs.BRANCO,self.jogador2.rect)
        placar(self.jogador1.vida,self.jogador2.vida)
        pg.display.flip()

    def gerarMinions(self):
        if len(self.sprites_minions) < 5 and self.tempoImunidade > 500 :
            Minion((randint(Configs.BLOCOS_TAMANHO,Configs.LARGURA_TELA-Configs.BLOCOS_TAMANHO),
            randint(Configs.BLOCOS_TAMANHO, Configs.ALTURA_TELA-Configs.BLOCOS_TAMANHO)), [self.sprites_minions], self.sprites_obstaculos)
            self.tempoImunidade = 0
        self.tempoImunidade += 1