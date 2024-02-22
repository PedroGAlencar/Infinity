def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

def verificar_situacao(media):
    if media == 10:
        return 'Parabéns, sua média é 10!'
    elif media >= 7:
        return 'APROVADO!'
    else:
        return 'REPROVADO!'

notas = list()
while True:
    nota = input('Digite sua nota(ou digite f pra finalizar):')
    if nota.lower() == 'f':
        break
    notas.append(float(nota))
if notas :
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    print(f'Sua média foi de {media :.2f}')
    print(f'Situação: {situacao}')
else:
    print('Nenhuma nota foi inserida!')
    
    
    