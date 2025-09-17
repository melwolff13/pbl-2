codigosUsuarios = []
usuariosRegistrados = []
limiteDeErros = 3

ESTOQUE_POR_CATEGORIA = {
    "VESTUARIO": {"min": 20, "max": 150},
    "CALÇADOS": {"min": 15, "max": 100},
    "EQUIPAMENTOS DE VOLEI": {"min": 10, "max": 80},
    "EQUIPAMENTOS DE ACADEMIA": {"min": 10, "max": 120},
    "ACESSORIOS": {"min": 25, "max": 200}
}

def perguntaSimNao(pergunta):
    resposta = int(input(pergunta + " (1) SIM (2) NÃO\n"))
    return resposta


def pedirDadosUsuario(acao):
    while True:
        codigo = input("Código: ")
        if acao == "cadastro" and codigo in codigosUsuarios:
            print("\n"+"Já existe um usuário com esse código.\n")
        elif not codigo or not codigo.isdigit():
            print("\n"+"Código inválido. Tente novamente.\n")
        else:
            codigosUsuarios.append(codigo)
            break
      
    while True:
        nome = input("Nome: ")
        if not nome:
            print("\n"+"Digite um nome válido.\n")
        else:
            break
    
    while True:
        senha = input("Senha: ")
        if not senha:
            print("\n"+"Digite uma senha válida.\n")
        else:
            break
    print()
    usuario = [codigo, nome, senha]
    return usuario


def cadastrarUsuario():
    print("-- CADASTRAR NOVO USUÁRIO --\n")
    novoUsuario = pedirDadosUsuario("cadastro")
    usuariosRegistrados.append(novoUsuario)
    print("Usuário cadastrado com sucesso!\n")
    return novoUsuario


def loginUsuario(usuariosRegistrados):
    print("-- LOGIN --\n")
    tentativas = 1
    
    while True:
        usuario = pedirDadosUsuario("login")
        if tentativas >= limiteDeErros:
            print("Limite de erros excedido.\n")
            usuarioLogado = False
            break
        elif usuario in usuariosRegistrados:
            print("Login feito com sucesso!\n")
            usuarioLogado = usuario
            break
        else:
            tentativas+=1
            print("Usuário não encontrado\n")
            print("Tente novamente\n")
    
    return usuarioLogado


produtos = {}
codigosProdutos = []


def pedirDadosProduto():
    while True:
        nome = input("Nome: ")
        if not nome:
            print("\n"+"Digite um nome válido.\n")
        else:
            break

    while True:
        categoria = input("Categoria: ")
        if not categoria:
            print("\n"+"Digite uma categoria válida")
        else:
            break

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            break
        except ValueError:
            print("\n"+"Digite um valor inteiro.\n")
    while True:
        try:
            preco = float(input("Preço: R$"))
            break
        except ValueError:
            print("\n"+"Digite um valor numérico válido.\n")

    dadosProduto = [nome, categoria.upper(), quantidade, preco]

    return dadosProduto

    
def cadastrarProduto(produtos):
    print("-- CADASTRAR PRODUTO --\n")
    while True:
        codigo = input("Código: ")
        if not codigo.isdigit():
            print("\n"+"Apenas números são válidos")
        elif codigo in codigosProdutos:
            print("\n"+"Esse código já existe. Tente novamente.\n")
        else:
            codigosProdutos.append(codigo)
            break        

    produtos[codigo] = pedirDadosProduto()
    print()

    print("Produto cadastrado com sucesso!\n")


def exibirProdutosRegistrados(produtos, codigosProdutos):
    print("-- PRODUTOS REGISTRADOS --\n")
    if len(produtos) > 0:
        for codigo in codigosProdutos:
            print(f"PRODUTO {codigo}")
                
            print(f"Nome: {produtos[codigo][0]}")
            print(f"Categoria: {produtos[codigo][1]}")
            print(f"Quantidade: {produtos[codigo][2]}")
            print(f"Preço: R${produtos[codigo][3]}")
            print()
    else:
        print("Sem produtos registrados.\n")


def editarProduto(produtos, codigosProdutos):
    print("-- EDITAR PRDUTO --\n")
    print("Insira o código do produto que deseja editar:\n")
    exibirProdutosRegistrados(produtos, codigosProdutos)
    while True:
        codigoEscolhido = input()
        print()
        if not codigoEscolhido.isdigit():
            print("Apenas números são válidos.\n")
        elif codigoEscolhido not in codigosProdutos:
            print("Não há registro desse produto na lista. Tente novamente.\n")
        else:    
            print(f"Editar PRODUTO {codigoEscolhido}")
            
            produtos[codigoEscolhido] = pedirDadosProduto()
            print()

            print("Produto editado com sucesso!\n")
            break

                
