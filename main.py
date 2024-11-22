import csv


def abrirCSV():
    saida = []

    with open("drinks.csv", mode="r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        next(arquivo_csv)
        for linha in arquivo_csv:
            saida.append([
                linha[0],
                int(linha[1]),
                int(linha[2]),
                int(linha[3]),
                float(linha[4])
            ])

    return saida


def buscarPais(lista):
    pais = input("Digite o nome de um país: ").strip(' ').upper()
    for linha in lista:
        if linha[0].upper() == pais:
            return formartar_dados(linha)

    return "Não encontrado"


def listarRanking(dados):
    menuRanking()
    try:
        opcao = int(input("Digite uma opção: "))
        if opcao == 0:
            menuPrincipal()
        else:
            ranking = rankiar(dados, opcao)
            quantidade = int(input("Quantidade de posições: "))
            exibirRanking(ranking, quantidade, opcao)
    except ValueError:
        print("Digite uma opção válida")


def rankiar(dados, opcao):
    ordenada = sorted(dados, key=lambda x: x[opcao], reverse=True)
    return ordenada


def exibirRanking(ranking, quantidade, opcao):
    quant = 0
    for elemento in ranking:
        quant += 1
        print(f"{quant}º - {elemento[0]}: {elemento[opcao]}")

        if quantidade == quant:
            break


def paisesSemAlcool(dados):
    for elemento in dados:
        if elemento[4] == 0:
            print(elemento[0])


def menuPrincipal(dados):
    while True:
        str_menu()
        try:
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                print(buscarPais(dados))
            elif opcao == 2:
                listarRanking(dados)
            elif opcao == 3:
                paisesSemAlcool(dados)

            elif opcao == 0:
                break

            else:
                print("Digite uma opção válida")

        except ValueError:
            print("Digite uma opção válida")


def str_menu():
    print("-------- menu ----------\n"
          "1 - Buscar País\n"
          "2 - Rankings\n"
          "3 - Paises que não consomem alcool\n"
          "0 - Sair\n"
          "--------------------------------")


def menuRanking():
    print("------------------------")
    print('1 - Cerveja\n'
          '2 - Destilado \n'
          '3 - Vinho\n'
          '4 - Total\n'
          '0 - Voltar Menu principal')


def formartar_dados(array):
    return (
        f'-----------------------\nPaís: {array[0]},\nCervejas: {array[1]}L\n'
        f'Destilados: {array[2]}L\nVinho: {array[3]}L'
        f'\n------------\nTotal: {array[4]}L'
    )


def main():
    dados = abrirCSV()
    menuPrincipal(dados)


if __name__ == "__main__":
    main()
