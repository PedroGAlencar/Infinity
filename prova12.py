import time

lista_compras = list()
valor_total = []


def adcionar_produto():
    nome = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))
    valor_uni = float(input('Digite o valor do produto: '))
    valor_total_produto = valor_uni * quantidade
    lista_compras.append({'Nome': nome, 'Quantidade': quantidade, 'Valor unitário': valor_uni, 'Valor total do produto': valor_total_produto})
    valor_total.append(valor_total_produto)

def ver_lista():
    if not lista_compras:
        print(f'Nenhum produto foi adcionado na lista de compras!')
    total_compras = sum(compra['Valor total do produto'] for compra in lista_compras)
    for compra in lista_compras:
        print(f"Nome:{compra['Nome']},Quantidade:{compra['Quantidade']},Valor unitário:{compra['Valor unitário']},Valor total do produto:{compra['Valor total do produto']}")
    print(f'O valor total da lista de compras é {total_compras} reais')
                
def atualizar_produto():
    nome = input('Digite o nome do produto que quer atualizar: ')
    for compra in lista_compras:
        if nome == compra['Nome']:
            compra['Nome'] = input('Digite o novo nome do produto: ')
            compra['Quantidade'] = int(input('Digite a nova quantidade do produto: '))
            compra['Valor unitário'] = float(input('Digite o novo valor unitário do produto: '))
            compra['Valor total do produto'] = compra['Quantidade'] * compra['Valor unitário']
            
                       
def remover_produto():
    nome = input('Digite o nome do produto que deseja remover: ')
    for compra in lista_compras:
        if compra['Nome'] == nome:
            lista_compras.remove(compra)
            print('Produto removido da lista das compras')

while True:
    print('abrindo menu...')
    menu = int(input('''
    Escolha uma das opções abaixo:
        [1] Adcionar produto
        [2] Ver lista de compras
        [3] Atualizar produto
        [4] Remover produto
        [5] Sair do programa
        :'''))
    if menu == 1:
        adcionar_produto()
    elif menu == 2:
        ver_lista()
    elif menu == 3:
        atualizar_produto()
    elif menu == 4:
        remover_produto()
    elif menu == 5:
        print('Finalizando o programa')
        time.sleep(0.5)
        break
    else:
        print('Opção inválida! Tente outra opção')
        time.sleep(1)