def deletarProduto(produtos, codigosProdutos):
    print("-- DELETAR PRODUTO --\n")
    print("Insira o código do produto que deseja deletar:\n")
    exibirProdutosRegistrados(produtos, codigosProdutos)
    while True:
        codigoEscolhido = input("Código: ")
        print()
        if codigoEscolhido in codigosProdutos:
            confirmar = perguntaSimNao(f"Deseja excluir o produto {codigoEscolhido}?")
            print()
            if confirmar == 1:
                del produtos[codigoEscolhido]
                codigosProdutos.remove(codigoEscolhido)
                print(f"Produto {codigoEscolhido} deletado\n")
                exibirProdutosRegistrados(produtos, codigosProdutos)
                break
        else:
            print("Não há registro desse produto na lista. Tente novamente.\n")


def exibirRelatorioEstoque(usuarioLogado, produtos):
    print("-- RELATÓRIO DE ESTOQUE --\n")
    nome_usuario = usuarioLogado[1]
    codigo_usuario = usuarioLogado[0]
    print(f"Usuário: {nome_usuario} - Código: {codigo_usuario}\n")

    if len(produtos) == 0:
        print("Sem produtos em estoque para gerar relatório.\n")
        return

    quantidadeTotalProdutos = 0
    valorTotalEstoque = 0
    estoquePorCategoria = {}

    for dadosProduto in produtos.values():
        quantidadeProduto = dadosProduto[2]
        valorProduto = dadosProduto[3]
        categoriaProduto = dadosProduto[1]

        quantidadeTotalProdutos += quantidadeProduto
        valorTotalEstoque += quantidadeProduto * valorProduto

        if categoriaProduto in estoquePorCategoria:
            estoquePorCategoria[categoriaProduto] += quantidadeProduto
        else:
            estoquePorCategoria[categoriaProduto] = quantidadeProduto

    print(f"- Valor total em estoque: R${valorTotalEstoque:,.2f}\n")
    print(f"- Quantidade total de produtos em estoque: {quantidadeTotalProdutos}\n")
    print("-- Estoque por categoria --\n")

    for categoria, quantidade in estoquePorCategoria.items():
        porcentagemCategoria = (quantidade / quantidadeTotalProdutos) * 100
        print(f"- {categoria}: {porcentagemCategoria:,.2f}%")

    print()


primeiroAcesso = perguntaSimNao("\nPrimeiro acesso?")

if primeiroAcesso == 1:
    cadastrarUsuario()

usuarioLogado = loginUsuario(usuariosRegistrados)

if usuarioLogado:
    while True:
        acao = int(input("Selecione uma opção:\n"+
                        "(1) Cadastrar Produto\n"+
                        "(2) Editar Produto\n"+
                        "(3) Deletar Produto\n"+
                        "(4) Cadastrar Usuário\n"+
                        "(5) Exibir relatório de estoque\n"+
                        "(6) Encerrar\n"+
                        "\n"))
        print()
        match acao:
            case 1:
                cadastrarProduto(produtos)
            case 2:
                editarProduto(produtos, codigosProdutos)
            case 3:
                deletarProduto(produtos, codigosProdutos)
            case 4:
                cadastrarUsuario()
            case 5:
                exibirRelatorioEstoque(usuarioLogado, produtos)
            case 6:
                print("Programa encerrado.\n")
                break
            case _:
                print("Digite uma ação válida.\n")
                
                
<<<<<<< HEAD



# Selecionar uma entre 4 opções: Cadastro de Produto, Edição de Produto e Deleção de Produto, Cadastrar Usuário.

# Registrar 5 entradas por produto (código, nome, categoria, quantidade e preço);

# Registrar 3 entradas por usuário (código, nome, senha); 

# Declarar o valor mínimo e o valor máximo permitido em estoque por categoria, em constantes; 

# Calcular o quantitativo total de produtos em estoque em uma variável, e o valor total que eles representam em estoque (R$); 

# Apresentar a porcentagem de estoque no prompt de comando por categoria, junto do nome do usuário que está logado atualmente no sistema.
=======
>>>>>>> d677eb659635e4bde0500423f7b765d77e4a70c5
