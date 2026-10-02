import streamlit as st
from leitor import (
    carregar_dados,
    obter_resumo_colunas,
    aplicar_estilo_grafico,
    gerar_grafico_barras,
    gerar_grafico_pizza,
    gerar_grafico_hist,
    gerar_grafico_boxplot,
    gerar_grafico_dispersao
)

st.set_page_config(page_title="Dashboard CSV com Múltiplos Estilos", layout="wide")

st.title("📊 Dashboard com Opções Estilizadas de Gráficos")

# --- Barra Lateral para Configuração de Estilo e Tema ---
st.sidebar.header("🎨 Configuração Visual")

estilo_fundo = st.sidebar.selectbox(
    "Estilo do Fundo / Grade:",
    ["whitegrid", "darkgrid", "white", "dark", "ticks"]
)

paleta_cores = st.sidebar.selectbox(
    "Paleta de Cores:",
    ["viridis", "plasma", "magma", "deep", "Set2", "coolwarm", "tab10"]
)

# Aplica as preferências selecionadas na sidebar
aplicar_estilo_grafico(estilo=estilo_fundo, paleta=paleta_cores)

# --- Upload de Arquivo ---
uploaded_file = st.file_uploader("Carregue o arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = carregar_dados(uploaded_file)
    colunas_texto, colunas_numericas = obter_resumo_colunas(df)

    st.subheader("📋 Prévia do Arquivo")
    st.dataframe(df.head(10))

    st.markdown("---")
    st.subheader("📈 Gerador Personalizado de Gráficos")

    tipo_grafico = st.selectbox(
        "Selecione o Tipo de Gráfico:",
        ["Gráfico de Barras", "Gráfico de Pizza / Setores", "Histograma (Distribuição)"]
    )

    fig = None

    # --- Seleção de Parâmetros ---
    if tipo_grafico in ["Gráfico de Barras", "Gráfico de Pizza / Setores"]:
        if colunas_texto:
            col = st.selectbox("Selecione a coluna categórica:", colunas_texto)
            if tipo_grafico == "Gráfico de Barras":
                fig = gerar_grafico_barras(df, col, paleta=paleta_cores)
            else:
                fig = gerar_grafico_pizza(df, col, paleta=paleta_cores)
        else:
            st.warning("O arquivo não possui colunas de texto/categorias.")

    elif tipo_grafico == "Histograma (Distribuição)":
        if colunas_numericas:
            col = st.selectbox("Selecione a coluna numérica:", colunas_numericas)
            fig = gerar_grafico_hist(df, col, paleta=paleta_cores)
        else:
            st.warning("O arquivo não possui colunas numéricas.")

    # --- EXIBIÇÃO CENTRALIZADA DO GRÁFICO ---
    if fig is not None:
        # Cria 3 colunas: a central ([1, 3, 1]) ocupa o centro da tela
        col_esq, col_centro, col_dir = st.columns([1, 3, 1])
        with col_centro:
            st.pyplot(fig)

else:
    st.info("Aguardando upload do arquivo CSV.")