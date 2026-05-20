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
        return "Fale um numero positivo."
    return sqrt(num)

while True:
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciar")
    print("6. Raiz quadrada")
    print()
    try:
        escolha = int(input("Qual opção você quer: "))
        if 1<= escolha <=5:
            num1, num2 = dois_numeros()
        match escolha:

            case 1:
                print(soma(num1, num2))
            case 2:
                print(subtracao(num1, num2))
            case 3:
                print(multiplicacao(num1, num2))
            case 4:
                print(divisao(num1, num2))
            case 5:
                print(potencia(num1, num2))
            case 6:
                numero = float(input("Fale qual numero voce quer a raiz quadrada: "))
                print(raiz_quadrada(numero))
            case _:
                print("Escolha uma das opções acima.")

        continuar = input("Deseja continuar(S/N): ").upper()
        if continuar == "N":
            print("Tchau tchau!!")
            break
        elif continuar != "S":
            print("Digite S ou N.")
            sleep(2)
            continue
    except ValueError:
        print("Digite uma das opções acima.")
        sleep(2)