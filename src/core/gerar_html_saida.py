import os

def gerar_html_saida(resultados, output_path="PATENTES.HTML"):
    """
    Gera um arquivo HTML com os resultados, incluindo colunas para informações adicionais.

    Args:
        resultados (list): Lista de dicionários contendo informações extraídas.
        output_path (str): Caminho para salvar o arquivo HTML gerado.
    """
    def formatar_cnpj(cnpj):
        """
        Formata um CNPJ no padrão XX.XXX.XXX/XXXX-XX.

        Args:
            cnpj (str): CNPJ a ser formatado (apenas números).

        Returns:
            str: CNPJ formatado ou "N/A" se o valor for inválido.
        """
        if len(cnpj) == 14 and cnpj.isdigit():
            return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
        return "N/A"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("<html><head><title>Resultados das Patentes</title></head><body>")
        f.write("<h1>Resultados das Patentes</h1>")
        f.write("<table border='1'>")
        # Adiciona cabeçalho da tabela com a coluna 'Arquivo' como primeira coluna
        f.write(
            "<tr><th>Arquivo</th><th>CNPJ</th><th>Número do Pedido</th><th>Resultado</th>"
            "<th>Data do Depósito</th><th>Título</th><th>IPC</th></tr>"
        )

        for resultado in resultados:
            arquivo = resultado.get("Arquivo", "N/A")  # Obtém o nome do arquivo
            cnpj = formatar_cnpj(resultado.get("CNPJ", ""))
            numero_pedido = resultado.get("Pedido", "N/A")
            resultado_texto = resultado.get("RESULTADO", "N/A")
            data_deposito = resultado.get("Deposito", "N/A")
            titulo = resultado.get("Titulo", "N/A")
            ipc = resultado.get("IPC", "N/A")

            # Adiciona o nome do arquivo como a primeira coluna da linha
            f.write(
                f"<tr><td>{arquivo}</td><td>{cnpj}</td><td>{numero_pedido}</td><td>{resultado_texto}</td>"
                f"<td>{data_deposito}</td><td>{titulo}</td><td>{ipc}</td></tr>"
            )

        f.write("</table>")
        f.write("</body></html>")

    print(f"HTML gerado com sucesso em: {os.path.abspath(output_path)}")
