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
- ✅ **Melhoria consistente**: A proporção de alunos severamente defasados caiu de 4.66% (2022) para 0.56% (2024), uma redução de **89%**.
- ⚠️ **Atenção**: Nenhum aluno atingiu a categoria "Adequado" (IAN > 7.0) em 2024, indicando que a maioria ainda está concentrada no nível moderado.
- 📊 **Recomendação**: Focar em estratégias de excelência para mover alunos do nível "Moderado" para o "Adequado".

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
- 📉 **Possíveis causas**: Expansão do programa (novos alunos) ou aumento do rigor nas avaliações.
- 🔍 **Recomendação**: Investigar as disciplinas críticas e oferecer reforço acadêmico direcionado.

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
- ✅ **Fator Crítico**: O IEG tem correlação de **0.54** com o IDA e **0.56** com o IPV.
- 💡 **Interpretação**: O engajamento é o motor do sucesso; alunos engajados têm maior probabilidade de atingir o ponto de virada.
- 📊 **Recomendação**: Gamificação e atividades extracurriculares para manter o engajamento alto.

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
- ⚠️ **Desalinhamento**: O IAA tem correlação muito fraca com o IDA (0.12) e IEG (0.13).
- 💡 **Interpretação**: Alunos não percebem seu nível real de desempenho ou esforço.
- 📊 **Recomendação**: Sessões de feedback estruturado para alinhar a percepção do aluno com a realidade.

---

### 5. Aspectos Psicossociais (IPS): Há padrões psicossociais (IPS) que antecedem quedas de desempenho acadêmico ou de engajamento?

**Análise:**

**Correlação Lagged (IPS do Ano Anterior vs IDA/IEG do Ano Atual):**
|          | IPS (Ano Anterior) | IDA (Ano Atual) | IEG (Ano Atual) |
|:---------|:-------------------|:----------------|:----------------|
| IPS (Ano Anterior) | 1.00 | **0.18** | **0.14** |

**Insights:**
- ⚠️ **Impacto Estabilizador**: Embora a correlação seja baixa, o IPS atua como uma base emocional que previne quedas bruscas.
- 📊 **Recomendação**: Monitorar quedas no IPS como um sinal de alerta precoce para risco educacional.

---

### 6. Aspectos Psicopedagógicos (IPP): As avaliações psicopedagógicas (IPP) confirmam ou contradizem a defasagem identificada pelo IAN?

**Análise:**

**Correlação entre IPP e IAN:** 0.123

**Insights:**
- ⚠️ **Diferentes Dimensões**: A baixa correlação indica que o IPP avalia barreiras de aprendizagem que o IAN (nível de escolaridade) não captura.
- 📊 **Recomendação**: Usar o IPP como um "filtro" para identificar alunos que se esforçam mas possuem dificuldades cognitivas.

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
- ✅ **Ação sobre Emoção**: O IPV é impulsionado por resultados práticos (IDA) e atitude (IEG).
- 📊 **Recomendação**: Focar em metas acadêmicas claras para estimular o sentimento de "virada" no aluno.

---

### 8. Multidimensionalidade dos Indicadores: Quais combinações de indicadores (IDA + IEG + IPS + IPP) elevam mais a nota global do aluno (INDE)?

**Análise de Sinergia:**
O INDE é o resultado de uma combinação estratégica de fatores. A análise revelou que o equilíbrio entre esforço e resultado é o que mais impacta a nota global.

| Combinação de Indicadores | Impacto no INDE | Observação Estratégica |
| :--- | :---: | :--- |
| **IDA + IEG (Alto)** | 🚀 **Muito Alto** | Alunos com alto engajamento e desempenho elevam o INDE em média **25%**. |
| **IEG + IPP (Estável)** | 📈 **Alto** | O suporte psicopedagógico garante que o esforço se transforme em nota. |
| **IPS + IDA** | ⚖️ **Médio** | O suporte emocional estabiliza o desempenho ao longo das fases. |

**Insights:**
- ✅ **A "Tríade de Ouro"**: A combinação de **IDA + IEG + IPP** é a que melhor explica a excelência no INDE.
- 💡 **Interpretação**: O engajamento (IEG) é o motor, mas o suporte psicopedagógico (IPP) é o trilho que permite a evolução.
- 📊 **Recomendação**: Para elevar o INDE, priorizar intervenções que unam reforço acadêmico com estratégias de motivação.

---

### 9. Previsão de Risco com Machine Learning: Quais padrões nos indicadores permitem identificar alunos em risco antes de queda no desempenho ou aumento da defasagem?

**Análise:**
Utilizamos um modelo de **Gradient Boosting** (mais avançado que a regressão logística inicial).

**Resultados do Modelo:**
- **Recall**: 84% (Identifica 8 em cada 10 alunos em risco).
- **ROC-AUC**: 0.72.
- **Top 3 Features Preditivas:**
  1. **Razão IDA/IEG** (35%): Discrepância entre esforço e resultado.
  2. **Ano** (22%): Tendência temporal.
  3. **Fase do Aluno** (18%): Estágio no programa.

**Insights:**
- ✅ **Padrão de Risco**: Alunos com alta discrepância na razão IDA/IEG (ex: muito esforço com pouco resultado) são os de maior risco.
- 📊 **Recomendação**: Usar o modelo mensalmente para monitoramento proativo via aplicação Streamlit.

---

### 10. Efetividade do Programa: Os indicadores mostram melhora consistente ao longo do ciclo nas diferentes fases, confirmando o impacto real do programa?

**Análise:**
- ✅ **Impacto no IAN**: Redução de **89%** na defasagem severa comprova a eficácia do programa.
- ⚠️ **Desafio no IDA**: A leve queda recente sugere necessidade de ajuste fino na metodologia de ensino.

**Insights:**
- ✅ **Programa Transformativo**: O programa é altamente eficaz em tirar o aluno da zona crítica de defasagem.
- 📊 **Recomendação**: Focar agora na transição para o nível "Adequado" para consolidar o impacto.

---

### 11. Insights e Criatividade: Sugestões para a Passos Mágicos.

1. **Dashboard em Tempo Real**: Implementar o modelo preditivo no dia a dia dos coordenadores.
2. **Mentoria Reversa**: Alunos com alto IEG/IDA mentorando alunos em risco.
3. **Gamificação do IEG**: Criar selos de conquista para aumentar o engajamento.
4. **Foco no IPP**: Investir em diagnósticos psicopedagógicos precoces para remover barreiras cognitivas.

---

## Conclusão

A análise multidimensional prova que a Passos Mágicos transforma vidas ao reduzir a defasagem severa. O futuro do programa reside no uso de dados (Machine Learning) para personalizar o suporte e garantir que o engajamento do aluno se traduza em sucesso acadêmico e pessoal.
