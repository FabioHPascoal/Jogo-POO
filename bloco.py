import pygame as pg
from configs import*

class Bloco(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/parede.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Grama(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/grama.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Caixa(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/caixa.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = posicao)

class Chamas(pg.sprite.Sprite):
    def __init__(self,posicao,grupos_sprites):
        super().__init__(grupos_sprites)
        self.image = pg.image.load("sprites/chamas.png").convert_alpha()
        self.sprites = []
        self.rect = self.image.get_rect(topleft = posicao)
        contadorFrames = 0
        self.frame_atual = 0
        
    #     for _ in range(7):
    #         self.sprites(self.sprite_selecionado(self.image, contadorFrames, (64,64)))
    #         contadorFrames += 1

    # def update(self):
    #     if pg.time.get_ticks() - self.tempo_anterior >= Configs.DURACAO_FRAME:
    #         self.frame_atual += 1

    #         if self.frame_atual == len(self.sprites_arqueiro):
    #             self.frame_atual = 0
    #         self.tempo_anterior = pg.time.get_ticks()


    def sprite_selecionado(self, sheet, frame, dimensoes):
        imagem = pg.Surface(dimensoes).convert_alpha()
        imagem.blit(sheet, (0, 0), (frame * dimensoes[0], 0, dimensoes[0], dimensoes[1]))
        imagem.set_colorkey((0, 0, 0, 0))
        return imagem

