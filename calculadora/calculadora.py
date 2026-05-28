from math import sqrt
from time import sleep

print("------------Calculadora------------")

def dois_numeros():
    n1 = float(input("Fale o 1° número: "))
    n2 = float(input("Fale o 2° número: "))
    return n1, n2

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(num):
    if num < 0:
        return "Fale um número positivo."
    return sqrt(num)

while True:

    print("\n1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciar")
    print("6. Raiz quadrada")

    try:
        escolha = int(input("\nQual opção você quer: "))

        match escolha:

            case 1:
                num1, num2 = dois_numeros()
                print(soma(num1, num2))

            case 2:
                num1, num2 = dois_numeros()
                print(subtracao(num1, num2))

            case 3:
                num1, num2 = dois_numeros()
                print(multiplicacao(num1, num2))

            case 4:
                num1, num2 = dois_numeros()
                print(divisao(num1, num2))

            case 5:
                num1, num2 = dois_numeros()
                print(potencia(num1, num2))

            case 6:
                numero = float(input("Fale qual número você quer a raiz quadrada: "))
                print(raiz_quadrada(numero))

            case _:
                print("Escolha uma opção válida.")
                continue

        while True:
            continuar = input("Deseja continuar (S/N): ").upper()

            if continuar == "S":
                break

            elif continuar == "N":
                print("Tchau tchau!!")
                exit()
            else:
                print("Digite apenas S ou N.")

    except ValueError:
        print("Digite valores válidos.")
        sleep(2)