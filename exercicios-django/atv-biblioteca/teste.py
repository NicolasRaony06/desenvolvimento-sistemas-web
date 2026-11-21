from pathlib import Path

arquivo = Path(r'E:\Documents\desenvolvimento\desenvolvimento-sistemas-web\exercicios-django\atv-biblioteca\dados.json')

conteudo = arquivo.read_text(encoding='utf-16')

arquivo.write_text(conteudo, encoding='utf-8')