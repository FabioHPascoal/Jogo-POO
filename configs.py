import math
class Configs:
    LARGURA_TELA = 1080
    ALTURA_TELA = 720
    FrameRate = 60

    angulo = {
        "direita": 0,
        "cima": math.pi/2,
        "esquerda": math.pi,
        "baixo": (3/2) * math.pi
    }
    
    spawnX_1 = (0.2 * LARGURA_TELA)
    spawnY_1 = (0.5 * ALTURA_TELA)
    spawnX_2 = (0.8 * LARGURA_TELA)
    spawnY_2 = (0.5 * ALTURA_TELA)

    velocidade_personagem = {
        "warrior": 10,
        "archer": 20
    }
   
    raio_personagem = {
        "warrior": 150,
        "archer": 75
    }
    
    massa_personagem = {
        "warrior": 20,
        "archer": 2
    }

    cor_personagem = {
        "warrior": (0, 0, 0),
        "archer": (100, 100, 100)
    }

    COR_FUNDO = (71, 175, 191)