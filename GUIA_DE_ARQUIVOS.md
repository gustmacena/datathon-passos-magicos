# Guia Completo de Arquivos do Repositório

Este documento explica **o que é** e **para que serve** cada arquivo do repositório GitHub do projeto Datathon Passos Mágicos.

---

## 📁 Estrutura Geral do Repositório

```
datathon-passos-magicos/
├── 📄 Arquivos de Documentação (Raiz)
├── 📂 app/ - Aplicação Streamlit
├── 📂 data/ - Datasets (não versionados no GitHub)
├── 📂 models/ - Modelos treinados
├── 📂 notebooks/ - Análises e visualizações
├── 📂 presentation/ - Apresentação final
└── 📂 src/ - Scripts Python
```

---

## 🔴 ARQUIVOS ESSENCIAIS (Obrigatórios)

Estes são os arquivos **críticos** para o funcionamento do projeto. Sem eles, a aplicação não funciona.

### 1. **requirements.txt** ⭐⭐⭐
**O que é:** Lista de todas as bibliotecas Python necessárias para rodar o projeto.

**Para que serve:** O Streamlit Cloud e qualquer desenvolvedor usam este arquivo para instalar as dependências automaticamente.

**Conteúdo:**
```
streamlit>=1.31.0
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
joblib>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0
openpyxl>=3.1.0
```

**Importância:** 🔴 **CRÍTICO** - Sem ele, a aplicação não instala as bibliotecas e não funciona.

---

### 2. **app/app_streamlit.py** ⭐⭐⭐
**O que é:** Código-fonte principal da aplicação web Streamlit.

**Para que serve:** É a interface que os educadores usam para fazer predições de risco. Contém toda a lógica de carregamento do modelo, entrada de dados e exibição de resultados.

**Principais Funções:**
- Carrega o modelo treinado (`gradient_boosting_model.pkl`)
- Cria a interface com sliders para entrada de dados
- Faz a predição de risco em tempo real
- Exibe resultados com gráficos e recomendações

**Importância:** 🔴 **CRÍTICO** - É o coração da aplicação web.

---

### 3. **models/gradient_boosting_model.pkl** ⭐⭐⭐
**O que é:** Arquivo binário contendo o modelo de Machine Learning treinado.

**Para que serve:** É o "cérebro" da aplicação. Contém todos os pesos e parâmetros do algoritmo Gradient Boosting que faz as predições.

**Tamanho:** ~1.2 MB

**Importância:** 🔴 **CRÍTICO** - Sem ele, a aplicação não consegue fazer predições.

---

### 4. **models/scaler.pkl** ⭐⭐⭐
**O que é:** Arquivo binário contendo o "normalizador" de dados.

**Para que serve:** Transforma os valores de entrada (IDA, IEG, etc.) para a mesma escala usada no treinamento. Isso garante que o modelo funcione corretamente.

**Importância:** 🔴 **CRÍTICO** - Sem ele, as predições ficam incorretas.

---

### 5. **models/feature_cols.pkl** ⭐⭐⭐
**O que é:** Arquivo binário contendo a lista de features (variáveis) usadas pelo modelo.

**Para que serve:** Garante que os dados de entrada sejam organizados na mesma ordem que o modelo espera.

**Importância:** 🔴 **CRÍTICO** - Sem ele, o modelo não sabe quais variáveis usar.

---

### 6. **.streamlit/config.toml** ⭐⭐
**O que é:** Arquivo de configuração do tema da aplicação Streamlit.

**Para que serve:** Define as cores, fontes e aparência da aplicação (modo dark).

**Conteúdo:**
```toml
[theme]
base = "dark"
primaryColor = "#FF4D00"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
```

**Importância:** 🟡 **IMPORTANTE** - Sem ele, a aplicação fica com tema padrão (branco).

---

## 🟢 ARQUIVOS PRINCIPAIS (Importantes para Entendimento)

Estes arquivos são essenciais para entender o projeto, mas não são necessários para a aplicação funcionar.

### 7. **README.md** ⭐⭐
**O que é:** Documento de apresentação do projeto no GitHub.

**Para que serve:** É a "porta de entrada" do repositório. Explica o que é o projeto, como usar, e fornece links importantes.

