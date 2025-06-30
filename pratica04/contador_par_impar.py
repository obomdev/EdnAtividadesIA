# Exercício 4: Par ou ímpar até “fim” e contagem
cont_par = 0
cont_impar = 0
while True:
    entrada = input("Digite um inteiro (ou 'fim' para encerrar): ").strip().lower()
    if entrada == "fim":
        break
    try:
        n = int(entrada)
        if n % 2 == 0:
            print(f"{n} é par.")
            cont_par += 1
        else:
            print(f"{n} é ímpar.")
            cont_impar += 1
    except ValueError:
        print("Erro: não é um inteiro. Tente novamente.")
print(f"Total de pares: {cont_par}")
print(f"Total de ímpares: {cont_impar}")
