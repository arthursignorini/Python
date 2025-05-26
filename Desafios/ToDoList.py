class Tarefa:
    
    tarefas = []
    
    def __init__(self, n, d, p, v):
        self.nome = n
        self.descrição = d
        self.prioridade = p
        self.vencimento = v
        self.concluida = False
        
    
    def adicionar(self):
        Tarefa.tarefas.append(self)

    def __str__(self):

        return f"Tarefa: {self.nome}\nDescrição: {self.descrição}\nPrioridade: {self.prioridade}\nVencimento: {self.vencimento}\nStatus: {self.concluida}\n"



def criarTarefa():

    nome = str(input("Digite o nome da tarefa: "))
    descrição = str(input("Digite a descrição da tarefa: "))
    prioridade = str(input("Digite a prioridade da tarefa (baixa, média, alta): "))
    vencimento = str(input("Digite o vencimento da tarefa: DD/MM/AAAA: "))
    
    t = Tarefa(nome, descrição, prioridade, vencimento)
    Tarefa.adicionar(t)

def mostrarTarefas():

    for tarefa in Tarefa.tarefas:
        print(tarefa)

def finalizarTarefa():

    mostrarTarefas()

    try:
        op = str(input("Digite o nome da tarefa que voce quer finalizar: "))
        for tarefa in Tarefa.tarefas:
            if(tarefa.nome.lower() == op.lower()):
                tarefa.concluida = True
                Tarefa.tarefas.remove(tarefa)
                print("Tarefa finzalizada com sucesso")
                break
    except ValueError:
        print("Nao existe uma tarefa com esse nome")

def removerTarefa():

    mostrarTarefas()

    try:
        op = str(input("Digite o nome da tarefa que você quer remover: "))
        for tarefa in Tarefa.tarefas:
            if(tarefa.nome.lower() == op.lower()):
                Tarefa.tarefas.remove(tarefa)
                print("Tarefa removida com sucesso")
                break
    except ValueError:
        print("Não existe uma tarefa com esse nome")


def editarTarefa():

    mostrarTarefas()

    try: 
        op = str(input("Digite o nome da tarefa que você quer editar: "))
        for tarefa in Tarefa.tarefas:
            if(tarefa.nome.lower() == op.lower()):
                nome = str(input("Digite o novo nome da tarefa: "))
                descriçao = str(input("Digite a nova descrição da tarefa: "))
                prioridade = str(input("Digite a nova prioridade da tarefa: "))
                vencimento = str(input("Digite o vencimento da tarefa: "))

                tarefa.nome = nome
                tarefa.descriçao = descriçao
                tarefa.prioridade = prioridade
                tarefa.vencimento = vencimento

                print("Tarefa editada com sucesso")
                break
    except ValueError:
        print("Não existe uma tarefa com esse nome")


def menu():
    op = -1  
    while op != 0:
        print("\nDigite uma opção:")
        print("1) Criar tarefa")
        print("2) Finalizar tarefa")
        print("3) Remover tarefa")
        print("4) Editar tarefa")
        print("5) Mostrar tarefas")
        print("0) Finalizar")

        try:
            op = int(input("Opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if op == 1:
            criarTarefa()
        elif op == 2:
            finalizarTarefa()
        elif op == 3:
            removerTarefa()
        elif op == 4:
            editarTarefa()
        elif op == 5:
            mostrarTarefas()
        elif op == 0:
            print("Encerrando o programa...")
        else:
            print("Opção inválida, tente novamente.")


def main():
    menu()

if __name__ == "__main__":
    main()