**Importância:** 🟢 **IMPORTANTE** - Primeira impressão do projeto no GitHub.

---

### 8. **notebooks/Datathon_Passos_Magicos_Completo.ipynb** ⭐⭐⭐
**O que é:** Jupyter Notebook consolidado com todo o pipeline de análise.

**Para que serve:** Contém todo o código de análise de dados, desde a limpeza até o treinamento do modelo. É o arquivo que você apresentaria para mostrar o processo completo.

**Seções:**
1. Carregamento e limpeza de dados
2. Análise exploratória (EDA)
3. Feature engineering
4. Treinamento de modelos
5. Avaliação e interpretação

**Importância:** 🔴 **ESSENCIAL PARA APRESENTAÇÃO** - É o entregável técnico principal do Tech Challenge.

---

### 9. **PROJETO_COMPLETO.md** ⭐⭐
**O que é:** Documento consolidado com todos os resultados, insights e recomendações.

**Para que serve:** É o "relatório executivo" do projeto. Contém um resumo completo de tudo que foi feito, descoberto e recomendado.

**Importância:** 🟢 **IMPORTANTE** - Útil para apresentações e documentação.

---

### 10. **presentation/VIDEO_SCRIPT.md** ⭐⭐
**O que é:** Roteiro detalhado para o vídeo de apresentação de 5 minutos.

**Para que serve:** Guia para gravar o vídeo final do Tech Challenge, com narração, timing e visuais sugeridos.

**Importância:** 🟢 **IMPORTANTE** - Necessário para o vídeo final.

---

## 🔵 ARQUIVOS DE ANÁLISE E DOCUMENTAÇÃO

### 11. **notebooks/FASE_2_EDA_Aprofundada_Insights.md** ⭐⭐
**O que é:** Documento com as respostas às 11 perguntas de negócio.

**Para que serve:** Contém todos os insights estratégicos descobertos na análise de dados.

**Importância:** 🟢 **IMPORTANTE** - Responde aos requisitos do Tech Challenge.

---

### 12. **notebooks/FASE_3_Modelo_Preditivo.md** ⭐
**O que é:** Documentação técnica do modelo de Machine Learning.

**Para que serve:** Explica como o modelo foi treinado, otimizado e avaliado.

**Importância:** 🔵 **ÚTIL** - Documentação técnica para referência.

---

### 13. **DEPLOY_GUIDE.md** ⭐
**O que é:** Guia passo a passo para fazer o deploy da aplicação no Streamlit Cloud.

**Para que serve:** Instruções detalhadas para publicar a aplicação online.

**Importância:** 🔵 **ÚTIL** - Necessário apenas se você for redesenhar a aplicação.

---

## 🟣 SCRIPTS PYTHON (src/)

Estes são os scripts que foram usados para processar os dados e treinar o modelo. **Não são necessários para a aplicação funcionar**, mas são importantes para entender o processo.

### 14. **src/data_preparation.py** ⭐
**O que é:** Script para carregar e unificar os dados das 3 abas do Excel.

**Para que serve:** Lê o arquivo Excel e cria um dataset único.

**Importância:** 🔵 **ÚTIL** - Usado apenas durante o desenvolvimento.

---

### 15. **src/data_cleaning.py** ⭐
**O que é:** Script para limpar e pré-processar os dados.

**Para que serve:** Remove valores nulos, padroniza colunas e cria a variável alvo (`risco_defasagem`).

**Importância:** 🔵 **ÚTIL** - Usado apenas durante o desenvolvimento.

---

### 16. **src/model_preparation.py** ⭐
**O que é:** Script para feature engineering (criação de novas variáveis).

**Para que serve:** Cria 38 features derivadas (razões, interações, lags) para melhorar o modelo.

**Importância:** 🔵 **ÚTIL** - Usado apenas durante o desenvolvimento.

---

### 17. **src/model_training.py** ⭐
**O que é:** Script para treinar e comparar 3 modelos de Machine Learning.

**Para que serve:** Treina Logistic Regression, Random Forest e Gradient Boosting, e compara suas métricas.

**Importância:** 🔵 **ÚTIL** - Usado apenas durante o desenvolvimento.

---

### 18. **src/model_interpretation.py** ⭐
**O que é:** Script para otimizar o melhor modelo e gerar interpretações.

