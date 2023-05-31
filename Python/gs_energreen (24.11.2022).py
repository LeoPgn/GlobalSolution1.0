'''INTEGRANTES:
    Jhonn Brandon Cabrera Tacachiri - rm 97305
    Leonardo Paganini - rm 96562
    Matheus Leite Oliveira Scalfo - rm 96893'''

'''DESCRIÇÃO DA SOLUÇÃO:
    Ferramenta que ajuda as pessoas a localizar carregadores de carros elétricos pela cidade de São Paulo
    '''

resp = 1
usuario = {}

while (resp !=0):
    print("1 - Criar/gerenciar cadastro")
    print("2 - Localizar carregador")
    print("3 - Calcular tempo de carregamento")
    print("4 - Adicionar/gerenciar forma de pagamento")
    print("5 - Avaliação do equipamento(carregador) utilizado")
    opcao = int(input("Escolha uma opção: "))
    if (opcao == 1):
        print("1-Criar uma conta")
        print("2-Editar sua conta")
        print("3-Exibir dados da sua conta")
        print("4-Excluir dados da sua conta")
        opc_conta = print(input("Escolha uma opção: "))
        if (opc_conta == 1):
            nome_usuario = print(input("Insira seu nome: "))
            telefone_usuario = print(input("Insira seu numero de telefone: "))
            email_usuario = print(input("Insira seu email: "))
            cpf_usuario = print(input("Insira seu CPF: "))
            senha_usuario = print(input("Insira sua senha: "))
            usuario[nome_usuario] = {'nome': nome_usuario, 'telefone': telefone_usuario, 'email': email_usuario,
                                     'CPF': cpf_usuario, 'senha': senha_usuario}
        elif (opc_conta == 2):
            nome_usuario = (input("Insira o nome do qual deseja editar os dados: "))
            if (nome_usuario in usuario):
                print("1 - Telefone")
                print("2 - email")
                print("3 - senha")
                opc_editar_conta = int(input("Qual dado deseja editar? "))
        else:
            print("já era")
        print("opção 1")
    elif (opcao == 2):
        print("Olá")
    elif (opcao == 3):
        print("tchau")
    elif (opcao == 4):
        print("tchau")
    elif (opcao == 5):
        print("tchau")
    else:
        print("opção invalida")
    resp = int(input("Deseja continuar? - 1-SIM | 0-NÃO: "))