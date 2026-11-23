#!/usr/bin/env python3
"""Baixa para a pasta assets/ todas as imagens que hoje estão hospedadas no Landingi.
Roda sozinho no GitHub (Actions) — não precisa executar no seu computador."""
import json, os, urllib.request

lista = json.load(open('assets-lista.json', encoding='utf-8'))
os.makedirs('assets', exist_ok=True)
ok = falhas = 0
for item in lista:
    destino = item['arquivo']
    if os.path.exists(destino) and os.path.getsize(destino) > 0:
        continue
    try:
        req = urllib.request.Request(item['url'], headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=60) as r:
            dados = r.read()
        with open(destino, 'wb') as f:
            f.write(dados)
        ok += 1
        print('OK   ', destino)
    except Exception as e:
        falhas += 1
        print('FALHA', item['url'], e)
print(f'{ok} baixadas, {falhas} falhas')
