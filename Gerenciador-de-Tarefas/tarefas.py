def main():
    tarefas = []  # Lista para armazenar tarefas

    while True:
        print("\nBem-vindo ao Gerenciador de Tarefas!")
        print("Escolha uma opção:")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            visualizar_tarefas(tarefas)
        elif escolha == '3':
            remover_tarefa(tarefas)
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefas.append(descricao)  # Adiciona a tarefa à lista
    print("Tarefa adicionada com sucesso!")

def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas pendentes.")
    else:
        print("Tarefas pendentes:")
        for i, tarefa in enumerate(tarefas, start=1):  # Enumera as tarefas a partir de 1
            print(f"{i}. {tarefa}")

def remover_tarefa(tarefas):
    visualizar_tarefas(tarefas)  # Mostra as tarefas antes de remover
    if tarefas:  # Verifica se há tarefas na lista
        numero = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= numero < len(tarefas):
            tarefas.pop(numero)  # Remove a tarefa da lista
            print("Tarefa removida com sucesso!")
        else:
            print("Número inválido. Nenhuma tarefa foi removida.")

if __name__ == "__main__":
    main()
