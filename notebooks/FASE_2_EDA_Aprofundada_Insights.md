# FASE 2 — Análise Exploratória de Dados (EDA) Aprofundada e Geração de Insights

## Objetivo

Responder às **11 perguntas de negócio** propostas pelo Datathon, utilizando análise exploratória de dados multidimensional e gerando insights estratégicos para a Associação Passos Mágicos.

---

## Respostas às Perguntas de Negócio

### 1. Adequação do Nível (IAN): Qual é o perfil geral de defasagem dos alunos (IAN) e como ele evolui ao longo do ano?

**Análise:**
O Indicador de Adequação do Nível (IAN) apresenta apenas **3 valores discretos** (2.5, 5.0 e 10.0), representando níveis de defasagem:
- **2.5**: Severamente Defasado
- **5.0**: Moderadamente Defasado
- **10.0**: Adequado

**Evolução ao Longo dos Anos:**

| Ano | Severamente Defasado (<5.0) | Moderadamente Defasado (5.0-7.0) | Adequado (>7.0) |
|:---|:---|:---|:---|
| 2022 | 4.66% | 95.34% | 0% |
| 2023 | 2.54% | 97.46% | 0% |
| 2024 | 0.56% | 99.44% | 0% |

**Insights:**
- ✅ **Melhoria consistente**: A proporção de alunos severamente defasados caiu de 4.66% (2022) para 0.56% (2024).
- ⚠️ **Atenção**: Nenhum aluno atingiu a categoria "Adequado" (IAN > 7.0), indicando que a maioria ainda está moderadamente defasada.
- 📊 **Recomendação**: Investigar as barreiras que impedem a transição de "Moderadamente Defasado" para "Adequado".

---

### 2. Desempenho Acadêmico (IDA): O desempenho acadêmico médio (IDA) está melhorando, estagnado ou caindo ao longo das fases e anos?

**Análise:**

**IDA Médio por Ano:**
| Ano | IDA Médio |
|:---|:---|
| 2023 | 6.66 |
| 2024 | 6.35 |

**Insights:**
- ⚠️ **Queda no IDA**: O desempenho acadêmico médio caiu de 6.66 (2023) para 6.35 (2024), uma redução de **4.7%**.
- 📉 **Possíveis causas**: Aumento no número de alunos, mudanças na metodologia de avaliação, ou desafios externos (ex: pandemia, contexto socioeconômico).
- 🔍 **Recomendação**: Realizar análise qualitativa com educadores para identificar as causas da queda e implementar intervenções pedagógicas direcionadas.

---

### 3. Engajamento nas Atividades (IEG): O grau de engajamento dos alunos (IEG) tem relação direta com seus indicadores de desempenho (IDA) e do ponto de virada (IPV)?

**Análise:**

**Matriz de Correlação:**
|     | IEG | IDA | IPV |
|:----|:----|:----|:----|
| IEG | 1.00 | **0.54** | **0.56** |
| IDA | 0.54 | 1.00 | 0.56 |
| IPV | 0.56 | 0.56 | 1.00 |

**Insights:**
- ✅ **Correlação moderada positiva**: O IEG tem correlação de **0.54** com o IDA e **0.56** com o IPV.
- 💡 **Interpretação**: Alunos mais engajados tendem a ter melhor desempenho acadêmico e maior probabilidade de atingir o ponto de virada.
- 📊 **Recomendação**: Implementar estratégias para aumentar o engajamento (ex: gamificação, mentoria, atividades extracurriculares).

---

### 4. Autoavaliação (IAA): As percepções dos alunos sobre si mesmos (IAA) são coerentes com seu desempenho real (IDA) e engajamento (IEG)?

**Análise:**

**Matriz de Correlação:**
|     | IAA | IDA | IEG |
|:----|:----|:----|:----|
| IAA | 1.00 | **0.12** | **0.13** |
| IDA | 0.12 | 1.00 | 0.54 |
| IEG | 0.13 | 0.54 | 1.00 |

**Insights:**
- ⚠️ **Baixa correlação**: O IAA tem correlação muito fraca com o IDA (0.12) e IEG (0.13).
- 💡 **Interpretação**: A autoavaliação dos alunos **não reflete** seu desempenho real ou engajamento. Isso pode indicar:
  - Falta de autocrítica ou consciência sobre o próprio desempenho.
  - Viés de otimismo ou pessimismo na autoavaliação.
