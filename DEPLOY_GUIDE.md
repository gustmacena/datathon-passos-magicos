# Guia de Deploy no Streamlit Community Cloud

## ✅ Pré-requisitos Concluídos

Todos os arquivos de configuração necessários já foram adicionados ao repositório GitHub:

- ✅ `requirements.txt` - Dependências Python
- ✅ `.streamlit/config.toml` - Configuração do tema
- ✅ `app/app_streamlit.py` - Aplicação principal
- ✅ `models/gradient_boosting_model.pkl` - Modelo treinado
- ✅ `models/scaler.pkl` - Scaler para normalização
- ✅ `README.md` - Documentação completa

## 🚀 Passos para Deploy (2 minutos)

### 1. Acesse o Streamlit Community Cloud

Acesse: [https://share.streamlit.io/](https://share.streamlit.io/)

### 2. Faça Login com GitHub

- Clique em **"Sign in with GitHub"**
- Autorize o acesso do Streamlit ao seu GitHub

### 3. Crie um Novo App

- Clique em **"New app"**
- Selecione as seguintes configurações:

```
Repository: gustmacena/datathon-passos-magicos
Branch: main
Main file path: app/app_streamlit.py
App URL (opcional): datathon-passos-magicos
```

### 4. Deploy Avançado (Opcional)

Se você quiser personalizar a URL ou configurações avançadas:

- Clique em **"Advanced settings"**
- Python version: `3.11`
- Secrets: (não necessário para este projeto)

### 5. Clique em "Deploy!"

O Streamlit Cloud irá:
1. Clonar o repositório
2. Instalar as dependências do `requirements.txt`
3. Iniciar a aplicação
4. Fornecer uma URL pública

**Tempo estimado**: 2-3 minutos

### 6. Teste a Aplicação

Após o deploy, você receberá uma URL como:
```
https://datathon-passos-magicos.streamlit.app
```

Teste a aplicação inserindo valores nos sliders e verificando as predições.

## 🔧 Troubleshooting

### Erro: "ModuleNotFoundError"

**Causa**: Dependência faltando no `requirements.txt`

**Solução**: 
```bash
# Adicione a dependência ao requirements.txt
echo "nome-do-pacote==versao" >> requirements.txt
git add requirements.txt
git commit -m "Adiciona dependência faltante"
git push origin main
```

O Streamlit Cloud irá automaticamente redesenhar a aplicação.

### Erro: "FileNotFoundError: models/..."

**Causa**: Arquivos do modelo não estão no repositório

**Solução**:
```bash
# Verifique se os arquivos existem
ls -la models/

# Se não existirem, adicione-os
git add models/gradient_boosting_model.pkl models/scaler.pkl
git commit -m "Adiciona modelos treinados"
git push origin main
```

### Aplicação Lenta ou Timeout

**Causa**: Modelo muito grande ou processamento pesado

**Solução**: 
- Use `@st.cache_resource` para carregar o modelo uma única vez
- Otimize o código de predição
- Considere usar um modelo mais leve

## 📊 Monitoramento

Após o deploy, você pode:

- **Ver logs em tempo real**: Clique em "Manage app" → "Logs"
- **Reiniciar a aplicação**: Clique em "Reboot app"
- **Atualizar automaticamente**: Qualquer push para `main` irá redesenhar

## 🔒 Segurança

Para este projeto educacional, não há dados sensíveis. Em projetos futuros:

- Use **Secrets** no Streamlit Cloud para API keys
- Adicione autenticação se necessário
- Configure variáveis de ambiente

## 📝 Notas Importantes

1. **Limite de recursos**: O Streamlit Community Cloud tem limites de CPU/RAM. Para aplicações maiores, considere o plano pago.
2. **Inatividade**: Apps inativos por 7 dias podem entrar em "sleep mode" e levar alguns segundos para acordar.
3. **Atualizações automáticas**: Qualquer commit na branch `main` irá redesenhar automaticamente.

## ✅ Checklist Final

- [ ] Login no Streamlit Cloud com GitHub
- [ ] Criar novo app apontando para `app/app_streamlit.py`
- [ ] Aguardar o deploy (2-3 minutos)
- [ ] Testar a aplicação com dados de exemplo
- [ ] Compartilhar a URL com a equipe

---

**Pronto!** Sua aplicação estará disponível publicamente e pronta para uso pela equipe da Passos Mágicos.
