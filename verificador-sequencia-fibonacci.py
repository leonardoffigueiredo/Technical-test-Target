def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
