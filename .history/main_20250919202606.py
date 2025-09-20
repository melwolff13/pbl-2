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
    while True:
        try:
            resposta = int(input(pergunta + " (1) SIM (2) NÃO\n"))
            if resposta != 1 and resposta != 2:
                print("\n"+"Digite 1 para sim e 2 para não.\n")
            else:
                break
        except ValueError:
            print("\n"+"Entrada inválida. Digite um inteiro.\n")
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
        if not nome or nome.isdigit():
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
avisos = []


def pedirDadosProduto():
    while True:
        nome = input("Nome: ")
        if not nome or nome.isdigit():
            print("\n"+"Digite um nome válido.\n")
        else:
            break

    while True:
        categoria = input("Categoria: ")
        categoria = categoria.upper()
        if not categoria:
            print("\n"+"Digite uma categoria válida")        
        elif categoria not in ESTOQUE_POR_CATEGORIA:
            print(f"\nAVISO: A categoria '{categoria}' não possui limites de estoque pré-definidos.\n")
            break
        else:
            break

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if categoria in ESTOQUE_POR_CATEGORIA:
                if quantidade < ESTOQUE_POR_CATEGORIA[categoria]["min"]:
                    print(f"\nAVISO: Estoque de '{nome}' menor do que o mínimo.\n")
                elif quantidade > ESTOQUE_POR_CATEGORIA[categoria]["max"]:
                    print(f"\nAVISO: Estoque de '{nome}' maior do que o máximo.\n")
            break
        except ValueError:
            print("\n"+"Digite um valor inteiro.\n")

    while True:
        try:
            preco = float(input("Preço: R$"))
            break
        except ValueError:
            print("\n"+"Digite um valor numérico válido.\n")

    dadosProduto = [nome, categoria, quantidade, preco]

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
    exibirProdutosRegistrados(produtos, codigosProdutos)
    print("Insira o código do produto que deseja deletar (ou digite 0 para voltar ao menu):\n")
    
    def perguntaSimNaoLocal(pergunta):
        while True:
            try:
                resposta = int(input(pergunta + " (0) CANCELAR (1) SIM (2) NÃO\n"))
                if resposta not in (0, 1, 2):
                    print("\nDigite 1 para SIM, 2 para NÃO ou 0 para CANCELAR.\n")
                else:
                    return resposta
            except ValueError:
                print("\nEntrada inválida. Digite um inteiro.\n")
    
    while True:
        codigoEscolhido = input("Código: ").strip()
        print()

        if codigoEscolhido == "0":
            return

        if codigoEscolhido in codigosProdutos:
            confirmar = perguntaSimNaoLocal(f"Deseja excluir o produto {codigoEscolhido}?")
            print()

            if confirmar == 1:
                del produtos[codigoEscolhido]
                codigosProdutos.remove(codigoEscolhido)
                print(f"Produto {codigoEscolhido} deletado\n")
                exibirProdutosRegistrados(produtos, codigosProdutos)
                
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

print()
primeiroAcesso = perguntaSimNao("Primeiro acesso?")

if primeiroAcesso == 1:
    cadastrarUsuario()

usuarioLogado = loginUsuario(usuariosRegistrados)

if usuarioLogado:
    while True:
        acao = input("Selecione uma opção:\n"+
                        "(1) Cadastrar Produto\n"+
                        "(2) Editar Produto\n"+
                        "(3) Deletar Produto\n"+
                        "(4) Exibir Produtos Registrados\n"+
                        "(5) Cadastrar Usuário\n"+
                        "(6) Exibir Relatório de Estoque\n"+
                        "(7) Encerrar\n"+
                        "\n")
        print()
        match acao:
            case "1":
                cadastrarProduto(produtos)
            case "2":
                editarProduto(produtos, codigosProdutos)
            case "3":
                deletarProduto(produtos, codigosProdutos)
            case "4":
                exibirProdutosRegistrados(produtos, codigosProdutos)
            case "5":
                cadastrarUsuario()
            case "6":
                exibirRelatorioEstoque(usuarioLogado, produtos)
            case "7":
                print("Programa encerrado.\n")
                break
            case _:
                print("Digite uma ação válida.\n")
                

                
