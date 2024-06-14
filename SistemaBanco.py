import datetime
import textwrap


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair

=> """

def deposito(saldo, extrato, valor_desejado, /):
    if valor_desejado > 0:
        saldo += valor_desejado
        extrato += f"Depósito: R$ {valor_desejado:.2f}\n"

        print(saldo, extrato)

        return saldo, extrato
    
def saque(*, saldo, quantidade_saque, extrato, limite, limite_saques, numero_saques):          
    if quantidade_saque > saldo:

        print('Saldo não disponível.')

    elif quantidade_saque > limite:
            print("Foi excedido o limite de saque")

    elif numero_saques > limite_saques:
            print("você excedeu o limite de saques diários!")
        
    elif quantidade_saque > 0:

        saldo -= quantidade_saque
        extrato += f"Saque: R$ {quantidade_saque: .2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso!")

    else:
        print(" Falha na operação! Tente novamente")
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
        
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def novo_usuario(usuarios):
     cpf = input("Informe o CPF (somente número): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n Já existe usuário com esse CPF! ")
          return
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco })

     print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n Conta criada com sucesso!! ")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("Usuário não encontrado, fluxo de criação de conta encerrado! ")


def listar_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" + 100)
        print(textwrap.dedent(linha))

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_desejado = float(input("Informe o valor que deseja depositar: "))
        saldo, extrato = deposito(saldo, extrato, valor_desejado)

    elif opcao == "s":
        quantidade_saque = float(input("Informe o valor que deseja sacar: "))
        saldo, extrato = saque(saldo=saldo, quantidade_saque=quantidade_saque, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)
    
    elif opcao == "nu":
         novo_usuario(usuarios)

    elif opcao == "nc":

        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
             contas.append(conta)

    elif opcao == "lc":
         listar_contas(contas)

    elif opcao == "q":
        break

    else: 
        print("Erro! Operação inválida, tente novamente.")