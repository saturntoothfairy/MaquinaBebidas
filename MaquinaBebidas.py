produto = [[0,1,2,3,4,5],
           ['0', 'coca-cola', 'pepsi', 'monster', 'café', 'redbull'],
           [0, 3.75, 3.67, 9.96, 1.25, 13.99],
           [0, 2, 5, 1, 100, 2]]
dinheiro = [[20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01],
            [5, 5, 5, 5, 10, 10, 10, 10, 10, 1]]

def funcao1(x):
    return produto[1][x]
def funcao2(x):
    return produto[2][x]

def calculoTroco(troco):
    receber = []
    cont = 0
    while cont < troco:
        cont = round(cont,2)
        for i in range(len(dinheiro[0])):
            devolver = dinheiro[0][i]
            estoque = dinheiro[1][i]
            if (devolver + cont) <= troco and estoque > 0:
                cont += devolver
                dinheiro[1][i] -= 1
                receber.append(devolver)
    return receber

def cadastrar(mercadora, quantidade, preco):

    produto[1].append(mercadoria)
    produto[2].append(quantidade)
    produto[3].append(preco)

def editar(mudar, novaQuant, novoPreco):

    produto[3][mudar] = novaQuant
    produto[2][mudar] = novoPreco

soma = 0


while True:
    modo = input('Deseja usar o modo adm? (s/n) ')
    if modo == 's':
        tipoADM = int(input('Qual função do ADM você quer usar? cadastrar(1) editar(2) remover(3) '))
        if tipoADM == 1:
            mercadoria = input('Qual produto você deseja cadastrar? ')
            quantidade = int(input('Qual a quantidade você deseja cadastrar? '))
            preco = float(input('Qual o valor do produto? '))
            cadastrar(mercadoria, quantidade, preco)
            print(produto)
        elif tipoADM == 2:
            mudar = int(input('Qual produto você quer editar? coca-cola(1) pepsi(2) monster(3) café(4) redbull(5) '))
            novaQuant = int(input('Qual a nova quantidade?'))
            novoPreco = float(input('Qual o novo preço? '))
            editar(mudar, novaQuant, novoPreco)
            print(produto)
        elif tipoADM == 3:
            remover = int(input('Qual produto você deseja remover? coca-cola(1) pepsi(2) monster(3) café(4) redbull(5) '))
            for i in range(len(produto)):
                del produto[i][remover]
            print(produto)
    else:
        escolha = int(input('Escolha um produto: coca-cola(1) pepsi(2) monster(3) café(4) redbull(5) '))
        if produto[3][escolha] > 0:
            if escolha in produto[0]:
                print(f'O valor do(a) {funcao1(escolha)} é {funcao2(escolha)}')
                soma += funcao2(escolha)
                produto[3][escolha] -= 1
                continuar = input('Deseja escolher mais um produto? (s/n)')
                if continuar == 's':
                    continue
                else:
                    print(f'O valor total é {soma:.2f}')
                    while True:
                        valor = float(input('Insira o pagamento: '))
                        if valor > soma:
                            troco = round(valor - soma, 2)
                            print(f'Seu troco é {troco} '
                                  f' Você irá receber {calculoTroco(troco)}')
                            soma = 0
                            break
                        elif valor == soma:
                            print('Obrigado pela compra')
                            soma = 0
                            break
                        else:
                            print('Valor inválido')
                            continue
            else:
                print('Código inválido')
        else:
            print('Produto fora de estoque')

