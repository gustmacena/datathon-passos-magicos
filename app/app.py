import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Configuração da página
st.set_page_config(page_title="Passos Mágicos - Previsão de Risco", layout="wide")

# Título e descrição
st.title("🎓 Passos Mágicos - Modelo de Previsão de Risco de Defasagem")
st.markdown("""
Este aplicativo utiliza um modelo de Machine Learning para prever o risco de defasagem educacional
dos alunos da Associação Passos Mágicos. O modelo foi treinado com dados educacionais de 2022 a 2024.
""")

# Carregar o modelo e o scaler
@st.cache_resource
def load_model_and_scaler():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'logistic_model.pkl')
    scaler_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'scaler.pkl')
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    return model, scaler

model, scaler = load_model_and_scaler()

# Sidebar para entrada de dados
st.sidebar.header("📊 Dados do Aluno")
st.sidebar.markdown("---")

# Inputs do usuário
ida = st.sidebar.slider("IDA (Desempenho Acadêmico)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ieg = st.sidebar.slider("IEG (Engajamento)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ips = st.sidebar.slider("IPS (Aspectos Psicossociais)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ipp = st.sidebar.slider("IPP (Aspectos Psicopedagógicos)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
iaa = st.sidebar.slider("IAA (Autoavaliação)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
ano = st.sidebar.selectbox("Ano", options=[2022, 2023, 2024], index=2)

# Preparar os dados para previsão
input_data = np.array([[ida, ieg, ips, ipp, iaa, ano]])
input_data_scaled = scaler.transform(input_data)

# Fazer a previsão
prediction = model.predict(input_data_scaled)[0]
prediction_proba = model.predict_proba(input_data_scaled)[0]

# Exibir os resultados
st.markdown("---")
st.header("📈 Resultados da Previsão")

# Criar colunas para exibir os resultados
col1, col2 = st.columns(2)

with col1:
    st.subheader("Classificação de Risco")
    if prediction == 1:
        st.error("🚨 **ALTO RISCO** de Defasagem")
        risk_level = "Alto Risco"
        risk_color = "red"
    else:
        st.success("✅ **BAIXO RISCO** de Defasagem")
        risk_level = "Baixo Risco"
        risk_color = "green"

with col2:
    st.subheader("Probabilidade de Risco")
    risk_probability = prediction_proba[1] * 100
    st.metric(label="Probabilidade de Alto Risco", value=f"{risk_probability:.1f}%")

# Exibir a interpretação do modelo
st.markdown("---")
st.header("🔍 Interpretação do Modelo")

st.markdown("""
O modelo de Regressão Logística utiliza os seguintes indicadores para fazer a previsão:

- **IDA (Desempenho Acadêmico)**: Quanto maior, menor o risco de defasagem.
- **IEG (Engajamento)**: Quanto maior, menor o risco de defasagem.
- **IPS (Aspectos Psicossociais)**: Tem impacto mínimo no risco.
- **IPP (Aspectos Psicopedagógicos)**: Quanto maior, menor o risco de defasagem.
- **IAA (Autoavaliação)**: Quanto maior, menor o risco de defasagem.
- **Ano**: Anos mais recentes tendem a ter menor risco (melhoria do programa).
""")

# Exibir os dados de entrada
st.markdown("---")
st.header("📝 Dados de Entrada")

input_df = pd.DataFrame({
    'Indicador': ['IDA', 'IEG', 'IPS', 'IPP', 'IAA', 'Ano'],
    'Valor': [ida, ieg, ips, ipp, iaa, ano]
})

st.table(input_df)

# Informações adicionais
st.markdown("---")
st.header("ℹ️ Informações Adicionais")

st.markdown("""
### Sobre o Modelo
- **Tipo**: Regressão Logística
- **Variável Alvo**: Risco de Defasagem (1 se IAN < 7.0, 0 caso contrário)
- **Acurácia**: ~57%
- **AUC Score**: 0.6074

### Sobre os Indicadores
- **IAN (Indicador de Adequação do Nível)**: Mede a defasagem educacional do aluno.
- **IDA (Indicador de Desempenho Acadêmico)**: Avalia o desempenho nas disciplinas.
- **IEG (Indicador de Engajamento)**: Mede o envolvimento do aluno nas atividades.
- **IPS (Indicador de Aspectos Psicossociais)**: Avalia o bem-estar emocional e social.
- **IPP (Indicador de Aspectos Psicopedagógicos)**: Avalia o desenvolvimento psicopedagógico.
- **IAA (Indicador de Autoavaliação)**: Mede a percepção do aluno sobre si mesmo.

### Próximos Passos
Para melhorar o modelo, recomenda-se:
1. Coletar mais dados históricos.
2. Explorar modelos mais complexos (Random Forest, Gradient Boosting).
3. Realizar feature engineering mais avançado.
4. Implementar validação cruzada.
""")

# Rodapé
st.markdown("---")
st.markdown("""
**Desenvolvido por**: Manus AI | **Projeto**: Datathon - Passos Mágicos | **Fase**: 5
""")
