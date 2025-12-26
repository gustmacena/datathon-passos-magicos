# FASE 1 — Exploração e Limpeza de Dados

## 1. Exploração Inicial de Dados (EDA)

A exploração inicial foi realizada no dataset unificado, que combinou os dados de 2022, 2023 e 2024.

### Principais Descobertas:

| Indicador | Observação | Implicação para a Análise |
| :--- | :--- | :--- |
| **IAN (Indicador de Adequação do Nível)** | Possui apenas 3 valores discretos (2.5, 5.0, 10.0). | Simplifica a criação da variável alvo de risco. |
| **Valores Nulos** | Alta contagem de nulos em colunas específicas de ano (ex: `ingls`, `matem`, `portug` de 2022) e colunas de avaliação (ex: `avaliador5`, `avaliador6`). | A análise temporal e a modelagem preditiva devem considerar a exclusão de linhas com nulos nas *features* principais. |
| **Gênero** | Necessidade de padronização: `Menina` e `Menino` foram unificados para `Feminino` e `Masculino`. | Essencial para análises demográficas consistentes. |
| **IDA Médio** | O IDA médio por ano mostrou uma ligeira queda de 2023 (6.66) para 2024 (6.35). | Sugere uma necessidade de investigação mais profunda na FASE 2 sobre a efetividade do programa. |

## 2. Limpeza e Pré-processamento de Dados

O script `src/data_cleaning.py` foi executado para realizar as seguintes etapas:

1. **Padronização Categórica:** Unificação dos valores da coluna `gnero` (`Menina`/`Menino` para `Feminino`/`Masculino`).
2. **Seleção de Colunas:** Foram mantidas apenas as colunas principais relevantes para a análise multidimensional e o modelo preditivo (indicadores e dados demográficos).
3. **Criação da Variável Alvo:** A coluna `risco_defasagem` foi criada, onde:
    - **1 (Alto Risco):** Se `ian` < 7.0 (inclui 2.5 e 5.0)
    - **0 (Baixo Risco):** Se `ian` >= 7.0 (inclui 10.0)
4. **Tratamento de Nulos Categóricos:** Valores nulos na coluna `fase` e `gnero` foram preenchidos com `NAO_INFORMADO`.

## 3. Validação da Limpeza

O dataset final (`pedagogy_data_final.csv`) está pronto para a próxima fase de Análise Exploratória de Dados (EDA) aprofundada e Modelagem Preditiva.

| Coluna | Tipo de Dado | Observação |
| :--- | :--- | :--- |
| `risco_defasagem` | Inteiro (0 ou 1) | Variável alvo criada com sucesso. |
| `gnero` | Categórico | Padronizado (Feminino, Masculino, NAO_INFORMADO). |
| `ida`, `ieg`, `ips`, `ipp`, `iaa`, `ipv` | Numérico | Mantidos para a modelagem, com NaNs a serem tratados na etapa de *feature engineering* do modelo. |

**Próximo Passo:** Iniciar a FASE 2 — Análise Exploratória de Dados (EDA) Aprofundada.
