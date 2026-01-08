import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def load_data(file_path):
    """Carrega o DataFrame processado."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
        return None

def feature_engineering(df):
    """
    Realiza feature engineering avançado para melhorar o modelo preditivo.
    """
    print("Iniciando feature engineering...")
    
    df_fe = df.copy()
    
    # 1. Criar features de interação
    # Interação entre IDA e IEG (desempenho e engajamento)
    df_fe['ida_ieg_interaction'] = df_fe['ida'] * df_fe['ieg']
    
    # Interação entre IPP e IPS (psicopedagógico e psicossocial)
    df_fe['ipp_ips_interaction'] = df_fe['ipp'] * df_fe['ips']
    
    # 2. Criar features de razão
    # Razão entre IDA e IEG (desempenho relativo ao engajamento)
    df_fe['ida_ieg_ratio'] = df_fe['ida'] / (df_fe['ieg'] + 0.001)  # Evitar divisão por zero
    
    # 3. Criar features agregadas (média de indicadores)
    df_fe['mean_indicators'] = df_fe[['ida', 'ieg', 'ips', 'ipp', 'iaa', 'ipv']].mean(axis=1, skipna=True)
    
    # 4. Criar features de defasagem temporal (se houver dados de anos anteriores)
    # Ordenar por aluno_id e ano
    df_fe = df_fe.sort_values(['aluno_id', 'ano'])
    
    # Criar lag features (valores do ano anterior)
    df_fe['ida_lag1'] = df_fe.groupby('aluno_id')['ida'].shift(1)
    df_fe['ieg_lag1'] = df_fe.groupby('aluno_id')['ieg'].shift(1)
    df_fe['ips_lag1'] = df_fe.groupby('aluno_id')['ips'].shift(1)
    
    # 5. Criar features de variação (delta entre anos)
    df_fe['ida_delta'] = df_fe['ida'] - df_fe['ida_lag1']
    df_fe['ieg_delta'] = df_fe['ieg'] - df_fe['ieg_lag1']
    
    # 6. Encoding de variáveis categóricas
    # Gênero
    le_genero = LabelEncoder()
    df_fe['gnero_encoded'] = le_genero.fit_transform(df_fe['gnero'].fillna('NAO_INFORMADO'))
    
    # Fase
    le_fase = LabelEncoder()
    df_fe['fase_encoded'] = le_fase.fit_transform(df_fe['fase'].fillna('NAO_INFORMADO'))
    
    print(f"Feature engineering concluído. Total de features: {len(df_fe.columns)}")
    
    return df_fe

def prepare_model_data(df):
    """
    Prepara os dados para modelagem, selecionando features e criando train/test split.
    """
    print("Preparando dados para modelagem...")
    
    # Selecionar features para o modelo
    feature_cols = [
        'ida', 'ieg', 'ips', 'ipp', 'iaa', 'ipv',
        'ida_ieg_interaction', 'ipp_ips_interaction', 'ida_ieg_ratio',
        'mean_indicators', 'ida_lag1', 'ieg_lag1', 'ips_lag1',
        'ida_delta', 'ieg_delta', 'gnero_encoded', 'fase_encoded', 'ano'
    ]
    
    # Variável alvo
    target_col = 'risco_defasagem'
    
    # Filtrar apenas linhas com target válido
    df_model = df[df[target_col].notna()].copy()
    
    # Remover linhas com muitos NaNs nas features principais
    df_model = df_model.dropna(subset=['ida', 'ieg', 'ipp', 'iaa', 'ipv'], thresh=4)
    
    # Preencher NaNs restantes com a mediana
    for col in feature_cols:
        if col in df_model.columns:
            df_model[col] = df_model[col].fillna(df_model[col].median())
    
    # Separar features e target
    X = df_model[feature_cols]
    y = df_model[target_col]
    
    # Split treino/teste (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Normalização
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"Dados preparados:")
    print(f"  - Treino: {X_train.shape[0]} amostras")
    print(f"  - Teste: {X_test.shape[0]} amostras")
    print(f"  - Features: {X_train.shape[1]}")
    print(f"  - Distribuição do target (treino): {y_train.value_counts().to_dict()}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, feature_cols

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    processed_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_final.csv')
    
    df = load_data(processed_data_path)
    
    if df is not None:
        # Feature Engineering
        df_fe = feature_engineering(df)
        
        # Salvar DataFrame com features
        fe_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_fe.csv')
        df_fe.to_csv(fe_data_path, index=False)
        print(f"\nDataFrame com feature engineering salvo em: {fe_data_path}")
        
        # Preparar dados para modelagem
        X_train, X_test, y_train, y_test, scaler, feature_cols = prepare_model_data(df_fe)
        
        # Salvar dados preparados
        np.save(os.path.join(base_dir, 'data', 'processed', 'X_train.npy'), X_train)
        np.save(os.path.join(base_dir, 'data', 'processed', 'X_test.npy'), X_test)
        np.save(os.path.join(base_dir, 'data', 'processed', 'y_train.npy'), y_train)
        np.save(os.path.join(base_dir, 'data', 'processed', 'y_test.npy'), y_test)
        
        # Salvar scaler e feature_cols
        import joblib
        joblib.dump(scaler, os.path.join(base_dir, 'src', 'scaler_v2.pkl'))
        joblib.dump(feature_cols, os.path.join(base_dir, 'src', 'feature_cols.pkl'))
        
        print("\nDados preparados e salvos com sucesso!")

if __name__ == "__main__":
    main()
