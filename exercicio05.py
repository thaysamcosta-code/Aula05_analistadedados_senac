print("Digite 5 números inteiros: ")

for (contador) in range (1,6):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")
        
