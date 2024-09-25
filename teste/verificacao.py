def contar_a(string):
    quantidade = string.lower().count('a')
    if quantidade > 0:
        print(f"A letra 'a' ocorre {quantidade} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

texto = input("Informe uma string: ")
contar_a(texto)
