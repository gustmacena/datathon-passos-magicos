# Datathon Passos Mágicos - Projeto Completo

**Projeto:** Prevenção de Risco Educacional  
**Equipe:** Gustavo Macena & Data Analytics Team  
**Data:** Janeiro 2025  
**Repositório:** https://github.com/gustmacena/datathon-passos-magicos

---

## 📋 Resumo Executivo

Este projeto foi desenvolvido para o **Datathon Passos Mágicos 2025** com o objetivo de criar uma solução completa de análise de dados educacionais e predição de risco de defasagem. O projeto entrega não apenas insights estratégicos, mas também uma ferramenta prática e escalável para uso pela equipe pedagógica da Associação Passos Mágicos.

**Principais Resultados:**
- ✅ Análise completa de dados de 2022 a 2024 (2.852 registros)
- ✅ Modelo preditivo com ROC-AUC de 0.72 e Recall de 84%
- ✅ Aplicação web interativa para predição em tempo real
- ✅ 11 insights estratégicos respondidos
- ✅ 5 recomendações acionáveis para maximizar impacto

---

## 🎯 Objetivos Alcançados

### 1. Análise de Dados Educacionais

Analisamos os dados de 2.852 alunos ao longo de 3 anos (2022-2024), focando em 6 indicadores principais:

| Indicador | Descrição | Faixa |
|:---|:---|:---|
| **IAN** | Adequação do Nível | 0-10 |
| **IDA** | Desempenho Acadêmico | 0-10 |
| **IEG** | Engajamento | 0-10 |
| **IPS** | Aspectos Psicossociais | 0-10 |
| **IAA** | Autoavaliação | 0-10 |
| **IPV** | Ponto de Virada | 0-10 |

### 2. Respostas às 11 Perguntas de Negócio

Todas as 11 perguntas estratégicas foram respondidas com base em análise de dados rigorosa. Os insights estão documentados em `notebooks/FASE_2_EDA_Aprofundada_Insights.md`.

**Destaques:**
- **IAN**: Redução de 89% na taxa de alunos severamente defasados
- **IDA**: Queda de 4.7% em 2024 - ponto de atenção
- **IEG x IDA**: Correlação de 0.54 - engajamento é fator crítico
- **IAA**: Correlação muito fraca (0.12-0.13) - desalinhamento com realidade

### 3. Modelo Preditivo de Risco

Desenvolvemos um modelo de Machine Learning capaz de prever o risco de defasagem de cada aluno com alta precisão.

**Especificações Técnicas:**

| Métrica | Valor | Interpretação |
|:---|:---|:---|
| **Algoritmo** | Gradient Boosting Classifier | Otimizado com Grid Search |
| **ROC-AUC** | 0.72 | Boa capacidade de distinção |
| **Acurácia** | 70% | Taxa global de acertos |
| **Recall** | 84% | Identifica 8 em cada 10 alunos em risco |
| **Precisão** | 71% | Reduz falsos positivos |

**Top 3 Features Preditivas:**
1. **Razão IDA/IEG** (35%) - Discrepância entre desempenho e engajamento
2. **Ano** (22%) - Tendência temporal
3. **Fase do Aluno** (18%) - Estágio de maturação no programa

### 4. Aplicação Web Interativa

Desenvolvemos uma aplicação Streamlit que transforma o modelo em uma ferramenta prática para a equipe pedagógica.

**Funcionalidades:**
- Interface intuitiva com sliders para entrada de dados
- Predição em tempo real da probabilidade de risco
- Visualização clara com gráficos e classificação (Alto/Baixo Risco)
- Recomendações personalizadas baseadas no resultado
- Análise detalhada de cada indicador

**Acesso:** https://datathon-passos-magicos.streamlit.app

---

## 📊 Insights Estratégicos

### Insight 1: Sucesso na Redução de Defasagem Severa

A taxa de alunos severamente defasados (IAN < 5.0) caiu de **4.66% em 2022** para **0.56% em 2024**, uma redução de **89%**. Isso comprova a eficácia das intervenções pedagógicas implementadas pela Passos Mágicos.

**Ponto de Atenção:** Apesar da melhora, nenhum aluno atingiu a categoria "Adequado" (IAN > 7.0) em 2024, indicando que o foco deve mudar para a excelência.

### Insight 2: Queda no Desempenho Acadêmico

O IDA (Desempenho Acadêmico) teve uma queda de **6.66 em 2023** para **6.35 em 2024** (-4.7%). Isso pode estar relacionado ao aumento no número de alunos atendidos ou a mudanças na metodologia de avaliação.

**Recomendação:** Investigar as causas raiz e implementar intervenções pedagógicas focadas nas disciplinas críticas.

### Insight 3: Engajamento como Fator Crítico

Alunos mais engajados (IEG) têm **54% mais probabilidade** de apresentar melhor desempenho acadêmico (IDA). A correlação entre IEG e IPV (Ponto de Virada) é ainda maior: **0.56**.

**Recomendação:** Implementar estratégias de gamificação e atividades extracurriculares para aumentar o engajamento.

### Insight 4: Desalinhamento na Autoavaliação

A autoavaliação dos alunos (IAA) tem correlação muito fraca com o desempenho real (IDA: 0.12) e com o engajamento (IEG: 0.13). Isso indica que os alunos não têm clareza sobre seus próprios resultados.

**Recomendação:** Implementar sessões de feedback estruturado para alinhar a percepção dos alunos com a realidade.

### Insight 5: Razão IDA/IEG como Principal Preditor

A **razão entre desempenho e engajamento** é o fator mais importante para prever risco de defasagem. Alunos com alta discrepância (esforço sem resultado ou resultado sem esforço) apresentam maior risco.

