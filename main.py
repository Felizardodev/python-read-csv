from leitor import carregar_dados, obter_resumo_colunas, gerar_grafico_barras

def main():
    caminho_csv = 'dados.csv'  # Altere para o seu arquivo CSV de teste
    
    try:
        df = carregar_dados(caminho_csv)
        print("--- Dados Carregados com Sucesso via main.py ---")
        print(df.head())

        colunas_texto, colunas_numericas = obter_resumo_colunas(df)
        
        # Se houver colunas categóricas, gera e salva um gráfico de teste
        if colunas_texto:
            coluna_teste = colunas_texto[0]
            fig = gerar_grafico_barras(df, coluna_teste)
            fig.savefig('grafico_gerado_main.png')
            print(f"-> Gráfico salvo com sucesso: 'grafico_gerado_main.png'")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_csv}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro no main: {e}")

if __name__ == '__main__':
    main()