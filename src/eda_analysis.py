import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuração para evitar problemas com caracteres especiais no Matplotlib
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']

def load_processed_data(file_path):
    """Carrega o DataFrame processado."""
    try:
        df = pd.read_csv(file_path)
        print(f"Dados carregados com sucesso. Total de linhas: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
        return None

def analyze_ian(df):
    """
    1. Adequação do nível (IAN): Qual é o perfil geral de defasagem dos
    alunos (IAN) e como ele evolui ao longo do ano?
    """
    print("\n--- Análise do Indicador de Adequação do Nível (IAN) ---")
    
    ian_data = df[['ano', 'ian']].dropna()
    
    # Estatísticas descritivas
    print("\nEstatísticas Descritivas do IAN:")
    print(ian_data.groupby('ano')['ian'].describe())
    
    # Definir categorias de defasagem (exemplo hipotético, pode ser ajustado com base no dicionário de dados real)
    # Assumindo que IAN é uma métrica de 0 a 10.
    bins = [0, 5.0, 7.0, 10.0]
    labels = ['Severamente Defasado (<5.0)', 'Moderadamente Defasado (5.0-7.0)', 'Adequado (>7.0)']
    ian_data['Categoria_IAN'] = pd.cut(ian_data['ian'], bins=bins, labels=labels, right=False)
    
    ian_profile = ian_data.groupby(['ano', 'Categoria_IAN']).size().unstack(fill_value=0)
    ian_profile_percent = ian_profile.apply(lambda x: x / x.sum() * 100, axis=1)
    
    print("\nPerfil de Defasagem (IAN) por Ano (%):")
    print(ian_profile_percent.round(2))
    
    # Visualização
    plt.figure(figsize=(10, 6))
    ian_profile_percent.plot(kind='bar', stacked=True)
    plt.title('Evolução do Perfil de Defasagem (IAN) ao Longo dos Anos')
    plt.xlabel('Ano')
    plt.ylabel('Percentual de Alunos')
    plt.xticks(rotation=0)
    plt.legend(title='Categoria IAN')
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ian_evolution.png'))
    plt.close()
    
    return ian_profile_percent

def analyze_ida(df):
    """
    2. Desempenho acadêmico (IDA): O desempenho acadêmico médio
    (IDA) está melhorando, estagnado ou caindo ao longo das fases e anos?
    """
    print("\n--- Análise do Indicador de Desempenho Acadêmico (IDA) ---")
    
    ida_data = df[['ano', 'ida', 'fase']].dropna(subset=['ida', 'fase'])
    
    # IDA médio por ano
    ida_mean_year = ida_data.groupby('ano')['ida'].mean().reset_index()
    
    # IDA médio por fase e ano
    ida_mean_phase_year = ida_data.groupby(['ano', 'fase'])['ida'].mean().unstack()
    
    # Visualização da evolução do IDA
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=ida_mean_year, x='ano', y='ida', marker='o')
    plt.title('Evolução do IDA Médio ao Longo dos Anos')
    plt.xlabel('Ano')
    plt.ylabel('IDA Médio')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ida_evolution_year.png'))
    plt.close()
    
    # Visualização da evolução do IDA por fase
    plt.figure(figsize=(12, 7))
    ida_mean_phase_year.T.plot(kind='line', marker='o')
    plt.title('Evolução do IDA Médio por Fase ao Longo dos Anos')
    plt.xlabel('Ano')
    plt.ylabel('IDA Médio')
    plt.xticks(ida_mean_phase_year.index)
    plt.legend(title='Fase', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ida_evolution_phase.png'))
    plt.close()
    
    return ida_mean_year, ida_mean_phase_year

def analyze_ieg_ida_ipv(df):
    """
    3. Engajamento nas atividades (IEG): O grau de engajamento dos
    alunos (IEG) tem relação direta com seus indicadores de desempenho (IDA) e
    do ponto de virada (IPV)?
    """
    print("\n--- Análise da Relação entre IEG, IDA e IPV ---")
    
    corr_data = df[['ieg', 'ida', 'ipv']].dropna()
    correlation_matrix = corr_data.corr()
    
    # Visualização da correlação (Heatmap)
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de Correlação entre IEG, IDA e IPV')
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ieg_ida_ipv_heatmap.png'))
    plt.close()
    
    return correlation_matrix

def analyze_iaa_ida_ieg(df):
    """
    4. Autoavaliação (IAA): As percepções dos alunos sobre si mesmos
    (IAA) são coerentes com seu desempenho real (IDA) e engajamento (IEG)?
    """
    print("\n--- Análise da Coerência entre IAA, IDA e IEG ---")
    
    corr_data = df[['iaa', 'ida', 'ieg']].dropna()
    correlation_matrix = corr_data.corr()
    
    print("\nMatriz de Correlação entre IAA, IDA e IEG:")
    print(correlation_matrix.round(3))
    
    # Visualização da correlação (Heatmap)
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de Correlação entre IAA, IDA e IEG')
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'iaa_ida_ieg_heatmap.png'))
    plt.close()
    
    return correlation_matrix

