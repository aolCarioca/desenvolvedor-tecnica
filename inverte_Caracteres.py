# Função para inverter a string
def inverter_string(s):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""
    
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

# Função principal
def main():
    # Entrada de string
    string = input("Informe uma string para inverter: ")
    
    # Chama a função para inverter a string
    resultado = inverter_string(string)
    
    # Exibe o resultado
    print(f"String invertida: {resultado}")

if __name__ == "__main__":
    main()
