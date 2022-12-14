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
    def __init__(self, tela, classe1:str, classe2:str, tempoGastoSelecaoPersonagem:int)->None:
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
        self.ultimaAtualizacaoAgua = pg.time.get_ticks()
        self.movimentoAgua = True
        self.funcoes.velocidade_colisao(1, 1, 1, 1)
        self.hud = HUD(Configs.vitalidade[self.classe1], Configs.vitalidade[self.classe2])
        # Captura a superfície da tela
        self.superficie_tela = pg.display.get_surface()

        # Grupos de sprites
        self.sprites_visiveis = pg.sprite.Group()
        self.sprites_obstaculos = pg.sprite.Group()
        self.sprites_objetosQuebraveis = pg.sprite.Group()
        self.sprites_agua = pg.sprite.Group()
        self.sprites_minions = pg.sprite.Group()
        self.sprites_ataques_basicos = pg.sprite.Group()
        self.sprites_coracoes = pg.sprite.Group()
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

        # Ladino- Facada:
        self.facada_sprites = []
        self.facada_original = pg.image.load("sprites/facada.png").convert_alpha()
        for i in range(4):
            self.facada_sprites.append(self.funcoes.sprite_selecionado(self.facada_original, i, self.escala, (39, 32)))

        # Mago - Fireball:
        self.fireball_sprites = []
        self.fireball_original = pg.image.load("sprites/fireball.png").convert_alpha()
        for i in range(4):
            self.fireball_sprites.append(self.funcoes.sprite_selecionado(self.fireball_original, i, self.escala, (32, 32)))
   
        # Mago - Fire_floor
        self.fire_floor = pg.image.load("sprites/fire_floor.png").convert_alpha()
        self.fire_floor = pg.transform.scale(self.fire_floor, (128, 128))

        #Mapa com posição dos sprites
        self.cria_mapa()

        self.sprite_jogador1.add(self.jogador1)
        self.sprite_jogador2.add(self.jogador2)

    def cria_mapa(self)->None:
        for indice_linha, linha in enumerate(Configs.MAPA_FASE1):
            for indice_coluna, coluna in enumerate(linha):
                x = indice_coluna * Configs.BLOCOS_TAMANHO
                y = indice_linha * Configs.BLOCOS_TAMANHO
             
                if coluna == "4":
                    Bloco((x, y), [self.sprites_visiveis, self.sprites_obstaculos])

                if coluna == "5":
                    GramaCentro((x, y), [self.sprites_visiveis])
                    Caixa((x, y), [self.sprites_visiveis, self.sprites_objetosQuebraveis])

                if coluna == "6":
                    Agua((x, y), [self.sprites_visiveis,self.sprites_agua])
             
                if coluna == "7":
                    GramaRioD((x, y), [self.sprites_visiveis])

                if coluna == "8":
                    GramaRioE((x, y), [self.sprites_visiveis])

                if coluna == '9':
                    GramaRioE((x, y), [self.sprites_visiveis])
                    Ponte((x, y), [self.sprites_visiveis],0)
                if coluna == '10':
                    Ponte((x, y), [self.sprites_visiveis],1)
                if coluna == '11':
                    Ponte((x, y), [self.sprites_visiveis],2)
                if coluna == '12':
                    Ponte((x, y), [self.sprites_visiveis],3)
                if coluna == '13':
                    GramaRioD((x, y), [self.sprites_visiveis])
                    Ponte((x, y), [self.sprites_visiveis],4)
                if coluna == '14':
                    GramaRioE((x, y), [self.sprites_visiveis])
                    Ponte((x, y), [self.sprites_visiveis],5)
                if coluna == '15':
                    Ponte((x, y), [self.sprites_visiveis],6)
                if coluna == '16':
                    Ponte((x, y), [self.sprites_visiveis],7)
                if coluna == '17':
                    Ponte((x, y), [self.sprites_visiveis],8)
                if coluna == '18':
                    GramaRioD((x, y), [self.sprites_visiveis])
                    Ponte((x, y), [self.sprites_visiveis],9)

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

    def rodar(self)->None:
        while self.rodando:
            self.gera_minions()
            self.tratamento_eventos()
            self.cria_ataques()
            self.cria_habilidades()
            self.atualiza_estado()
            self.desenha()
            self.frameRate.tick(Configs.FRAME_RATE)

    def tratamento_eventos(self)->None:
        pg.event.get()

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)

        # Jogador 1
        # Ataque básico
        if self.jogador1.livre:
            if pg.key.get_pressed()[pg.K_c]:
                self.jogador1.ataqueBasico()
            if pg.key.get_pressed()[pg.K_v]:
                self.jogador1.habilidade()

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
            if pg.key.get_pressed()[pg.K_SEMICOLON]:
                self.jogador2.habilidade()

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

    def atualiza_estado(self)->None:
            
        P1 = self.jogador1.posicaoBackup
        P2 = self.jogador2.posicaoBackup

        V1 = self.jogador1.velocidade
        V2 = self.jogador2.velocidade

        M1 = self.jogador1.massa
        M2 = self.jogador2.massa

        #Atualizar frame da agua
        if pg.time.get_ticks() - self.ultimaAtualizacaoAgua > 800:
            contador = 0
            posicaoOndas1 = [0,1,2,6,7,11,12,13]
            posicaoOndas2 = [3,4,5,8,9,10,14,15,16]
            if self.movimentoAgua:
                for agua in self.sprites_agua:
                    if contador in posicaoOndas1:
                        agua.update(1)
                    if contador in posicaoOndas2:
                        agua.update(0)
                    contador += 1
                    if contador == 17:
                        contador = 0
                    self.ultimaAtualizacaoAgua = pg.time.get_ticks()
                    self.movimentoAgua = False
            else:
                for agua in self.sprites_agua:
                    if contador in posicaoOndas1:
                        agua.update(0)
                    if contador in posicaoOndas2:
                        agua.update(1)
                    contador += 1
                    if contador == 17:
                        contador = 0
                    self.ultimaAtualizacaoAgua = pg.time.get_ticks()
                    self.movimentoAgua = True  

        #Verificar fim de jogo e vencedor
        if self.jogador1.verificarMorte() or self.jogador2.verificarMorte():
            if self.jogador1.morte:
                self.vencedor = 'jogador2'
            else:
                self.vencedor = 'jogador1'
            self.rodando = False

        if self.cronometro.cronometrado <= 0:
            if self.jogador1.minionsDerrotados > self.jogador2.minionsDerrotados:
                self.vencedor = 'jogador1'
            else:
                self.vencedor = 'jogador2'
            self.rodando = False

        self.sprites_visiveis
        self.sprites_ataques_basicos.update()
      
        self.jogador1.atualizaVelocidade()
        self.jogador2.atualizaVelocidade()
      
        self.jogador1.moverX()
        self.jogador2.moverX()
      
        # Jogador 1 colidiu com obstáculo em X
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
            self.jogador1.rect.centerx = self.jogador1.posicaoBackup[0]

        # if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
        #     print(self.jogador1.velocidadeTotal[0])
        #     for i in range(1, self.jogador1.velocidadeTotal[0]):
        #         self.jogador1.rect.centerx -= i
        #         if pg.sprite.spritecollide(self.sprite_jogador1.sprite, self.sprites_obstaculos, False, pg.sprite.collide_mask):
        #             self.jogador1.rect.centerx += i
        #             print(i)
        #         else:
        #             break
        #     print("")

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

        # Colisão dos ataques do J1 com o J2
        for ataque in self.ataques_basicos1:
            if pg.sprite.collide_mask(ataque, self.sprite_jogador2.sprite):
                if pg.time.get_ticks() - self.jogador2.tempoDoUltimoDano > self.jogador2.tempoDeImunidade:
                    self.jogador2.vida -= 1
                    self.jogador2.tempoDoUltimoDano = pg.time.get_ticks()
                    if self.classe1 in Configs.ataques_sao_desenhados:
                        ataque.kill()
                if self.classe1 == "cavaleiro":
                    self.jogador2.stunnado = True
                    self.jogador2.inicioStun = pg.time.get_ticks()
                    velocidades_adicionais = self.funcoes.velocidadeColisao(P1, P2, (3, 3), V2, 2, M2)
                    self.jogador2.Vadicional[0] += velocidades_adicionais[1][0]
                    self.jogador2.Vadicional[1] += velocidades_adicionais[1][1]

        # Colisão dos ataques do J2 com o J1
        for ataque in self.ataques_basicos2:
            if pg.sprite.collide_mask(ataque, self.sprite_jogador1.sprite):
                if pg.time.get_ticks() - self.jogador1.tempoDoUltimoDano > self.jogador1.tempoDeImunidade:
                    self.jogador1.vida -= 1
                    self.jogador1.tempoDoUltimoDano = pg.time.get_ticks()
                    if self.classe2 in Configs.ataques_sao_desenhados:
                        ataque.kill()
                    if self.classe2 == "cavaleiro":
                        velocidades_adicionais = self.funcoes.velocidadeColisao(P1, P2, V1, (3, 3), M1, 2)
                        self.jogador1.Vadicional[0] += velocidades_adicionais[0][0]
                        self.jogador1.Vadicional[1] += velocidades_adicionais[0][1]
      
        # Colisão entre os jogadores
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

            if distancia1 <= distancia2:
                if distancia1 > 50:
                    Pnext = CenaPrincipal.calc_pos(self, Pminion, P1)
                    inclinacao1 = self.funcoes.inclinacaoPontos(Pnext[0], Pnext[1], Pminion[0], Pminion[1])
                else:
                    inclinacao1 = self.funcoes.inclinacaoPontos(P1[0], P1[1], Pminion[0], Pminion[1])
                self.lista_minions[i].vetorUnitario = [self.funcoes.sinal(math.cos(inclinacao1)), self.funcoes.sinal(math.sin(inclinacao1))]

            else:
                if distancia2 > 50:
                    Pnext = CenaPrincipal.calc_pos(self, Pminion, P2)
                    inclinacao2 = self.funcoes.inclinacaoPontos(Pnext[0], Pnext[1], Pminion[0], Pminion[1])
                else:
                    inclinacao2 = self.funcoes.inclinacaoPontos(P2[0], P2[1], Pminion[0], Pminion[1])
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

            self.lista_minions[i].moverX()
            self.lista_minions[i].moverY()

        # Colisão dos minions com ataques do J1
        for minion in self.sprites_minions:
            for ataque in self.ataques_basicos1:
                if pg.sprite.collide_mask(minion, ataque):
                    minion.morte = True
                    self.jogador1.minionsDerrotados += 1
                    if ataque.projetil:
                        ataque.kill()

        # Colisão dos minions com ataques do J2
        for minion in self.sprites_minions:
            for ataque in self.ataques_basicos2:
                if pg.sprite.collide_mask(minion, ataque):
                    minion.morte = True
                    self.jogador2.minionsDerrotados += 1
                    if ataque.projetil:
                        ataque.kill()

        for minion in self.lista_minions:
            if minion.morte == True:
                self.lista_minions.remove(minion)

        for minion in self.lista_objetos:
            if minion.morte == True:
                self.lista_objetos.remove(minion)  

        for minion in self.sprites_minions:
            if minion.morte == True:
                minion.kill()

        #Colisão dos ataques com os objetos quebráveis
        for objeto in self.sprites_objetosQuebraveis:
            if pg.sprite.spritecollide(objeto,self.sprites_ataques_basicos,False):
                Coracao((objeto.rect.x,objeto.rect.y), [self.sprites_visiveis,self.sprites_coracoes])
                objeto.kill()

        #Colisão dos ataques com objetos não quebráveis
        for ataque in self.sprites_ataques_basicos:
            if pg.sprite.spritecollide(ataque,self.sprites_obstaculos,False):
                if ataque.projetil:
                    ataque.kill()

        #J1 na agua
        if pg.sprite.spritecollide(self.sprite_jogador1.sprite,self.sprites_agua, False, pg.sprite.collide_mask):
            self.jogador1.naAgua = True
        else:
            self.jogador1.naAgua = False

        #J2 na agua
        if pg.sprite.spritecollide(self.sprite_jogador2.sprite, self.sprites_agua, False, pg.sprite.collide_mask):
            self.jogador2.naAgua = True
        else:
            self.jogador2.naAgua = False

        #Minion na agua
        for minion in self.sprites_minions:
            if pg.sprite.spritecollide(minion, self.sprites_agua, False):
                minion.naAgua = True
            else:
                minion.naAgua = False

        #capturar coração
        for coracao in self.sprites_coracoes:
            if pg.sprite.collide_rect(coracao,self.sprite_jogador1.sprite):
                coracao.kill()
                self.jogador1.vida += 1
            if pg.sprite.collide_rect(coracao,self.sprite_jogador2.sprite):
                coracao.kill()
                self.jogador2.vida += 1

        #verificar stun
        self.jogador1.stun()
        self.jogador2.stun()

    def desenha(self)->None:
        self.sprites_visiveis.draw(self.superficie_tela)

        if self.classe1 in Configs.ataques_sao_desenhados:
            self.ataques_basicos1.draw(self.superficie_tela)

        if self.classe2 in Configs.ataques_sao_desenhados:
            self.ataques_basicos2.draw(self.superficie_tela)

        # Adiciona as coordenadas Y de todos os objetos em uma lista
        for objeto in self.lista_objetos:
            self.lista_PosicaoY.append(objeto.rect.centery)

        lista_PosicaoY_numpy = numpy.array(self.lista_PosicaoY)

        # Gera uma lista com o índice dos objetos na ordem em que devem ser desenhados na tela
        lista_indice_sorted = numpy.argsort(lista_PosicaoY_numpy)

        for indice in lista_indice_sorted:
            self.lista_objetos[indice].desenha(self.tela, pg.time.get_ticks())

        # self.sprite_jogador1.draw(self.superficie_tela)
        # self.sprite_jogador2.draw(self.superficie_tela)

        self.lista_PosicaoY.clear()
        self.hud.exibirHUD(self.jogador1.vida,self.jogador2.vida,self.cronometro.tempoPassado(pg.time.get_ticks() - self.tempoGastoSelecaoPersonagem))

        pg.display.flip()

    def gera_minions(self)->None:
        if len(self.sprites_minions) < 4 and pg.time.get_ticks() - self.tempoEntreSpawn > 5000:
            minion = Jogadores((randint(Configs.BLOCOS_TAMANHO,Configs.LARGURA_TELA-Configs.BLOCOS_TAMANHO),
            randint(Configs.BLOCOS_TAMANHO, Configs.ALTURA_TELA-Configs.BLOCOS_TAMANHO)), "goblin")
            self.lista_minions.append(minion)
            self.lista_objetos.append(minion)
            self.sprites_minions.add(minion)
            self.tempoEntreSpawn = pg.time.get_ticks()

    def cria_ataques(self)->None:

        if self.jogador1.atacando and self.jogador1.frame_atual in Configs.frames_de_ataque[self.classe1]:   
            direcao = self.jogador1.direcaoInicial
         
            if self.classe1 == "cavaleiro":
                ataque = Espadada(self.jogador1.rect.center, direcao, self.espadada_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe1 == "arqueiro":
                ataque = Flecha(self.jogador1.rect.center, direcao, self.flecha_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe1 == "ladino":
                ataque = Facada(self.jogador1.rect.center, direcao, self.facada_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
                self.jogador1.Vadicional[0] += 25 * direcao[0]
                self.jogador1.Vadicional[1] += 25 * direcao[1]
            if self.classe1 == "mago":
                no_fireball = True
                for ataque_mago in self.ataques_basicos1:  
                    if isinstance(ataque_mago, Fireball):
                        fireball = ataque_mago
                        no_fireball = False
                
                if no_fireball:        
                    ataque = Fireball(self.jogador1.rect.center, direcao, self.fireball_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
                
                else:
                    ataque = Fire_floor(ataque_mago.rect.center, self.fire_floor)
                    fireball.kill()
                
            self.ataques_basicos1.add(ataque)
            self.sprites_ataques_basicos.add(ataque)
            self.jogador1.atacando = False

        if self.jogador2.atacando and self.jogador2.frame_atual in Configs.frames_de_ataque[self.classe2]:
            direcao = self.jogador2.direcaoInicial
        
            if self.classe2 == "cavaleiro":
                ataque = Espadada(self.jogador2.rect.center, direcao, self.espadada_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe2 == "arqueiro":
                ataque = Flecha(self.jogador2.rect.center, direcao, self.flecha_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
            if self.classe2 == "ladino":
                ataque = Facada(self.jogador2.rect.center, direcao, self.facada_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
                self.jogador2.Vadicional[0] += 25 * direcao[0]
                self.jogador2.Vadicional[1] += 25 * direcao[1]
            if self.classe2 == "mago":
                no_fireball = True
                for ataque_mago in self.ataques_basicos2:  
                    if isinstance(ataque_mago, Fireball):
                        fireball = ataque_mago
                        no_fireball = False
                
                if no_fireball:        
                    ataque = Fireball(self.jogador2.rect.center, direcao, self.fireball_sprites[Configs.seleciona_frame_ataque[direcao[0], direcao[1]]])
                
                else:
                    ataque = Fire_floor(ataque_mago.rect.center, self.fire_floor)
                    fireball.kill()
       
            self.ataques_basicos2.add(ataque)
            self.sprites_ataques_basicos.add(ataque)
            self.jogador2.atacando = False

    def cria_habilidades(self)->None:  
        if self.jogador1.castando_skill and self.jogador1.frame_atual in Configs.frames_de_habilidade[self.classe1]:
            if self.classe1 == "cavaleiro":
                pass
            if self.classe1 == "arqueiro":
                pass
            if self.classe1 == "ladino":
                pass
            if self.classe1 == "mago":
                if self.jogador1.vida < Configs.vitalidade[self.classe1]:
                    self.jogador1.vida += 1

            self.jogador1.castando_skill = False

        if self.jogador2.castando_skill and self.jogador2.frame_atual in Configs.frames_de_habilidade[self.classe2]:
            if self.classe2 == "cavaleiro":
                pass
            if self.classe2 == "arqueiro":
                pass
            if self.classe2 == "ladino":
                pass
            if self.classe2 == "mago":
                if self.jogador2.vida < Configs.vitalidade[self.classe2]:
                    self.jogador2.vida += 1

            self.jogador2.castando_skill = False

    def calc_pos(self, Pminion, Pplayer):
        pos1 = [math.trunc(Pminion[0]/Configs.BLOCOS_TAMANHO), math.trunc(Pminion[1]/Configs.BLOCOS_TAMANHO)]
        pos2 = [math.trunc(Pplayer[0]/Configs.BLOCOS_TAMANHO), math.trunc(Pplayer[1]/Configs.BLOCOS_TAMANHO)]

        mapa_col = [[0]*Configs.BLOCOS_Y for i in range(Configs.BLOCOS_X)]
        for i in range(Configs.BLOCOS_X):
            for j in range(Configs.BLOCOS_Y):
                if Configs.MAPA_FASE1[j][i] == '4' or Configs.MAPA_FASE1[j][i] == '5':
                    mapa_col[i][j] = -1

        if (mapa_col[pos1[0]][pos1[1]] == -1):
            return (0, 0)
        mapa_pos = CenaPrincipal.goblin_mode(mapa_col, pos2, pos1)

        next_pos = [0, 0]
        if (pos1[0] - 1 > -1):
            if (mapa_pos[pos1[0] - 1][pos1[1]] == mapa_pos[pos1[0]][pos1[1]] - 1):
                next_pos = [(pos1[0] - 1)*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2, (pos1[1])*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2]
        if (pos1[0] + 1 < Configs.BLOCOS_X):
            if (mapa_pos[pos1[0] + 1][pos1[1]] == mapa_pos[pos1[0]][pos1[1]] - 1):
                next_pos = [(pos1[0] + 1)*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2, (pos1[1])*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2]
        if (pos1[1] - 1 > -1):
            if (mapa_pos[pos1[0]][pos1[1] - 1] == mapa_pos[pos1[0]][pos1[1]] - 1):
                next_pos = [(pos1[0])*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2, (pos1[1] - 1)*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2]
        if (pos1[1] + 1 < Configs.BLOCOS_Y):
            if (mapa_pos[pos1[0]][pos1[1] + 1] == mapa_pos[pos1[0]][pos1[1]] - 1):
                next_pos = [(pos1[0])*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2, (pos1[1] + 1)*Configs.BLOCOS_TAMANHO + Configs.BLOCOS_TAMANHO/2]
        
        return next_pos

    def goblin_mode(mapa_pos:int, ponto, pos2)->None:
        cont = 1
        mapa_pos[ponto[0]][ponto[1]] = 1
        frontier = [[ponto[0], ponto[1]]]
        while (len(frontier) > 0 and frontier[0] != pos2):
            ponto = frontier.pop(0)
            cont = mapa_pos[ponto[0]][ponto[1]] + 1

            if (ponto[0] - 1 > -1):
                if (mapa_pos[ponto[0] - 1][ponto[1]] > cont or mapa_pos[ponto[0] - 1][ponto[1]] == 0):
                    ponto[0]-=1
                    mapa_pos[ponto[0]][ponto[1]] = cont
                    frontier.append([ponto[0], ponto[1]])
                    ponto[0]+=1
            if (ponto[0] + 1 < Configs.BLOCOS_X):
                if (mapa_pos[ponto[0] + 1][ponto[1]] > cont or mapa_pos[ponto[0] + 1][ponto[1]] == 0):
                    ponto[0]+=1
                    mapa_pos[ponto[0]][ponto[1]] = cont
                    frontier.append([ponto[0], ponto[1]])
                    ponto[0]-=1
            if (ponto[1] - 1 > -1):
                if (mapa_pos[ponto[0]][ponto[1] - 1] > cont or mapa_pos[ponto[0]][ponto[1] - 1] == 0):
                    ponto[1]-=1
                    mapa_pos[ponto[0]][ponto[1]] = cont
                    frontier.append([ponto[0], ponto[1]])
                    ponto[1]+=1
            if (ponto[1] + 1 < Configs.BLOCOS_Y):
                if (mapa_pos[ponto[0]][ponto[1] + 1] > cont or mapa_pos[ponto[0]][ponto[1] + 1] == 0):
                    ponto[1]+=1
                    mapa_pos[ponto[0]][ponto[1]] = cont
                    frontier.append([ponto[0], ponto[1]])
                    ponto[1]-=1
        return(mapa_pos)