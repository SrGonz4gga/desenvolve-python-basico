import csv
from collections import namedtuple
from collections import OrderedDict
from getpass import getpass
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt



ARQUIVO_FUNCIONARIOS = 'funcionarios_supermercado.csv'
ARQUIVO_PRODUTOS = 'produtos_supermercado.csv'
FUNCIONARIO_LOGADO = None

def ler_funcionarios(arquivo_csv):
    Funcionario = namedtuple('Funcionario', ['nome', 'idade', 'senha', 'cargo', 'salario', 'tempo'])
    funcionarios = {}

    with open(arquivo_csv, mode = 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            nome, idade, senha, cargo, salario, tempo = row
            funcionarios[nome] = Funcionario(nome = nome, idade = idade, senha = senha, cargo = cargo, salario = salario, tempo = tempo)

    return funcionarios


def ler_produtos(arquivo_csv):
    Produto = namedtuple('Produto', ['nome', 'quantidade_em_estoque', 'preco_unidade'])
    produtos = {}

    with open(arquivo_csv, mode = 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            nome, quantidade_em_estoque, preco_unidade = row
            produtos[nome] = Produto(nome = nome, quantidade_em_estoque = quantidade_em_estoque, preco_unidade = preco_unidade)
    
    return produtos

def ver_funcionarios(arquivo_csv):
    console = Console()
    with open(arquivo_csv, mode = 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            console.print(Panel(f"[bold cyan]Nome:[/bold cyan] {linha['nome']} | [bold cyan]Idade:[/bold cyan] {linha['idade']} | [bold cyan]Senha:[/bold cyan] {linha['senha']} | [bold cyan]Cargo:[/bold cyan] {linha['cargo']} | [bold cyan]Salário:[/bold cyan] {linha['salario']} | [bold cyan]Tempo de empresa:[/bold cyan] {linha['tempo']} anos"))
    menu_secundario()

def ver_produtos(arquivo_csv):
    console = Console()
    with open(arquivo_csv, mode = 'r', newline = '') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            console.print(Panel(f"[bold cyan]Nome:[/bold cyan] {linha['nome']} | [bold cyan]Quantidade em estoque:[/bold cyan] {linha['quantidade_em_estoque']} | [bold cyan]Preço:[/bold cyan] {linha['preco_unidade']}"))

    menu_secundario()

def pesquisa_produto(produtos):
    console = Console()
    opcao = Prompt.ask("Nome do produto desejado: ")
    if opcao in produtos:
        console.print(f"Produto: [bold cyan]{produtos[opcao][0]}[/bold cyan], Quantidade estocada: {produtos[opcao][1]} unidades, Valor: R${produtos[opcao][2]}")
    else:
        console.print(f"[bold red]Produto não encontrado[/bold red]")

    menu_secundario()

def ordena_produtos(produtos):
    console = Console()
    console.print("Ordenar por nome [1]\nOrdenar por preço[2]")
    opcao = Prompt.ask("Como deseja ordenar os produtos?", choices = ['1', '2'])

    if opcao == "1":
        ordenadonome = dict(sorted(produtos.items(), key=lambda item:item[0]))
        console.print("Ordenação por [bold cyan]NOME: [/bold cyan]")
        for chave, valor in ordenadonome.items():
            if chave == "nome":
                continue
            else: console.print(f"Nome: [bold cyan]{ordenadonome[chave][0]}[/bold cyan], Quantidade estocada: {ordenadonome[chave][1]}, Valor: R${ordenadonome[chave][2]}")

    else:
        ordenadopreco = dict(sorted(produtos.items(), key=lambda item: item[1][2]))
        console.print("Ordenação por [bold cyan]PREÇO: [/bold cyan]")
        for chave in ordenadopreco:
            if chave == "nome":
                continue
            console.print(f"Nome: [bold cyan]{ordenadopreco[chave][0]}[/bold cyan], Quantidade estocada: {ordenadopreco[chave][1]}, Valor: R${ordenadopreco[chave][2]} ")

    menu_secundario()

def fazer_login(funcionarios):
    global FUNCIONARIO_LOGADO
    console = Console()

    console.print(Panel("Insira suas credenciais", expand = False, title = "[bold cyan]Login[/bold cyan]"))
    console.print("[bold purple]Nome:[/bold purple]")
    username = input("Nome: ")
    console.print("[bold purple]Senha:[/bold purple]")
    senha = getpass("Senha: ")

    user = funcionarios.get(username, None)
    if user is not None and user.senha == senha:
        print("Login bem sucedido!")
        FUNCIONARIO_LOGADO = user
        return True
    else:
        print("Erro: Usuário ou senha incorretos!")
        return False

def cadastrar_funcionario(funcionarios, arquivo_csv):
    console = Console()
    console.print(Panel("Por favor, insira os dados do novo usuário.", title = "[bold cyan]Cadastro de funcionário[/bold cyan]", expand = False))

    nome = input("Nome do funcionário: ")
    if funcionarios.get(nome, None) is not None:
        console.print(f" [bold red]{nome} já está no quadro de funcionários[/bold red]")
        menu_secundario()
        return
    senha = getpass("Senha: ") 
    cargo = input("Tipo de novo funcionário: (Gerente, Açogueiro, Segurança, Caixa, Repositor, Estoquista, Assistente administrativo, Operador de caixa, Estagiário, Padeiro )")
    idade = input("Idade do funcionário: ")
    salario = input("Salário do funcionário: ")
    tempo = input("Tempo na empresa") 

    with open(arquivo_csv, mode = 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([nome, idade, senha, cargo, salario, tempo])
    console.print(f"[bold green]{nome} cadastrado com sucesso![/bold green]")
    ler_funcionarios(ARQUIVO_FUNCIONARIOS)
    menu_secundario()


def excluir_funcionario(funcionarios, arquivo_csv):
    console = Console()

    global FUNCIONARIO_LOGADO

    console.print(Panel("Por favor insira o nome do funcionário a ser excluído.", title = "[bold cyan]Exclusão de funcionário[/bold cyan]", expand = False))
    nome = Prompt.ask("Nome: (Digite 0 para sair)")

    if nome == "0":
        tela_saida()
        return 

    if funcionarios.get(nome, None) is not None:
        with open(arquivo_csv, mode = 'w', newline = '' ) as file:
            writer = csv.writer(file)
            for funcionario in funcionarios.values():
                if funcionario.nome != nome:
                    writer.writerow([funcionario.nome, funcionario.idade, funcionario.senha, funcionario.cargo, funcionario.salario, funcionario.tempo])
            console.print("[bold green]Funcionário excluído com sucesso![/bold green]")
            ler_funcionarios(ARQUIVO_FUNCIONARIOS)
            menu_secundario()
    else:
        console.print("[bold red]Funcionário não encontrado![/bold red]")
        menu_secundario()
    


def atualiza_senha(funcionarios, arquivo_csv):
    console = Console()

    if FUNCIONARIO_LOGADO.cargo == "Gerente":
        print("Por favor informe o nome do funcionário que terá a senha alterada: ")
        nome = input("Nome do funcionário: ")
        senha = getpass("Nova senha: ")
        achou = False

        with open(arquivo_csv, mode = 'w', newline = '') as file:
            writer = csv.writer(file)
            for _, funcionario in funcionarios.items():
                if funcionario.nome != nome:
                    writer.writerow([funcionario.nome, funcionario.idade, funcionario.senha, funcionario.cargo, funcionario.salario, funcionario.tempo])
                else:
                    writer.writerow([funcionario.nome, funcionario.idade, senha, funcionario.cargo, funcionario.salario, funcionario.tempo])
                    console.print(f"[bold green]Senha de {nome} atualizada![/bold green]")
                    ler_funcionarios(ARQUIVO_FUNCIONARIOS)
                    menu_secundario()
                    achou = True
        if achou == False:
            console.print(f"[bold red]Funcionário(a) {nome} não encontrado(a)[/bold red]")
            menu_secundario()

        
            
    else:
        nome = FUNCIONARIO_LOGADO.nome
        print(f"Atualizando senha de {nome} ")
        senha = getpass("Nova senha: ")


        with open(arquivo_csv, mode = 'w', newline = '') as file:
            writer = csv.writer(file)
            for _, funcionario in funcionarios.items():
                if funcionario.nome != nome:
                    writer.writerow([funcionario.nome, funcionario.idade, funcionario.senha, funcionario.cargo, funcionario.salario, funcionario.tempo])
                else:
                    writer.writerow([funcionario.nome, funcionario.idade, senha, funcionario.cargo, funcionario.salario, funcionario.tempo])
        console.print(f"[bold green]Senha de {nome} atualizada![/bold green]")
        ler_funcionarios(ARQUIVO_FUNCIONARIOS)
        menu_secundario()

def tela_saida():
    print("Saiu")
    return 


def menu_principal():
    console = Console()
    console.print(Panel("[bold grey]Sistema de funcionários da empresa[/bold grey]", title = "[bold cyan]Menu Principal[/bold cyan]", expand = False ))
    console.print("[bold cyan]Selecione uma opção[/bold cyan]")
    console.print("[bold cyan]1.[/bold cyan] [bold white]Fazer login[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Sair[/bold white]")

    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]: ", choices = ["1", "2"])
    if opcao == "1":
        while FUNCIONARIO_LOGADO == None:
            fazer_login(funcionarios)
        menu_secundario()
    else:
        tela_saida()


def menu_secundario():
    console = Console()
    if FUNCIONARIO_LOGADO.cargo == "Gerente":
        console.print(Panel("Selecione uma opção", expand = False, title = "[bold cyan]Ações[/bold cyan]"))
        console.print("[bold cyan]1.[/bold cyan] Ver quadro de funcionários")
        console.print("[bold cyan]2.[/bold cyan] Atualização de senhas")
        console.print("[bold cyan]3.[/bold cyan] Excluir funcionário do quadro")
        console.print("[bold cyan]4.[/bold cyan] Cadastrar novo funcionário")
        console.print("[bold cyan]5.[/bold cyan] Sair")
        
        opcao = Prompt.ask("[bold cyan]Digite o número da opção desejada[/bold cyan]", choices = ['1', '2', '3', '4', '5'])
        if opcao == "1":
            ver_funcionarios(ARQUIVO_FUNCIONARIOS)
        elif opcao == "2":
            atualiza_senha(funcionarios, ARQUIVO_FUNCIONARIOS)
        elif opcao == "3":
            excluir_funcionario(funcionarios, ARQUIVO_FUNCIONARIOS)
        elif opcao == "4":
            cadastrar_funcionario(funcionarios, ARQUIVO_FUNCIONARIOS)
        elif opcao == '5':
            tela_saida()
        else:
            console.print("[bold red]Opção inválida[/bold red]")
        
    
    else:
        console.print(Panel("Selecione uma opção", expand = False, title = "[bold cyan]Ações[/bold cyan]"))
        console.print("[bold cyan]1.[/bold cyan] Ver quadro de produtos")
        console.print("[bold cyan]2.[/bold cyan] Pesquisar produto específico")
        console.print("[bold cyan]3.[/bold cyan] Ver produtos ordenados")
        console.print("[bold cyan]4.[/bold cyan] Atualizar sua senha")
        console.print("[bold cyan]5.[/bold cyan] Sair")

        opcao = Prompt.ask("[bold cyan]Digite o número da opção desejada[/bold cyan]", choices = ['1','2','3','4', '5'])
        if opcao == "1":
            ver_produtos(ARQUIVO_PRODUTOS)
        elif opcao == "2":
            pesquisa_produto(produtos)
        elif opcao == "3":
            ordena_produtos(produtos)
        elif opcao == "4":
            atualiza_senha(funcionarios, ARQUIVO_FUNCIONARIOS)
        elif opcao == "5":
            tela_saida()
        else:
            console.print("[bold red]Opção inválida[/bold red]")
        return opcao
    

funcionarios = ler_funcionarios(ARQUIVO_FUNCIONARIOS)
produtos = ler_produtos(ARQUIVO_PRODUTOS)
menu_principal()