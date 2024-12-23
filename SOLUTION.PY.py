from src.core.processar_arquivos import processar_arquivos
from src.core.gerar_html_saida import gerar_html_saida

try:
    diretorio_patentes = "./PATENTES"
    resultados = processar_arquivos(diretorio_patentes)
    gerar_html_saida(resultados)
    print("Processamento concluído! O arquivo PATENTES.HTML foi gerado.")
except Exception as e:
    print(f"Ocorreu um erro durante o processamento: {e}")
