import csv
def main():
    dados = abrirCSV()
    menuPrincipal(dados)
    
def abrirCSV():
    saida = []

    with open("drinks.csv", mode = "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter = ",")
        next(arquivo_csv)
        for linha in arquivo_csv:
            saida.append([linha[0], int(linha[1]), int(linha[2]), int(linha[3]), float(linha[4])])

    return saida

def buscarPais(lista):
    pais = input("Digite o nome de um país: ").strip(' ').upper()
    for linha in lista:
        if linha[0].upper() == pais:
            return formartar_dados(linha)
    return "Não encontrado"

def listarRanking(dados):
    menuRanking()
    opcao = int(input("Digite uma opção: "))
    if opcao == 0:
        menuPrincipal()
    else:
        ranking = rankiar(dados, opcao)
        quantidade = int(input("Quantidade de posições: "))
        exibirRanking(ranking, quantidade, opcao)



def rankiar(dados, opcao):
    ordenada = sorted(dados, key=lambda x: x[opcao],reverse=True)
    return ordenada

def exibirRanking(ranking, quantidade, opcao):
    quant = 0
    for elemento in ranking:
        quant+=1
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
        opcao = int(input("Digite uma opção: "))
        if opcao == 1:
            print(buscarPais(dados))
        elif opcao == 2:
            listarRanking(dados)
        elif opcao == 3:
            paisesSemAlcool(dados)

        elif opcao == 0:
            break

def str_menu():
    print("""-------- menu ----------
    1 - Buscar País
    2 - Rankings
    3 - Paises que não consomem alcool
    0 - Sair
    --------------------------------""")

def menuRanking():
    print("------------------------")
    print('1 - Cerveja\n2 - Destilado \n3 - Vinho\n4 - Total\n0 - Voltar Menu principal')

def formartar_dados(array):
    return f'-----------------------\nPaís: {array[0]},\nCervejas: {array[1]}\nDestilados: {array[2]}\nVinho: {array[3]}\n------------\nTotal: {array[4]}'

if __name__ == "__main__":
    main()