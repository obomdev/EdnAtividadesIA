# Exercício 1: Calculadora com tratamento de erros
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        oper = input("Escolha a operação (+, -, *, /): ")
        if oper == "+":
            resultado = num1 + num2
        elif oper == "-":
            resultado = num1 - num2
        elif oper == "*":
            resultado = num1 * num2
        elif oper == "/":
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")
        print(f"Resultado: {resultado}")
        break
    except ValueError as ve:
        print("Erro de valor:", ve)
    except ZeroDivisionError as zde:
        print("Erro de divisão:", zde)
