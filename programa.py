elif opcao == "0":
    while True:
        print("Digite a combinação desejada:")
        categoria = input()

        # caso número
        if categoria.isdigit():
            c = int(categoria)

            if c not in cartela['regra_simples']:
                print("Combinação inválida. Tente novamente.")
                continue

            if cartela['regra_simples'][c] != -1:
                print("Essa combinação já foi utilizada.")
                continue

            cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
            break

        # caso regra avançada
        elif categoria in cartela['regra_avancada']:
            if cartela['regra_avancada'][categoria] != -1:
                print("Essa combinação já foi utilizada.")
                continue

            cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
            break

        # qualquer outra coisa
        else:
            print("Combinação inválida. Tente novamente.")

    break