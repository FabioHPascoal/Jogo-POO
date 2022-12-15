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
    ['4',' ',' ',' ',' ',' ',' ','9','10','11','12','13',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ','14','15','16','17','18',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ',' ','4',' ',' ',' ','8','6','6','6','7',' ',' ',' ',' ','4',' ',' ','4'],
    ['4',' ',' ','4',' ',' ',' ','8','6','6','6','7',' ',' ',' ',' ','4',' ',' ','4'],
    ['4',' ',' ','4',' ',' ',' ','8','6','5','6','7',' ',' ',' ',' ','4',' ',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ','8','6','6','6','7',' ',' ',' ',' ',' ',' ',' ','4'],
    ['4',' ','1',' ',' ',' ',' ','8','6','6','6','7',' ',' ',' ',' ',' ','2',' ','4'],
    ['4',' ',' ',' ',' ',' ',' ','8','6','6','6','7',' ',' ',' ',' ',' ',' ',' ','4'],
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

    ataques_sao_desenhados = ["arqueiro", "mago"]

    velocidade_personagem = {
        "cavaleiro": 4,
        "arqueiro": 6,
        "ladino": 5,
        "mago": 6,
        "goblin": 2
    }

    velocidade_projeteis = {
        "flecha": 10,
        "fireball": 6,
        "facada": 22
    }

    massa_personagem = {
        "cavaleiro": 5,
        "arqueiro": 3,
        "ladino": 4,
        "mago": 3,
        "goblin": 3
    }

    vitalidade = {
        "cavaleiro": 8,
        "arqueiro": 5,
        "ladino": 6,
        "mago": 5,
        "goblin": 5
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
        "cavaleiro": [1, 8, 6, 0, 1, 8, 6, 0, 1, 8, 6, 0, 1, 8, 6, 0, 6],
        "arqueiro": [1, 8, 11, 0, 1, 8, 11, 0, 1, 8, 11, 0, 1, 8, 11, 0, 6],
        "ladino": [1, 8, 6, 0, 1, 8, 6, 0, 1, 8, 6, 0, 1, 8, 6, 0, 6],
        "mago": [1, 8, 8, 7, 1, 8, 8, 7, 1, 8, 8, 7, 1, 8, 8, 7, 6],
        "goblin": [1, 8, 6, 0, 1, 8, 6, 0, 1, 8, 6, 0, 1, 8, 6, 0, 6]
    }

    frames_de_ataque = {
        "cavaleiro": [4, 5],
        "arqueiro": [9],
        "ladino": [3, 4, 5],
        "mago": [6],
        "goblin": [3, 4, 5]
    }

    frames_de_habilidade = {
        "cavaleiro": [],
        "arqueiro": [],
        "ladino": [],
        "mago": [5],
        "goblin": []
    }

    duracao_frame_estado = {
        "atacando": {
            "cavaleiro": [120, 120, 120, 120, 50, 50],
            "arqueiro": [50, 50, 50, 50, 50, 50, 50, 50, 400, 50, 50],
            "ladino": [300, 300, 150, 30, 30, 400],
            "mago": [80, 80, 80, 80, 80, 80, 80, 80],
            "goblin": [50, 50, 50, 50, 50, 50]
        },
        "livre": {
            "cavaleiro": [100, 100, 100, 100, 100, 100, 100, 100],
            "arqueiro": [80, 80, 80, 80, 80, 80, 80, 80],
            "ladino": [80, 80, 80, 80, 80, 80, 80, 80],
            "mago": [80, 80, 80, 80, 80, 80, 80, 80],
            "goblin": [80, 80, 80, 80, 80, 80, 80, 80]
        },
        "castando_skill": {
            "cavaleiro": [],
            "arqueiro": [],
            "ladino": [],
            "mago": [120, 120, 120, 120, 120, 400, 120],
            "goblin": []
        }
    }

    seleciona_animacoes = {
        (-1, 0): 1,
        (1, 0): 5,
        (0, -1): 9,
        (0, 1): 13,
        (0, 0): 5
    }

    seleciona_animacoes_parado = {
        (-1, 0): 0,
        (1, 0): 4,
        (0, -1): 8,
        (0, 1): 12,
        (0, 0): 4
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