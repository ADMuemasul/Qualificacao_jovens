@echo off
chcp 65001 >nul
title Túnel Público - ngrok

echo.
echo ════════════════════════════════════════════════════════════
echo     CRIANDO TÚNEL PÚBLICO COM NGROK
echo ════════════════════════════════════════════════════════════
echo.
echo ⚠️  IMPORTANTE: O servidor deve estar rodando primeiro!
echo.
echo Iniciando ngrok...
echo.
echo ════════════════════════════════════════════════════════════
echo.

ngrok http 5000

pause

