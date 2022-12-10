import sys
import pygame as pg
from jogadores import*
from bloco import*
from configs import Configs
from funcoes import Funcoes
from HUD import HUD
from random import randint
from cronometro import Cronometro

class CenaPrincipal:
    def __init__(self, tela):
        self.funcoes = Funcoes()
        self.frameRate = pg.time.Clock()
        self.tela = tela
        self.rodando = True
        self.classe1 = "cavaleiro"
        self.classe2 = "arqueiro"
        self.minion = "goblin"
        self.lista_minions = []
        self.tempoEntreSpawn = 0
        self.massa1 = Configs.massa_personagem[self.classe1]
        self.massa2 = Configs.massa_personagem[self.classe2]
        self.cronometro = Cronometro()
        self.funcoes.velocidade_colisao(1, 1, 1, 1)
       
        #Captura a superfície da tela
        self.superficie_tela = pg.display.get_surface()

        #Grupos de sprites
        self.sprites_visiveis = pg.sprite.Group()
        self.sprites_obstaculos = pg.sprite.Group()
        self.sprite_jogador1 = pg.sprite.GroupSingle()
        self.sprite_jogador2 = pg.sprite.GroupSingle()
        self.sprites_minions = pg.sprite.Group()

        #Mapa com posição dos sprites
        self.cria_mapa()

        self.sprite_jogador1.add(self.jogador1)
        self.sprite_jogador2.add(self.jogador2)

    def cria_mapa(self):
        for indice_linha, linha in enumerate(Configs.MAPA_FASE1):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna * Configs.BLOCOS_TAMANHO
                y = indice_linha * Configs.BLOCOS_TAMANHO
             
                if coluna == "4":
                    Bloco((x, y), [self.sprites_visiveis, self.sprites_obstaculos])
             
                if coluna == " ":
                    Grama((x, y), [self.sprites_visiveis])
             
                if coluna == "1":
                    Grama((x, y), [self.sprites_visiveis])
                    self.jogador1 = Jogadores((x, y), self.classe1)
            
                if coluna == "2":
                    Grama((x, y), [self.sprites_visiveis])
                    self.jogador2 = Jogadores((x, y), self.classe2)

    def rodar(self):
        while self.rodando:
            self.geraMinions()
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()
            self.frameRate.tick(Configs.FRAME_RATE)
          
            # if len(self.lista_minions) > 0:
            #     print(self.lista_minions[0].animacao_atual)

    def tratamento_eventos(self):
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Jogador 1
        # Ataque básico
        if self.jogador1.livre:
            if pg.key.get_pressed()[pg.K_c]:
                self.jogador1.ataqueBasico()
        
        # Movimento em X
        if pg.key.get_pressed()[pg.K_a]:
            self.jogador1.vetorUnitario[0] = -1
        elif pg.key.get_pressed()[pg.K_d]:
            self.jogador1.vetorUnitario[0] = 1
        else:
            self.jogador1.vetorUnitario[0] = 0
    
        # Movimento em Y
        if pg.key.get_pressed()[pg.K_w]:
            self.jogador1.vetorUnitario[1] = -1
        elif pg.key.get_pressed()[pg.K_s]:
            self.jogador1.vetorUnitario[1] = 1
        else:
            self.jogador1.vetorUnitario[1] = 0

        # Jogador 2  
        # Ataque básico
        if self.jogador2.livre:
            if pg.key.get_pressed()[pg.K_PERIOD]:
                self.jogador2.ataqueBasico()
        
        # Movimento em X
        if pg.key.get_pressed()[pg.K_j]:
            self.jogador2.vetorUnitario[0] = -1
        elif pg.key.get_pressed()[pg.K_l]:
            self.jogador2.vetorUnitario[0] = 1
        else:
            self.jogador2.vetorUnitario[0] = 0
     
        # Movimento em Y
        if pg.key.get_pressed()[pg.K_i]:
            self.jogador2.vetorUnitario[1] = -1
        elif pg.key.get_pressed()[pg.K_k]:
            self.jogador2.vetorUnitario[1] = 1
        else:
            self.jogador2.vetorUnitario[1] = 0

    def atualiza_estado(self):
        self.sprites_visiveis
        self.jogador1.novaPosicao()
        self.jogador2.novaPosicao()

        P1 = self.jogador1.posicaoBackup
        P2 = self.jogador2.posicaoBackup

        V1 = self.jogador1.velocidade
        V2 = self.jogador2.velocidade

        M1 = self.massa1
        M2 = self.massa2
      
        for minion in self.lista_minions:
            Pminion = minion.rect.center
            
            distancia1 = self.funcoes.distancia_squared(P1[0], P1[1], Pminion[0], Pminion[1])
            distancia2 = self.funcoes.distancia_squared(P2[0], P2[1], Pminion[0], Pminion[1])

            inclinacao1 = self.funcoes.inclinacaoPontos(P1[0], P1[1], Pminion[0], Pminion[1])
            inclinacao2 = self.funcoes.inclinacaoPontos(P2[0], P2[1], Pminion[0], Pminion[1])

            if distancia1 <= distancia2:
                minion.vetorUnitario = [self.funcoes.sinal(math.cos(inclinacao1)), self.funcoes.sinal(math.sin(inclinacao1))]

            elif distancia1 > distancia2:
                minion.vetorUnitario = [self.funcoes.sinal(math.cos(inclinacao2)), self.funcoes.sinal(math.sin(inclinacao2))]
                
            minion.novaPosicao()

        #Jogadores colidiram
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprite_jogador2, False, pg.sprite.collide_mask):
            velocidades_adicionais = self.funcoes.velocidadeColisao(P1, P2, V1, V2, M1, M2)
            self.jogador1.Vadicional[0] += velocidades_adicionais[0][0]
            self.jogador1.Vadicional[1] += velocidades_adicionais[0][1]
            self.jogador2.Vadicional[0] += velocidades_adicionais[1][0]
            self.jogador2.Vadicional[1] += velocidades_adicionais[1][1]
         
            self.jogador1.rect.center = self.jogador1.posicaoBackup
            self.jogador2.rect.center = self.jogador2.posicaoBackup

        # Jogador 1 colidiu com obstáculo
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador1.rect.center = self.jogador1.posicaoBackup

        # # Jogador 1 colidiu com obstáculo
        # if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
        #     self.jogador1.rect.center = self.jogador1.posicaoBackup
            
        #     self.jogador1.rect.centerx = self.jogador1.proximaPosicao[0]
        #     if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
        #         self.jogador1.rect.centerx = self.jogador1.posicaoBackup[0]

        #     self.jogador1.rect.centery = self.jogador1.proximaPosicao[1]
        #     if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
        #         self.jogador1.rect.centery = self.jogador1.posicaoBackup[1]

        # Jogador 2 colidiu com obstáculo
        if pg.sprite.spritecollide(self.sprite_jogador2.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador2.rect.center = self.jogador2.posicaoBackup

    def desenha(self):
        self.sprites_visiveis.draw(self.superficie_tela)

        for minion in self.lista_minions:
            minion.desenha(self.tela, pg.time.get_ticks())
    
        if self.jogador1.rect.y < self.jogador2.rect.y:
            self.jogador1.desenha(self.tela, pg.time.get_ticks())
            self.jogador2.desenha(self.tela, pg.time.get_ticks())

        elif self.jogador1.rect.y >= self.jogador2.rect.y:
            self.jogador2.desenha(self.tela, pg.time.get_ticks())
            self.jogador1.desenha(self.tela, pg.time.get_ticks())
       
        # self.sprites_minions.draw(self.superficie_tela)
        # self.sprite_jogador1.draw(self.superficie_tela)
        # self.sprite_jogador2.draw(self.superficie_tela)

        HUD(self.jogador1.vida, self.jogador2.vida, self.cronometro.tempoPassado(pg.time.get_ticks()))

        pg.display.flip()

    def geraMinions(self):
        if len(self.sprites_minions) < 1 and pg.time.get_ticks() - self.tempoEntreSpawn > 10000 :
            minion = Jogadores((randint(Configs.BLOCOS_TAMANHO,Configs.LARGURA_TELA-Configs.BLOCOS_TAMANHO),
            randint(Configs.BLOCOS_TAMANHO, Configs.ALTURA_TELA-Configs.BLOCOS_TAMANHO)), "goblin")
            self.lista_minions.append(minion)
            self.sprites_minions.add(minion)
            self.tempoEntreSpawn = pg.time.get_ticks()