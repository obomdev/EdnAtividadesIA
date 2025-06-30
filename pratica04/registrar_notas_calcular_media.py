# Exercício 2: Registro de notas e cálculo de média
notas = []
while True:
    entrada = input("Digite uma nota de 0 a 10 (ou 'fim' para encerrar): ").strip().lower()
    if entrada == "fim":
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número de 0 a 10 ou 'fim'.")
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
