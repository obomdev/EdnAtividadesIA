nota1 = float(input("Digite a nota N1: "))
nota2 = float(input("Digite a nota N2: "))
nota3 = float(input("Digite a nota N3: "))
nota4 = float(input("Digite a nota N4: "))

media = (nota1*2 + nota2*3 + nota3*4 + nota4*1) / 10
print("Media: " + str(round(media, 1)))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print("Nota do exame: " + str(round(nota_exame, 1)))
    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
        
    else:
        print("Aluno reprovado.")
    print("Media final: " + str(round(media_final, 1)))
