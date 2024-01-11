# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
while True:
    numero = int(input('Digite um número inteiro pra a tabuada:(1 a 10)'))
    if numero > 10:
        print('Digite um número de 1 a 10!')
        continue
    for num in range(1):
        tabuada =f'''
                    {numero} x 1 = {numero * 1}
                    {numero} x 2 = {numero * 2}
                    {numero} x 3 = {numero * 3}
                    {numero} x 4 = {numero * 4}
                    {numero} x 5 = {numero * 5}
                    {numero} x 6 = {numero * 6}
                    {numero} x 7 = {numero * 7}
                    {numero} x 8 = {numero * 8}
                    {numero} x 9 = {numero * 9}
                    {numero} x 10 = {numero * 10}
    '''
    if numero == 0:
        break
    print(tabuada)