def analyze_ips_performance(df):
    """
    5. Aspectos psicossociais (IPS): Há padrões psicossociais (IPS) que
    antecedem quedas de desempenho acadêmico ou de engajamento?
    """
    print("\n--- Análise de IPS e Quedas de Desempenho/Engajamento ---")
    
    # Para esta análise, precisamos de dados de IPS de um ano e IDA/IEG do ano seguinte.
    # Como o dataset está unificado, vamos criar um DataFrame com os dados do ano anterior.
    
    # Renomear colunas para o ano atual
    current_cols = ['aluno_id', 'ano', 'ida', 'ieg']
    df_current = df[current_cols].copy()
    
    # Renomear colunas para o ano anterior (IPS)
    prev_cols = ['aluno_id', 'ano', 'ips']
    df_prev = df[prev_cols].copy()
    df_prev['ano'] = df_prev['ano'] + 1
    df_prev = df_prev.rename(columns={'ips': 'ips_prev'})
    
    # Merge dos dados
    merged_df = pd.merge(df_current, df_prev, on=['aluno_id', 'ano'], how='inner').dropna()
    
    # Correlação entre IPS do ano anterior e IDA/IEG do ano atual
    correlation_matrix = merged_df[['ips_prev', 'ida', 'ieg']].corr()
    
    print("\nMatriz de Correlação: IPS (Ano Anterior) vs IDA/IEG (Ano Atual):")
    print(correlation_matrix.round(3))
    
    # Visualização da correlação (Heatmap)
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('IPS (Ano Anterior) vs IDA/IEG (Ano Atual)')
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ips_lag_correlation_heatmap.png'))
    plt.close()
    
    return correlation_matrix

def analyze_ipp_ian(df):
    """
    6. Aspectos psicopedagógicos (IPP): As avaliações psicopedagógicas
    (IPP) confirmam ou contradizem a defasagem identificada pelo IAN?
    """
    print("\n--- Análise da Coerência entre IPP e IAN ---")
    
    # Filtrar colunas relevantes e remover NaNs para esta análise
    corr_data = df[['ipp', 'ian']].dropna()
    
    # Correlação
    correlation = corr_data['ipp'].corr(corr_data['ian'])
    
    print(f"\nCorrelação entre IPP e IAN: {correlation:.3f}")
    
    # Visualização (Scatter plot)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=corr_data, x='ian', y='ipp')
    plt.title(f'Relação entre IAN e IPP (Correlação: {correlation:.2f})')
    plt.xlabel('IAN (Indicador de Adequação do Nível)')
    plt.ylabel('IPP (Aspectos Psicopedagógicos)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ipp_ian_correlation.png'))
    plt.close()
    
    return correlation

def analyze_ipv_influencers(df):
    """
    7. Ponto de virada (IPV): Quais comportamentos - acadêmicos,
    emocionais ou de engajamento - mais influenciam o IPV ao longo do tempo?
    """
    print("\n--- Análise dos Influenciadores do Ponto de Virada (IPV) ---")
    
    # Vamos analisar a correlação do IPV com os indicadores: IDA (acadêmico), IEG (engajamento) e IPS (emocional/psicossocial).
    # Já temos a correlação com IDA e IEG da pergunta 3. Vamos incluir IPS.
    
    corr_data = df[['ipv', 'ida', 'ieg', 'ips']].dropna()
    correlation_matrix = corr_data.corr()
    
    # Correlação do IPV com os outros indicadores
    ipv_correlations = correlation_matrix.loc['ipv', ['ida', 'ieg', 'ips']].sort_values(ascending=False)
    
    print("\nCorrelação do IPV com Indicadores (IDA, IEG, IPS):")
    print(ipv_correlations.round(3))
    
    # Visualização (Bar plot)
    plt.figure(figsize=(8, 6))
    ipv_correlations.plot(kind='bar', color=['skyblue', 'lightcoral', 'lightgreen'])
    plt.title('Influência dos Indicadores no Ponto de Virada (IPV)')
    plt.ylabel('Correlação com IPV')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'ipv_influencers_bar.png'))
    plt.close()
    
    return ipv_correlations

