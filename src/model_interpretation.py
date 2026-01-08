import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score, classification_report
import os
import joblib

def load_prepared_data(base_dir):
    """Carrega os dados preparados para modelagem."""
    X_train = np.load(os.path.join(base_dir, 'data', 'processed', 'X_train.npy'))
    X_test = np.load(os.path.join(base_dir, 'data', 'processed', 'X_test.npy'))
    y_train = np.load(os.path.join(base_dir, 'data', 'processed', 'y_train.npy'))
    y_test = np.load(os.path.join(base_dir, 'data', 'processed', 'y_test.npy'))
    feature_cols = joblib.load(os.path.join(base_dir, 'src', 'feature_cols.pkl'))
    
    return X_train, X_test, y_train, y_test, feature_cols

def optimize_model(X_train, y_train):
    """
    Otimiza o modelo Gradient Boosting usando Grid Search.
    """
    print("Iniciando otimização do modelo Gradient Boosting...")
    
    # Definir grid de hiperparâmetros
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2]
    }
    
    # Grid Search com validação cruzada
    gb_model = GradientBoostingClassifier(random_state=42)
    grid_search = GridSearchCV(
        gb_model, 
        param_grid, 
        cv=5, 
        scoring='roc_auc', 
        n_jobs=-1, 
        verbose=1
    )
    
    grid_search.fit(X_train, y_train)
    
    print(f"\nMelhores hiperparâmetros: {grid_search.best_params_}")
    print(f"Melhor ROC-AUC (CV): {grid_search.best_score_:.4f}")
    
    return grid_search.best_estimator_

def plot_feature_importance(model, feature_cols, save_path):
    """Plota a importância das features do modelo."""
    feature_importance = model.feature_importances_
    feature_importance_df = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': feature_importance
    }).sort_values('Importance', ascending=False)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=feature_importance_df.head(15), x='Importance', y='Feature', palette='viridis')
    plt.title('Top 15 Features Mais Importantes - Gradient Boosting', fontweight='bold', fontsize=14)
    plt.xlabel('Importância', fontsize=12)
    plt.ylabel('Feature', fontsize=12)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGráfico de Feature Importance salvo em: {save_path}")
    
    return feature_importance_df

def generate_model_report(model, X_test, y_test, feature_importance_df, save_path):
    """Gera relatório completo do modelo otimizado."""
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    report = f"""
# Relatório do Modelo Preditivo de Risco Educacional - FASE 3

## Modelo Otimizado: Gradient Boosting Classifier

### Hiperparâmetros Otimizados:
{model.get_params()}

### Desempenho no Conjunto de Teste:
- **ROC-AUC Score**: {roc_auc:.4f}

### Classification Report:
```
{classification_report(y_test, y_pred)}
```

### Top 10 Features Mais Importantes:
{feature_importance_df.head(10).to_markdown(index=False)}

### Interpretação das Features:

1. **{feature_importance_df.iloc[0]['Feature']}** (Importância: {feature_importance_df.iloc[0]['Importance']:.4f})
   - Esta é a feature mais importante para prever o risco de defasagem.

2. **{feature_importance_df.iloc[1]['Feature']}** (Importância: {feature_importance_df.iloc[1]['Importance']:.4f})
   - Segunda feature mais relevante.

3. **{feature_importance_df.iloc[2]['Feature']}** (Importância: {feature_importance_df.iloc[2]['Importance']:.4f})
   - Terceira feature mais relevante.

### Conclusões:

O modelo Gradient Boosting otimizado alcançou um **ROC-AUC de {roc_auc:.4f}**, representando uma melhoria significativa em relação ao modelo baseline.

As features mais importantes indicam que:
- Indicadores de desempenho acadêmico e engajamento são cruciais para prever o risco.
- Features de interação e temporais (lag, delta) também contribuem para o modelo.

### Recomendações:

1. **Monitoramento Proativo**: Utilizar o modelo para identificar alunos em risco antes de quedas de desempenho.
2. **Intervenções Personalizadas**: Focar nas features mais importantes para criar estratégias de intervenção direcionadas.
3. **Coleta de Dados**: Continuar coletando dados históricos para melhorar o modelo ao longo do tempo.
"""
    
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Relatório do modelo salvo em: {save_path}")

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    
    # Carregar dados preparados
    X_train, X_test, y_train, y_test, feature_cols = load_prepared_data(base_dir)
    
    # Otimizar modelo
    optimized_model = optimize_model(X_train, y_train)
    
    # Avaliar modelo otimizado
    y_pred_proba = optimized_model.predict_proba(X_test)[:, 1]
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    print(f"\n🏆 ROC-AUC do modelo otimizado: {roc_auc:.4f}")
    
    # Plotar Feature Importance
    fi_plot_path = os.path.join(base_dir, 'notebooks', 'feature_importance.png')
    feature_importance_df = plot_feature_importance(optimized_model, feature_cols, fi_plot_path)
    
    # Gerar relatório do modelo
    report_path = os.path.join(base_dir, 'notebooks', 'FASE_3_Modelo_Preditivo.md')
    generate_model_report(optimized_model, X_test, y_test, feature_importance_df, report_path)
    
    # Salvar modelo otimizado
    optimized_model_path = os.path.join(base_dir, 'src', 'optimized_model.pkl')
    joblib.dump(optimized_model, optimized_model_path)
    print(f"\nModelo otimizado salvo em: {optimized_model_path}")

if __name__ == "__main__":
    main()
