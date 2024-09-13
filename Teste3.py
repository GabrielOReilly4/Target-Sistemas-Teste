import json

with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

faturamentos_validos = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

menor_faturamento = min(faturamentos_validos)

maior_faturamento = max(faturamentos_validos)

media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

dias_acima_da_media = [dia for dia in faturamentos_validos if dia > media_mensal]
numero_dias_acima_media = len(dias_acima_da_media)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {numero_dias_acima_media}")
