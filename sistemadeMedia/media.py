from time import sleep

alunos = []
medias = []
notas = []
print("---------- CADASTRO DE ALUNOS ----------")
input("Pressione ENTER para começar...")
sleep(1)
print("\nSistema de Cadastro de Alunos\n")

while True:
    nome = input("Digite o nome do aluno: ")
    print(f"O aluno {nome} foi cadastrado com sucesso!")
    alunos.append(nome)
    sleep(1)

    notas = []

    i = 0
    while i < 3:
        try:
            nota = float(input(f"Digite a {i + 1}° nota: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                i += 1
            else:
                print("Digite uma nota entre 0 e 10")
        except ValueError:
            print("Digite um numero")

    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "Aprovado!"
    elif media >= 5:
        situacao = "Recuperação!"
    else:
        situacao = "Reprovado!"

    medias.append(media)
    print(f"Média do aluno {nome}: {media:.1f} -- Situação: {situacao}")

    escolha = input("Deseja continuar? (S/N): ").upper()

    if escolha == "S":
        print("Adicionando outro aluno...")
        continue
    elif escolha == "N":
        print("Sistema encerrado!")
        print(f"Alunos cadastrados: {alunos}")
        print(f"Quantidade de alunos cadastrados: {len(alunos)}")
        print(f"Maior média: {max(medias):.1f}")
        print(f"Menor média: {min(medias):.1f}")
        break
    else:
        print("Opção inválida, encerrando...")
        break
