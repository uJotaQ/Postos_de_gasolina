"""
*******************************************************************************
Sistema Operacional: Windows 10 - 64 Bits
Versão Da Linguagem: Python 3.11.1
Autor: João Gabriel Santos Silva
Componente Curricular: Algoritmos I
Concluido em: 28/08/2023
Declaro que este código foi elaborado por mim de forma
individual e não contém nenhum trecho de código de outro
 colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet.
Qualquer trecho de código de outra autoria que não a minha
está destacado com uma citação para o autor e a fonte do código,
e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
"""

# (1) Declaração De Variáveis
nome_posto_a: str = ""
nome_posto_b: str = ""
nome_posto_c: str = ""
valor_gasolina_posto_a: float = 0
valor_gasolina_posto_b: float = 0
valor_gasolina_posto_c: float = 0
valor_etanol_posto_a: float = 0
valor_etanol_posto_b: float = 0
valor_etanol_posto_c: float = 0
valor_diesel_posto_a: float = 0
valor_diesel_posto_b: float = 0
valor_diesel_posto_c: float = 0
escolha = "0"
escolha_combustivel = "0"
litros: float = 0
strings = ""
escolha_voltar: bool = False
string_voltar: str = ""
consultas: int = 0
menor_valor_a: int = 0
menor_valor_b: int = 0
menor_valor_c: int = 0
litros_posto_a: float = 0
litros_posto_b: float = 0
litros_posto_c: float = 0
gasolina_mais_barata: int = 0
etanol_mais_barato: int = 0
diesel_mais_barato: int = 0
# (2) Menu De Cadastramento
print("-=-" * 10)
print("     Preços De Combustível")
print("-=-" * 10)
print("")
# (3) Input de Nome e Preços De Combustiveis Dos Postos
# Com Validação De Dados Do Posto 1
nome_posto_a = input("Digite o nome do Posto 1: ").strip()

