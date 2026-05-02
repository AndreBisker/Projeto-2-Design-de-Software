from funcoes import *

# inicializa cartela
cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

def cartela_completa(cartela):
    for v in cartela['regra_simples'].values():
        if v == -1:
            return False
    for v in cartela['regra_avancada'].values():
        if v == -1:
            return False
    return True

# jogo
while not cartela_completa(cartela):

    dados_guardados = []
    dados_rolados = rolar_dados(5)
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input(">")

        # GUARDAR
        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input(">"))
            if 0 <= idx < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, idx)
            else:
                print("Opção inválida. Tente novamente.")

        # REMOVER
        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input(">"))
            if 0 <= idx < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, idx)
            else:
                print("Opção inválida. Tente novamente.")

        # RERROLAR
        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                novos = rolar_dados(len(dados_rolados))
                dados_rolados = novos
                rerrolagens += 1

        # VER CARTELA
        elif opcao == "4":
            imprime_cartela(cartela)

        # MARCAR PONTUAÇÃO
        elif opcao == "0":
            print("Digite a combinação desejada:")
            comb = input(">")

            todas_combinacoes = list(map(str, range(1,7))) + list(cartela['regra_avancada'].keys())

            if comb not in todas_combinacoes:
                print("Combinação inválida. Tente novamente.")
                continue

            # verifica se já foi usada
            if comb in map(str, range(1,7)):
                if cartela['regra_simples'][int(comb)] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
            else:
                if cartela['regra_avancada'][comb] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue

            # faz jogada
            todos_dados = dados_rolados + dados_guardados
            cartela = faz_jogada(todos_dados, comb, cartela)

            break  # encerra rodada

        else:
            print("Opção inválida. Tente novamente.")

# cálculo final
total = 0

# soma simples
soma_simples = sum(cartela['regra_simples'].values())
total += soma_simples

# bônus
if soma_simples >= 63:
    total += 35

# soma avançada
total += sum(cartela['regra_avancada'].values())

imprime_cartela(cartela)
print(f"Pontuação total: {total}")