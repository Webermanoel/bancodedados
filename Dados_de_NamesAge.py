def introduction_bank():
    print("###################################################")
    print("Bem-vindo ao armazenador de dados NamesAge ")
    print("###################################################\n")


def armazenador_nomes():
    names = []

    while len(names) < 5:
        nome = input(f"Digite um nome ({len(names) + 1}/5): ").strip()

        if nome == "":
            print("Nome inválido! Tente novamente.")
            continue

        names.append(nome)
        print(f"Nome '{nome}' armazenado com sucesso!\n")

    print("\nVocê atingiu o limite de 5 nomes.")
    return names


def armazenador_idades():
    idades = []

    while len(idades) < 5:
        try:
            idade = int(input(f"Digite uma idade ({len(idades) + 1}/5): "))

            if idade < 0:
                print("Idade não pode ser negativa! Tente novamente.")
                continue

            idades.append(idade)
            print(f"Idade '{idade}' armazenada com sucesso!\n")

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    print("\nVocê atingiu o limite de 5 idades.")
    return idades

introduction_bank()

nomes = armazenador_nomes()
idades = armazenador_idades()

print("\nSua lista com nomes e idades é:\n")
for i in range(5):
    print(f"{i+1}. Nome: {nomes[i]} | Idade: {idades[i]}")
