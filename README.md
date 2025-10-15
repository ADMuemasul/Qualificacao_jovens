# 📋 Questionário PIBETX 2024/2025

Sistema de questionário online para avaliação do curso de capacitação em ferramentas Microsoft Office.

## 🚀 Como Executar em Localhost

### Opção 1: Servidor Python (Recomendado)

1. **Certifique-se de ter Python instalado**
   ```bash
   python --version
   ```

2. **Execute o servidor**
   ```bash
   python server.py
   ```

3. **Acesse no navegador**
   ```
   http://localhost:8000/index.html
   ```

### Opção 2: Apenas HTML (sem salvamento no servidor)

Você também pode abrir o arquivo `index.html` diretamente no navegador, mas as respostas só serão salvas localmente no navegador.

## 🌍 Como Criar um Túnel Público

Para compartilhar o questionário com outras pessoas pela internet, você precisa criar um túnel público. Aqui estão 3 opções:

### Opção 1: ngrok (Mais Popular)

1. **Baixe o ngrok**
   - Acesse: https://ngrok.com/download
   - Faça o download para Windows
   - Extraia o arquivo `ngrok.exe`

2. **Execute o servidor Python**
   ```bash
   python server.py
   ```

3. **Em outro terminal, execute o ngrok**
   ```bash
   ngrok http 8000
   ```

4. **Copie o link público**
   - O ngrok vai mostrar um link como: `https://abc123.ngrok.io`
   - Compartilhe esse link com as pessoas!

**Exemplo de saída do ngrok:**
```
Session Status                online
Forwarding                    https://abc123.ngrok.io -> http://localhost:8000
```

### Opção 2: localtunnel (Grátis e sem cadastro)

1. **Instale o Node.js** (se ainda não tiver)
   - https://nodejs.org/

2. **Instale o localtunnel**
   ```bash
   npm install -g localtunnel
   ```

3. **Execute o servidor Python**
   ```bash
   python server.py
   ```

4. **Crie o túnel**
   ```bash
   lt --port 8000
   ```

5. **Compartilhe o link gerado**

### Opção 3: serveo (Sem instalação)

1. **Execute o servidor Python**
   ```bash
   python server.py
   ```

2. **Use SSH para criar o túnel** (já vem no Windows 10+)
   ```bash
   ssh -R 80:localhost:8000 serveo.net
   ```

## 📊 Como Ver as Respostas

As respostas são salvas no arquivo `respostas.json` na mesma pasta do projeto.

Você pode:
- Abrir o arquivo `respostas.json` com qualquer editor de texto
- Importar para Excel/Google Sheets
- Usar Python para analisar os dados

### Exemplo de código Python para ver as respostas:

```python
import json
import pandas as pd

# Ler respostas
with open('respostas.json', 'r', encoding='utf-8') as f:
    respostas = json.load(f)

# Converter para DataFrame
df = pd.DataFrame(respostas)

# Ver estatísticas
print(f"Total de respostas: {len(df)}")
print("\nFerramenta mais importante:")
print(df['q1'].value_counts())

# Salvar em Excel
df.to_excel('respostas.xlsx', index=False)
```

## 🔒 Dicas de Segurança

1. **Não deixe o servidor rodando permanentemente** - Use apenas durante o período de coleta
2. **ngrok grátis** - O link muda toda vez que você reinicia
3. **Túneis públicos** - Qualquer pessoa com o link pode acessar

## 📱 Funcionalidades

- ✅ Interface responsiva (funciona em celular e desktop)
- ✅ Validação de campos obrigatórios
- ✅ Salvamento automático das respostas
- ✅ Feedback visual para o usuário
- ✅ Design moderno e profissional

## 🛠️ Tecnologias Utilizadas

- HTML5
- CSS3
- Vue.js 3
- Python (servidor HTTP)

## 📞 Suporte

Se tiver problemas:
1. Verifique se o Python está instalado
2. Verifique se a porta 8000 está livre
3. Tente usar outra porta (modifique `PORT = 8000` no `server.py`)

---

**Desenvolvido para o Projeto PIBETX 2024/2025 - UEMASUL**