- 📊 **Recomendação**: Implementar sessões de feedback estruturado para alinhar a percepção dos alunos com seu desempenho real.

---

### 5. Aspectos Psicossociais (IPS): Há padrões psicossociais (IPS) que antecedem quedas de desempenho acadêmico ou de engajamento?

**Análise:**

**Correlação Lagged (IPS do Ano Anterior vs IDA/IEG do Ano Atual):**
|          | IPS (Ano Anterior) | IDA (Ano Atual) | IEG (Ano Atual) |
|:---------|:-------------------|:----------------|:----------------|
| IPS (Ano Anterior) | 1.00 | **0.18** | **0.14** |

**Insights:**
- ⚠️ **Correlação fraca**: O IPS do ano anterior tem correlação fraca com o IDA (0.18) e IEG (0.14) do ano atual.
- 💡 **Interpretação**: Aspectos psicossociais têm impacto limitado no desempenho futuro, mas ainda assim positivo.
- 📊 **Recomendação**: Monitorar alunos com IPS baixo e oferecer suporte psicológico proativo para prevenir quedas de desempenho.

---

### 6. Aspectos Psicopedagógicos (IPP): As avaliações psicopedagógicas (IPP) confirmam ou contradizem a defasagem identificada pelo IAN?

**Análise:**

**Correlação entre IPP e IAN:** 0.123

**Insights:**
- ⚠️ **Baixa correlação**: O IPP tem correlação muito fraca com o IAN (0.12).
- 💡 **Interpretação**: As avaliações psicopedagógicas **não confirmam** a defasagem identificada pelo IAN. Isso pode indicar:
  - Desalinhamento entre os critérios de avaliação do IPP e do IAN.
  - Necessidade de revisar a metodologia de avaliação psicopedagógica.
- 📊 **Recomendação**: Alinhar os critérios de avaliação do IPP com o IAN para garantir consistência.

---

### 7. Ponto de Virada (IPV): Quais comportamentos - acadêmicos, emocionais ou de engajamento - mais influenciam o IPV ao longo do tempo?

**Análise:**

**Correlação do IPV com Indicadores:**
| Indicador | Correlação com IPV |
|:----------|:-------------------|
| IEG (Engajamento) | **0.56** |
| IDA (Desempenho Acadêmico) | **0.56** |
| IPS (Aspectos Psicossociais) | **-0.05** |

**Insights:**
- ✅ **IEG e IDA são os principais influenciadores**: Ambos têm correlação moderada positiva (0.56) com o IPV.
- ⚠️ **IPS tem impacto mínimo**: Correlação negativa e muito fraca (-0.05).
- 💡 **Interpretação**: O ponto de virada é mais influenciado por **engajamento** e **desempenho acadêmico** do que por aspectos emocionais.
- 📊 **Recomendação**: Focar em estratégias que aumentem o engajamento e o desempenho acadêmico para maximizar o IPV.

---

### 8. Multidimensionalidade dos Indicadores: Quais combinações de indicadores (IDA + IEG + IPS + IPP) melhor explicam o desempenho global do aluno (INDE)?

**Análise:**

**Correlação dos Indicadores com o INDE:**
| Indicador | Correlação com INDE |
|:----------|:--------------------|
| IEG (Engajamento) | **0.47** |
| IDA (Desempenho Acadêmico) | **0.46** |
| IPP (Aspectos Psicopedagógicos) | **0.36** |
| IPS (Aspectos Psicossociais) | **0.07** |

**Insights:**
- ✅ **IEG e IDA são os principais preditores**: Explicam a maior parte da variação no INDE.
- ⚠️ **IPS tem impacto mínimo**: Correlação muito fraca (0.07).
- 💡 **Interpretação**: O desempenho global (INDE) é principalmente determinado por **engajamento** e **desempenho acadêmico**.
- 📊 **Recomendação**: Priorizar intervenções que aumentem o IEG e o IDA para melhorar o INDE.

---

### 9. Previsão de Risco com Machine Learning: Quais padrões nos indicadores permitem identificar alunos em risco antes de queda no desempenho ou aumento da defasagem?

**Análise:**

Um modelo de **Regressão Logística** foi treinado para prever o risco de defasagem (baseado no IAN < 7.0).

