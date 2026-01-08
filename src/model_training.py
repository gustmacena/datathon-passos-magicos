import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

def load_prepared_data(base_dir):
    """Carrega os dados preparados para modelagem."""
    X_train = np.load(os.path.join(base_dir, 'data', 'processed', 'X_train.npy'))
    X_test = np.load(os.path.join(base_dir, 'data', 'processed', 'X_test.npy'))
    y_train = np.load(os.path.join(base_dir, 'data', 'processed', 'y_train.npy'))
    y_test = np.load(os.path.join(base_dir, 'data', 'processed', 'y_test.npy'))
    
    return X_train, X_test, y_train, y_test

def train_and_evaluate_models(X_train, X_test, y_train, y_test):
    """
    Treina e avalia múltiplos modelos de Machine Learning.
    """
    print("Iniciando treinamento de modelos...")
    
    # Definir modelos
    models = {
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42, max_depth=5)
    }
    
    results = []
    
    for name, model in models.items():
        print(f"\n--- Treinando {name} ---")
        
        # Treinar modelo
        model.fit(X_train, y_train)
        
        # Predições
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        # Métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        print(f"Acurácia: {accuracy:.4f}")
        print(f"Precisão: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
        print(f"ROC-AUC: {roc_auc:.4f}")
        
        results.append({
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1-Score': f1,
            'ROC-AUC': roc_auc
        })
    
    # Criar DataFrame com resultados
    results_df = pd.DataFrame(results)
    
    return results_df, models

def plot_model_comparison(results_df, save_path):
    """Plota comparação de desempenho dos modelos."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Comparação de Desempenho dos Modelos', fontsize=16, fontweight='bold')
    
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
    
    for idx, metric in enumerate(metrics):
        row = idx // 3
        col = idx % 3
        ax = axes[row, col]
        
        sns.barplot(data=results_df, x='Model', y=metric, ax=ax, palette='viridis')
        ax.set_title(f'{metric}', fontweight='bold')
        ax.set_xlabel('')
        ax.set_ylabel(metric)
        ax.set_ylim(0, 1)
        ax.tick_params(axis='x', rotation=45)
        
        # Adicionar valores nas barras
        for container in ax.containers:
            ax.bar_label(container, fmt='%.3f')
    
    # Remover o último subplot vazio
    fig.delaxes(axes[1, 2])
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"\nGráfico de comparação salvo em: {save_path}")

def plot_confusion_matrix(y_test, y_pred, model_name, save_path):
    """Plota matriz de confusão."""
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True)
    plt.title(f'Matriz de Confusão - {model_name}', fontweight='bold')
    plt.xlabel('Predito')
    plt.ylabel('Real')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Matriz de confusão salva em: {save_path}")

def main():
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    
    # Carregar dados preparados
    X_train, X_test, y_train, y_test = load_prepared_data(base_dir)
    
    # Treinar e avaliar modelos
    results_df, models = train_and_evaluate_models(X_train, X_test, y_train, y_test)
    
    # Salvar resultados
    results_path = os.path.join(base_dir, 'notebooks', 'model_comparison_results.csv')
    results_df.to_csv(results_path, index=False)
    print(f"\nResultados salvos em: {results_path}")
    
    # Plotar comparação de modelos
    comparison_plot_path = os.path.join(base_dir, 'notebooks', 'model_comparison.png')
    plot_model_comparison(results_df, comparison_plot_path)
    
    # Identificar o melhor modelo (baseado em ROC-AUC)
    best_model_name = results_df.loc[results_df['ROC-AUC'].idxmax(), 'Model']
    best_model = models[best_model_name]
    
    print(f"\n🏆 Melhor modelo: {best_model_name} (ROC-AUC: {results_df['ROC-AUC'].max():.4f})")
    
    # Plotar matriz de confusão do melhor modelo
    y_pred_best = best_model.predict(X_test)
    cm_path = os.path.join(base_dir, 'notebooks', f'confusion_matrix_{best_model_name.replace(" ", "_")}.png')
    plot_confusion_matrix(y_test, y_pred_best, best_model_name, cm_path)
    
    # Salvar o melhor modelo
    best_model_path = os.path.join(base_dir, 'src', 'best_model.pkl')
    joblib.dump(best_model, best_model_path)
    print(f"\nMelhor modelo salvo em: {best_model_path}")

if __name__ == "__main__":
    main()
