# Faturamento por estado
faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Função para calcular o faturamento total
def calcular_faturamento_total(faturamento_estado):
    return sum(faturamento_estado.values())

# Função para calcular o percentual de contribuição de cada estado
def calcular_percentual_contribuicao(faturamento_estado, faturamento_total):
    percentual_contribuicao = {}
    for estado, faturamento in faturamento_estado.items():
        percentual_contribuicao[estado] = (faturamento / faturamento_total) * 100
    return percentual_contribuicao

# Função para identificar o estado com maior e menor faturamento
def identificar_extremos(faturamento_estado):
    maior_estado = max(faturamento_estado, key=faturamento_estado.get)
    menor_estado = min(faturamento_estado, key=faturamento_estado.get)
    return maior_estado, faturamento_estado[maior_estado], menor_estado, faturamento_estado[menor_estado]

# Função principal
def main():
    # Calculando o faturamento total
    faturamento_total = calcular_faturamento_total(faturamento_estado)
    
    # Calculando os percentuais de contribuição de cada estado
    percentual_contribuicao = calcular_percentual_contribuicao(faturamento_estado, faturamento_total)
    
    # Identificando o estado com maior e menor faturamento
    maior_estado, maior_faturamento, menor_estado, menor_faturamento = identificar_extremos(faturamento_estado)
    
    # Exibindo os resultados
    print(f"Faturamento Total: R${faturamento_total:.2f}")
    print("\nPercentual de Contribuição de Cada Estado:")
    for estado, percentual in percentual_contribuicao.items():
        print(f"{estado}: {percentual:.2f}%")
    
    print(f"\nEstado com Maior Faturamento: {maior_estado} - R${maior_faturamento:.2f}")
    print(f"Estado com Menor Faturamento: {menor_estado} - R${menor_faturamento:.2f}")

if __name__ == "__main__":
    main()