while True:
    strings = input("Digite o valor da gasolina do Posto 1: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_gasolina_posto_a = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_gasolina_posto_a = float(strings)
        break
    else:
        print("Digite um número válido!")

while True:
    strings = input("Digite o valor do etanol do Posto 1: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_etanol_posto_a = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_etanol_posto_a = float(strings)
        break
    else:
        print("Digite um número válido!")

while True:
    strings = input("Digite o valor do diesel do Posto 1: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_diesel_posto_a = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_diesel_posto_a = float(strings)
        break
    else:
        print("Digite um número válido!")
# (4) Input de Nome e Preços De Combustiveis Dos Postos
# Com Validação De Dados Do Posto 2
print("-" * 40)
nome_posto_b = input("Digite o nome do Posto 2: ").strip()
while True:
    strings = input("Digite o valor da gasolina do Posto 2: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_gasolina_posto_b = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_gasolina_posto_b = float(strings)
        break
    else:
        print("Digite um número válido!")

while True:
    strings = input("Digite o valor do etanol do Posto 2: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_etanol_posto_b = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_etanol_posto_b = float(strings)
        break
    else:
        print("Digite um número válido!")

while True:
    strings = input("Digite o valor do diesel do Posto 2: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_diesel_posto_b = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_diesel_posto_b = float(strings)
        break
    else:
        print("Digite um número válido!")

print("-" * 40)
# (5) Input de Nome e Preços De Combustiveis Dos Postos
# Com Validação De Dados Do Posto 3
nome_posto_c = input("Digite o nome do Posto 3: ").strip()
while True:
    strings = input("Digite o valor da gasolina do Posto 3: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_gasolina_posto_c = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_gasolina_posto_c = float(strings)
        break
    else:
        print("Digite um número válido!")

while True:
    strings = input("Digite o valor do etanol do Posto 3: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_etanol_posto_c = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_etanol_posto_c = float(strings)
        break
    else:
        print("Digite um número válido!")

while True:
    strings = input("Digite o valor do diesel do Posto 3: R$").strip()
    if strings.replace(".", "0").isnumeric():
        valor_diesel_posto_c = float(strings)
        break
    elif strings.replace(",", "0").isnumeric():
        strings = strings.replace(",", ".")
        valor_diesel_posto_c = float(strings)
        break
    else:
        print("Digite um número válido!")


# (6) Verificação Da Gasolina Mais Barata
if (valor_gasolina_posto_a <= valor_gasolina_posto_b
        and valor_gasolina_posto_a <= valor_gasolina_posto_c):
    gasolina_mais_barata = 1
elif (valor_gasolina_posto_b <= valor_gasolina_posto_a
        and valor_gasolina_posto_b <= valor_gasolina_posto_c):
    gasolina_mais_barata = 2
elif (valor_gasolina_posto_c <= valor_gasolina_posto_a
        and valor_gasolina_posto_c <= valor_gasolina_posto_b):
    gasolina_mais_barata = 3

# (7) Verificação Do Etanol Mais Barato
if (valor_etanol_posto_a <= valor_etanol_posto_b
        and valor_etanol_posto_a <= valor_etanol_posto_c):
    etanol_mais_barato = 1
elif (valor_etanol_posto_b <= valor_etanol_posto_a
        and valor_etanol_posto_b <= valor_etanol_posto_c):
    etanol_mais_barato = 2
elif (valor_etanol_posto_c <= valor_etanol_posto_a
        and valor_etanol_posto_c <= valor_etanol_posto_b):
    etanol_mais_barato = 3

# (8) Verificação Do Diesel Mais Barato
if (valor_diesel_posto_a <= valor_diesel_posto_b
        and valor_diesel_posto_a <= valor_diesel_posto_c):
    diesel_mais_barato = 1
elif (valor_diesel_posto_b <= valor_diesel_posto_a
        and valor_diesel_posto_b <= valor_diesel_posto_c):
    diesel_mais_barato = 2
elif (valor_diesel_posto_c <= valor_diesel_posto_a
        and valor_diesel_posto_c <= valor_diesel_posto_b):
    diesel_mais_barato = 3
 
# (9) Looping Principal Do Progama
while escolha == "0":
    print("")
    print("-=-" * 3)
    print("   Menu")
    print("-=-" * 3)
    print("")
    print("[1] Simulação De Abastecimento")
    print("[2] Consulta De Postos Mais Baratos")
    print("[3] Informações Dos Postos")
    print("[4] Sair")
    print("")
    escolha = input("Digite o número da opção desejada: ")
    # (10) Condicional Para Escolha De Simulação De Abastecimento
    if escolha == "1":
        print("-" * 40)
        print("[1] Gasolina")
        print("[2] Etanol")
        print("[3] Diesel")
        print("[4] Voltar")
        print("")
        escolha_combustivel = input("Digite o número da opção desejada: ")
        print("-" * 40)
        # (11) Verificação de escolha do combustível
        if (escolha_combustivel == "1" or escolha_combustivel == "2"
                or escolha_combustivel == "3"):
            while True:
                strings = input("Quantos litros deseja abastecer: ")
                if strings.replace(".", "0").isnumeric():
                    litros = float(strings)
                    break
                elif strings.replace(",", "0").isnumeric():
                    strings = strings.replace(",", ".")
                    litros = float(strings)
                    break
                else:
                    print("Digite um número válido!")
                    print("")
            print("-" * 40)
        elif escolha_combustivel == "4":
            escolha_voltar = True
        else:
            escolha_voltar = True
        # (12) Verificação De Gasolina Mais Barata
        if escolha_combustivel == "1":
            if gasolina_mais_barata == 1:
                print("")
                print("O Posto Com Menor Valor de Gasolina É O Posto ",
                      nome_posto_a,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_gasolina_posto_a))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_gasolina_posto_a)))
                print("-" * 40)
                litros_posto_a += litros
                consultas += 1
                menor_valor_a += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
            elif gasolina_mais_barata == 2:
                print("")
                print("O Posto Com Menor Valor de Gasolina É O Posto ",
                      nome_posto_b,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_gasolina_posto_b))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_gasolina_posto_b)))
                print("-" * 40)
                consultas += 1
                litros_posto_b += litros
                menor_valor_b += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
            elif gasolina_mais_barata == 3:
                print("")
                print(" Posto Com Menor Valor de Gasolina É O Posto ",
                      nome_posto_c,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_gasolina_posto_c))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_gasolina_posto_c)))
                print("-" * 40)
                consultas += 1
                litros_posto_c += litros
                menor_valor_c += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
        elif escolha_combustivel == "2":
            # (13) Verificação De Etanol Mais Barato
            if etanol_mais_barato == 1:
                print("")
                print("O Posto Com Menor Valor de Etanol É O Posto ",
                      nome_posto_a,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_etanol_posto_a))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_etanol_posto_a)))
                print("-" * 40)
                consultas += 1
                litros_posto_a += litros
                menor_valor_a += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
            elif etanol_mais_barato == 2:
                print("")
                print("O Posto Com Menor Valor de Etanol É O Posto ",
                      nome_posto_b,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_etanol_posto_b))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_etanol_posto_b)))
                print("-" * 40)
                consultas += 1
                litros_posto_b += litros
                menor_valor_b += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
            elif etanol_mais_barato == 3:
                print("")
                print("O Posto Com Menor Valor de Etanol É O Posto ",
                      nome_posto_c,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_etanol_posto_c))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_etanol_posto_c)))
                print("-" * 40)
                consultas += 1
                litros_posto_c += litros
                menor_valor_c += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
        elif escolha_combustivel == "3":
            # (14) Verificação De Diesel Mais Barato
            if diesel_mais_barato == 1:
                print("")
                print("O Posto Com Menor Valor de Diesel É O Posto ",
                      nome_posto_a,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_diesel_posto_a))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_diesel_posto_a)))
                print("-" * 40)
                consultas += 1
                litros_posto_a += litros
                menor_valor_a += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
            elif diesel_mais_barato == 2:
                print("")
                print("O Posto Com Menor Valor de Diesel É O Posto ",
                      nome_posto_b,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_diesel_posto_b))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_diesel_posto_b)))
                print("-" * 40)
                consultas += 1
                litros_posto_b += litros
                menor_valor_b += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
            elif diesel_mais_barato == 3:
                print("")
                print("O Posto Com Menor Valor de Diesel É O Posto ",
                      nome_posto_c,
                      " Com O Valor De R$%.2f Por Litro"
                      % (valor_diesel_posto_c))
                print("E Abastecendo %.2fL, você pagará R$%.2f" %
                      (litros, (litros * valor_diesel_posto_c)))
                print("-" * 40)
                consultas += 1
                litros_posto_c += litros
                menor_valor_c += 1
                string_voltar = input(
                  "Pressione [Enter] Para Voltar Ao Menu Principal!")
                if string_voltar == "":
                    escolha_voltar = True
                else:
                    escolha_voltar = True
        elif escolha_combustivel == "4":
            escolha_voltar is True
        else:
            print("")
            print("Escolha Uma Opção Válida!")
            escolha_voltar is True
    elif escolha == "2":
        # (15) Verificação De Todos Combustiveis Mais Baratos Para A Tabela
        if gasolina_mais_barata == 1:
            print("")
            print("O Posto Com Menor Valor de Gasolina É O Posto ",
                  nome_posto_a,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_gasolina_posto_a))
        elif gasolina_mais_barata == 2:
            print("")
            print("O Posto Com Menor Valor de Gasolina É O Posto ",
                  nome_posto_b,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_gasolina_posto_b))
        elif gasolina_mais_barata == 3:
            print("")
            print("O Posto Com Menor Valor de Gasolina É O Posto ",
                  nome_posto_c,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_gasolina_posto_c))
        print("-" * 40)
        if etanol_mais_barato == 1:
            print("")
            print("O Posto Com Menor Valor de Etanol É O Posto ",
                  nome_posto_a,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_etanol_posto_a))
        elif etanol_mais_barato == 2:
            print("")
            print("O Posto Com Menor Valor de Etanol É O Posto ",
                  nome_posto_b,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_etanol_posto_b))
        elif etanol_mais_barato == 3:
            print("")
            print("O Posto Com Menor Valor de Etanol É O Posto ",
                  nome_posto_c,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_etanol_posto_c))
        print("-" * 40)
        if diesel_mais_barato == 1:
            print("")
            print("O Posto Com Menor Valor de Diesel É O Posto ",
                  nome_posto_a,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_diesel_posto_a))
        elif diesel_mais_barato == 2:
            print("")
            print("O Posto Com Menor Valor de Diesel É O Posto ",
                  nome_posto_b,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_diesel_posto_b))
        elif diesel_mais_barato == 3:
            print("")
            print("O Posto Com Menor Valor de Diesel É O Posto ",
                  nome_posto_c,
                  " Com O Valor De R$%.2f Por Litro"
                  % (valor_diesel_posto_c))
        print("-" * 40)
        string_voltar = input(
            "Pressione [Enter] Para Voltar Ao Menu Principal!")
        if string_voltar == "":
            escolha_voltar = True
        else:
            escolha_voltar = True
    elif escolha == "3":
        # (16) Impressão De Todas As Informações Dos Postos
        print("")
        print("-" * 40)
        print(nome_posto_a)
        print("")
        print("Valor Da Gasolina: R$", valor_gasolina_posto_a)
        print("Valor Do Etanol: R$", valor_etanol_posto_a)
        print("Valor Do Diesel: R$", valor_diesel_posto_a)
        print("-" * 40)
        print(nome_posto_b)
        print("")
        print("Valor Da Gasolina: R$", valor_gasolina_posto_b)
        print("Valor Do Etanol: R$", valor_etanol_posto_b)
        print("Valor Do Diesel: R$", valor_diesel_posto_b)
        print("-" * 40)
        print(nome_posto_c)
        print("")
        print("Valor Da Gasolina: R$", valor_gasolina_posto_c)
        print("Valor Do Etanol: R$", valor_etanol_posto_c)
        print("Valor Do Diesel: R$", valor_diesel_posto_c)
        print("-" * 40)
        string_voltar = input(
            "Pressione [Enter] Para Voltar Ao Menu Principal!")
        if string_voltar == "":
            escolha_voltar = True
        else:
            escolha_voltar = True
    elif escolha == "4":
        # (17) Verificar Saída Do Programa
        break
    else:
        print("")
        print("Escolha Uma Opção Válida!")
        escolha = "0"
    if escolha_voltar is True:
        escolha = "0"
