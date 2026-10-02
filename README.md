# 📊 Data Analytics & Dashboard CSV

Uma aplicação modular em Python desenvolvida para leitura, processamento e visualização gráfica interativa de dados a partir de arquivos CSV. O projeto oferece execução via linha de comando (CLI) para análises rápidas e uma interface web interativa (Front-End) construída com Streamlit.

🔗 **Acesse a aplicação online:** [https://python-read-csv-dtzs8srcmukkpkqnd2mpiv.streamlit.app/](https://python-read-csv-dtzs8srcmukkpkqnd2mpiv.streamlit.app/)

---

## 🎯 Funcionalidades

* **Leitura Inteligente de CSV:** Processamento automatizado de dados usando Pandas.

* **Identificação Automática de Colunas:** Separação dinâmica entre dados categóricos (texto) e numéricos.

* **Gráficos Personalizáveis:**

  * **Barras e Pizza/Setores:** Para análise de frequência e proporcionalidade categórica.

  * **Histogramas:** Para verificação de distribuição de dados numéricos.

  * **Boxplot:** Para análise de dispersão e identificação de *outliers*.

  * **Scatter Plot (Dispersão 2D):** Para comparação entre duas variáveis numéricas.

* **Interface Web Interativa:** Alterne estilos gráficos, temas e paletas de cores (*Viridis*, *Plasma*, *Magma*, *Set2*, etc.) diretamente pela barra lateral do Streamlit.

* **Arquitetura Modular:** Separação entre regra de negócios (`leitor.py`), automação de terminal (`main.py`) e dashboard web (`app.py`).

## 📁 Estrutura do Projeto

```
python-read-csv/
├── leitor.py        # Módulo central com lógica de processamento e geração de gráficos
├── main.py          # Script para execução via linha de comando (CLI)
├── app.py           # Interface gráfica web (Streamlit)
├── dados.csv        # Arquivo de dados de exemplo
├── requirements.txt # Lista de dependências do projeto
└── README.md        # Documentação do projeto
```

## 🚀 Como Executar Localmente (Pelo Terminal)

### Pré-requisitos

* Python 3.12+

* Git instalado

### 1. Clonar o Repositório e Configurar o Ambiente Virtual

No seu terminal **Git Bash**:

```bash
# 1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/python-read-csv.git
cd python-read-csv

# 2. Criar o ambiente virtual com Python 3.12
py -3.12 -m venv venv

# 3. Ativar o ambiente virtual
source venv/Scripts/activate

# 4. Instalar as dependências
python -m pip install -r requirements.txt
```

### 2. Executar via Linha de Comando (CLI)

Para rodar a análise automatizada diretamente no terminal e salvar gráficos como imagens localmente:

```bash
python main.py
```

### 3. Executar o Dashboard Web (Local)

Para abrir o aplicativo no navegador e interagir com o front-end localmente:

```bash
streamlit run app.py
```

O aplicativo abrirá automaticamente no seu navegador no endereço: **`http://localhost:8501`**.

## 🌐 Acesso Web & Deployment

### Aplicação em Produção (Streamlit Community Cloud)

O projeto está hospedado e disponível publicamente no seguinte link:  
👉 **[https://python-read-csv-dtzs8srcmukkpkqnd2mpiv.streamlit.app/](https://python-read-csv-dtzs8srcmukkpkqnd2mpiv.streamlit.app/)**

### Atualizações Automáticas (CI/CD)

Como a aplicação está conectada ao repositório GitHub, qualquer alteração enviada para a branch `main` atualizará automaticamente o site online:

```bash
git add .
git commit -m "Atualização do projeto"
git push origin main
```

## 🛠️ Tecnologias Utilizadas

* [**Python**](https://www.python.org/)**:** Linguagem principal do projeto.

* [**Pandas**](https://pandas.pydata.org/)**:** Leitura e manipulação estruturada de dados.

* [**Matplotlib**](https://matplotlib.org/) **& [Seaborn](https://seaborn.pydata.org/):** Geração e estilização gráfica.

* [**Streamlit**](https://streamlit.io/)**:** Framework para construção rápida de dashboards web interativos.