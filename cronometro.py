class Cronometro:
    def __init__(self):
        self.reset()

    def reset(self):
        self.contagem = 2 * 60 * 1000 #2minutos

    def tempoPassado(self,tempoDeJogo):
        return (self.contagem - tempoDeJogo)//1000