**Recomendação:** Focar intervenções personalizadas nesses alunos.

---

## 🎓 Recomendações Estratégicas

### 1. Monitoramento Proativo

Utilizar o modelo preditivo **mensalmente** para identificar alunos em risco antes que a defasagem se consolide. A aplicação Streamlit permite que qualquer educador faça essa análise em segundos.

### 2. Aumento do Engajamento

Implementar estratégias de **gamificação** e **atividades extracurriculares**, dado o alto impacto do IEG no desempenho. Exemplos: competições, projetos colaborativos, reconhecimento público.

### 3. Feedback Estruturado

Realizar **sessões individuais** para alinhar a autoavaliação (IAA) do aluno com seus resultados reais (IDA). Isso promove maior autoconsciência e responsabilidade.

### 4. Intervenções Personalizadas

Focar ações pedagógicas nos alunos com **alta discrepância na razão IDA/IEG** (esforço vs. resultado). Esses alunos requerem abordagens diferenciadas.

### 5. Coleta de Dados Contínua

Manter o histórico de dados atualizado para **retreinar e refinar o modelo preditivo anualmente**. Isso garante que o modelo se adapte às mudanças no programa.

---

## 📈 Impacto Projetado (2 Anos)

Com a implementação das recomendações e o uso contínuo do modelo preditivo, projetamos:

| Métrica | Impacto Esperado |
|:---|:---|
| **Taxa de Defasagem** | **-30%** (redução nos níveis moderado e severo) |
| **Engajamento Médio (IEG)** | **+20%** (através de intervenções direcionadas) |
| **Alunos Identificados Precocemente** | **+50%** (antes da consolidação da defasagem) |

---

## 📦 Entregáveis do Projeto

### 1. Repositório GitHub

**Link:** https://github.com/gustmacena/datathon-passos-magicos

**Conteúdo:**
- Código-fonte completo (Python)
- Scripts de limpeza, análise e modelagem
- Notebook consolidado (`.ipynb`)
- Modelos treinados (`.pkl`)
- Documentação completa

### 2. Notebook Consolidado

**Arquivo:** `notebooks/Datathon_Passos_Magicos_Completo.ipynb`

Notebook Jupyter com todo o pipeline de análise:
- Limpeza e pré-processamento de dados
- Análise exploratória (EDA)
- Feature engineering
- Treinamento e avaliação de modelos
- Interpretação dos resultados

### 3. Aplicação Streamlit

**Link:** https://datathon-passos-magicos.streamlit.app

Aplicação web interativa para predição de risco em tempo real.

### 4. Apresentação Final

**Formato:** Slides HTML (12 páginas)

Apresentação executiva com storytelling de dados, incluindo:
- Contexto e objetivos
- Principais insights
- Modelo preditivo
- Aplicação prática
- Recomendações e impacto

### 5. Roteiro do Vídeo

**Arquivo:** `presentation/VIDEO_SCRIPT.md`

Roteiro detalhado para vídeo de apresentação de 5 minutos, com estrutura, narração e checklist de produção.

### 6. Documentação Técnica

**Arquivos:**
- `README.md` - Visão geral e instruções de uso
- `DEPLOY_GUIDE.md` - Guia de deploy no Streamlit Cloud
- `FASE_1_Exploracao_Limpeza.md` - Documentação da Fase 1
- `FASE_2_EDA_Aprofundada_Insights.md` - Respostas às 11 perguntas
- `FASE_3_Modelo_Preditivo.md` - Documentação do modelo

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologias |
|:---|:---|
| **Linguagem** | Python 3.11 |
| **Análise de Dados** | Pandas, NumPy |
| **Visualização** | Matplotlib, Seaborn, Plotly |
| **Machine Learning** | Scikit-learn |
| **Aplicação Web** | Streamlit |
| **Versionamento** | Git, GitHub |
| **Deploy** | Streamlit Community Cloud |

---

## 📚 Como Usar Este Projeto

### Para Educadores da Passos Mágicos

1. **Acesse a aplicação:** https://datathon-passos-magicos.streamlit.app
2. **Insira os indicadores do aluno** usando os sliders
3. **Clique em "Prever Risco"**
4. **Analise o resultado** e as recomendações personalizadas
5. **Implemente as intervenções sugeridas**

### Para Desenvolvedores

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/gustmacena/datathon-passos-magicos.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação localmente:**
   ```bash
   streamlit run app/app_streamlit.py
   ```

4. **Explore os notebooks:**
   ```bash
   jupyter notebook notebooks/Datathon_Passos_Magicos_Completo.ipynb
   ```

---

## 🏆 Conclusão

Este projeto entrega uma solução completa e sustentável para potencializar o impacto da Associação Passos Mágicos. Ao combinar análise de dados rigorosa, Machine Learning interpretável e uma ferramenta prática de fácil uso, criamos um sistema que não apenas identifica alunos em risco, mas também orienta ações pedagógicas personalizadas.

**O diferencial deste projeto:**
- ✅ **Acionável:** Ferramenta prática para uso diário
- ✅ **Interpretável:** Explicação clara das predições
- ✅ **Escalável:** Fácil de atualizar e expandir
- ✅ **Sustentável:** Documentação completa para manutenção

**Transformando dados em oportunidades para transformar vidas através da educação.**

---

## 📞 Contato

**Gustavo Macena**  
Data Analyst & Machine Learning Engineer

**Repositório:** https://github.com/gustmacena/datathon-passos-magicos  
**Aplicação:** https://datathon-passos-magicos.streamlit.app

---

**Desenvolvido com ❤️ para a Associação Passos Mágicos**
