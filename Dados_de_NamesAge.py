def introduction_bank():
    print("###################################################")
    print("Bem-vindo ao armazenador de dados NamesAge ")
    print("###################################################\n")


def armazenador_nomes():
    names = []
    while len(names) < 5:
        nome = input(f"Digite um nome ou 'exit' para sair ({len(names) + 1}/5): ").strip()
        if nome.lower() == "exit":
            break
        if nome == "":
            print("Nome inválido! Tente novamente.")
            continue
        names.append(nome)
        print(f"Nome '{nome}' armazenado com sucesso!\n")

    print("\nFinalizando o armazenamento de nomes.")
    return names


def armazenador_idades():
    idades = []
    while len(idades) < 5:
        idade_input = input(f"Digite uma idade ou '1' para sair ({len(idades) + 1}/5): ").strip()

        if idade_input == "1":
            break

        try:
            idade = int(idade_input)
            if idade < 0:
                print("Idade não pode ser negativa! Tente novamente.")
                continue
            idades.append(idade)
            print(f"Idade '{idade}' armazenada com sucesso!\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    print("\nFinalizando o armazenamento de idades.")
    return idades


def armazenador_planos():
    planos = {
        "1": "Plano Básico: Acesso essencial (5 saques, 10 transferências, 3 extratos mensais)",
        "2": "Plano Intermediário: Mais flexibilidade (15 saques, 30 transferências, 10 extratos mensais)",
        "3": "Plano Premium: Acesso ilimitado (saques e transferências ilimitadas, 30 extratos mensais, suporte prioritário)"
    }

    print("\nEscolha um plano:")
    for key, value in planos.items():
        print(f"{key} - {value}")

    while True:
        escolha = input("\nDigite o número do plano desejado ou '0' para sair: ").strip()

        if escolha == "0":
            print("\nVocê optou por não escolher um plano.")
            return None

        if escolha in planos:
            print(f"\nVocê escolheu: {planos[escolha]}")
            return planos[escolha]

        print("Opção inválida! Tente novamente.")


introduction_bank()

nomes = armazenador_nomes()
idades = armazenador_idades()
plano_escolhido = armazenador_planos()

print("\nSua lista com nomes, idades e plano escolhido:\n")
for i in range(len(nomes)):
    print(f"{i + 1}. Nome: {nomes[i]} | Idade: {idades[i] if i < len(idades) else 'N/A'}")

if plano_escolhido:
    print(f"\nPlano escolhido: {plano_escolhido}")
else:
    print("\nNenhum plano foi escolhido.")
