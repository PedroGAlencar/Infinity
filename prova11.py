import time
tarefas = []
#Função para adcionar tarefa!
def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = int(input("Prioridade da tarefa (1-3): "))
    categoria = input("Categoria da tarefa (Estudo, Trabalho ou Casa): ")
    tarefas.append({"nome": nome, "descricao": descricao, "prioridade": prioridade, "categoria": categoria, "feita": False})
    print('Tarefa adcionada com sucesso!!!')
    
#Função para listar as tarefas!
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
    else:
        for tarefa in tarefas:
            status = "Feita" if tarefa["feita"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['categoria']} - Prioridade: {tarefa['prioridade']} - {status}")
#Função exibir em ordem de prioridade
def exibir_tarefas_por_prioridade():
    ordenadas = sorted(tarefas, key=lambda x: x['prioridade'], reverse=True)
    for tarefa in ordenadas:
        status = "Feita" if tarefa["feita"] else "Pendente"
        print(f"{tarefa['nome']} - Prioridade: {tarefa['prioridade']} - {status}")
#Função marcar tarefa
def marcar_tarefa_feita():
    nome = input("Digite o nome da tarefa a marcar como concluída: ")
    for tarefa in tarefas:
        if tarefa["nome"] == nome:
            tarefa["feita"] = True
            print(f"Tarefa '{nome}' marcada como feita.")
            return
    print("Tarefa não encontrada.")

while True:
    print('Abrindo menu')
    time.sleep(0.5)
    menu = int(input('''Escolha sua opção
                     [1]  Adicionar Tarefa
                     [2]  Listar Tarefas
                     [3]   Exibir Tarefas por Prioridade
                     [4]   Marcar Tarefa Feita
                     [5]   Sair do Sistema
:'''))
    if menu == 1:
        adicionar_tarefa()
    elif menu == 2:
        listar_tarefas()
    elif menu == 3:
        exibir_tarefas_por_prioridade()
    elif menu == 4:
        marcar_tarefa_feita()
    elif menu == 5:
        print('Saindo do sistema...')
        time.sleep(1)
        print('Sistema finalizado!')
        break
    else:
        print('Não existe essa opção! Tente novamente')
        time.sleep(0.5)