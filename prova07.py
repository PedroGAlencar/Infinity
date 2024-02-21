import time
aluno = dict()

while True:
    print('Sistema iniciando...')  
    time.sleep(1)  
    sistema = int(input(''' Qual opção você deseja :
                        (1) Cadastro de alunos
                        (2) Remover Aluno
                        (3) Visualizar Alunos cadastrados
                        (4) Finalizar Sistemas
                        :'''))
    if sistema == 1:
        nome = input('Digite o nome do aluno :')
        matricula = input('Digite o número da matrícula:')
        aluno[matricula] = nome
    elif sistema == 2:
        matricula = input("Digite o número de matrícula do aluno a ser removido: ")
        if matricula in aluno:
            nome = aluno.pop(matricula)
            print(f"Aluno {nome} removido com sucesso.")
            
        else:
            print('Matrícula não encontrada!')
            time.sleep(0.5)
    elif sistema == 3:
        if aluno:
            for matricula,nome in aluno.items():
                print(f'Matrícula: {matricula}, Nome : {nome}')
        else:
            print('Nenhum aluno cadastrado!')
    elif sistema == 4:
        print('Finalizando sistema...')
        time.sleep(1)
        print('Fim do sistema!')
        break
    else:
        print('Não existe essa opção! Tente novamente')     
           
       
