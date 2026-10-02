import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def carregar_dados(fonte_dados):
    """Lê o arquivo CSV e devolve um DataFrame."""
    return pd.read_csv(fonte_dados)

def obter_resumo_colunas(df):
    """Retorna listas de colunas categóricas e numéricas."""
    colunas_texto = df.select_dtypes(include=['object', 'category']).columns.tolist()
    colunas_numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    return colunas_texto, colunas_numericas

def aplicar_estilo_grafico(estilo="whitegrid", paleta="viridis"):
    """Configura o estilo e a paleta de cores para o Matplotlib/Seaborn."""
    sns.set_theme(style=estilo, palette=paleta)

def gerar_grafico_barras(df, coluna_cat, paleta="viridis"):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    contagem = df[coluna_cat].value_counts().head(10)
    sns.barplot(x=contagem.index, y=contagem.values, ax=ax, palette=paleta, hue=contagem.index, legend=False)
    ax.set_title(f"Contagem por {coluna_cat}", fontsize=12, fontweight='bold')
    ax.set_xlabel(coluna_cat)
    ax.set_ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def gerar_grafico_pizza(df, coluna_cat, paleta="Set2"):
    fig, ax = plt.subplots(figsize=(6, 5))
    contagem = df[coluna_cat].value_counts().head(7)
    cores = sns.color_palette(paleta, len(contagem))
    ax.pie(contagem.values, labels=contagem.index, autopct='%1.1f%%', startangle=140, colors=cores)
    ax.set_title(f"Proporção por {coluna_cat}", fontsize=12, fontweight='bold')
    plt.tight_layout()
    return fig

def gerar_grafico_hist(df, coluna_num, paleta="magma"):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    sns.histplot(df[coluna_num], kde=True, ax=ax, color=sns.color_palette(paleta)[0])
    ax.set_title(f"Distribuição de {coluna_num}", fontsize=12, fontweight='bold')
    ax.set_xlabel(coluna_num)
    ax.set_ylabel("Frequência")
    plt.tight_layout()
    return fig

def converter_figura_para_bytes(fig):
    """Converte a figura Matplotlib para bytes para exibição no Streamlit."""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return buf