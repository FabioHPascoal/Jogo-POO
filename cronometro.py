class Cronometro:
    def __init__(self)->None:
        self.reset()
        self.cronometrado = 10 #tanto faz esse valor, mas tem que ser maior que 0
    def reset(self)->None:
        self.contagem = 2 * 60 * 1000 #2minutos

    def tempoPassado(self,tempoDeJogo:int)->int:
        self.cronometrado = (self.contagem - tempoDeJogo)//1000
        return self.cronometrado


