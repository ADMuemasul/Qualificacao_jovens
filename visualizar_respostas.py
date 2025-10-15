#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para visualizar as respostas do questionário
Execute com: python visualizar_respostas.py
"""

import json
import os
from collections import Counter
from datetime import datetime

def carregar_respostas():
    """Carrega as respostas do arquivo JSON"""
    if not os.path.exists('respostas.json'):
        print("[ERRO] Arquivo respostas.json nao encontrado!")
        print("   As respostas aparecerao aqui apos alguem responder o questionario.")
        return []
    
    try:
        with open('respostas.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERRO] Erro ao ler respostas: {e}")
        return []

def mostrar_estatisticas(respostas):
    """Mostra estatísticas das respostas"""
    if not respostas:
        print("\n[INFO] Nenhuma resposta recebida ainda.")
        return
    
    print("\n" + "="*70)
    print(f"[INFO] ESTATISTICAS DO QUESTIONARIO - Total: {len(respostas)} respostas")
    print("="*70)
    
    # Questão 1: Ferramenta mais importante
    print("\n1. Ferramenta mais importante:")
    q1_map = {
        'word': 'Word (textos e normas ABNT)',
        'excel': 'Excel (planilhas e organização de dados)',
        'powerpoint': 'PowerPoint (apresentações criativas)',
        'powerbi': 'Power BI (análise de dados e dashboards)'
    }
    q1_counts = Counter([r['q1'] for r in respostas])
    for opcao, count in q1_counts.most_common():
        percent = (count / len(respostas)) * 100
        print(f"   {q1_map.get(opcao, opcao)}: {count} ({percent:.1f}%)")
    
    # Questão 2: Nível de satisfação
    print("\n2. Nivel de satisfacao geral:")
    q2_counts = Counter([r['q2'] for r in respostas])
    q2_labels = {
        '1': '1 - Muito Insatisfeito',
        '2': '2 - Insatisfeito',
        '3': '3 - Neutro',
        '4': '4 - Satisfeito',
        '5': '5 - Muito Satisfeito'
    }
    for nivel in ['5', '4', '3', '2', '1']:
        count = q2_counts.get(nivel, 0)
        percent = (count / len(respostas)) * 100 if len(respostas) > 0 else 0
        print(f"   {q2_labels[nivel]}: {count} ({percent:.1f}%)")
    
    # Média de satisfação
    try:
        media = sum([int(r['q2']) for r in respostas]) / len(respostas)
        print(f"   [INFO] Media: {media:.2f}/5.0")
    except:
        pass
    
    # Questão 3: Atendeu expectativas
    print("\n3. O curso atendeu as expectativas:")
    q3_map = {
        'superou': 'Sim, superou minhas expectativas',
        'totalmente': 'Sim, atendeu totalmente',
        'parcialmente': 'Parcialmente',
        'nao': 'Não, não atendeu'
    }
    q3_counts = Counter([r['q3'] for r in respostas])
    for opcao, count in q3_counts.most_common():
        percent = (count / len(respostas)) * 100
        print(f"   {q3_map.get(opcao, opcao)}: {count} ({percent:.1f}%)")
    
    # Questão 4: Recomendaria
    print("\n4. Recomendaria o curso:")
    q4_counts = Counter([r['q4'] for r in respostas])
    sim = q4_counts.get('sim', 0)
    nao = q4_counts.get('nao', 0)
    percent_sim = (sim / len(respostas)) * 100 if len(respostas) > 0 else 0
    print(f"   [OK] Sim: {sim} ({percent_sim:.1f}%)")
    print(f"   [NO] Nao: {nao} ({100-percent_sim:.1f}%)")
    
    # Questão 5: Carga horária
    print("\n5. Carga horaria (30h):")
    q5_map = {
        'suficiente': 'Sim, foi suficiente',
        'curta': 'Não, achei muito curta',
        'longa': 'Não, achei muito longa'
    }
    q5_counts = Counter([r['q5'] for r in respostas])
    for opcao, count in q5_counts.most_common():
        percent = (count / len(respostas)) * 100
        print(f"   {q5_map.get(opcao, opcao)}: {count} ({percent:.1f}%)")
    
    # Questão 6: Avaliação dos instrutores
    print("\n6. Avaliacao dos instrutores:")
    
    print("   [INFO] Conhecimento do assunto:")
    q6a_counts = Counter([r['q6a'] for r in respostas])
    for nivel in ['otimo', 'bom', 'regular', 'ruim']:
        count = q6a_counts.get(nivel, 0)
        percent = (count / len(respostas)) * 100 if len(respostas) > 0 else 0
        print(f"      {nivel.capitalize()}: {count} ({percent:.1f}%)")
    
    print("   [INFO] Clareza na comunicacao:")
    q6b_counts = Counter([r['q6b'] for r in respostas])
    for nivel in ['otimo', 'bom', 'regular', 'ruim']:
        count = q6b_counts.get(nivel, 0)
        percent = (count / len(respostas)) * 100 if len(respostas) > 0 else 0
        print(f"      {nivel.capitalize()}: {count} ({percent:.1f}%)")
    
    print("   [INFO] Atencao para tirar duvidas:")
    q6c_counts = Counter([r['q6c'] for r in respostas])
    for nivel in ['otimo', 'bom', 'regular', 'ruim']:
        count = q6c_counts.get(nivel, 0)
        percent = (count / len(respostas)) * 100 if len(respostas) > 0 else 0
        print(f"      {nivel.capitalize()}: {count} ({percent:.1f}%)")
    
    # Questão 7: Materiais
    print("\n7. Materiais didaticos:")
    q7_map = {
        'muito_uteis': 'Sim, muito úteis',
        'poderiam_melhorar': 'Sim, mas poderiam ser melhores',
        'nao_uteis': 'Não foram muito úteis'
    }
    q7_counts = Counter([r['q7'] for r in respostas])
    for opcao, count in q7_counts.most_common():
        percent = (count / len(respostas)) * 100
        print(f"   {q7_map.get(opcao, opcao)}: {count} ({percent:.1f}%)")
    
    # Questão 8: Estrutura
    print("\n8. Estrutura do laboratorio:")
    q8_map = {
        'adequada': 'Sim, atendeu todas as necessidades',
        'dificuldades': 'Sim, mas com algumas dificuldades',
        'inadequada': 'Não, a estrutura atrapalhou'
    }
    q8_counts = Counter([r['q8'] for r in respostas])
    for opcao, count in q8_counts.most_common():
        percent = (count / len(respostas)) * 100
        print(f"   {q8_map.get(opcao, opcao)}: {count} ({percent:.1f}%)")
    
    # Timestamps
    print("\n[INFO] Periodo de respostas:")
    timestamps = [datetime.fromisoformat(r['timestamp'].replace('Z', '+00:00')) for r in respostas if 'timestamp' in r]
    if timestamps:
        print(f"   Primeira resposta: {min(timestamps).strftime('%d/%m/%Y %H:%M')}")
        print(f"   Ultima resposta: {max(timestamps).strftime('%d/%m/%Y %H:%M')}")
    
    # Lista de participantes
    print("\n[INFO] Participantes:")
    for i, resposta in enumerate(respostas, 1):
        nome = resposta.get('nome', 'Nome nao informado')
        data = resposta.get('timestamp', 'Data nao disponivel')
        try:
            if data != 'Data nao disponivel':
                data_obj = datetime.fromisoformat(data.replace('Z', '+00:00'))
                data_formatada = data_obj.strftime('%d/%m/%Y %H:%M')
            else:
                data_formatada = data
        except:
            data_formatada = 'Data invalida'
        
        print(f"   {i}. {nome} - {data_formatada}")
    
    print("\n" + "="*70)

def exportar_csv(respostas):
    """Exporta respostas para CSV"""
    if not respostas:
        return
    
    try:
        import csv
        
        with open('respostas.csv', 'w', newline='', encoding='utf-8-sig') as f:
            if not respostas:
                return
            
            # Obter todos os campos únicos de todas as respostas
            todos_campos = set()
            for resposta in respostas:
                todos_campos.update(resposta.keys())
            
            # Ordenar campos para ter ordem consistente
            campos_ordenados = sorted(todos_campos)
            
            writer = csv.DictWriter(f, fieldnames=campos_ordenados)
            writer.writeheader()
            writer.writerows(respostas)
        
        print("\n[OK] Arquivo respostas.csv criado com sucesso!")
        print("   Voce pode abrir no Excel ou Google Sheets")
    except Exception as e:
        print(f"\n[AVISO] Erro ao criar CSV: {e}")

def main():
    print("\n" + "="*70)
    print(" [INFO] VISUALIZADOR DE RESPOSTAS - QUESTIONARIO PIBETX 2024/2025")
    print("="*70)
    
    respostas = carregar_respostas()
    mostrar_estatisticas(respostas)
    
    if respostas:
        exportar_csv(respostas)
    
    print("\n[INFO] Dica: Execute este script novamente para ver atualizacoes!")
    print()

if __name__ == "__main__":
    main()

