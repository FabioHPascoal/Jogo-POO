import math
class Configs:
    LARGURA_TELA = 1080
    ALTURA_TELA = 720
    FPS = 60

    angulo = {
        "direita": 0,
        "cima": math.pi/2,
        "esquerda": math.pi,
        "baixo": (3/2) * math.pi
    }
    
    spawnX_1 = (0.1 * LARGURA_TELA)
    spawnY_1 = (0.7 * ALTURA_TELA)
    spawnX_2 = (0.9 * LARGURA_TELA)
    spawnY_2 = (0.1 * ALTURA_TELA)

    velocidade_personagem = {
        "warrior": 2,
        "archer": 5
    }
   
    raio_personagem = {
        "warrior": 50,
        "archer": 25
    }
    
    massa_personagem = {
        "warrior": 50,
        "archer": 25
    }

    cor_personagem = {
        "warrior": (0, 0, 0),
        "archer": (100, 100, 100)
    }

    COR_FUNDO = (71, 175, 191)