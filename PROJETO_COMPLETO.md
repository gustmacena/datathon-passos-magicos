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
- **IAN**: Redução de **89%** na taxa de alunos severamente defasados.
- **IDA**: Queda de **4.7%** em 2024 - ponto de atenção.
- **IEG x IDA**: Correlação de **0.54** - engajamento é fator crítico.
- **IAA**: Correlação muito fraca (**0.12**) - desalinhamento com realidade.

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
1. **Razão IDA/IEG** (35%) - Discrepância entre desempenho e engajamento.
2. **Ano** (22%) - Tendência temporal.
3. **Fase do Aluno** (18%) - Estágio de maturação no programa.

### 4. Aplicação Web Interativa

Desenvolvemos uma aplicação Streamlit que transforma o modelo em uma ferramenta prática para a equipe pedagógica.

**Funcionalidades:**
- Interface intuitiva com sliders para entrada de dados.
- Predição em tempo real da probabilidade de risco.
- Visualização clara com gráficos e classificação (Alto/Baixo Risco).
- Recomendações personalizadas baseadas no resultado.

**Acesso:** https://datathon-passos-magicos.streamlit.app

---

## 📊 Insights Estratégicos

### Insight 1: Sucesso na Redução de Defasagem Severa
A taxa de alunos severamente defasados (IAN < 5.0) caiu de **4.66% em 2022** para **0.56% em 2024**, uma redução de **89%**. Isso comprova a eficácia das intervenções pedagógicas da Passos Mágicos.

### Insight 2: Queda no Desempenho Acadêmico
O IDA (Desempenho Acadêmico) teve uma queda de **6.66 em 2023** para **6.35 em 2024** (-4.7%). Isso requer atenção imediata e investigação das causas raiz.

### Insight 3: Engajamento como Fator Crítico
Alunos mais engajados (IEG) têm **54% mais probabilidade** de apresentar melhor desempenho acadêmico (IDA). O engajamento é o motor do sucesso no programa.

### Insight 4: Desalinhamento na Autoavaliação
A autoavaliação dos alunos (IAA) tem correlação muito fraca com o desempenho real (0.12). Os alunos não têm clareza sobre seus próprios resultados.

### Insight 5: Multidimensionalidade e o INDE (Pergunta 8)
A combinação de **IDA + IEG + IPP** é a que mais eleva a nota global (INDE). O engajamento (IEG) impulsiona a nota, mas o suporte psicopedagógico (IPP) é o que garante a estabilidade do aprendizado.

---

## 🎓 Recomendações Estratégicas

1. **Monitoramento Proativo**: Utilizar o modelo preditivo **mensalmente** para identificar alunos em risco.
2. **Aumento do Engajamento**: Implementar estratégias de **gamificação** e atividades extracurriculares.
3. **Feedback Estruturado**: Realizar sessões individuais para alinhar a autoavaliação (IAA) com os resultados reais.
4. **Intervenções Personalizadas**: Focar nos alunos com **alta discrepância na razão IDA/IEG** (esforço vs. resultado).
5. **Foco Psicopedagógico**: Fortalecer o suporte de IPP para alunos que se esforçam mas não evoluem no IDA.

---

## 📈 Impacto Projetado (2 Anos)

| Métrica | Impacto Esperado |
|:---|:---|
| **Taxa de Defasagem** | **-30%** (redução nos níveis moderado e severo) |
| **Engajamento Médio (IEG)** | **+20%** (através de intervenções direcionadas) |
| **Alunos Identificados Precocemente** | **+50%** (antes da consolidação da defasagem) |

---

## 📦 Entregáveis do Projeto

1. **Repositório GitHub**: Código-fonte completo e documentação.
2. **Notebook Consolidado**: Pipeline técnico completo (`notebooks/Datathon_Passos_Magicos_Completo.ipynb`).
3. **Aplicação Streamlit**: Ferramenta de predição em tempo real.
4. **Relatório Executivo**: Este documento (`PROJETO_COMPLETO.md`).

---

## 🏆 Conclusão

Este projeto entrega uma solução sustentável para potencializar o impacto da Associação Passos Mágicos. Ao combinar análise de dados rigorosa, Machine Learning interpretável e uma ferramenta prática, criamos um sistema que não apenas identifica alunos em risco, mas também orienta ações pedagógicas personalizadas.

**Transformando dados em oportunidades para transformar vidas através da educação.**

---

## 📞 Contato
**Gustavo Macena** - Data Analyst & Machine Learning Engineer  
**Repositório:** https://github.com/gustmacena/datathon-passos-magicos  
**Aplicação:** https://datathon-passos-magicos.streamlit.app
