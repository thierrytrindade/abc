# Definição das cores (usadas para dar formato ao texto na consola)
PREDEFENIDO = ""
AMARELO = "\033[1;33m"   
AZUL = "\033[1;34m"      
BRANCO = "\033[1;37m"    
CIANO = "\033[0;36m"     
ROXO = "\033[1;35m"      
VERDE = "\033[1;32m"     
VERMELHO = "\033[1;31m"  
END = "\033[0m"  # Anula a formatação anterior
il="\n\t» " # formatacao do inicio de todas as lineas fora do menu
me="\t║" # formatacao a esquerda do menu
t3 = f"{'\t'*3}" # prefixo dos prints finais com o X e o O com 3 tabulações




def mudarCor(jogador):
    # Define as opções válidas para a escolha de cores de 0 a 7
    opcoesValidas = [str(i) for i in range(8)]#str(i) serve para transformar o i em string para executar a verificacao
    # Pede a entrada do usuário e verifica se está entre as opções válidas
    while True:
        inputValido = inputVazio(inputCores)
        if inputValido not in opcoesValidas:
            printP(f"Entrada inválida! Por favor, insira um número válido entre {opcoesValidas[0]} e {opcoesValidas[-1]}.")
        else:
            break

    inputCor = int(inputValido)

    # Dicionário que mapeia as opções para (código da cor, nome da cor)
    cores = {
        0: (PREDEFENIDO, "Predefenido"),
        1: (AMARELO, "Amarelo"),
        2: (AZUL, "Azul"),
        3: (BRANCO, "Branco"),
        4: (CIANO, "Ciano"),
        5: (ROXO, "Roxo"),
        6: (VERDE, "Verde"),
        7: (VERMELHO, "Vermelho")
    }
    
    # Atualiza a cor do jogador de acordo com a escolha
    jogador[2], nomeCor = cores[inputCor]
    update = f"Personalização efetuada : A cor do(a) {jogador[0]} é {jogador[2] + nomeCor + END}"
    return update

# Jogo do Galo
# Rotinas

# Funções e seus significados
# 'continue' - serve para recomeçar um while

def inputVazio(mensagem):
    
    # Função que pede input e não permite que o utilizador deixe a entrada vazia
    while True:
        valor = input(il+mensagem)
        if valor == "":
            printP(f"Você não digitou nada! Por favor, insira um valor válido.")
        else:
            return valor
        

def printP(mensagem):
    # permite assim colocar automaticamente o prefixo antes do print reduzindo assim a quantidade de vezes em que o prefixo é escrito ou chamado dentro do print
    il="\n\t» "
    print(il+mensagem)


def inicializaJogadores():
    # Inicializa a lista de jogadores com [nome, símbolo, cor e vitórias (inicialmente 0)]
    return [
        ["Jogador 1", "X", AZUL, 0],
        ["Jogador 2", "O", VERDE, 0]
    ]

def resumo(nome1, nome2, vitorias1, vitorias2, empates):
    
    # Função para apresentar o resumo dos jogos (vitórias e empates)
    numeroDeJogos = vitorias1 + vitorias2 + empates # Calcula o total de jogos realizados
    printP(f"--- Resumo de {numeroDeJogos} Jogo(s) ---")
    if numeroDeJogos > 0:
        # Calcula e exibe a porcentagem de vitórias de cada jogador e de empates
        printP(f"{nome1} têm {vitorias1} vitória(s), {(vitorias1 / numeroDeJogos) * 100} %")
        printP(f"{nome2} têm {vitorias2} vitória(s), {(vitorias2 / numeroDeJogos) * 100} %")
        printP(f"Empates: {empates}, {(empates / numeroDeJogos) * 100}%")    
    else:
        printP(f"Nenhuma partida foi concluída!")

def criaTabuleiro(linha, coluna, valor):
    # Cria uma matriz (lista de listas) que representa o tabuleiro
    tabuleiro = []  # o tabuleiro é a matriz
    for i in range(linha):
        linhai = []
        for j in range(coluna):
            linhai += [valor]  # Preenche a linha com o valor indicado
        tabuleiro += [linhai]  # Adiciona a linha à matriz do tabuleiro
    return tabuleiro

