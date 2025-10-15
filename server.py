#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor HTTP simples para o questionário
Execute com: python server.py
"""

import http.server
import socketserver
import os
import json
from datetime import datetime

PORT = 5000

def encontrar_porta_livre(porta_inicial=5000):
    """Encontra uma porta livre começando da porta inicial"""
    import socket
    porta = porta_inicial
    while porta < porta_inicial + 100:  # Tenta até 100 portas
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', porta))
                return porta
        except OSError:
            porta += 1
    return porta_inicial  # Fallback

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers CORS para permitir requisições
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        """Lidar com requisições GET"""
        if self.path == '/api/responses':
            try:
                # Ler respostas do arquivo
                responses_file = 'respostas.json'
                responses = []
                
                if os.path.exists(responses_file):
                    with open(responses_file, 'r', encoding='utf-8') as f:
                        try:
                            responses = json.load(f)
                        except:
                            responses = []
                
                # Enviar resposta JSON
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(responses, ensure_ascii=False).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': str(e)
                }).encode())
        elif self.path == '/' or self.path == '/index':
            # Servir página de navegação como página inicial
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            try:
                with open('navegacao.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                self.wfile.write(content.encode('utf-8'))
            except FileNotFoundError:
                self.wfile.write(b'<h1>Arquivo navegacao.html nao encontrado</h1>')
        else:
            # Servir arquivos estáticos normalmente
            super().do_GET()

    def do_POST(self):
        """Lidar com requisições POST para salvar respostas"""
        if self.path == '/api/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Decodificar dados JSON
                data = json.loads(post_data.decode('utf-8'))
                
                # Adicionar timestamp
                data['timestamp'] = datetime.now().isoformat()
                
                # Salvar em arquivo JSON
                responses_file = 'respostas.json'
                responses = []
                
                # Ler respostas existentes
                if os.path.exists(responses_file):
                    with open(responses_file, 'r', encoding='utf-8') as f:
                        try:
                            responses = json.load(f)
                        except:
                            responses = []
                
                # Adicionar nova resposta
                responses.append(data)
                
                # Salvar arquivo atualizado
                with open(responses_file, 'w', encoding='utf-8') as f:
                    json.dump(responses, f, ensure_ascii=False, indent=2)
                
                # Enviar resposta de sucesso
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': True,
                    'message': 'Resposta salva com sucesso!'
                }).encode())
                
                print(f"[OK] Nova resposta salva! Total: {len(responses)}")
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'success': False,
                    'message': str(e)
                }).encode())
                print(f"[ERRO] Erro ao salvar resposta: {e}")
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        """Lidar com requisições OPTIONS para CORS"""
        self.send_response(200)
        self.end_headers()

def main():
    # Mudar para o diretório do script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Encontrar porta livre
    porta_usada = encontrar_porta_livre(PORT)
    
    with socketserver.TCPServer(("0.0.0.0", porta_usada), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print(f"[OK] Servidor rodando em: http://localhost:{porta_usada}")
        print(f"[OK] Acesse o questionario: http://localhost:{porta_usada}/index.html")
        print(f"[OK] Acesse o dashboard: http://localhost:{porta_usada}/dashboard.html")
        print(f"[OK] Acesso externo: http://192.168.0.14:{porta_usada}")
        print("=" * 60)
        print("\n[INFO] As respostas serao salvas em: respostas.json")
        print("\n[AVISO] Para criar um tunel publico, use:")
        print(f"   ngrok http {porta_usada}")
        print("\n   Pressione Ctrl+C para parar o servidor\n")
        print("=" * 60)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n[OK] Servidor encerrado!")

if __name__ == "__main__":
    main()

