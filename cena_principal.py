import sys
import pygame as pg
import numpy
from jogadores import*
from bloco import*
from configs import Configs
from funcoes import Funcoes
from HUD import HUD
from random import randint
from cronometro import Cronometro
from habilidades import*

class CenaPrincipal:
    def __init__(self, tela,classe1,classe2,tempoGastoSelecaoPersonagem):
        self.tempoGastoSelecaoPersonagem = tempoGastoSelecaoPersonagem
        self.funcoes = Funcoes()
        self.frameRate = pg.time.Clock()
        self.escala = Configs.ESCALA
        self.tela = tela
        self.rodando = True
        self.classe1 = classe1
        self.classe2 = classe2
        self.minion = "goblin"
        self.lista_minions = []
        self.lista_objetos = []
        self.lista_PosicaoY = []
        self.tempoEntreSpawn = 0
        self.cronometro = Cronometro()
        self.funcoes.velocidade_colisao(1, 1, 1, 1)
        self.hud = HUD(Configs.vitalidade[self.classe1], Configs.vitalidade[self.classe2])
        # Captura a superfície da tela
        self.superficie_tela = pg.display.get_surface()

        # Grupos de sprites
        self.sprites_visiveis = pg.sprite.Group()
        self.sprites_obstaculos = pg.sprite.Group()
        self.sprites_chamas = pg.sprite.Group()
        self.sprites_minions = pg.sprite.Group()
      
        self.sprite_jogador1 = pg.sprite.GroupSingle()
        self.ataques_basicos1 = pg.sprite.Group()
     
        self.sprite_jogador2 = pg.sprite.GroupSingle()
        self.ataques_basicos2 = pg.sprite.Group()

        # Formação das listas que contêm os sprites dos projéteis
       
        # Arqueiro - Flecha:
        self.flecha_sprites = []
        self.flecha_original = pg.image.load("sprites/flecha.png").convert_alpha()
        for i in range(4):
            self.flecha_sprites.append(self.funcoes.sprite_selecionado(self.flecha_original, i, self.escala, (32, 32)))

        # Cavaleiro - Espadada:
        self.espadada_sprites = []
        self.espadada_original = pg.image.load("sprites/espadada.png").convert_alpha()
        for i in range(4):
            self.espadada_sprites.append(self.funcoes.sprite_selecionado(self.espadada_original, i, self.escala, (151, 110)))

        # Mago - Fireball:
        self.fireball_sprites = []
        self.fireball_original = pg.image.load("sprites/fireball.png").convert_alpha()
        for i in range(4):
            self.fireball_sprites.append(self.funcoes.sprite_selecionado(self.fireball_original, i, self.escala, (32, 32)))
   
        # Mago - Fire_floor
        self.fire_floor = pg.image.load("sprites/fire_floor.png").convert_alpha()

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

                if coluna == "5":
                    Grama((x, y), [self.sprites_visiveis])
                    Caixa((x, y), [self.sprites_visiveis, self.sprites_obstaculos])

                if coluna == "6":
                    Grama((x, y), [self.sprites_visiveis])
                    Chamas((x, y), [self.sprites_visiveis,self.sprites_chamas])
             
                if coluna == " ":
                    Grama((x, y), [self.sprites_visiveis])
             
                if coluna == "1":
                    Grama((x, y), [self.sprites_visiveis])
                    self.jogador1 = Jogadores((x, y), self.classe1)
                    self.lista_objetos.append(self.jogador1)

                if coluna == "2":
                    Grama((x, y), [self.sprites_visiveis])
                    self.jogador2 = Jogadores((x, y), self.classe2)
                    self.lista_objetos.append(self.jogador2)

    def rodar(self):
        while self.rodando:
            self.gera_minions()
            self.tratamento_eventos()
            self.cria_ataques()
            self.atualiza_estado()
            self.desenha()
            self.frameRate.tick(Configs.FRAME_RATE)

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

        #Verificar fim de jogo
        if self.jogador1.verificarMorte() or self.jogador2.verificarMorte():
            self.rodando = False
        if self.cronometro.cronometrado <= 0:
            self.rodando = False

        self.sprites_visiveis
        self.ataques_basicos1.update()
        self.ataques_basicos2.update()
      
        self.jogador1.atualizaVelocidade()
        self.jogador2.atualizaVelocidade()
      
        self.jogador1.moverX()
        self.jogador2.moverX()
      
        # Jogador 1 colidiu com obstáculo em X
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador1.rect.centerx = self.jogador1.posicaoBackup[0]

        # Jogador 2 colidiu com obstáculo em X
        if pg.sprite.spritecollide(self.sprite_jogador2.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador2.rect.centerx = self.jogador2.posicaoBackup[0]

        self.jogador1.moverY()
        self.jogador2.moverY()
      
        # Jogador 1 colidiu com obstáculo em Y
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador1.rect.centery = self.jogador1.posicaoBackup[1]

        # Jogador 2 colidiu com obstáculo em Y
        if pg.sprite.spritecollide(self.sprite_jogador2.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador2.rect.centery = self.jogador2.posicaoBackup[1]

        P1 = self.jogador1.posicaoBackup
        P2 = self.jogador2.posicaoBackup

        V1 = self.jogador1.velocidade
        V2 = self.jogador2.velocidade

        M1 = self.jogador1.massa
        M2 = self.jogador2.massa

        #Jogadores colidiram
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprite_jogador2, False, pg.sprite.collide_mask):
            velocidades_adicionais = self.funcoes.velocidadeColisao(P1, P2, V1, V2, M1, M2)
            self.jogador1.Vadicional[0] += velocidades_adicionais[0][0]
            self.jogador1.Vadicional[1] += velocidades_adicionais[0][1]
            self.jogador2.Vadicional[0] += velocidades_adicionais[1][0]
            self.jogador2.Vadicional[1] += velocidades_adicionais[1][1]
         
            self.jogador1.rect.center = self.jogador1.posicaoBackup
            self.jogador2.rect.center = self.jogador2.posicaoBackup
      
        # Loop de movimentação e colisão dos minions
        for i in range(len(self.lista_minions)):
            Pminion = self.lista_minions[i].rect.center
            Vminion = self.lista_minions[i].velocidade
            Mminion = self.lista_minions[i].massa
            
            distancia1 = self.funcoes.distancia_squared(P1[0], P1[1], Pminion[0], Pminion[1])
            distancia2 = self.funcoes.distancia_squared(P2[0], P2[1], Pminion[0], Pminion[1])

            inclinacao1 = self.funcoes.inclinacaoPontos(P1[0], P1[1], Pminion[0], Pminion[1])
            inclinacao2 = self.funcoes.inclinacaoPontos(P2[0], P2[1], Pminion[0], Pminion[1])

            if distancia1 <= distancia2:
                self.lista_minions[i].vetorUnitario = [self.funcoes.sinal(math.cos(inclinacao1)), self.funcoes.sinal(math.sin(inclinacao1))]

            elif distancia1 > distancia2:
                self.lista_minions[i].vetorUnitario = [self.funcoes.sinal(math.cos(inclinacao2)), self.funcoes.sinal(math.sin(inclinacao2))]

            # Colisão dos minions com o jogador 1
            if pg.sprite.collide_mask(self.sprite_jogador1.sprite, self.lista_minions[i]):
                if pg.time.get_ticks() - self.jogador1.tempoDoUltimoDano > self.jogador1.tempoDeImunidade:
                    self.jogador1.vida -= 1
                    self.jogador1.tempoDoUltimoDano = pg.time.get_ticks()

                velocidades_adicionais = self.funcoes.velocidadeColisao(P1, Pminion, V1, Vminion, M1, Mminion)
                
                self.jogador1.Vadicional[0] += velocidades_adicionais[0][0]
                self.jogador1.Vadicional[1] += velocidades_adicionais[0][1]
                self.lista_minions[i].Vadicional[0] += velocidades_adicionais[1][0]
                self.lista_minions[i].Vadicional[1] += velocidades_adicionais[1][1]
            
                self.jogador1.rect.center = self.jogador1.posicaoBackup
                self.lista_minions[i].rect.center = self.lista_minions[i].posicaoBackup

            # Colisão dos minions com o jogador 2
            if pg.sprite.collide_mask(self.sprite_jogador2.sprite, self.lista_minions[i]):
                if pg.time.get_ticks() - self.jogador2.tempoDoUltimoDano > self.jogador2.tempoDeImunidade:
                    self.jogador2.vida -= 1
                    self.jogador2.tempoDoUltimoDano = pg.time.get_ticks()

                velocidades_adicionais = self.funcoes.velocidadeColisao(P2, Pminion, V2, Vminion, M2, Mminion)
                self.jogador2.Vadicional[0] += velocidades_adicionais[0][0]
                self.jogador2.Vadicional[1] += velocidades_adicionais[0][1]
                self.lista_minions[i].Vadicional[0] += velocidades_adicionais[1][0]
                self.lista_minions[i].Vadicional[1] += velocidades_adicionais[1][1]
            
                self.jogador2.rect.center = self.jogador2.posicaoBackup
                self.lista_minions[i].rect.center = self.lista_minions[i].posicaoBackup

            self.lista_minions[i].atualizaVelocidade()

            # Colisão entre os minions
            for j in range(i + 1, len(self.lista_minions)):
                if pg.sprite.collide_mask(self.lista_minions[i], self.lista_minions[j]):
                    self.lista_minions[i].rect.center = self.lista_minions[i].posicaoBackup
                    self.lista_minions[j].rect.center = self.lista_minions[j].posicaoBackup

            # Colisão dos minions com obstáculos
            self.lista_minions[i].moverX()
            self.lista_minions[i].moverY()
            if pg.sprite.spritecollide(self.lista_minions[i], self.sprites_obstaculos, True, pg.sprite.collide_mask):
                self.lista_minions[i].rect.center = self.lista_minions[i].posicaoBackup

        # Colisão dos ataques
        
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.ataques_basicos2, True, pg.sprite.collide_mask):
            self.jogador1.vida -= 1

        if pg.sprite.spritecollide(self.sprite_jogador2.sprite, self.ataques_basicos1, True, pg.sprite.collide_mask):
            self.jogador2.vida -= 1  

        # Colisão J1 com chamas
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_chamas, True, pg.sprite.collide_mask):
            self.jogador1.vida -= 1

        # Colisão J2 com chamas
        if pg.sprite.spritecollide(self.sprite_jogador2.sprite, self.sprites_chamas, True, pg.sprite.collide_mask):
            self.jogador2.vida -= 1

    def desenha(self):
        self.sprites_visiveis.draw(self.superficie_tela)
        self.ataques_basicos1.draw(self.superficie_tela)
        self.ataques_basicos2.draw(self.superficie_tela)

        # Adiciona as coordenadas Y de todos os objetos em uma lista
        for objeto in self.lista_objetos:
            self.lista_PosicaoY.append(objeto.rect.centery)

        lista_PosicaoY_numpy = numpy.array(self.lista_PosicaoY)
        
        # Gera uma lista com o índice dos objetos na ordem em que devem ser desenhados na tela
        lista_indice_sorted = numpy.argsort(lista_PosicaoY_numpy)

        for indice in lista_indice_sorted:
            self.lista_objetos[indice].desenha(self.tela, pg.time.get_ticks())

        self.lista_PosicaoY.clear()
        self.hud.exibirHUD(self.jogador1.vida,self.jogador2.vida,self.cronometro.tempoPassado(pg.time.get_ticks() - self.tempoGastoSelecaoPersonagem))

        pg.display.flip()

    def gera_minions(self):
        if len(self.sprites_minions) < 0 and pg.time.get_ticks() - self.tempoEntreSpawn > 5000 :
            minion = Jogadores((randint(Configs.BLOCOS_TAMANHO,Configs.LARGURA_TELA-Configs.BLOCOS_TAMANHO),
            randint(Configs.BLOCOS_TAMANHO, Configs.ALTURA_TELA-Configs.BLOCOS_TAMANHO)), "goblin")
            self.lista_minions.append(minion)
            self.lista_objetos.append(minion)
            self.sprites_minions.add(minion)
            self.tempoEntreSpawn = pg.time.get_ticks()

    def cria_ataques(self):

        if self.jogador1.atacando and self.jogador1.frame_atual in Configs.frames_de_ataque[self.classe1]:   
            direcao = self.jogador1.direcaoInicial
         
            if self.classe1 == "cavaleiro":
                ataque = Espadada(self.jogador1.rect.center, direcao, self.espadada_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe1 == "arqueiro":
                ataque = Flecha(self.jogador1.rect.center, direcao, self.flecha_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe1 == "ladino":
                pass
            if self.classe1 == "mago":
                ataque = Fireball(self.jogador1.rect.center, direcao, self.fireball_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            
            self.ataques_basicos1.add(ataque)
            self.jogador1.atacando = False

        if self.jogador2.atacando and self.jogador2.frame_atual in Configs.frames_de_ataque[self.classe2]:
            direcao = self.jogador2.direcaoInicial
         
            if self.classe2 == "cavaleiro":
                ataque = Espadada(self.jogador2.rect.center, direcao, self.espadada_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe2 == "arqueiro":
                ataque = Flecha(self.jogador2.rect.center, direcao, self.flecha_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe2 == "ladino":
                pass
            if self.classe2 == "mago":
                ataque = Fireball(self.jogador2.rect.center, direcao, self.fireball_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
       
            self.ataques_basicos2.add(ataque)

            self.jogador2.atacando = False