def inicializaTabuleiro(tabuleiro, linha, coluna, valor):
    # Inicializa (ou limpa) o tabuleiro, atribuindo a cada célula o valor indicado
    for i in range(linha):
        for j in range(coluna):
            tabuleiro[i][j] = valor
    return tabuleiro


def mostraTabuleiro(tabuleiro, linha, coluna, jogador1, jogador2):
    print()# para iniciar com um espacamento de uma linha entre a opcao e o jogo
    # Percorre cada linha do tabuleiro.
    # 'linha' indica o número total de linhas que o tabuleiro possui.
    for i in range(linha):
        # Inicializa uma string vazia que armazenará a representação da linha atual.
        linhaExibicao = ""
        
        # Percorre cada coluna da linha atual.
        # 'coluna' indica o número total de colunas que o tabuleiro possui.
        for j in range(coluna):
            # Recupera o valor presente na célula atual do tabuleiro (linha i, coluna j).
            simboloMomento = tabuleiro[i][j]
            
            # Verifica se a célula está vazia.
            if simboloMomento == ' ':
                exibicao = ' '  # Se estiver vazia, exibe apenas um espaço.
            else:
                # Se a célula não está vazia, verifica se ela contém o símbolo do jogador 1.
                if simboloMomento == jogador1[1]:
                    # Se for o símbolo do jogador 1, adiciona a cor correspondente (jogador1[2]),
                    # seguido pelo símbolo e pela sequência de reset de cor (END) para não afetar o restante do texto.
                    exibicao = jogador1[2] + simboloMomento + END
                # Se não for o símbolo do jogador 1, verifica se é o símbolo do jogador 2.
                elif simboloMomento == jogador2[1]:
                    # Se for o símbolo do jogador 2, aplica a cor do jogador 2 (jogador2[2])
                    # seguida do símbolo e do reset de cor (END).
                    exibicao = jogador2[2] + simboloMomento + END
                else:
                    # Se a célula contém outro valor, apenas utiliza esse valor sem formatação adicional.
                    exibicao = simboloMomento
            
            # Adiciona à string da linha a célula formatada.
            # Coloca um espaço antes e depois do conteúdo para melhorar a visualização.
            linhaExibicao += f" {exibicao} "
            
            # Se não for a última coluna da linha, adiciona o separador vertical '|'
            if j < coluna - 1:
                linhaExibicao += "|"
        
        # Após montar a string completa da linha, imprime-a na tela.
        print("\t"*4+linhaExibicao)
        
        # Se não for a última linha do tabuleiro, imprime uma linha divisória.
        # Essa linha divisória ajuda a separar visualmente as linhas do tabuleiro.
        if i < linha - 1:
            print("\t"*4+"---+---+---")


#em vez de meter no input meto aqui, assim consigo fazer a verificação de se o valor introduzido no codigo é simplesmente um enter ou nao, pois metendo in(input(...)) caso que a pessoa simplesmente fizesse enter dava logo erro fechando o programa e a ideia é podermos verificar e permitir ao utilizador de retificar os seus erros sem ter que ter que andar sempre a abrir o programa de novo apos um erro e assim nao tendo que voltar a fazer tudo o que ja tinha feito antes e que foi perdido pelo programa se fechar