# (18) Saída Do Looping Principal / Impressão Do Relatório Final
print("-+-" * 4)
print(" Relatório")
print("-+-" * 4)
print("")
print("Quantidade de consultas realizadas no sistema: ", consultas)
print("-"*40)
# (19) Verificação De Quantidade De Vezes Que Cada Posto Foi O Mais Barato
if menor_valor_a != 0:
    print("O Posto ", nome_posto_a,
          " Teve O Menor Valor %d Vezes" % (menor_valor_a))
else:
    print("O Posto ", nome_posto_a,
          " Não teve o menor valor nenhuma vez nas consultas")
if menor_valor_b != 0:
    print("O Posto ", nome_posto_b,
          " Teve O Menor Valor %d Vezes" % (menor_valor_b))
else:
    print("O Posto ", nome_posto_b,
          " Não teve o menor valor nenhuma vez nas consultas")
if menor_valor_c != 0:
    print("O Posto ", nome_posto_c,
          " Teve O Menor Valor %d Vezes" % (menor_valor_c))
else:
    print("O Posto ", nome_posto_c,
          " Não teve o menor valor nenhuma vez nas consultas")
print("-"*40)
# (20) Verificação Para Impressão Da Média De Litros Por Posto
if menor_valor_a != 0:
    print("A Média de litros consultados no posto ", nome_posto_a,
          " Foi de %.2fL" % (litros_posto_a / menor_valor_a))
