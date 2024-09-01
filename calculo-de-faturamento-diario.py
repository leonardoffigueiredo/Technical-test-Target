import json

dados_json = '''
[
  {"dia": 1, "valor": 1000.0},
  {"dia": 2, "valor": 0.0},
  {"dia": 3, "valor": 1500.0},
  {"dia": 4, "valor": 0.0},
  {"dia": 5, "valor": 2000.0}
]
'''

dados = json.loads(dados_json)

valores = [d["valor"] for d in dados if d["valor"] > 0]  

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for v in valores if v > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