def menuJogo(espaco, menuTemporario, update, jogador1, jogador2, larguraTotal):
    
    # Função para apresentar menus diferentes consoante o estado do jogo (jogar, personalizar, etc.)

    pSair = f"{me}{'       9 - Sair       '.center(larguraTotal - 2)}║"
    pVoltar = f"{me}{'        9 - Voltar ao menu anterior       '.center(larguraTotal - 2)}║"
    END = "\033[0m"
    NEGRITO = "\033[1m"
    larguraTotal = 60

    print(espaco)

    while True:
        if menuTemporario == 1:
            # Menu principal: opções para Jogar ou Personalizar
            opcoesValidas = ("1", "2", "9")
                
            print(espaco)
            print("\t╔" + "═" * (larguraTotal - 2) + "╗    ,~.") 
            print(f"\t║{(NEGRITO + 'JOGO DO GALO' + END).center(larguraTotal + 6)}║    ( 9>")#print("\t║" + (NEGRITO+"JOGO DO GALO"+END).center(larguraTotal + 6) + "║")
            print(f"{me}{'      1 - Jogar       '.center(larguraTotal - 2)}║    /)_ )")
            print(f"{me}{'   2 - Personalizar   '.center(larguraTotal - 2)}║")
            print(pSair)
            print("\t╚" + "═" * (larguraTotal - 2) + "╝")

        if menuTemporario == 2:
            # Menu para escolher o tipo de partida (simples, melhor de 3, melhor de 5, etc.)
            opcoesValidas = ("1", "2", "3", "4", "9")
                       
            print(espaco)
            print("\t╔" + "═" * (larguraTotal - 2) + "╗") 
            print(f"{me}{(NEGRITO+" => Jogar "+END).center(larguraTotal + 6)}║")
            print(f"{me}{'      1 - Partida simples/indefinida      '.center(larguraTotal - 2)}║")
            print(f"{me}{'              2 - Melhor de 3             '.center(larguraTotal - 2)}║")
            print(f"{me}{'              3 - Melhor de 5             '.center(larguraTotal - 2)}║")
            print(f"{me}{'    4 - Personalizar o número de jogos    '.center(larguraTotal - 2)}║")
            print(pVoltar)
            print("\t╚" + "═" * (larguraTotal - 2) + "╝")
            
        if menuTemporario == 3:
            # Menu para personalizar as opções (nomes, cores, símbolos)
            opcoesValidas = ("1", "2", "3", "4", "5", "6", "9")
                
            print(espaco)
            if update != "":
                print(f"\t>>> {update}")
            print("\t╔" + "═" * (larguraTotal - 2) + "╗") 
            print(f"{me}{(NEGRITO+" => Personalizar "+END).center(larguraTotal + 6)}║")
            print(f"{me}{('1 - Mudar nome do(a) ' + jogador1).center(larguraTotal - 2)}║")
            print(f"{me}{('2 - Mudar cor do(a) ' + jogador1).center(larguraTotal - 2)}║")
            print(f"{me}{('3 - Mudar nome do(a) ' + jogador2).center(larguraTotal - 2)}║")
            print(f"{me}{('4 - Mudar cor do(a) ' + jogador2).center(larguraTotal - 2)}║")
            print(f"{me}{'5 - Mudar Simbolo de jogo'.center(larguraTotal - 2)}║")
            print(f"{me}{'6 - Mudar Simbolo para desistir'.center(larguraTotal - 2)}║")
            print(pVoltar)
            print("\t╚" + "═" * (larguraTotal - 2) + "╝")

        opcao = inputVazio(f"Escolha uma opção: ")

        if opcao not in opcoesValidas:
            print(espaco)
            printP("Entrada inválida! Por favor, insira um número válido.")
        else: 
            # Verifica a opção escolhida e ajusta o menu conforme necessário
            if opcao == "9" and menuTemporario != 1:
                menuTemporario = 1
            elif opcao == "9" and menuTemporario == 1:
                opcao = int(opcao)
                return 9, 1
            elif menuTemporario == 1 and opcao == "1":
                menuTemporario = 2
            elif menuTemporario == 1 and opcao == "2":
                menuTemporario = 3
            elif menuTemporario == 2 and opcao == "1":
                opcao = int(opcao)
                return 1, 1
            elif menuTemporario == 2 and opcao == "2":
                opcao = int(opcao)
                return 1, 3
            elif menuTemporario == 2 and opcao == "3":
                opcao = int(opcao)
                return 1, 5
            elif menuTemporario == 2 and opcao == "4":
                opcao = int(opcao)
                return 1, 2
            elif menuTemporario == 3 and opcao == "1":
                opcao = "2"
                opcao = int(opcao)
                return 2, 1
            elif menuTemporario == 3 and opcao == "2":
                opcao = "3"
                opcao = int(opcao)
                return 3, 1
            elif menuTemporario == 3 and opcao == "3":
                opcao = "4"
                opcao = int(opcao)
                return 4, 1
            elif menuTemporario == 3 and opcao == "4":
                opcao = "5"
                opcao = int(opcao)
                return 5, 1
            elif menuTemporario == 3 and opcao == "5":
                opcao = "6"
                opcao = int(opcao)
                return 6, 1
            elif menuTemporario == 3 and opcao == "6":
                opcao = "7"
                opcao = int(opcao)
                return 7, 1

