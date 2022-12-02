import math
class Configs:
    LARGURA_TELA = 1280
    ALTURA_TELA = 720
    ESCALA = 2
    FRAME_RATE = 60
    DURACAO_FRAME = 150
    BLOCOS_TAMANHO = 32

    spawnX_1 = (0.2 * LARGURA_TELA)
    spawnY_1 = (0.5 * ALTURA_TELA)
    spawnX_2 = (0.8 * LARGURA_TELA)
    spawnY_2 = (0.5 * ALTURA_TELA)

    #CORES
    PRETO = (0,0,0)
    BRANCO = (255,255,255)
    VERMELHO = (255,0,0)
    VERDE = (0,255,0)
    AZUL = (0,0,255)

    MAPA_FASE1 = [
    ['4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ','4','4','4',' ',' ',' ',' ',' ',' ','4','4',' ',' ',' ','4','4',' ',' ','4',' ','4',' ','4','4','4',' ','4',' ',' ','4',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4',' ','4',' ','4',' ','4',' ','4',' ','4',' ','4','4',' ','4',' ',' ',' ',' ','4'],
    ['4',' ','4',' ',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4',' ','4',' ','4',' ','4',' ','4',' ','4',' ','4','4',' ','4',' ',' ',' ',' ','4'],
    ['4',' ','4',' ',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4','4',' ',' ',' ','4',' ',' ','4','4','4',' ','4',' ','4','4',' ',' ',' ',' ','4'],
    ['4',' ','4','4','4','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4',' ','4',' ',' ','4',' ',' ','4',' ','4',' ','4',' ','4','4',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ','4',' ','4',' ',' ','4',' ',' ','4',' ','4',' ','4',' ',' ','4',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4',' ','4',' ',' ','4',' ',' ','4',' ','4',' ','4',' ',' ','4',' ',' ',' ',' ','4'],
    ['4',' ','4','4','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4'],
    ]

    frames_por_animacao1 = [1, 8, 1, 8, 1, 8, 1, 8, 6]
    
    angulo = {
        "direita": 0,
        "cima": math.pi/2,
        "esquerda": math.pi,
        "baixo": (3/2) * math.pi
    }

    velocidade_personagem = {
        "cavaleiro": 5,
        "arqueiro": 7
    }

    dimensoes_personagem = {
        "cavaleiro": (64, 64),
        "arqueiro": (64, 64)
    }

    raio_personagem = 16 * ESCALA

    massa_personagem = {
        "cavaleiro": 10,
        "arqueiro": 2
    }

    cor_personagem = {
        "cavaleiro": (0, 0, 0),
        "arqueiro": (100, 100, 100)
    }

    seleciona_animacoes = {
        (-1, 0): 1,
        (1, 0): 3,
        (0, -1): 5,
        (0, 1): 7,
        (0, 0): 3
    }

    seleciona_animacoes_parado = {
        (-1, 0): 0,
        (1, 0): 2,
        (0, -1): 4,
        (0, 1): 6,
        (0, 0): 2
    }

    COR_FUNDO = (71, 175, 191)

    desaceleracao = 1