nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total de vendas: "))

comissao = vendas * 0.15
total = salario_fixo + comissao

print("Total a receber do vendedor " + nome + ": R$ " + format(total, ".2f"))