def verificaVencedor(tabuleiro, simbolo):
    # Verifica se há uma linha, coluna ou diagonal com o mesmo símbolo, indicando vitória
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == simbolo) or (tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == simbolo):
            return True
    # Verifica as diagonais
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == simbolo) or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == simbolo):
        return True
    return False

def verificaEmpate(tabuleiro):
    # Verifica se ainda há jogadas disponíveis (células vazias representadas por ' ')
    for linha in tabuleiro:
        if ' ' in linha:
            return False  # Ainda há jogadas disponíveis
    return True  # Tabuleiro cheio, é empate

def jogo(galo, sJ1, sJ2, espaco, jogador1, jogador2, desistir):
    
    # Função principal que gere o jogo (jogadas, verificação de vitória ou empate)
    VERMELHO = "\033[1;31m"
    VERDE = "\033[1;32m"  
    END = "\033[0m"
    for i in range(9):  # Máximo de 9 jogadas num tabuleiro 3x3
        mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
        # Alterna entre os jogadores
        if i % 2 == 0:
            simbolo = sJ1
            turno = jogador1  # Jogador 1 joga nas jogadas pares
            oponente = jogador2
        else:
            simbolo = sJ2
            turno = jogador2 # Jogador 2 joga nas jogadas ímpares
            oponente = jogador1

        # Validação da jogada
        printP(f"Jogador {turno[0]} ({simbolo})")
        while True:        
            while True:
                linha = inputVazio(f"Linha 1..3 (ou desistir): ")
                if linha == desistir:
                    printP(f" {turno[0]} {VERMELHO}desistiu!{END} {oponente[0]} {VERDE}vence por desistência!{END}")
                    return oponente[1]  # Retorna o símbolo do oponente como vencedor
                if linha != "1" and linha != "2" and linha != "3":  # Previne valores inválidos
                    printP(f"Coordenadas inválidas! Por favor, insira valores entre 1 e 3.")
                    continue
                linha = int(linha)  # Converte para inteiro
                break

            while True:
                coluna = inputVazio(f"Coluna 1..3: ")
                if coluna != "1" and coluna != "2" and coluna != "3":
                    printP(f"Coordenadas inválidas! Por favor, insira valores entre 1 e 3.")
                    continue
                coluna = int(coluna)
                break

            print(espaco)  # Espaço para separar visualmente as jogadas
            if galo[linha-1][coluna-1] == ' ':
                galo[linha-1][coluna-1] = simbolo  # Marca a jogada
                break     
            else:
                printP(f"------ Posição ocupada, escolha outra!!!\n") 
                mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
                printP(f"Jogador {simbolo}")  # Solicita nova jogada se a posição já estiver ocupada

        # Verifica se houve vencedor após a jogada
        if verificaVencedor(galo, simbolo):
            mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
            # Identifica qual jogador venceu
            if simbolo == jogador1[1]:
                vencedor = jogador1[0]
                cor = jogador1[2]
            else:
                vencedor = jogador2[0]
                cor = jogador2[2]
            
            # Formata o nome e o símbolo com a cor, se definida
            if cor:
                nomeFormatado = cor + vencedor + END
                simboloFormatado = cor + simbolo + END
            else:
                nomeFormatado = vencedor
                simboloFormatado = simbolo

            printP(f" Venceu o jogador: {nomeFormatado} que jogou com o símbolo {simboloFormatado}")
            return simbolo
        elif verificaEmpate(galo):
            mostraTabuleiro(galo, 3, 3, jogador1, jogador2)
            printP(f" -- Empate!")
            return "empate"
    return None  # Retorna nada caso nenhuma condição de vitória ou empate seja atingida, para prevenir erros

