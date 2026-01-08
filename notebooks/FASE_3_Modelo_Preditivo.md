
# Relatório do Modelo Preditivo de Risco Educacional - FASE 3

## Modelo Otimizado: Gradient Boosting Classifier

### Hiperparâmetros Otimizados:
{'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.1, 'loss': 'log_loss', 'max_depth': 7, 'max_features': None, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 100, 'n_iter_no_change': None, 'random_state': 42, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False}

### Desempenho no Conjunto de Teste:
- **ROC-AUC Score**: 0.7020

### Classification Report:
```
              precision    recall  f1-score   support

           0       0.63      0.51      0.56       234
           1       0.70      0.79      0.74       337

    accuracy                           0.68       571
   macro avg       0.66      0.65      0.65       571
weighted avg       0.67      0.68      0.67       571

```

### Top 10 Features Mais Importantes:
| Feature             |   Importance |
|:--------------------|-------------:|
| fase_encoded        |    0.135275  |
| ipv                 |    0.121718  |
| mean_indicators     |    0.093659  |
| ida_ieg_interaction |    0.0798123 |
| ida_ieg_ratio       |    0.0674313 |
| ida_delta           |    0.0613713 |
| ieg_lag1            |    0.0558974 |
| ipp_ips_interaction |    0.0523956 |
| ida                 |    0.0475822 |
| ipp                 |    0.0470004 |

### Interpretação das Features:

1. **fase_encoded** (Importância: 0.1353)
   - Esta é a feature mais importante para prever o risco de defasagem.

2. **ipv** (Importância: 0.1217)
   - Segunda feature mais relevante.

3. **mean_indicators** (Importância: 0.0937)
   - Terceira feature mais relevante.

### Conclusões:

O modelo Gradient Boosting otimizado alcançou um **ROC-AUC de 0.7020**, representando uma melhoria significativa em relação ao modelo baseline.

As features mais importantes indicam que:
- Indicadores de desempenho acadêmico e engajamento são cruciais para prever o risco.
- Features de interação e temporais (lag, delta) também contribuem para o modelo.

### Recomendações:

1. **Monitoramento Proativo**: Utilizar o modelo para identificar alunos em risco antes de quedas de desempenho.
2. **Intervenções Personalizadas**: Focar nas features mais importantes para criar estratégias de intervenção direcionadas.
3. **Coleta de Dados**: Continuar coletando dados históricos para melhorar o modelo ao longo do tempo.
