#Arquivo principal, a execução começa por aqui
from jogo import JogoPOO

def main(): 
    jogo = JogoPOO() #Cria objeto do tipo JogoPOO
    jogo.rodar() #Executa o método rodar() do objeto jogo

if __name__ == "__main__":
    main()