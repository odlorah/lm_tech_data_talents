from funcoes import soma
from funcoes import subtracao
from funcoes import multiplicacao
from funcoes import divisao

def calcule():
    while True:
        try:
            a = float(input("Digite um número inteiro para a: "))
            b = float(input("Digite um número decimal para b: "))
        except ValueError:
            print("Erro: a entrada não é um número inteiro ou decimal. Tente novamente.")
        else:
            break

    while True:
        print("Digite a operação desejada (+, -, *, / ou nome da operação):")
        operacao = input()
        if operacao in ['+', '-', '*', '/', 'soma', 'subtracao', 'multiplicacao', 'divisao']:
            break
        print("Operação inválida. Tente novamente.")


    if operacao == '+' or operacao == 'soma':
        resultado = soma(a, b)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(a, b)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(a, b)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(a, b)
        if resultado == 0:
            print("A divisão é inválida")
            
    return resultado