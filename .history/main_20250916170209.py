#Fazer login no sistema, demonstrando as tentativas de erro e permitindo que um usuário logado cadastre novos usuários.

usuariosRegistrados = []
limiteDeErros = 3

def perguntaSimNao(pergunta):
    resposta = int(input(pergunta + " (1) SIM (2) NÃO\n"))
    return resposta



def pedirDados():
    codigo = input("Código: ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    print()
    usuario = [codigo, nome, senha]
    return usuario



def cadastrarUsuario():
    print("-- CADASTRAR NOVO USUÁRIO --\n")
    novoUsuario = pedirDados()
    usuariosRegistrados.append(novoUsuario)
    print("Usuário cadastrado com sucesso!\n")
    return novoUsuario



def loginUsuario(usuariosRegistrados):
    print("-- LOGIN --\n")
    usuarioEncontrado = False
    tentativas = 1
    
    while True:
        usuario = pedirDados()
        if tentativas >= limiteDeErros:
            print("Limite de erros excedido.\n")
            break
        elif usuario in usuariosRegistrados:
            print("Login feito com sucesso!\n")
            usuarioEncontrado = True
            break
        else:
            tentativas+=1
            print("Usuário não encontrado\n")
            print("Tente novamente\n")
    
    return usuarioEncontrado



produtos = {}
codigos = []
    
def cadastrarProduto(produtos):
    print("-- CADASTRAR PRODUTO --\n")
    codigo = input("Código: ")
    codigos.append(codigo)
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    quantidade = input("Quantidade: ")
    preco = input("Preço: ")
    print()

    produtos[codigo] = [nome, categoria, quantidade, preco]

    print("Produto cadastrado com sucesso!\n")



def exibirProdutosRegistrados(produtos, codigos):
    print("-- PRODUTOS REGISTRADOS --\n")
    if len(produtos) > 0:
        for codigo in codigos:
            print(f"PRODUTO {codigo}")
                
            print(f"Nome: {produtos[codigo][0]}")
            print(f"Categoria: {produtos[codigo][1]}")
            print(f"Quantidade: {produtos[codigo][2]}")
            print(f"Preço: {produtos[codigo][3]}")
            print()
    else:
        print("Sem produtos registrados.\n")



def editarProduto(produtos, codigos):
    print("-- EDITAR PRDUTO --\n")
    print("Insira o código do produto que deseja editar:\n")
    exibirProdutosRegistrados(produtos, codigos)
    while True:
        codigoEscolhido = input()
        print()
        if codigoEscolhido in codigos:
            print(f"Editar PRODUTO {codigoEscolhido}")
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            quantidade = input("Quantidade: ")
            preco = input("Preço: ")
            print()

            produtos[codigoEscolhido] = [nome, categoria, quantidade, preco]

            print("Produto editado com sucesso!\n")
            break

        else:
            print("Não há registro desse produto na lista. Tente novamente.\n")



def deletarProduto(produtos, codigos):
    print("-- DELETAR PRODUTO --\n")
    print("Insira o código do produto que deseja deletar:\n")
    exibirProdutosRegistrados(produtos, codigos)
    while True:
        codigoEscolhido = input()
        if codigoEscolhido in codigos:
            confirmar = perguntaSimNao(f"Deseja excluir o produto {codigoEscolhido}?")
            print()
            if confirmar == 1:
                del produtos[codigoEscolhido]
                codigos.remove(codigoEscolhido)
                print(f"Produto {codigoEscolhido} deletado\n")
                exibirProdutosRegistrados(produtos, codigos)
                break
        else:
            print("Não há registro desse produto na lista. Tente novamente.\n")



primeiroAcesso = perguntaSimNao("Primeiro acesso?")

if primeiroAcesso == 1:
    cadastrarUsuario()

usuarioEncontrado = loginUsuario(usuariosRegistrados)

if usuarioEncontrado:
    while True:
        acao = int(input("Selecione uma opção:\n"+
                        "(1) Cadastrar Produto\n"+
                        "(2) Editar Produto\n"+
                        "(3) Deletar Produto\n"+
                        "(4) Cadastrar Usuário\n"+
                        "\n"))
        print()
        match acao:
            case 1:
                cadastrarProduto(produtos)
            case 2:
                editarProduto(produtos, codigos)
            case 3:
                deletarProduto(produtos, codigos)

                



# Selecionar uma entre 4 opções: Cadastro de Produto, Edição de Produto e Deleção de Produto, Cadastrar Usuário.

# Registrar 5 entradas por produto (código, nome, categoria, quantidade e preço);

# Registrar 3 entradas por usuário (código, nome, senha); 

#  Declarar o valor mínimo e o valor máximo permitido em estoque por categoria, em constantes; 

# Calcular o quantitativo total de produtos em estoque em uma variável, e o valor total que eles representam em estoque (R$); 

# Apresentar a porcentagem de estoque no prompt de comando por categoria, junto do nome do usuário que está logado atualmente no sistema.