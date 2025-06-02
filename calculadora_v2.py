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
    else:
        return a / b

def calculadora(num1, num2, op):
    op = op.lower()
    if op in ['+', 'adicao', 'adição', 'soma']:
        return adicao(num1, num2)
    elif op in ['-', 'subtracao', 'subtração', 'subtrair']:
        return subtracao(num1, num2)
    elif op in ['*', 'multiplicacao', 'multiplicação', 'multiplicar']:
        return multiplicacao(num1, num2)
    elif op in ['/', 'divisao', 'divisão', 'dividir']:
        return divisao(num1, num2)
    else:
        return "Operação inválida"

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    
    op = input("Digite a operação (+, -, *, /) ou o nome da operação: ")
    resultado = calculadora(num1, num2, op)
    print(f"Resultado da operação: {resultado}")
    
    saida = input("Deseja continuar? (S/N): ")
    while saida.lower() not in ['s', 'n']:
        saida = input("Resposta inválida. Deseja continuar? (S/N): ")

print("Programa encerrado.")
