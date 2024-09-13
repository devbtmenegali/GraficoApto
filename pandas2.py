import matplotlib.pyplot as plt
import pandas as pd

def importar_dados ():

    url_dados = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

    leitura_dados = pd.read_csv(url_dados,sep=";")

    return leitura_dados

def manipulacao_dos_dados(leitura_dados):

    numero_de_imoveis = leitura_dados["Tipo"].value_counts()

    return numero_de_imoveis

def graficos (leitura_dados, numero_de_imoveis):

    tipo = leitura_dados["Tipo"]

    plt.bar(tipo,numero_de_imoveis)

    plt.xlabel ("Tipos de Imóveis")
    plt.ylabel ("Quantidade")

    plt.title("Tipos de Imóveis")

    plt.show()

def main():

    leitura_dados = importar_dados()
    numero_de_imoveis = manipulacao_dos_dados(leitura_dados)
    
    graficos(leitura_dados,numero_de_imoveis)

if __name__=="__main__":

    main()