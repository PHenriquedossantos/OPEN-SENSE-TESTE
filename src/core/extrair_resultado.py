import re

def extrair_resultado(soup):
    """
    Extrai o número de processos encontrados no arquivo HTML.
    """
    numero_processos = 0
    resultado_tag = soup.find(string=re.compile(r"Foram encontrados"))
    if resultado_tag:
        numero_processos_tag = resultado_tag.find_next('b')
        if numero_processos_tag and numero_processos_tag.string.isdigit():
            numero_processos = int(numero_processos_tag.string)
    return numero_processos
