tarefas = []

while True:
    print ('Lista de tarefas')
    print('1. Adicionar itens a lista.')
    print('2. Listar tarefas.') # Lista todas as tarefas
    print('3. Deletar tarefas da lista.') # Deleta um item da lista
    print('4. Sair.') # Finaliza

    opcao = input('Selecione uma das opcoes: ')

    if opcao == '1':
        tarefa = input('Digite uma nova tarefa: ')
        tarefas.append(tarefa)
        print('Tarefa adicionada!')

    elif opcao == '2':
        if not tarefas:
            print('Nenhuma tarefa na lista.')
        else:
            print('Tarefas: ')
            for i, tarefa in enumerate(tarefas):
                print(f'{i}. {tarefa}')
    elif opcao == '3':
        if not tarefas:
            print('Nenhuma tarefa na lista.')
        else:
            print('Tarefas:')
            for i, tarefa in enumerate(tarefas, 1):
                print(f'{i}. {tarefa}')
            try:
                indice = int(input('Digite o numero da tarefa que deseja remover:')) - 1
                if 0 <= indice < len(tarefas):
                    tarefas.pop(indice)
                    print('Tarefa removida.')
                else:
                    print('Numero invalido.')
            except ValueError:
                print('Por favor, digite m numero valido.')
    elif opcao == '4':
        print('Encerrando o programa...')
        break