**Para que serve:** Faz Grid Search para encontrar os melhores hiperparâmetros e gera gráficos de feature importance.

**Importância:** 🔵 **ÚTIL** - Usado apenas durante o desenvolvimento.

---

## 🟤 ARQUIVOS DE VISUALIZAÇÃO (notebooks/)

Estes são gráficos gerados durante a análise. **Não são necessários para a aplicação funcionar**.

### 19-30. **Gráficos (.png)**
**Exemplos:**
- `ian_evolution.png` - Evolução do IAN ao longo dos anos
- `feature_importance.png` - Importância das features no modelo
- `confusion_matrix_Gradient_Boosting.png` - Matriz de confusão do modelo

**Para que serve:** Visualizações usadas nos notebooks e na apresentação.

**Importância:** 🟤 **OPCIONAL** - Útil para apresentações, mas não essencial.

---

## ⚫ ARQUIVOS INTERMEDIÁRIOS (Podem ser Ignorados)

Estes arquivos foram gerados durante o desenvolvimento e **não são necessários**.

### 31. **src/best_model.pkl**
**O que é:** Versão intermediária do modelo (antes da otimização).

**Importância:** ⚫ **IGNORAR** - Substituído por `models/gradient_boosting_model.pkl`.

---

### 32. **src/logistic_model.pkl**
**O que é:** Modelo de Regressão Logística (não foi o melhor).

**Importância:** ⚫ **IGNORAR** - Não é usado na aplicação.

---

### 33. **notebooks/eda_initial_report.txt**
**O que é:** Relatório de texto da EDA inicial.

**Importância:** ⚫ **IGNORAR** - Informação já está nos documentos finais.

---

## 📊 RESUMO: ARQUIVOS POR IMPORTÂNCIA

### 🔴 CRÍTICOS (Sem eles, a aplicação não funciona)
1. `requirements.txt`
2. `app/app_streamlit.py`
3. `models/gradient_boosting_model.pkl`
4. `models/scaler.pkl`
5. `models/feature_cols.pkl`

### 🟢 IMPORTANTES (Essenciais para apresentação)
6. `README.md`
7. `notebooks/Datathon_Passos_Magicos_Completo.ipynb`
8. `PROJETO_COMPLETO.md`
9. `presentation/VIDEO_SCRIPT.md`
10. `notebooks/FASE_2_EDA_Aprofundada_Insights.md`

### 🔵 ÚTEIS (Documentação e scripts de desenvolvimento)
11. `.streamlit/config.toml`
12. `DEPLOY_GUIDE.md`
13. `notebooks/FASE_3_Modelo_Preditivo.md`
14-18. Scripts Python em `src/`

### 🟤 OPCIONAIS (Visualizações)
19-30. Gráficos `.png` em `notebooks/`

### ⚫ IGNORAR (Arquivos intermediários)
31-33. Modelos e relatórios intermediários

---

## 🎯 Para o Tech Challenge, você precisa de:

### Entregáveis Obrigatórios:
1. ✅ **Repositório GitHub** (todos os arquivos críticos + importantes)
2. ✅ **Notebook Consolidado** (`Datathon_Passos_Magicos_Completo.ipynb`)
3. ✅ **Aplicação Streamlit** (funcionando online)
4. ✅ **Apresentação** (slides HTML ou PDF)
5. ✅ **Vídeo de 5 minutos** (usando o roteiro fornecido)

### Para Apresentar:
- `README.md` - Visão geral do projeto
- `PROJETO_COMPLETO.md` - Relatório executivo
- `notebooks/Datathon_Passos_Magicos_Completo.ipynb` - Código técnico
- Aplicação online: https://datathon-passos-magicos.streamlit.app

---

## 💡 Dica Final

**Se você fosse explicar o projeto para alguém, mostre nesta ordem:**

1. **README.md** - "O que é o projeto"
2. **Aplicação Streamlit** - "Como funciona na prática"
3. **PROJETO_COMPLETO.md** - "Quais foram os resultados"
4. **Notebook Consolidado** - "Como foi feito tecnicamente"

---

**Agora você sabe exatamente o que é cada arquivo e qual a importância de cada um!** 🎯
