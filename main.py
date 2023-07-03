var = "OLá"


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):

    return a / b


print("""Digite dois números:""")


numero1 = float(input())


numero2 = float(input())


print("A soma dos números é: ", soma(numero1, numero2))
print("A subtração dos números é: ", subtracao(numero1, numero2))
print("A multiplicação dos números é: ", multiplicacao(numero1, numero2))
print("A divisão dos números é: ", divisao(numero1, numero2))
