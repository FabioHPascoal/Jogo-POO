import pygame as pg
from configs import*
from random import randint
class Bloco(pg.sprite.Sprite):
    def __init__(self,posicao:list,grupos_sprites) -> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/parede.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Grama(pg.sprite.Sprite):
    def __init__(self,posicao:list,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/grama.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class GramaCentro(pg.sprite.Sprite):
    def __init__(self,posicao:list,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/gramaCentro.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class GramaRioD(pg.sprite.Sprite):
    def __init__(self,posicao:list,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/gramaRioD.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class GramaRioE(pg.sprite.Sprite):
    def __init__(self,posicao:list,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/gramaRioE.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Ponte(pg.sprite.Sprite):
    def __init__(self,posicao:list,grupos_sprites,frame)-> None:
        super().__init__(grupos_sprites)
        self.sheet = pg.image.load("sprites/ponte.png").convert_alpha()
        self.image =  self.sprite_selecionado(self.sheet,frame,(Configs.BLOCOS_TAMANHO,Configs.BLOCOS_TAMANHO))
        self.rect = self.image.get_rect(topleft = posicao)

    def sprite_selecionado(self, sheet, frame, dimensoes):
        imagem = pg.Surface(dimensoes).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem = pg.transform.scale(imagem, (dimensoes[0] , dimensoes[1]))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

class Caixa(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/caixa.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Coracao(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/coracao.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Agua(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites)-> None:
        super().__init__(grupos_sprites)
        self.sheet = pg.image.load("sprites/agua.png").convert_alpha()
        self.sprites = []
        self.posicao = posicao
        self.frame_atual = 0
        self.image = self.sprite_selecionado(self.sheet,0,(Configs.BLOCOS_TAMANHO,Configs.BLOCOS_TAMANHO))
        self.rect = self.image.get_rect(topleft = self.posicao)

        for frame in range(4):
            self.sprites.append(self.sprite_selecionado(self.sheet,frame,(Configs.BLOCOS_TAMANHO,Configs.BLOCOS_TAMANHO)))
            
    def update(self,frame)-> None:
        self.image = self.sprites[frame]

    def sprite_selecionado(self, sheet, frame, dimensoes):
        imagem = pg.Surface(dimensoes).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem = pg.transform.scale(imagem, (dimensoes[0] * 3, dimensoes[1] * 3))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

    #     for _ in range(7):
    #         self.sprites(self.sprite_selecionado(self.image, contadorFrames, (64,64)))
    #         contadorFrames += 1

    # def update(self):
    #     if pg.time.get_ticks() - self.tempo_anterior >= Configs.DURACAO_FRAME:
    #         self.frame_atual += 1

    #         if self.frame_atual == len(self.sprites_arqueiro):
    #             self.frame_atual = 0
    #         self.tempo_anterior = pg.time.get_ticks()


    def sprite_selecionado(self, sheet, frame:int, dimensoes:list):
        imagem = pg.Surface(dimensoes).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