def analyze_multidimensionality(df):
    """
    8. Multidimensionalidade dos indicadores: Quais combinações de
    indicadores (IDA + IEG + IPS + IPP) melhor explicam o desempenho global do
    aluno (INDE)?
    """
    print("\n--- Análise da Multidimensionalidade (INDE) ---")
    
    # Vamos usar Regressão Linear Múltipla para ver a contribuição de cada indicador para o INDE.
    # Para simplificar a EDA, vamos analisar a correlação de cada indicador com o INDE.
    
    # Colunas de interesse
    cols = ['inde22', 'ida', 'ieg', 'ips', 'ipp']
    corr_data = df[cols].dropna()
    
    # Correlação com INDE
    inde_correlations = corr_data.corr().loc['inde22', ['ida', 'ieg', 'ips', 'ipp']].sort_values(ascending=False)
    
    print("\nCorrelação dos Indicadores com o Desempenho Global (INDE):")
    print(inde_correlations.round(3))
    
    # Visualização (Bar plot)
    plt.figure(figsize=(8, 6))
    inde_correlations.plot(kind='bar', color='gold')
    plt.title('Correlação dos Indicadores com o Desempenho Global (INDE)')
    plt.ylabel('Correlação com INDE')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'inde_influencers_bar.png'))
    plt.close()
    
    return inde_correlations

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    processed_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_clean.csv')
    
    df = load_processed_data(processed_data_path)
    
    if df is not None:
        # 1. Análise do IAN
        ian_results = analyze_ian(df)
        
        # 2. Análise do IDA
        ida_results_year, ida_results_phase = analyze_ida(df)
        
        # 3. Análise da Correlação IEG, IDA, IPV
        corr_ieg_ida_ipv = analyze_ieg_ida_ipv(df)
        
        # 4. Análise da Coerência IAA, IDA, IEG
        corr_iaa_ida_ieg = analyze_iaa_ida_ieg(df)
        
        # 5. Análise de IPS e Quedas de Desempenho/Engajamento
        corr_ips_lag = analyze_ips_performance(df)
        
        # 6. Análise da Coerência IPP e IAN
        corr_ipp_ian = analyze_ipp_ian(df)
        
        # 7. Análise dos Influenciadores do Ponto de Virada (IPV)
        ipv_influencers = analyze_ipv_influencers(df)
        
        # 8. Análise da Multidimensionalidade (INDE)
        inde_influencers = analyze_multidimensionality(df)
        
        # Salvando os insights em um arquivo de texto para o relatório
        with open(os.path.join(base_dir, 'notebooks', 'eda_insights_full.txt'), 'w', encoding='utf-8') as f:
            f.write("--- Insights da Análise Exploratória de Dados (EDA) - Respostas às Perguntas de Negócio ---\n\n")
            
            f.write("1. Adequação do Nível (IAN):\n")
            f.write("Estatísticas Descritivas do IAN:\n")
            f.write(ian_results.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("2. Desempenho Acadêmico (IDA):\n")
            f.write("IDA Médio por Ano:\n")
            f.write(ida_results_year.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            f.write("IDA Médio por Fase e Ano:\n")
            f.write(ida_results_phase.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("3. Engajamento (IEG) vs Desempenho (IDA) e Ponto de Virada (IPV):\n")
            f.write("Matriz de Correlação:\n")
            f.write(corr_ieg_ida_ipv.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("4. Autoavaliação (IAA) vs Desempenho (IDA) e Engajamento (IEG):\n")
            f.write("Matriz de Correlação:\n")
            f.write(corr_iaa_ida_ieg.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("5. Aspectos Psicossociais (IPS) e Quedas de Desempenho/Engajamento (Lagged):\n")
            f.write("Matriz de Correlação: IPS (Ano Anterior) vs IDA/IEG (Ano Atual):\n")
            f.write(corr_ips_lag.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("6. Aspectos Psicopedagógicos (IPP) vs Defasagem (IAN):\n")
            f.write(f"Correlação entre IPP e IAN: {corr_ipp_ian:.3f}\n\n")
            
            f.write("7. Influenciadores do Ponto de Virada (IPV):\n")
            f.write("Correlação do IPV com Indicadores (IDA, IEG, IPS):\n")
            f.write(ipv_influencers.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("8. Multidimensionalidade (INDE):\n")
            f.write("Correlação dos Indicadores (IDA, IEG, IPS, IPP) com o Desempenho Global (INDE):\n")
            f.write(inde_influencers.to_markdown(numalign="left", stralign="left"))
            f.write("\n\n")
            
            f.write("\n\n--- Próximos Passos ---\n")
            f.write("Iniciar o desenvolvimento do Modelo Preditivo de Risco Educacional (pergunta 9).\n")

if __name__ == "__main__":
    main()
