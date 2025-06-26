numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

salario = horas_trabalhadas * valor_por_hora

print(f"Funcionário: {numero_funcionario}")
print(f"Salário: R$ {salario:.2f}")