else:
    print("O Posto ", nome_posto_a, " Não teve média de litros computadas!")
if menor_valor_b != 0:
    print("A Média de litros consultados no posto ", nome_posto_b,
          " Foi de %.2fL" % (litros_posto_b / menor_valor_b))
else:
    print("O Posto ", nome_posto_b, " Não teve média de litros computadas!")
if menor_valor_c != 0:
    print("A Média de litros consultados no posto ", nome_posto_c,
          " Foi de %.2fL" % (litros_posto_c / menor_valor_c))
else:
    print("O Posto ", nome_posto_c, " Não teve média de litros computadas!")
print("-"*40)
# (21) Valor e Nome Da Gasolina Mais Barata Com Relação Aos Outros Postos
if gasolina_mais_barata == 1:
    print(
          f"A gasolina mais barata foi do posto {nome_posto_a}"
          f" com o valor de %.2fR$"
          % (valor_gasolina_posto_a))
    print(
          f"Comprando neste posto, você economizará %.2fR$"
          f" em relação ao posto {nome_posto_b}"
          % (valor_gasolina_posto_b - valor_gasolina_posto_a))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_c}" %
          (valor_gasolina_posto_c - valor_gasolina_posto_a))
elif gasolina_mais_barata == 2:
    print(
        f"A gasolina mais barata foi do posto {nome_posto_b}"
        f" com o valor de %.2fR$"
        % (valor_gasolina_posto_b))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_a}"
        % (valor_gasolina_posto_a - valor_gasolina_posto_b))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_c}" %
          (valor_gasolina_posto_c - valor_gasolina_posto_b))
