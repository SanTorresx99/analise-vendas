# Funções auxiliares podem ser adicionadas aqui
import pandas as pd

def carregar_dados(caminho_csv):
    """
    Lê um arquivo CSV e realiza pré-processamento padrão.
    """
    df = pd.read_csv(caminho_csv)
    df['Data'] = pd.to_datetime(df['Data'])
    df['Faturamento'] = df['Preço'] * df['Quantidade']
    return df

def faturamento_agrupado(df, por='Cidade'):
    """
    Retorna o total de faturamento agrupado por uma coluna (ex: Cidade, Categoria, Produto).
    """
    return df.groupby(por)['Faturamento'].sum().sort_values(ascending=False)

def produto_mais_vendido(df):
    """
    Retorna a quantidade total vendida por produto, ordenado do maior para o menor.
    """
    return df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

def faturamento_temporal(df, freq='W'):
    """
    Retorna o faturamento ao longo do tempo agrupado pela frequência desejada.
    Frequência: 'D' = diária, 'W' = semanal, 'M' = mensal
    """
    return df.resample(freq, on='Data')['Faturamento'].sum()
