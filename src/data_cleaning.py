import pandas as pd
import numpy as np
import os

def load_data(file_path):
    """Carrega o DataFrame processado."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
        return None

def clean_data(df):
    """
    Realiza a limpeza e pré-processamento dos dados.
    """
    print("Iniciando limpeza de dados...")
    
    # 1. Padronização da coluna 'gnero'
    df['gnero'] = df['gnero'].replace({'Menina': 'Feminino', 'Menino': 'Masculino'})
    
    # 2. Tratamento de valores nulos nas colunas de indicadores
    # Indicadores principais (IDA, IEG, IPS, IPP, IAA, IPV, IAN)
    indicator_cols = ['ida', 'ieg', 'ips', 'ipp', 'iaa', 'ipv', 'ian', 'mat', 'por', 'ing']
    
    # Para a maioria dos indicadores, a imputação com a média ou mediana pode ser arriscada.
    # Vamos preencher com um valor que indique "dado não coletado" ou "ausência" para evitar distorção,
    # mas para o modelo preditivo, usaremos apenas linhas completas.
    # Para fins de EDA, vamos manter os NaNs por enquanto, mas vamos garantir que os tipos estejam corretos.
    
    # 3. Tratamento de colunas com muitos nulos e que parecem ser redundantes ou específicas de um ano
    # Colunas com mais de 90% de nulos (ex: idade, destaqueipv1, avaliador6, inde2024)
    # Vamos manter apenas as colunas que são relevantes para a análise multidimensional e o modelo preditivo.
    
    # Colunas a serem mantidas para o modelo e EDA
    core_cols = [
        'aluno_id', 'ano', 'gnero', 'fase', 'anoingresso',
        'ida', 'ieg', 'ips', 'ipp', 'iaa', 'ipv', 'ian', 'inde22', 'inde23',
        'mat', 'por', 'ing', 'matem', 'portug', 'ingls', # Notas detalhadas
        'defasagem', 'defas', # Indicadores de defasagem
        'instituiodeensino', 'escola', # Contexto
        'ativoinativo', 'ativoinativo1' # Status do aluno
    ]
    
    # Filtrar apenas as colunas principais
    df_clean = df[df.columns.intersection(core_cols)].copy()
    
    # 4. Criação da variável alvo para o modelo preditivo (Risco de Defasagem)
    # Risco = 1 se IAN < 7.0 (Moderadamente ou Severamente Defasado), 0 caso contrário.
    # O IAN já foi analisado e possui apenas 3 valores discretos (2.5, 5.0, 10.0).
    # Vamos criar a variável alvo com base no IAN.
    df_clean['risco_defasagem'] = np.where(df_clean['ian'] < 7.0, 1, 0)
    
    # 5. Renomear colunas para padronização (se necessário, mas já estão em minúsculas)
    
    # 6. Preenchimento de NaNs em colunas categóricas importantes
    df_clean['fase'] = df_clean['fase'].fillna('NAO_INFORMADO')
    df_clean['gnero'] = df_clean['gnero'].fillna('NAO_INFORMADO')
    
    print(f"Limpeza concluída. DataFrame final com {len(df_clean.columns)} colunas e {len(df_clean)} linhas.")
    
    return df_clean

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    raw_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_clean.csv')
    processed_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_final.csv')
    
    df = load_data(raw_data_path)
    
    if df is not None:
        df_clean = clean_data(df)
        
        # Salva o DataFrame limpo
        df_clean.to_csv(processed_data_path, index=False)
        print(f"\nDados limpos e pré-processados salvos em: {processed_data_path}")
        print(f"Contagem de nulos no DataFrame final (Top 10):\n{df_clean.isnull().sum().sort_values(ascending=False).head(10)}")

if __name__ == "__main__":
    main()
