@echo off
chcp 65001 >nul
title Servidor do Questionário PIBETX

echo.
echo ============================================================
echo     QUESTIONÁRIO PIBETX 2024/2025
echo ============================================================
echo.
echo Iniciando servidor na porta 5000...
echo.

python server.py

pause

