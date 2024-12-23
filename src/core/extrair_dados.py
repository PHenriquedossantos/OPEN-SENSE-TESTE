import re

def extrair_dados(soup):
    cnpj_tag = soup.find(string=re.compile(r"CPF ou CNPJ do Depositante:"))
    cnpj = re.search(r"CPF ou CNPJ do Depositante:\s*'([\d]+)'", cnpj_tag) if cnpj_tag else None
    cnpj = cnpj.group(1) if cnpj else "N/A"
    
    processos = []

    linhas_processos = soup.find_all('tr', bgcolor=['#E0E0E0', 'white'])
    
    for linha in linhas_processos:
        pedido = linha.find('a', class_='visitado').text.strip() if linha.find('a', class_='visitado') else None
        deposito = linha.find_all('td')[1].text.strip() if linha.find_all('td')[1] else None
        titulo = linha.find('b').text.strip() if linha.find('b') else None
        ipc = linha.find('font', class_='alerta').text.strip() if linha.find('font', class_='alerta') else None
        
        processos.append({
            "Pedido": pedido,
            "Deposito": deposito,
            "Titulo": titulo,
            "IPC": ipc
        })
    
    return {cnpj: processos}
