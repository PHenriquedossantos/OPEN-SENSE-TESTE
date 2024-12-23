import os
from bs4 import BeautifulSoup
from src.core.extrair_resultado import extrair_resultado
from src.core.extrair_dados import extrair_dados

def processar_arquivos(diretorio):

    resultados = []

    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_arquivo) and arquivo.endswith(".html"):
            with open(caminho_arquivo, 'r', encoding='ISO-8859-1') as f:
                conteudo = f.read()

            soup = BeautifulSoup(conteudo, 'html.parser')
            dados = extrair_dados(soup)
            numero_processos = extrair_resultado(soup)
            for cnpj, dados_extraidos in dados.items():
                for processo in dados_extraidos:
                    resultados.append({
                        "CNPJ": cnpj,
                        "Pedido": processo["Pedido"],
                        "Deposito": processo["Deposito"],
                        "Titulo": processo["Titulo"],
                        "IPC": processo["IPC"],
                        "RESULTADO": numero_processos,
                        "Arquivo": arquivo,
                    })

    return resultados

try:
    diretorio_patentes = "./PATENTES"
    resultados = processar_arquivos(diretorio_patentes)
except Exception as e:
    print(f"Ocorreu um erro durante o processamento: {e}")
