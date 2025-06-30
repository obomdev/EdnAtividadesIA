# Exercício 3: Validação de senha forte
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        print("Programa encerrado sem senha válida.")
        break
    if len(senha) >= 8 and any(car.isdigit() for car in senha):
        print("Senha válida!")
        break
    else:
        print("Senha fraca. Precisa ter ≥8 caracteres e pelo menos um número.")
