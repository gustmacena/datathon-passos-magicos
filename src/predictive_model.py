import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, roc_curve
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
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

def prepare_data_for_ml(df):
    """
    Prepara os dados para o modelo de Machine Learning.
    Define a variável alvo e seleciona as features.
    """
    # 1. Definir a Variável Alvo: Risco de Defasagem
    # Risco = 1 se IAN < 7.0 (Moderadamente ou Severamente Defasado), 0 caso contrário.
    # Usaremos o IAN do ano atual para prever o risco.
    df['Risco_Defasagem'] = np.where(df['ian'] < 7.0, 1, 0)
    
    # 2. Seleção de Features
    # Focaremos nos indicadores principais e nos que mostraram correlação na EDA.
    # Features: IDA, IEG, IPS, IPP, IAA, Ano
    features = ['ida', 'ieg', 'ips', 'ipp', 'iaa', 'ano']
    
    # 3. Filtrar dados completos para o modelo
    model_df = df.dropna(subset=features + ['Risco_Defasagem']).copy()
    
    # 4. Separar X e y
    X = model_df[features]
    y = model_df['Risco_Defasagem']
    
    # 5. Tratar variáveis categóricas (se houver, mas as selecionadas são numéricas)
    # 6. Normalização/Escalonamento
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, features, scaler

def train_and_evaluate_model(X, y, features):
    """
    Treina um modelo de Regressão Logística (interpretabilidade) e avalia.
    """
    # Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    # Treinamento do modelo (Regressão Logística para interpretabilidade)
    model = LogisticRegression(solver='liblinear', random_state=42)
    model.fit(X_train, y_train)
    
    # Previsões
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
    # Avaliação
    report = classification_report(y_test, y_pred, target_names=['Baixo Risco', 'Alto Risco'], output_dict=True)
    auc_score = roc_auc_score(y_test, y_proba)
    
    print("\n--- Relatório de Classificação (Regressão Logística) ---")
    print(classification_report(y_test, y_pred, target_names=['Baixo Risco', 'Alto Risco']))
    print(f"AUC Score: {auc_score:.4f}")
    
    # Interpretabilidade: Coeficientes
    coefficients = pd.DataFrame({
        'Feature': features,
        'Coefficient': model.coef_[0]
    }).sort_values(by='Coefficient', ascending=False)
    
    print("\n--- Interpretabilidade: Coeficientes do Modelo (Impacto no Risco) ---")
    print(coefficients.to_markdown(index=False))
    
    # Plot da Curva ROC
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'AUC = {auc_score:.4f}')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlabel('Taxa de Falsos Positivos (FPR)')
    plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
    plt.title('Curva ROC - Modelo de Risco de Defasagem')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.savefig(os.path.join(os.path.dirname(__file__), '..', 'notebooks', 'roc_curve.png'))
    plt.close()
    
    return model, report, auc_score, coefficients

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    processed_data_path = os.path.join(base_dir, 'data', 'processed', 'pedagogy_data_clean.csv')
    
    df = load_data(processed_data_path)
    
    if df is not None:
        X, y, features, scaler = prepare_data_for_ml(df)
        
        print(f"Tamanho do dataset para ML: {X.shape[0]} amostras.")
        print(f"Distribuição da Variável Alvo:\n{y.value_counts(normalize=True).mul(100).round(2)}")
        
        model, report, auc_score, coefficients = train_and_evaluate_model(X, y, features)
        
        # Salvar o modelo e o scaler para uso futuro (Streamlit)
        import joblib
        joblib.dump(model, os.path.join(base_dir, 'src', 'logistic_model.pkl'))
        joblib.dump(scaler, os.path.join(base_dir, 'src', 'scaler.pkl'))
        print("\nModelo e Scaler salvos com sucesso.")
        
        # Salvar os resultados do modelo em um arquivo de texto
        with open(os.path.join(base_dir, 'notebooks', 'model_results.txt'), 'w', encoding='utf-8') as f:
            f.write("--- Resultados do Modelo Preditivo de Risco de Defasagem ---\n\n")
            f.write("Modelo: Regressão Logística (Interpretabilidade)\n")
            f.write("Variável Alvo: Risco de Defasagem (1 se IAN < 7.0, 0 caso contrário)\n\n")
            
            f.write("Relatório de Classificação:\n")
            f.write(pd.DataFrame(report).transpose().to_markdown(numalign="left", stralign="left"))
            f.write(f"\n\nAUC Score: {auc_score:.4f}\n\n")
            
            f.write("Interpretabilidade: Coeficientes do Modelo (Impacto no Risco):\n")
            f.write(coefficients.to_markdown(index=False))
            f.write("\n\n")
            f.write("Observação: Coeficientes negativos indicam que o aumento da feature DIMINUI o risco de defasagem. Coeficientes positivos AUMENTAM o risco.\n")

if __name__ == "__main__":
    main()
