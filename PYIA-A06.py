# Desenvolver um programa de linha de comando que permite
# aos usuários gerenciar suas tarefas diárias, atribuindo-lhes
# prioridades e categorias. O projeto será organizado em várias
# partes e usará funções, listas, tuplas, dicionários, conjuntos e
# um ambiente virtual. Passos do projeto:

# Definição de Dados:
# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir
# informações como nome, descrição, prioridade e categoria. Você pode usar
# dicionários para representar as tarefas.


lista_de_tarefas = []

id_tarefa =  ""
descr_tarefa = ""
priorid_tarefa = int
categ_tarefa = int
status_tarefa = int

tarefa = {
    "id_tarefa": "",
    "descr_tarefa": "",
    "priorid_tarefa": int,
    "categ_tarefa": "",
    "status_tarefa": ""
}

# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
# como concluídas, exibir tarefas por prioridade ou categoria, e outras
# funcionalidades que desejar.



def criar_tarefa():
        print("Digite os dados abaixo: ")
        tarefa["id_tarefa"]  = str(input("Digite o nome da tarefa: "))
        tarefa["descr_tarefa"] = str(input("Descreva a tarefa: "))
        tarefa["priorid_tarefa"] = int(input("Digite a prioridade da tarefa (1. baixa, 2. média, 3. alta): "))
        tarefa["categ_tarefa"] = int(input("Digite a categoria: 1. tarefa complexa, 2. tarefa simples: "))
        tarefa["status_tarefa"] = int(input("Digite o status da tarefa: 1. concluida 2. parcialmente concluida 3. nao iniciada "))
        nova_tarefa = tarefa
        lista_de_tarefas.append(nova_tarefa)
        print("tarefa criada!")
        

def listar_tarefas():
    print(lista_de_tarefas)

def exibir_tarefa_priorid():
    tarefas_alta_prioridade = []
    tarefas_media_prioridade = []
    tarefas_baixa_prioridade = []

    for i in lista_de_tarefas:
        if i[priorid_tarefa] == 3:
            i[id_tarefa].append(tarefas_alta_prioridade)
        elif i[priorid_tarefa] == 2:
            i[id_tarefa].append(tarefas_media_prioridade)
        elif i[priorid_tarefa] == 1:
            i[id_tarefa].append(tarefas_baixa_prioridade)
    print(f"Estas são as tarefas de alta prioridade: {tarefas_alta_prioridade}")
    print(f"Estas são as tarefas de media prioridade: {tarefas_media_prioridade}")
    print(f"Estas são as tarefas de baixa prioridade: {tarefas_baixa_prioridade}")   


def exibir_tarefa_categ():
    tarefas_complexas = []
    tarefas_simples = []
    for i in lista_de_tarefas:
        if i[categ_tarefa] == 1:
            i[id_tarefa].append(tarefas_complexas)
        elif i[categ_tarefa] == 2:
            i[id_tarefa].append(tarefas_simples)
    print(f"Estas são as tarefas complexas: {tarefas_complexas}")
    print(f"Estas são as tarefas simples: {tarefas_simples}")

# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao
# usuário interagir com o programa.

programa_inicio = str(input("Bem vindo ao gerenciador de tarefas! Digite C para criar uma tarefa: "))

while True:
    
    if programa_inicio == "C" or programa_inicio == "c":
         criar_tarefa()
    proxima_tarefa = str(input("Deseja adicionar mais uma tarefa?: S. Sim N. Nao "))
    
    if proxima_tarefa == "S" or proxima_tarefa == "s":
         continue
    else:
         break
    

selecao_opcao = int(input("Agora digite o numero da operação desejada: 1. Listar as tarefas cadastradas 2. exibir tarefas ordenadas por categoria 3. exibir tarefas ordenadas por prioridade "))

if selecao_opcao == 1:
    listar_tarefas()

elif selecao_opcao == 2:
    exibir_tarefa_categ()

elif selecao_opcao == 3:
    exibir_tarefa_priorid()

else:
    print("opcao invalida")











