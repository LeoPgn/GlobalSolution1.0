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

    '''Criar/gerenciar cadastro'''
    if (opcao == 1):
        print("1-Criar uma conta")
        print("2-Editar sua conta")
        print("3-Exibir dados da sua conta")
        print("4-Excluir dados da sua conta")
        opc_conta = int(input("Escolha uma opção: "))

        if (opc_conta == 1):
            nome_usuario = input("Insira seu nome completo: ")
            telefone_usuario = int(input("Insira seu numero de telefone: "))
            email_usuario = input("Insira seu email: ")
            cpf_usuario = int(input("Insira seu CPF: "))
            senha_usuario = input("Insira sua senha: ")
            usuario[nome_usuario] = {'nome': nome_usuario, 'telefone': telefone_usuario, 'email': email_usuario,
                                 'CPF': cpf_usuario, 'senha': senha_usuario}
        elif (opc_conta == 2):
            print("1 - Telefone")
            print("2 - email")
            print("3 - senha")
            opc_editar_conta = int(input("Qual dado deseja editar? "))
            if (opc_editar_conta == 1):
                nome_usuario = (input("Insira o nome do usuário do qual deseja editar o número de telefone: "))
                if (nome_usuario in usuario):
                    nome_usuario[telefone] = (int(input("Insira o novo nº de telefone: ")))
                else:
                    print("Usuário não encontrado")

            elif (opc_editar_conta == 2):
                nome_usuario = (input("Insira o nome do usuário do qual deseja editar o email: "))
                if (nome_usuario in usuario):
                    nome_usuario['email'] = input("Insira o novo email email: ")
                else:
                    print("Usuário não encontrado")
            elif (opc_editar_conta == 3):
                nome_usuario = (input("Insira o nome do qual deseja editar a senha: "))
                if (nome_usuario in usuario):
                    nome_usuario['senha'] = input("senha: ")
                else:
                    print("Usuário não encontrado")
            else:
                print("Opção invalida.")
        elif (opc_conta == 3):
            nome_usuario = (input("Insira o nome do usuário que deseja ver os dados: "))
            if (nome_usuario in usuario):
                print(usuario[nome_usuario])
            else:
                print("Usuário não encontrado")
        elif (opc_conta == 4):
            nome_usuario = input("Digite o nome do usuário que deseja excluir algum dado: ")
            if nome_usuario in usuario:
                print("1 - Telefone")
                print("2 - Email")
                print("3 - Excluir conta")
                opc_excluir = int(input("Qual dado deseja excluir?: "))

    '''Localizar carregador'''
    elif (opcao == 2):
        print("1 - Zona Sul")
        print("2 - Zona Norte")
        print("3 - Zona Leste")
        print("4 - Zona Oeste")
        print("5 - Centro")
        zona_sp = int(input("Em qual zona de São Paulo você deseja carregar seu carro?: "))

        if (zona_sp == 1):
            print("Você pode recarregar seu carro no seguinte endereço: ")
        if (zona_sp == 2):
            print("Você pode recarregar seu carro no seguinte endereço:\n:"
                  "Rua Conselheiro Moreira de Barros, 1288 - Santana - CEP: 02018-012")
        if (zona_sp == 3):
            print("Você pode recarregar seu carro no seguinte endereço:\n"
                  "Rua Jacirendi, 850 - Tatuapé - CEP: 03080-000")
        if (zona_sp == 4):
            print("Você pode recarregar seu carro no seguinte endereço:\n"
                  "Rua Henrique Schaumann, 80 - Pinheiros - CEP: 05413-010")
        if (zona_sp == 5):
            print("Você pode recarregar seu carro no seguinte endereço:\n"
                  "Avenida Ipiranga, 200 - Centro - CEP: 01046-010")
        else:
            print("Opção inválida!")

    elif (opcao == 3):
        carga_atual=(float(input("Qual a carga atual do seu veiculo?: ")))
        kw_carregador = (float(input("Quantos Quilowatt-hora(kW) o carregador que você está utilizando possui?"
                                     "(7,4kW ou 22kW)")))
        

    '''elif (opcao == 4):
        print("Opção 4")
    elif (opcao == 5):
        print("Opção 5")
    else:
        print("Opção invalida!")'''
    resp = int(input("Deseja continuar? - 1-SIM | 0-NÃO: "))