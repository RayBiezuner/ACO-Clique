import matplotlib.pyplot as plt
import numpy as np
import glob
""""
-------------------------------------------------------------------
 Script auxiliar para transformar os logs em graficos de frequencia
 e realizar calculo de métricas
-------------------------------------------------------------------
"""
def process_file(filename):
    """
    Processa um arquivo de resultados, extrai os dados relevantes e gera um gráfico de barras.
    :param filename: Nome do arquivo a ser processado.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        data_lines = lines[5:]  # Armazena as linhas após o cabeçalho

        metadata = {}  # Dicionário para armazenar os metadados (Cabeçalho do arquivo)

        for line in lines[:5]:
            key, value = line.strip().split(':')
            metadata[key.strip()] = value.strip()
        results = []  

        for line in data_lines:
            data = line.strip().split(';')
            if len(data) == 2:
                run, result = data
                results.append(int(result))

        # Acessando os metadados armazenados
        input = metadata.get('input')
        max_iterations = metadata.get('Maximo de Iteracoes')
        formigas = metadata.get('Formigas')
        taxa_evaporacao = metadata.get('Taxa de evaporacao')

        # Configuração do gráfico de barras
        values, counts = np.unique(results, return_counts=True)
        mean = np.mean(results)
        std = np.std(results)
        
        plt.bar(values, counts,color = 'blue')
        plt.xlabel('Tamanho do Clique')
        plt.ylabel('Frequencia')
        subtitle = f"Média: {mean:.2f}, Desvio Padrão: {std:.2f}"
        plt.title(f"{input}, {max_iterations} Ciclos, {formigas} Formigas, Taxa de Evaporação: {taxa_evaporacao} \n {subtitle}")
        output_filename = f"{filename.rsplit('.', 1)[0]}.png"
        plt.savefig(output_filename)

if __name__ == "__main__":
    folder_path = 'logs-700'  # Substitua pelo caminho da pasta onde os logs forem armazenados
    txt_files = glob.glob(f"{folder_path}/*.txt")

    for file in txt_files:
        print(file)
        process_file(file)
