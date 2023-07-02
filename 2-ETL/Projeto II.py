"""
Projeto da matéria de Lógica de Programação II
Escolhi um dataset sobre de Formula 1
Disponível em: https://www.kaggle.com/datasets/dubradave/formula-1-drivers-dataset
"""
import csv
from functools import reduce

# Definindo caminho do arquivo
caminho_do_arquivo = "D:\DEV\Be The Next\Projeto II\F1DriversDataset.csv"

# Criando uma lista vazia para receber os dicionários com as informações de cada piloto
pilotos = []


# Função para acessar arquivo e tratar possíveis exceções
def acessar_arquivo(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, "r", encoding="utf8") as arquivo:
            csv_reader = csv.DictReader(arquivo)
            for linha in csv_reader:
                pilotos.append(linha)
    except IOError as e:
        print(f"Ocorreu um erro lendo o arquivo: {e}")


# Calculando número de campeonatos disputados desde o começo da F1
def total_gp(pilotos):
    total_campeonatos = sum(int(float(piloto["Championships"])) for piloto in pilotos)

    return total_campeonatos


"""
Pensei em usar:
reduce(lambda total, piloto: total + int(float(piloto["Championships"])), pilotos, 0)
Mas ficou mais inteligível da outra forma,
então acabou não sendo necessário usar essa estrutura.
"""


# Checando numero de campeoes
def numero_campeoes(pilotos):
    campeoes = 0
    for piloto in pilotos:
        campeonato = float(piloto["Championships"])
        if campeonato > 0:
            campeoes += 1
    return campeoes


# Calculando pilotos com maior numero de campeonatos
def campeonatos_ganhos(pilotos):
    maior_numero_campeonatos = 0
    campeao = []

    for piloto in pilotos:
        campeonatos = int(float(piloto["Championships"]))
        if campeonatos > maior_numero_campeonatos:
            maior_numero_campeonatos = campeonatos
            campeao = [piloto["Driver"]]
        elif campeonatos == maior_numero_campeonatos:
            campeao.append(piloto["Driver"])

    return campeao, maior_numero_campeonatos


# Checando o piloto com maior numero de vitórias
def vitorias(pilotos):
    maior_numero_vitorias = 0
    maior_vencedor = None

    for piloto in pilotos:
        vitorias = int(float(piloto["Race_Wins"]))
        if vitorias > maior_numero_vitorias:
            maior_numero_vitorias = vitorias
            maior_vencedor = piloto["Driver"]

    return maior_vencedor, maior_numero_vitorias


# Checando os campeões ainda ativos
def campeoes_ativos(pilotos):
    ativos = []
    for piloto in pilotos:
        if piloto["Championships"] != "0.0" and piloto["Active"] == "True":
            ativos.append(piloto["Driver"])

    return ativos


# Criando um arquivo de saída com os dados filtrados
def relatorio(
    total_campeonatos,
    num_campeoes,
    maior_campeao,
    maior_numero_campeonatos,
    maior_vencedor,
    maior_numero_vitorias,
    ativos,
):
    try:
        with open("relatorio.txt", "w") as saida:
            saida.write(f"Até hoje foram disputados {total_campeonatos} Grand Prix\n")
            saida.write("\n")
            saida.write(
                f"Tivemos {num_campeoes} campeões mundiais, os maiores sendo:\n"
            )
            for nome in maior_campeao:
                saida.write(f"{nome}\n")
            saida.write(f"Com {maior_numero_campeonatos} campeonatos cada um\n")
            saida.write("\n")
            saida.write(
                f"{maior_vencedor} é o maior vencedor de GPs com {maior_numero_vitorias} vitórias\n"
            )
            saida.write("\n")
            saida.write(f"Os campeões ainda ativos são:\n")
            for nome in ativos:
                saida.write(f"{nome}\n")
    except IOError as e:
        print(f"Ocorreu um erro ao criar o arquivo: {e}")


# Chamando as funções específicas para ler o arquivo, calcular ou filtrar
acessar_arquivo(caminho_do_arquivo)
total_campeonatos = total_gp(pilotos)
num_campeoes = numero_campeoes(pilotos)
maior_campeao, maior_numero_campeonatos = campeonatos_ganhos(pilotos)
maior_vencedor, maior_numero_vitorias = vitorias(pilotos)
ativos = campeoes_ativos(pilotos)

# Chamando a função relatorio para imprimir o arquivo de saida
relatorio(
    total_campeonatos,
    num_campeoes,
    maior_campeao,
    maior_numero_campeonatos,
    maior_vencedor,
    maior_numero_vitorias,
    ativos,
)
