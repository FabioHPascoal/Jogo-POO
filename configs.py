import math
class Configs:
    LARGURA_TELA = 1280
    ALTURA_TELA = 640
    ESCALA = 2
    FRAME_RATE = 60
    DURACAO_FRAME = 100
    BLOCOS_TAMANHO = 64
    BLOCOS_X = int(20)
    BLOCOS_Y = int(10)

    #CORES
    PRETO = (0,0,0)
    BRANCO = (255,255,255)
    VERMELHO = (255,0,0)
    VERDE = (0,255,0)
    AZUL = (0,0,255)
    CINZA = (197,197,197)
    CINZA_ESCURO = (127,127,127)
    COR_FUNDO = (71, 175, 191)

    MAPA_FASE1 = [
    ['4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','6','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','6',' ','4'],
    ['4',' ',' ','4','4','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ','1','4',' ',' ',' ',' ',' ','5',' ',' ',' ',' ',' ',' ',' ','2',' ','4'],
    ['4',' ',' ','4','4','4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4','6',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4'],
    ]

    DIMENSOES_PERSONAGEM = (32 * ESCALA, 16 * ESCALA)
    DESACELERACAO = 1

    angulo = {
        "direita": 0,
        "cima": math.pi/2,
        "esquerda": math.pi,
        "baixo": (3/2) * math.pi
    }
 
    tipo_de_classe = {
        "cavaleiro": "melee",
        "arqueiro": "ranged",
        "ladino": "melee",
        "mago": "ranged",
        "goblin": "melee"
    }

    velocidade_personagem = {
        "cavaleiro": 5,
        "arqueiro": 5,
        "ladino": 5,
        "mago": 5,
        "goblin": 2
    }

    velocidade_projeteis = {
        "flecha": 10,
        "fireball": 6,
    }

    massa_personagem = {
        "cavaleiro": 5,
        "arqueiro": 3,
        "ladino": 3,
        "mago": 3,
        "goblin": 3
    }

    vitalidade = {
        "cavaleiro": 5,
        "arqueiro": 3,
        "ladino": 3,
        "mago": 3,
        "goblin": 3
    }

    dimensoes_sprite = {
        "cavaleiro": (148, 90),
        "arqueiro": (64, 64),
        "ladino": (64, 64),
        "mago": (64, 64),
        "goblin": (64, 64)
    }

    subracao_rect = {
        "cavaleiro": (73, 62),
        "arqueiro": (31, 49),
        "ladino": (31, 49),
        "mago": (31, 50),
        "goblin": (31, 50)
    }

    frames_por_animacao = {
        "cavaleiro": [1, 8, 6, 1, 8, 6, 1, 8, 6, 1, 8, 6, 6],
        "arqueiro": [1, 8, 11, 1, 8, 11, 1, 8, 11, 1, 8, 11, 6],
        "ladino": [1, 8, 6, 1, 8, 6, 1, 8, 6, 1, 8, 6, 6],
        "mago": [1, 8, 8, 1, 8, 8, 1, 8, 8, 1, 8, 8, 6],
        "goblin": [1, 8, 6, 1, 8, 6, 1, 8, 6, 1, 8, 6, 6]
    }

    frames_de_ataque = {
        "cavaleiro": [4, 5],
        "arqueiro": [9],
        "ladino": [3, 4, 5],
        "mago": [6],
        "goblin": [3, 4, 5]
    }

    duracao_frame_ataque = {
        "cavaleiro": 100,
        "arqueiro": 80,
        "ladino": 30,
        "mago": 80,
        "goblin": 50
    }

    seleciona_animacoes = {
        (-1, 0): 1,
        (1, 0): 4,
        (0, -1): 7,
        (0, 1): 10,
        (0, 0): 4
    }

    seleciona_animacoes_parado = {
        (-1, 0): 0,
        (1, 0): 3,
        (0, -1): 6,
        (0, 1): 9,
        (0, 0): 3
    }

    seleciona_frame_ataque = {
        (-1, 0): 0,
        (1, 0): 1,
        (0, -1): 2,
        (0, 1): 3,
        (0, 0): 3
    }

    hitbox_arquivo = {
        "cavaleiro": "hitbox_jogadores",
        "arqueiro": "hitbox_jogadores",
        "ladino": "hitbox_jogadores",
        "mago": "hitbox_jogadores",
        "goblin": "hitbox_minions"
    }

    historia = {
        "cavaleiro": ("Honrado nas novelas de cavalaria,","defensor da princesa, sua Dulcineia"),
        "arqueiro": ("Amiga da princesa."," "),
        "ladino": ("Miserável sem vergonha,","pretende sequestrar a princesa."),
        "mago": ("Aluno da academia de magia que","se envolveu por acaso no conflito")
    }