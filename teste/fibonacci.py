def is_fibonacci(num):
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)
numero = int(input("Informe um número: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
