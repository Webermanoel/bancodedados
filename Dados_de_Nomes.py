def introduction_bank():
    print("###################################################")
    print("Bem-vindo ao armazenador de nomes do banco de dados")
    print("###################################################\n")


introduction_bank()


def armazenador_nomes():
    names = []

    while len(names) < 10:
        nome = input(f"Digite um nome ({len(names) + 1}/10): ")

        if nome.strip() == "":
            print("Nome inválido! Tente novamente.")
            continue

        names.append(nome)

        print(f"\nNome '{nome}' armazenado com sucesso!")

    print("\nVocê atingiu o limite de 10 nomes.")
    print("Lista final de nomes armazenados:", names)


armazenador_nomes()
