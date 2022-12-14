import pygame as pg
import math
from configs import Configs
from funcoes import Funcoes

class Jogadores(pg.sprite.Sprite):
    def __init__(self, posicao, classe):
        super().__init__()
        self.funcoes = Funcoes()
        
        self.classe = classe
        self.posicao = posicao
        self.posicaoBackup = posicao
        self.vetorUnitario = [0, 0]
        self.direcaoInicial = [0, 0]
        self.velocidade = [0, 0]
        self.Vadicional = [0, 0]
        self.massa = Configs.massa_personagem[classe]
        self.vida = Configs.vitalidade[classe]
        self.tempoDeImunidade = 2000 #2 segundos
        self.tempoDoUltimoDano = 0
        self.morte = False
        self.ultimoAtaque = 0
        self.largura_sprite, self.altura_sprite = Configs.dimensoes_sprite[self.classe]
        self.escala = Configs.ESCALA
        self.sprite_sheet = pg.image.load(f"sprites/{self.classe}.png").convert_alpha()
        self.image = pg.image.load(f"sprites/{Configs.hitbox_arquivo[self.classe]}.png").convert_alpha()
        self.image = pg.transform.scale(self.image, Configs.DIMENSOES_PERSONAGEM)
        self.rect = self.image.get_rect(center = self.posicao)
        self.mask = pg.mask.from_surface(self.image)
        self.tempo_anterior = pg.time.get_ticks()
        self.animacao_atual = 3
        self.frame_atual = 0
        self.sprites = []
        self.livre = True
        self.atacando = False

        # Forma uma lista de listas do tipo [movimento sendo executado][frame do movimento]
        contadorFrames = 0
        for i in range(len(Configs.frames_por_animacao[self.classe])):
            lista_temporaria = []
            for _ in range(Configs.frames_por_animacao[self.classe][i]):
                lista_temporaria.append(self.sprite_selecionado(self.sprite_sheet, contadorFrames, Configs.ESCALA))
                contadorFrames += 1
            self.sprites.append(lista_temporaria)

    def sprite_selecionado(self, sheet, frame, escala):
        imagem = pg.Surface((self.largura_sprite, self.altura_sprite)).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * self.largura_sprite, 0, self.largura_sprite, self.altura_sprite))
        imagem = pg.transform.scale(imagem, (self.largura_sprite * escala, self.altura_sprite * escala))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

    def atualizaVelocidade(self):
        # Desaceleracao
        if self.Vadicional[0] != 0:
            self.Vadicional[0] -= Configs.DESACELERACAO * self.funcoes.sinal(self.Vadicional[0])
        if self.Vadicional[1] != 0:
            self.Vadicional[1] -= Configs.DESACELERACAO * self.funcoes.sinal(self.Vadicional[1]) 

        # Movimento comandado pelo jogador
        if self.livre:
            if self.vetorUnitario[0] == self.vetorUnitario[1] == 0:
                self.velocidade = [0, 0]
                self.frame_atual = 0
                self.animacao_atual = Configs.seleciona_animacoes_parado[self.direcaoInicial[0], self.direcaoInicial[1]]
            else:
                angulo = self.funcoes.inclinacaoSinCos(self.vetorUnitario[1], self.vetorUnitario[0])
                Vmodulo = Configs.velocidade_personagem[self.classe]  
            
                if angulo % (math.pi/2) == 0:
                    self.direcaoInicial[0] = self.vetorUnitario[0]
                    self.direcaoInicial[1] = self.vetorUnitario[1]

                self.velocidade = [int(Vmodulo * math.cos(angulo)), int(Vmodulo * math.sin(angulo))]
                self.animacao_atual = Configs.seleciona_animacoes[self.direcaoInicial[0], self.direcaoInicial[1]]

        self.posicaoBackup = self.rect.center
        self.velocidadeTotal = [self.velocidade[0] + self.Vadicional[0], self.velocidade[1] + self.Vadicional[1]]

    def moverX(self):
        self.rect.centerx += self.velocidadeTotal[0]

    def moverY(self):
        self.rect.centery += self.velocidadeTotal[1]
    
    def ataqueBasico(self):
        self.frame_atual = 0
        self.animacao_atual = Configs.seleciona_animacoes[self.direcaoInicial[0], self.direcaoInicial[1]] + 1
       
        self.velocidade = [0, 0]
        self.livre = False
        self.atacando = True

    def desenha(self, tela, tempoAtual):
        self.posicao_rect = [self.rect.centerx - Configs.subracao_rect[self.classe][0] * self.escala, 
                             self.rect.centery - Configs.subracao_rect[self.classe][1] * self.escala]
        tela.blit(self.sprites[self.animacao_atual][self.frame_atual], self.posicao_rect)
        if tempoAtual - self.tempo_anterior >= Configs.DURACAO_FRAME:
            self.frame_atual += 1

            if self.frame_atual == len(self.sprites[self.animacao_atual]):
                self.livre = True
                self.frame_atual = 0
            self.tempo_anterior = tempoAtual  

    def verificarMorte(self):
        if self.vida <= 0:
            print(self.vida)
            self.morte = True
        return self.morte