import pandas as pd
import os

def load_data(file_path):
    """Carrega o DataFrame processado."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
        return None

def initial_eda(df):
    """Realiza a Análise Exploratória de Dados inicial."""
    
    print("\n--- Informações Gerais do DataFrame ---")
    df.info(verbose=False)
    
    print("\n--- Primeiras 5 Linhas ---")
    print(df.head())
    
    print("\n--- Contagem de Valores Nulos (Top 20) ---")
    null_counts = df.isnull().sum().sort_values(ascending=False)
    print(null_counts[null_counts > 0].head(20))
    
    print("\n--- Estatísticas Descritivas das Colunas Numéricas ---")
    print(df.describe().T)
    
    print("\n--- Distribuição da Variável Alvo (IAN) ---")
    # IAN é o indicador de defasagem. Vamos analisar sua distribuição.
    print(df['ian'].value_counts(dropna=False).head(10))
    
    print("\n--- Distribuição de Gênero ---")
    print(df['gnero'].value_counts(dropna=False))
    
    print("\n--- Distribuição de Fase (Fase do Aluno) ---")
    print(df['fase'].value_counts(dropna=False).head(10))
    
    # Salvar informações em um arquivo de texto para documentação
    with open(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'eda_initial_report.txt'), 'w', encoding='utf-8') as f:
        f.write("--- Relatório Inicial de EDA ---\n\n")
        
        f.write("Informações Gerais:\n")
        df.info(buf=f, verbose=False)
        f.write("\n\n")
        
        f.write("Contagem de Valores Nulos (Top 20):\n")
        null_counts.head(20).to_string(f)
        f.write("\n\n")
        
        f.write("Estatísticas Descritivas das Colunas Numéricas:\n")
        df.describe().T.to_string(f)
        f.write("\n\n")
        
        f.write("Distribuição da Variável Alvo (IAN):\n")
        df['ian'].value_counts(dropna=False).head(10).to_string(f)
        f.write("\n\n")
        
        f.write("Distribuição de Gênero:\n")
        df['gnero'].value_counts(dropna=False).to_string(f)
        f.write("\n\n")
        
        f.write("Distribuição de Fase:\n")
        df['fase'].value_counts(dropna=False).head(10).to_string(f)
        f.write("\n\n")

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    processed_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_clean.csv')
    
    df = load_data(processed_data_path)
    
    if df is not None:
        initial_eda(df)
        print("\nRelatório inicial de EDA salvo em notebooks/eda_initial_report.txt")

if __name__ == "__main__":
    main()