# Variáveis de estatísticas e configurações principais (fora do loop do jogo)
larguraTotal = 60
empates = 0
opcao = 0
espaco = "\n" * 3 # Cria um espaçamento com 3 quebras de linha para melhorar a visibilidade do codigo no terminal
update = ""
inputCores = (f"0 - PREDEFENIDO{il}1 - AMARELO{il}2 - AZUL{il}3 - BRANCO{il}4 - CIANO{il}5 - ROXO{il}6 - VERDE{il}7 - VERMELHO{il}Enumere a cor que deseja utilizar para os seus símbolos: ")
menuTemporario = 1
jogador1, jogador2 = inicializaJogadores()
opcaoDois = 0  # Valor default; altera conforme a escolha do utilizador
desistir = "9"

# Garante que os símbolos dos jogadores sejam 'X' e 'O'
if jogador1[1] != "X" and jogador1[1] != "O":
    jogador1[1] = "X"
    
if jogador1[1] == "X":
    jogador2[1] = "O"
else:
    jogador2[1] = "X"

while True:
    # Loop principal do jogo: exibe o menu e processa a opção escolhida, o tipo de partida é a opcaoDois
    opcao, opcaoDois = menuJogo(espaco, menuTemporario, update, jogador1[0], jogador2[0], larguraTotal)

    NEGRITO = "\033[1m"
    # Programa principal: cria e inicializa o tabuleiro
    galo = criaTabuleiro(3, 3, 0)
    galo = inicializaTabuleiro(galo, 3, 3, ' ')

    # Se a opção for jogar
    if opcao == 1:
        # Se opcaoDois > 1, então é uma série de partidas
        if opcaoDois > 1:
            # Se o utilizador escolheu 2, pede um valor superior a 5 para o número de partidas
            if opcaoDois == 2:
                while True:
                    opcaoDois = int(inputVazio(f"Insira o número de partidas superior a 5: "))
                    if opcaoDois < 6:  # Previne valores inválidos
                        printP(f"Insira um valor superior a 5.")
                        continue
                    opcaoDois = int(opcaoDois)
                    break
                
            winsNeeded = (opcaoDois // 2) + 1  # Número de vitórias necessárias para ganhar a série
            currentWins1 = 0
            currentWins2 = 0
            
            printP(f"Iniciando série melhor de {opcaoDois} (necessário {winsNeeded} vitórias).")
            
            while currentWins1 < winsNeeded and currentWins2 < winsNeeded:
                # Limpa o tabuleiro para cada partida da serie
                galo = inicializaTabuleiro(galo, 3, 3, ' ')
                
                # Executa uma partida
                resultado = jogo(galo, jogador1[1], jogador2[1], espaco, jogador1, jogador2, desistir)
                
                # Atualiza estatísticas e vitórias da série
                if resultado == jogador1[1]:
                    jogador1[3] += 1
                    currentWins1 += 1
                elif resultado == jogador2[1]:
                    jogador2[3] += 1
                    currentWins2 += 1
                elif resultado == "empate":
                    empates += 1
                    printP(f"Empate nesta partida!")

                # Se não houve empate, inverte a ordem para que o perdedor comece o próximo jogo
                if resultado != "empate":
                    if resultado == jogador1[1]:
                        jogador1, jogador2 = jogador2, jogador1
                        currentWins1, currentWins2 = currentWins2, currentWins1
                    # Se jogador2 venceu, a ordem já está correta
            
            # Verifica quem venceu a série e mostra o resultado
            if currentWins1 == winsNeeded:
                printP(f"-- {jogador1[0]} venceu a série!")
            else:
                printP(f"-- {jogador2[0]} venceu a série!")
            
            # Apresenta o resumo final da série
            resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
            # Reinicia os resultados para a próxima série
            jogador1[3] = 0
            jogador2[3] = 0
            empates = 0

            # Volta ao menu de "Jogar"
            menuTemporario = 2

        else:
            # Modo partida única (opcaoDois == 1)
            while True:
                galo = inicializaTabuleiro(galo, 3, 3, ' ')  # Limpa o tabuleiro
                
                # Executa uma partida única
                resultado = jogo(galo, jogador1[1], jogador2[1], espaco, jogador1, jogador2, desistir)
                
                # Atualiza as estatísticas gerais
                if resultado == jogador1[1]:
                    jogador1[3] += 1
                elif resultado == jogador2[1]:
                    jogador2[3] += 1
                elif resultado == "empate":
                    empates += 1
                
                numeroDeJogos = jogador1[3] + jogador2[3] + empates
                
                # Mostra o placar atual
                printP(f"Placar atual: {jogador1[0]} - {jogador1[3]} x {jogador2[3]} - {jogador2[0]} | Empates: {empates}")
                
                # Pergunta se o utilizador quer jogar novamente
                while True:
                    continuar = inputVazio(f"Deseja jogar novamente (S/N): ").upper()
                    if continuar not in ["S", "N"]:
                        printP("Entrada inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
                    else:
                        break
                if continuar != "S":
                    print(espaco)
                    resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
                    # Reinicia as estatísticas
                    jogador1[3] = 0
                    jogador2[3] = 0
                    empates = 0

                    # Volta ao menu de "Jogar"
                    menuTemporario = 2
                    break
                else:
                    print(espaco)
                    # Se o jogador que venceu foi o primeiro, inverte a ordem para o próximo jogo
                    if resultado == jogador1[1]:
                        jogador1, jogador2 = jogador2, jogador1
                        # Atualiza os símbolos (opcional, conforme a lógica do jogo)
                        simboloJ1 = jogador1[1]
                        simboloJ2 = jogador2[1]

    elif opcao == 2:  # Opção para personalizar (mudar nome do jogador 1)
        jogador1[0] = inputVazio(f"Nome do primeiro jogador: ")
        update = f"Personalização efetuada : O nome do jogador 1 é {jogador1[0]}"
        menuTemporario = 3

    

    elif opcao == 4:  # Opção para mudar o nome do jogador 2
        jogador2[0] = inputVazio(f"Nome do primeiro jogador: ")
        update = f"Personalização efetuada : O nome do jogador 2 é " + jogador2[0]
        menuTemporario = 3

    elif opcao == 3:  # Mudar a cor do jogador 1
        update = mudarCor(jogador1)
        menuTemporario = 3

    elif opcao == 5:  # Mudar a cor do jogador 2
        update = mudarCor(jogador2)
        menuTemporario = 3
    

    elif opcao == 6:  # Opção para mudar o símbolo do jogador 1 (e automaticamente do jogador 2)
        while True:
            opcoesValidas = ("X","O")
            jogador1[1] = inputVazio(f"Qual símbolo que o {jogador1[0]} quer utilizar (X ou O): ").upper()
            if jogador1[1] not in opcoesValidas:
                print(espaco)
                printP(f"Entrada inválida! Por favor, insira um número válido.")
                continue
            break
        jogador2[1] = "O" if jogador1[1] == "X" else "X"
        update = (f"Personalização efetuada : {jogador1[0]} está neste momento com o símbolo {jogador1[1]} e {jogador2[0]} está com {jogador2[1]}")
        menuTemporario = 3
    
    elif opcao == 7:  # Opção para mudar o símbolo de desistência
        while True:                
            desistir = inputVazio(f"Qual símbolo que o que deseja usar para desistir : ")
            # Verifica se o símbolo não é "1", "2" ou "3"
            if desistir in ["1", "2", "3"]:
                printP("Símbolo inválido! Não pode ser 1, 2 ou 3. Por favor, tente novamente.")
            else:
                break
        update = f"Personalização efetuada : o simbolo de desistir foi alterado e agora é {desistir}"
        menuTemporario = 3

    elif opcao == 9:
        # Opção para sair do jogo
        print(espaco)  # Limpa o ecrã com linhas em branco
        printP(f"A sair do jogo....")

        resumo(jogador1[0], jogador2[0], jogador1[3], jogador2[3], empates)
        print(espaco)

        # Exibe uma mensagem de despedida e os créditos finais
        print("\t╔" + "═" * (larguraTotal - 2) + "╗")
        print(f"{me}{'🚀 O JOGO MAIS ÉPICO DE SEMPRE! 🚀'.center(larguraTotal - 4)}║")
        print(f"{me}{'🎮  Desenvolvido por TT Games 🎮'.center(larguraTotal - 4)}║")
        print("\t╠" + "═" * (larguraTotal - 2) + "╣")
        print(f"{me}{'🌟 Equipe de Desenvolvimento 2024 / 2025 🌟'.center(larguraTotal - 4)}║")
        print("\t╠" + "═" * (larguraTotal - 2) + "╣")
        print(f"{me}{'Disciplina Aplicações Informaticas B'.center(larguraTotal - 2)}║")
        print(f"{me}{'Turma 12B'.center(larguraTotal - 2)}║")
        print(f"{me}{'Thierry \'Chefe Supremo\' Trindade'.center(larguraTotal - 2)}║")
        print(f"{me}{'Santiago Santos'.center(larguraTotal - 2)}║")
        print(f"{me}{'Andre Madail'.center(larguraTotal - 2)}║")
        print("\t╠" + "═" * (larguraTotal - 2) + "╣")
        print(f"{me}{'🕵️  Testadores'.center(larguraTotal - 1)}║")
        print(f"{me}{'Professor com paciência infinita'.center(larguraTotal - 2)}║")
        print("\t╠" + "═" * (larguraTotal - 2) + "╣")
        print(f"{me}{'🛠️  Engine & Ferramentas Utilizadas'.center(larguraTotal - 1)}║")
        print(f"{me}{'Desenvolvido em Python 🐍'.center(larguraTotal - 3)}║")
        print(f"{me}{'Google & CTRL+C / CTRL+V'.center(larguraTotal - 2)}║")
        print("\t╠" + "═" * (larguraTotal - 2) + "╣")
        print(f"{me}{'🙌  Agradecimentos Especiais'.center(larguraTotal - 3)}║")
        print(f"{me}{'Google, Wikipedia e tutoriais infinitos'.center(larguraTotal - 2)}║")
        print(f"{me}{'CTRL+Z, salvando vidas desde sempre'.center(larguraTotal - 2)}║")
        print(f"{me}{'Impulsionado por café e ansiedade! ☕😖'.center(larguraTotal - 4)}║")
        print("\t╠" + "═" * (larguraTotal - 2) + "╣")
        print(f"{me}{'🎖️    Mensagem Final     '.center(larguraTotal - 1)}║")
        print(f"{me}{'\"Obrigado por jogar e aguentar os bugs!\"'.center(larguraTotal - 2)}║")
        print(f"{me}{'Sair...'.center(larguraTotal - 2)}║")
        print("\t╚" + "═" * (larguraTotal - 2) + "╝")
        
        print(f"{t3}{AZUL}╲╲       ╱╱{END}      {VERDE}╔═════╗{END}")
        print(f"{t3}{AZUL} ╲╲     ╱╱ {END}     {VERDE}╔╝     ╚╗{END}")
        print(f"{t3}{AZUL}  ╲╲   ╱╱  {END}     {VERDE}║       ║{END}")
        print(f"{t3}{AZUL}   ╲╲ ╱╱   {END}     {VERDE}║       ║{END}")
        print(f"{t3}{AZUL}   ╱╱ ╲╲   {END}     {VERDE}║       ║{END}")
        print(f"{t3}{AZUL}  ╱╱   ╲╲  {END}     {VERDE}║       ║{END}")
        print(f"{t3}{AZUL} ╱╱     ╲╲ {END}     {VERDE}╚╗     ╔╝{END}")
        print(f"{t3}{AZUL}╱╱       ╲╲{END}      {VERDE}╚═════╝{END}")

        # Fim dos créditos e mensagem final
        break

    else:
        # Caso a opção introduzida não seja válida
        printP(f"Opção inválida")