**Resultados do Modelo:**
- **Acurácia**: 57%
- **AUC Score**: 0.61
- **Principais Features (Coeficientes):**
  - **IPP** (-0.17): Maior impacto negativo (quanto maior o IPP, menor o risco)
  - **Ano** (-0.14): Anos mais recentes têm menor risco
  - **IEG** (-0.11): Maior engajamento reduz o risco
  - **IAA** (-0.06): Maior autoavaliação reduz o risco
  - **IDA** (-0.05): Maior desempenho acadêmico reduz o risco
  - **IPS** (+0.004): Impacto mínimo

**Insights:**
- ✅ **IPP é o melhor preditor**: Avaliações psicopedagógicas são cruciais para identificar alunos em risco.
- ⚠️ **Modelo com desempenho moderado**: AUC de 0.61 indica que há espaço para melhoria.
- 📊 **Recomendação**: 
  - Coletar mais dados históricos para melhorar o modelo.
  - Explorar modelos mais complexos (Random Forest, Gradient Boosting).
  - Implementar feature engineering avançado (ex: interações entre indicadores).

---

### 10. Efetividade do Programa: Os indicadores mostram melhora consistente ao longo do ciclo nas diferentes fases (Quartzo, Ágata, Ametista e Topázio), confirmando o impacto real do programa?

**Análise:**

**Evolução do IAN (Defasagem):**
- ✅ **Melhoria consistente**: A proporção de alunos severamente defasados caiu de 4.66% (2022) para 0.56% (2024).

**Evolução do IDA (Desempenho Acadêmico):**
- ⚠️ **Queda no IDA**: O IDA médio caiu de 6.66 (2023) para 6.35 (2024).

**Insights:**
- ✅ **Impacto positivo no IAN**: O programa está reduzindo a defasagem severa.
- ⚠️ **Desafio no IDA**: A queda no desempenho acadêmico sugere que há desafios a serem enfrentados.
- 💡 **Interpretação**: O programa está sendo efetivo em reduzir a defasagem, mas precisa de ajustes para melhorar o desempenho acadêmico.
- 📊 **Recomendação**: Investigar as causas da queda no IDA e implementar intervenções pedagógicas direcionadas.

---

### 11. Insights e Criatividade: Você pode adicionar mais insights e pontos de vista não abordados nas perguntas, utilize a criatividade e a análise dos dados para trazer sugestões para a Passos Mágicos.

**Insights Adicionais:**

1. **Segmentação de Alunos por Perfil de Risco:**
   - Criar perfis de risco (Baixo, Médio, Alto) baseados em combinações de indicadores (IDA, IEG, IPP).
   - Implementar intervenções personalizadas para cada perfil.

2. **Análise de Gênero:**
   - Investigar se há diferenças significativas no desempenho entre alunos do sexo masculino e feminino.
   - Implementar estratégias específicas de gênero, se necessário.

3. **Análise de Instituição de Ensino:**
   - Comparar o desempenho de alunos de escolas públicas vs. privadas.
   - Identificar boas práticas em instituições com melhor desempenho.

4. **Dashboard Interativo:**
   - Desenvolver um dashboard em tempo real para monitorar os indicadores dos alunos.
   - Permitir que educadores identifiquem rapidamente alunos em risco.

5. **Programa de Mentoria:**
   - Implementar um programa de mentoria entre alunos com alto desempenho e alunos em risco.
   - Fomentar o aprendizado colaborativo e o engajamento.

---

## Conclusão

A análise exploratória aprofundada revelou que:
- ✅ O programa Passos Mágicos está reduzindo a defasagem severa (IAN).
- ⚠️ O desempenho acadêmico (IDA) caiu de 2023 para 2024, exigindo atenção.
- ✅ Engajamento (IEG) e Desempenho Acadêmico (IDA) são os principais preditores do sucesso dos alunos.
- ⚠️ Autoavaliação (IAA) e Aspectos Psicossociais (IPS) têm impacto limitado.
- ✅ O modelo preditivo de risco tem potencial, mas precisa de melhorias.

**Próximos Passos:**
- Implementar as recomendações estratégicas.
- Melhorar o modelo preditivo com mais dados e feature engineering.
- Desenvolver a aplicação Streamlit para disponibilizar o modelo para a equipe da Passos Mágicos.
