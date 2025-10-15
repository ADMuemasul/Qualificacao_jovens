# 📋 Questionário PIBETX 2024/2025

Sistema de questionário online para avaliação do curso de capacitação em ferramentas Microsoft Office.

## 🌐 GitHub Pages

Este projeto está hospedado no GitHub Pages e funciona de forma **offline** usando localStorage do navegador.

### 📱 Como Usar:

#### **1. Responder Questionário:**
- Acesse: https://admuemasul.github.io/Qualificacao_jovens/
- Preencha todas as questões
- Clique em "Enviar Avaliação"
- ✅ Dados salvos automaticamente no navegador

#### **2. Ver Dashboard:**
- Acesse: https://admuemasul.github.io/Qualificacao_jovens/dashboard.html
- Os dados aparecerão automaticamente se você respondeu o questionário
- Use "📥 Importar Dados" para carregar dados de outros navegadores

#### **3. Exportar Dados:**
- No dashboard, clique em "📊 Exportar CSV" ou "📄 Exportar JSON"
- Os arquivos serão baixados automaticamente

---

## 🔧 Para Desenvolvedores:

### **Funcionamento Offline:**
- **Questionário**: Salva respostas no localStorage
- **Dashboard**: Lê dados do localStorage
- **Exportação**: Gera arquivos CSV/JSON localmente

### **Backup de Dados:**
Para preservar dados entre sessões:
1. Responda o questionário
2. Acesse o dashboard
3. Exporte como JSON
4. Guarde o arquivo para backup

### **Importar Dados:**
Para carregar dados em outro navegador:
1. Acesse o dashboard
2. Clique em "📥 Importar Dados"
3. Selecione o arquivo JSON exportado

---

## 🚀 Versão Local (Com Servidor):

Para usar com servidor Python completo:

```bash
# Clone o repositório
git clone https://github.com/admuemasul/Qualificacao_jovens.git

# Entre na pasta
cd Qualificacao_jovens

# Execute o servidor
python server.py

# Acesse: http://localhost:5000
```

### **Funcionalidades do Servidor Local:**
- ✅ API REST completa
- ✅ Salvamento automático em JSON
- ✅ Dashboard em tempo real
- ✅ Túnel público com ngrok
- ✅ Validação inteligente

---

## 📊 Estrutura do Projeto:

```
📁 Qualificacao_jovens/
├── 📄 index.html              # Questionário principal
├── 📄 dashboard.html          # Dashboard de respostas
├── 📄 navegacao.html          # Menu de navegação
├── 🐍 server.py               # Servidor Python (local)
├── 📄 visualizar_respostas.py # Script de análise
├── 📄 respostas.json          # Dados salvos (local)
└── 📄 README_GITHUB.md        # Este arquivo
```

---

## 🎯 Tecnologias:

- **Frontend**: HTML5, CSS3, Vue.js 3, Chart.js
- **Backend**: Python (servidor local)
- **Hospedagem**: GitHub Pages (offline)
- **Dados**: localStorage + JSON

---

## 📞 Suporte:

- **GitHub Pages**: https://admuemasul.github.io/Qualificacao_jovens/
- **Repositório**: https://github.com/admuemasul/Qualificacao_jovens
- **Issues**: Use a aba Issues do GitHub

---

**Desenvolvido para o Projeto PIBETX 2024/2025 - UEMASUL** 🎓
