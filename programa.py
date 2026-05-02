from funcoes import *

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
    return all(v != -1 for v in cartela['regra_simples'].values()) and \
           all(v != -1 for v in cartela['regra_avancada'].values())

def calcular_total(cartela):
    total = 0
    soma_simples = sum(v for v in cartela['regra_simples'].values() if v != -1)
    total += soma_simples
    if soma_simples >= 63:
        total += 35
    total += sum(v for v in cartela['regra_avancada'].values() if v != -1)
    return total


imprime_cartela(cartela)

while not cartela_completa(cartela):

    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print("Dados rolados:", dados_rolados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            if 0 <= i < len(dados_rolados):
                dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, i)

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            if 0 <= i < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, i)

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                rerrolagens += 1
                dados_rolados = rolar_dados(5 - len(dados_guardados))

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            while True:
                print("Digite a combinação desejada:")
                categoria = input()

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

                elif categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                        continue

                    cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                    break

                else:
                    print("Combinação inválida. Tente novamente.")

            break  # encerra a rodada

        else:
            print("Opção inválida. Tente novamente.")


imprime_cartela(cartela)
print(f"Pontuação total: {calcular_total(cartela)}")