saida = ''


def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b


def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao' or operacao.lower() == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao' or operacao.lower() == 'subtração':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao' or operacao.lower() == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao' or operacao.lower() == 'divisão':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado


while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input(
            "Digite a operação desejada (+, -, *, / ou nome da operação): ")

        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Entrada inválida! Por favor, digite números válidos.")

    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado.")
