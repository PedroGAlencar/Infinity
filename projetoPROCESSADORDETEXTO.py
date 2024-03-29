def processador_de_texto(string,**kwargs):
    for chave,valor in kwargs.items():
        if valor == 'contar palavras':
            lista_de_palavras = string.split(' ')
            print(f'A string tem {len(lista_de_palavras)} palavra(s)')
        elif valor == 'contar letras':
            string_correta = string.replace(' ','')
            print(f'A quantidade de letras da string {len(string_correta)} letra(s)') 
        elif valor == 'inverter texto':
            string_reversa = string[::-1]
            print(f'A string reversa da string {string} é {string_reversa}')
        elif valor == 'substituir palavra':
            valor = input('Digite o que deseja trocar: ')
            novo_valor = input('Digite o novo valor: ')
            if valor in string:
                string = string.replace(valor,novo_valor)
                print(string)
            else:    
                print('Não existe esse caractere na string!')




processador_de_texto('Você foi o ultimo', valor = 'contar palavras')
processador_de_texto('Você foi o ultimo', valor = 'contar letras')
processador_de_texto('Você foi o ultimo', valor = 'inverter texto')
processador_de_texto('Você foi o ultimo', valor = 'substituir palavra')