elif gasolina_mais_barata == 3:
    print(
        f"A gasolina mais barata foi do posto {nome_posto_c}"
        f" com o valor de %.2fR$"
        % (valor_gasolina_posto_c))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_a}"
        % (valor_gasolina_posto_a - valor_gasolina_posto_c))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_b}" %
          (valor_gasolina_posto_b - valor_gasolina_posto_c))
print("-" * 50)
# (22) Valor e Nome Do Etanol Mais Barato Com Relação Aos Outros Postos
if etanol_mais_barato == 1:
    print(
        f"O etanol mais barato foi do posto {nome_posto_a}"
        f" com o valor de %.2fR$" %
        (valor_etanol_posto_a))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_b}"
        % (valor_etanol_posto_b - valor_etanol_posto_a))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_c}" %
          (valor_etanol_posto_c - valor_etanol_posto_a))
elif etanol_mais_barato == 2:
    print(
        f"O etanol mais barato foi do posto {nome_posto_b}"
        f" com o valor de %.2fR$" %
        (valor_etanol_posto_b))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_a}"
        % (valor_etanol_posto_a - valor_etanol_posto_b))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_c}" %
          (valor_etanol_posto_c - valor_etanol_posto_b))
elif etanol_mais_barato == 3:
    print(
        f"O etanol mais barato foi do posto {nome_posto_c}"
        f" com o valor de %.2fR$" %
        (valor_etanol_posto_c))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_a}"
        % (valor_etanol_posto_a - valor_etanol_posto_c))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_b}" %
          (valor_etanol_posto_b - valor_etanol_posto_c))
print("-" * 50)
# (23) Valor e Nome Do Diesel Mais Barato Com Relação Aos Outros Postos
if diesel_mais_barato == 1:
    print(
        f"O diesel mais barato foi do posto {nome_posto_a}"
        f" com o valor de %.2fR$" %
        (valor_diesel_posto_a))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_b}"
        % (valor_diesel_posto_b - valor_diesel_posto_a))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_c}" %
          (valor_diesel_posto_c - valor_diesel_posto_a))
elif diesel_mais_barato == 2:
    print(
        f"O diesel mais barato foi do posto {nome_posto_b}"
        f" com o valor de %.2fR$" %
        (valor_diesel_posto_b))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_a}"
        % (valor_diesel_posto_a - valor_diesel_posto_b))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_c}" %
          (valor_diesel_posto_c - valor_diesel_posto_b))
elif diesel_mais_barato == 3:
    print(
        f"O diesel mais barato foi do posto {nome_posto_c}"
        f" com o valor de %.2fR$" %
        (valor_diesel_posto_c))
    print(
        f"Comprando neste posto, você economizará %.2fR$"
        f" em relação ao posto {nome_posto_a}"
        % (valor_diesel_posto_a - valor_diesel_posto_c))
    print(f"E economizará %.2fR$ em relação ao posto {nome_posto_b}" %
          (valor_diesel_posto_b - valor_diesel_posto_c))
print("")
