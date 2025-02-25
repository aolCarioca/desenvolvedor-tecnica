def fibonacci(numero):
    """
    Gera a sequência de Fibonacci até o número informado.
    """
    seq = [0, 1]
    while seq[-1] < numero:
        seq.append(seq[-1] + seq[-2])
    return seq

def pertence_fibonacci(numero):
    """
    Verifica se o número informado pertence à sequência de Fibonacci.
    """
    seq = fibonacci(numero)
    return numero in seq

# Entrada do usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificação e resultado
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

