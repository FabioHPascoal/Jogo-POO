class Configs:
    LARGURA_TELA = 1080
    ALTURA_TELA = 720
    
    spawnX_1 = (0.1 * LARGURA_TELA)
    spawnY_1 = (0.7 * ALTURA_TELA)
    spawnX_2 = (0.9 * LARGURA_TELA)
    spawnY_2 = (0.1 * ALTURA_TELA)

    velocidade_personagem = {
        "warrior": 0.2,
        "archer": 0.5
    }
   
    dimensoes_personagem = {
        "warrior": (100, 100),
        "archer": (50, 50)
    }
    
    cor_personagem = {
        "warrior": (0, 0, 0),
        "archer": (100, 100, 100)
    }

    COR_FUNDO = (71, 175, 191)