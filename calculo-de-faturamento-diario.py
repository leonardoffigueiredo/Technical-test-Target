import json
from statistics import mean

dados_json = '''
[
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
]
'''

dados = json.loads(dados_json)

valores = [d["valor"] for d in dados if d["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = mean(valores)
dias_acima_da_media = sum(1 for v in valores if v > media_mensal)

print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
