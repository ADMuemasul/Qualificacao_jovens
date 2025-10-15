@echo off
chcp 65001 >nul
title Sistema PIBETX - Questionario e Dashboard

echo.
echo ════════════════════════════════════════════════════════════
echo     SISTEMA PIBETX 2024/2025 - QUESTIONARIO E DASHBOARD
echo ════════════════════════════════════════════════════════════
echo.
echo [INFO] Iniciando servidor...
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo [OK] Servidor iniciado com sucesso!
echo.
echo 📋 PAGINAS DISPONIVEIS:
echo    • http://localhost:5000/          - Menu principal
echo    • http://localhost:5000/index.html - Questionario
echo    • http://localhost:5000/dashboard.html - Dashboard
echo.
echo 📊 FUNCIONALIDADES:
echo    • Questionario interativo com Vue.js
echo    • Dashboard com graficos em tempo real
echo    • Exportacao para CSV e JSON
echo    • Atualizacao automatica a cada 30 segundos
echo.
echo 🌍 PARA COMPARTILHAR:
echo    1. Execute: ngrok http 5000
echo    2. Copie o link publico gerado
echo    3. Compartilhe com os participantes
echo.
echo ════════════════════════════════════════════════════════════
echo.

python server.py

pause
