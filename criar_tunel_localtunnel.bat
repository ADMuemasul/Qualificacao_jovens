@echo off
chcp 65001 >nul
title Túnel Público - LocalTunnel

echo.
echo ════════════════════════════════════════════════════════════
echo     CRIANDO TÚNEL PÚBLICO COM LOCALTUNNEL
echo ════════════════════════════════════════════════════════════
echo.
echo ⚠️  IMPORTANTE: O servidor deve estar rodando primeiro!
echo.
echo ⚠️  REQUER NODE.JS INSTALADO!
echo    Baixe em: https://nodejs.org/
echo.
echo Instalando localtunnel (primeira vez)...
call npm install -g localtunnel
echo.
echo Criando túnel...
echo.
echo ════════════════════════════════════════════════════════════
echo.

lt --port 5000

pause

