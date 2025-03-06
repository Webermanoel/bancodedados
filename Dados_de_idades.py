def introduction_bank_old():
    print("###################################################")
    print("Bem-vindo ao armazenador de idades do banco de dados")
    print("###################################################\n")

introduction_bank_old()

def armazenador_idades():
    idades = []

    while len(idades) < 10:
        try:
            idade = int(input(f"Digite uma idade ({len(idades) + 1}/10): "))  # Solicita idade

            if idade < 0:
                print("Idade não pode ser negativa! Tente novamente.")
                continue

            idades.append(idade)
            print(f"\nIdade '{idade}' armazenada com sucesso!")

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    print("\nVocê atingiu o limite de 10 idades.")
    print("Lista final de idades armazenadas:", idades)

armazenador_idades()
