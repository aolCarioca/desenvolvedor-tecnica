json

{
  "faturamento": [
    {"dia": 1, "faturamento": 200},
    {"dia": 2, "faturamento": 300},
    {"dia": 3, "faturamento": 0},
    {"dia": 4, "faturamento": 500},
    {"dia": 5, "faturamento": 450},
    {"dia": 6, "faturamento": 0},
    {"dia": 7, "faturamento": 600}
  ]
}

import json

# Função para calcular as métricas
def calcular_faturamento(faturamento_diario):
    # Filtra os dias com faturamento maior que 0
    dias_com_faturamento = [faturamento['faturamento'] for faturamento in faturamento_diario if faturamento['faturamento'] > 0]
    
    if not dias_com_faturamento:
        return None, None, 0  # Caso não haja dias com faturamento, retorna 0 para o número de dias
    
    # Calculando o menor e maior valor de faturamento
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    
    # Calculando a média mensal (excluindo os dias com faturamento 0)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    
    # Contando o número de dias em que o faturamento foi superior à média mensal
    dias_acima_da_media = sum(1 for faturamento in dias_com_faturamento if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Lendo o arquivo JSON
def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

# Função principal
def main():
    # Caminho para o arquivo JSON (modifique conforme necessário)
    caminho_arquivo = 'faturamento.json'
    
    # Lê os dados do faturamento a partir do arquivo JSON
    dados = ler_arquivo_json(caminho_arquivo)
    
    # Calculando as métricas
    menor_faturamento, maior_faturamento, dias_acima_media = calcular_faturamento(dados['faturamento'])
    
    # Exibindo os resultados
    if menor_faturamento is not None:
        print(f"Menor valor de faturamento: {menor_faturamento}")
        print(f"Maior valor de faturamento: {maior_faturamento}")
        print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
    else:
        print("Não há dias com faturamento.")

if __name__ == "__main__":
    main()
