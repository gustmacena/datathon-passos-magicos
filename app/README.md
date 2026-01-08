# Aplicação Streamlit - Predição de Risco Educacional

Esta aplicação permite que a equipe da Passos Mágicos utilize o modelo de Machine Learning treinado para prever o risco de defasagem de um aluno em tempo real.

## Como Executar

1.  **Instale as dependências:**

    ```bash
    pip install streamlit pandas numpy scikit-learn joblib matplotlib seaborn
    ```

2.  **Execute a aplicação:**

    ```bash
    streamlit run app/app_streamlit.py
    ```

## Funcionalidades

-   **Interface Intuitiva**: Sidebar com sliders para entrada dos indicadores do aluno.
-   **Predição em Tempo Real**: Botão para prever o risco de defasagem.
-   **Visualização de Resultados**: Classificação, probabilidade de risco e gráfico de distribuição.
-   **Recomendações Personalizadas**: Sugestões de intervenção baseadas no resultado.
-   **Análise Detalhada**: Tabela com status de cada indicador.
-   **Informações sobre o Modelo**: Detalhes técnicos do modelo de Gradient Boosting.
