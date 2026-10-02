import pandas as pd

# Substitua pelo nome do seu ficheiro CSV
caminho_csv = 'dados.csv'

try:
    df = pd.read_csv(caminho_csv)
    print("--- Dados carregados com sucesso ---")
    print(df.head())  # Exibe as 5 primeiras linhas
except FileNotFoundError:
    print(f"Erro: O ficheiro '{caminho_csv}' não foi encontrado na pasta do projeto.")