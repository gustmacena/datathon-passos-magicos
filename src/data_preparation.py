import pandas as pd
import os

def load_and_clean_data(file_path):
    """
    Carrega as abas do arquivo Excel, unifica os dados e realiza a limpeza inicial.
    """
    print(f"Carregando dados de: {file_path}")
    
    # Mapeamento das abas e seus respectivos anos
    sheet_to_year = {
        'PEDE2022': 2022,
        'PEDE2023': 2023,
        'PEDE2024': 2024
    }
    
    all_data = []
    
    for sheet_name, year in sheet_to_year.items():
        try:
            # Leitura da aba
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            
            # Adiciona a coluna 'Ano'
            df['Ano'] = year
            
            # Padroniza nomes de colunas para minúsculas e substitui caracteres especiais
            df.columns = df.columns.str.lower().str.replace('[^a-zA-Z0-9_]', '', regex=True)
            
            # Renomeia colunas com nomes muito parecidos (ex: Pedra 20, Pedra 21, Pedra 22)
            # A coluna 'Pedra' deve ser a fase do aluno no ano em questão.
            if f'pedra{year}' in df.columns:
                df = df.rename(columns={f'pedra{year}': 'fase_pedra_ano'})
            
            all_data.append(df)
            print(f"Aba '{sheet_name}' ({year}) carregada com {len(df)} linhas.")
            
        except ValueError as e:
            print(f"Aba '{sheet_name}' não encontrada ou erro de leitura: {e}")
            
    if not all_data:
        print("Nenhuma aba de dados foi carregada com sucesso.")
        return None
        
    # Concatena todos os DataFrames
    combined_df = pd.concat(all_data, ignore_index=True)
    print(f"Total de linhas após concatenação: {len(combined_df)}")
    
    # Limpeza adicional:
    # 1. Colunas de texto com espaços em branco (strip)
    for col in combined_df.select_dtypes(include=['object']).columns:
        combined_df[col] = combined_df[col].str.strip()
        
    # 2. Preenchimento de valores nulos em colunas numéricas (por enquanto, com 0 ou média, dependendo do contexto)
    # Para colunas de indicadores (IDA, IAN, IEG, IPS, IPP, IPV, INDE), vamos preencher com a média ou um valor que indique ausência de dado (NaN).
    # Por enquanto, vamos manter NaN para análise posterior.
    
    # 3. Remoção de linhas completamente vazias (se houver)
    combined_df.dropna(how='all', inplace=True)
    
    # 4. Criação de uma coluna de ID única para o aluno (se 'ra' for o identificador)
    if 'ra' in combined_df.columns:
        combined_df['aluno_id'] = combined_df['ra']
    
    return combined_df

if __name__ == "__main__":
    # Define o caminho para o arquivo de dados
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    raw_data_path = os.path.join(base_dir, 'data', 'raw', 'BASE DE DADOS PEDE 2024 - DATATHON.xlsx')
    processed_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_clean.csv')
    
    # Garante que o diretório de saída existe
    os.makedirs(os.path.join(base_dir, 'data', 'processed'), exist_ok=True)
    
    # Carrega e limpa os dados
    clean_df = load_and_clean_data(raw_data_path)
    
    if clean_df is not None:
        # Salva o DataFrame limpo
        clean_df.to_csv(processed_data_path, index=False)
        print(f"\nDados limpos salvos em: {processed_data_path}")
        print(f"Colunas do DataFrame final: {clean_df.columns.tolist()}")
        print(f"Primeiras 5 linhas do DataFrame final:\n{clean_df.head()}")
    else:
        print("Falha ao processar os dados.")
