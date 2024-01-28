# RAFAELA ALTHEMAN (24.123.0101) E MANUELLA PERES (24.123.0366)

# Função de importar data e hora:
from datetime import datetime
now = datetime.now()

# lista para adicionar clientes
clientes = []

# faz a leitura do arquivo chamado bancodedados
def carregar_dados():
    lista_dados = []
    #clientes = []
    bancodedados = open("dados.txt", "r")
    linhas = bancodedados.readlines()
    for linha in linhas:
        linha = linha.replace("\n", "")
        linha = linha.replace("[", "")
        linha = linha.replace("]", "")
        linha = linha.replace("'", "")
        linha.strip("\n")
        elementos = linha.split(", ")
        clientes.append(elementos)
    print(clientes)
    return lista_dados

carregar_dados()

#Função para salvar em um arquivo
def salvar():
    bancodedados = open("dados.txt", "w")
    for x in clientes:
        bancodedados.write(str(x) + "\n")    
    bancodedados.close()


# Funções do menu:
def novocliente(clientes):
    novocliente = []
    extrato = []
    razaosocial = input("Digite sua razão social: ")
    cnpj = input("Digite o CNPJ: ")
    tipodeconta = input("Digite o tipo de conta: ")
    valor = input("Digite o valor inicial da conta: ")
    senha = input("Digite sua senha: ")
    novocliente.append(razaosocial)
    novocliente.append(cnpj)
    novocliente.append(tipodeconta)
    novocliente.append(valor)
    novocliente.append(senha)
    novocliente.append(extrato)
    clientes.append(novocliente) #cliente adicionado
    # Adiciona clientes ao banco de dados:
    

# Apagar clientes criados com base no cnpj digitado
def apagacliente():
    print(clientes)
    cnpj = input("Digite o CNPJ: ")
    x = 0 
    while x <= len(clientes) - 1:
        if cnpj == clientes[x][1]:
            clientes.pop(x)
            x-=1
        x+=1
    

# Função que lista as informações do cliente a partir do cnpj inserido.
def listarcliente():
    for c in clientes:
        print()
        print("Razão Social: ",c[0])
        print("CNPJ: ",c[1])
        print("Tipo de Conta: ",c[2])
        print("Valor inicial: ",c[3])
        print()
    
       
#Percorremos pelos clientes da lista geral e selecionamos o cnpj e senha dele. Caso estejam corretos, diminuimos o valor debitado, ao valor inicial da conta!

def debito():
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite sua senha: ")
    valordebito = float(input("Digite o valor a ser debitado: "))
    for x in range (len(clientes)):
        if (cnpj == clientes[x][1]) and (senha == clientes[x][4]):
            if (clientes[x][2]=="comum"):
                valortotal = float(clientes[x][3]) - float(valordebito)*1.05
                tarifa = valordebito*0.05
                clientes[x][3] = valortotal 
                clientes[x][5]+=("Data: "+ str(now) + "  " + "-" + str(valordebito) + "    " + "Tarifa: " + str(tarifa) + "     " + "Saldo: " + str(valortotal) + "#") 
            if (clientes[x][2]=="comum") and (valortotal <= -1000):
                print("Saldo total após o débito atingiu o limite de -1000 reais")
                print() 
    for x in range (len(clientes)):
        if (cnpj == clientes[x][1]) and (senha == clientes[x][4]):       
            if (clientes[x][2]=="plus"):
                valortotal = float(clientes[x][3]) - float(valordebito)*1.03 
                tarifa = valordebito*0.03
                clientes[x][3] = valortotal 
                clientes[x][5]+=("Data: "+ str(now) + "  " +"-" + str(valordebito) + "    " + "Tarifa: " + str(tarifa) + "     " + "Saldo: " + str(valortotal) + "#")
            if (clientes[x][2]=="plus") and (valortotal <= -5000):
                print("Saldo total após o débito atingiu o limite de -5000 reais")
                print()
            return
         
    print("Senha ou CNPJ inválido!")
        

#Percorremos pelos clientes da lista geral e selecionamos o cnpj dele. Assim, somamos o valor depositado, ao valor inicial da conta!

def deposito():
    cnpj = input("Digite o CNPJ: ")
    valordeposito = input("Digite o valor a ser depositado: ")
    for x in range (len(clientes)):
        if (cnpj == clientes[x][1]):
            print()
            valortotal = float(clientes[x][3]) + float(valordeposito)
            tarifa = 0.00 
            print("Saldo após o depósito: ",valortotal)
            print()
            clientes[x][3] = valortotal 
            clientes[x][5]+=("Data: "+ str(now) + " + " + str(valordeposito) + "    " + "Tarifa: " + str(tarifa) + "     " + "Saldo: " + str(valortotal)+"#")
            return
    print("CNPJ inválido")

# Função que mostra todas as movimentações já realizadas na conta:

def extrato():
    cnpj = input("Digite o CNPJ: ")
    senha = input("Digite sua senha: ")
    for x in range (len(clientes)):
        if cnpj == clientes[x][1] and senha == clientes[x][4]:
            print("Razão social: ",clientes[x][0])
            print("CNPJ: ",clientes[x][1])
            print("Conta: ",clientes[x][2])
            for x in range(len(clientes)):
                print(clientes[x][5])
            # lista_extrato = clientes[x][5].split("#")
            # for item in lista_extrato:
            #     print(item)

#Se o cnpj e senha do primeiro cliente estiverem corretos, e o cnpj do segundo também, a transferência é realizada!!

def transferencia():
    cnpj = input("Digite o CNPJ de sua empresa: ")
    senha = input("Digite sua senha: ")
    cnpj2 = input("Digite o CNPJ do destinatário: ")
    valortransf = float(input("Digite o valor a ser transferido: "))
    remetente_encontrado = False
    destinatario_encontrado = False
    #Checa a lista clientes de acordo com as informações adicionadas anteriormente, caso o CNPJ  a senha estiverem certo, realiza a operação com base se a conta é comum ou plus.
    for remetente in clientes:
        if cnpj == remetente[1] and senha == remetente[4]:
            remetente_encontrado = True
            for destinatario in clientes:
                if cnpj2 == destinatario[1]:
                    destinatario_encontrado = True
                    if remetente[2] == "comum":
                        valortotal = float(remetente[3]) - float(valortransf) * 1.05
                        if valortotal <= -1000:
                            print("Transação não realizada")
                        else:
                            tarifa = valortransf * 0.05
                            remetente[3] = valortotal
                            remetente[5].append("Data: " + str(now) + "  " + "-" + str(valortransf) + "    " + "Tarifa: " + str(tarifa) + "     " + "Saldo: " + str(valortotal))

                            valortotal_destinatario = float(destinatario[3]) + float(valortransf)
                            destinatario[3] = valortotal_destinatario
                            tarifa2 = 0.00
                            destinatario[5].append("Data: " + str(now) + "  " + "+" + str(valortransf) + "    " + "Tarifa: " + str(tarifa2) + "     " + "Saldo: " + str(valortotal_destinatario))
                    
                    if remetente[2] == "plus":
                        valortotal = float(remetente[3]) - float(valortransf) * 1.03
                        if valortotal <= -5000:
                            print("Transação não realizada")
                        else:
                            tarifa = valortransf * 0.03
                            remetente[3] = valortotal
                            remetente[5].append("Data: " + str(now) + "  " + "-" + str(valortransf) + "    " + "Tarifa: " + str(tarifa) + "     " + "Saldo: " + str(valortotal))

                            valortotal_destinatario = float(destinatario[3]) + float(valortransf)
                            destinatario[3] = valortotal_destinatario
                            tarifa2 = 0.00
                            destinatario[5].append("Data: " + str(now) + "  " + "+" + str(valortransf) + "    " + "Tarifa: " + str(tarifa2) + "     " + "Saldo: " + str(valortotal_destinatario))
    #Caso não achar o remetente ou destinatário pelo CNPJ, a transferência não será realizada, caso contrário, será realizada.
    if not remetente_encontrado:
        print("CNPJ do remetente não encontrado. Transferência não realizada.")
    elif not destinatario_encontrado:
        print("CNPJ do destinatário não encontrado. Transferência não realizada.")
    else:
        print("Transferência realizada com sucesso.")

        
# Essa função irá realizar o cadastro de quantos clientes forem requisitados:

def cadastroclientes():
    numero = int(input("Digite a quantidade de clientes que deseja cadastrar: "))
    for x in range(numero):
        novocliente = []
        extrato = []
        razaosocial = input("Digite sua razão social: ")
        cnpj = input("Digite o CNPJ: ")
        tipodeconta = input("Digite o tipo de conta: ")
        valor = input("Digite o valor inicial da conta: ")
        senha = input("Digite sua senha: ")
        novocliente.append(razaosocial)
        novocliente.append(cnpj)
        novocliente.append(tipodeconta)
        novocliente.append(valor)
        novocliente.append(senha)
        novocliente.append(extrato)
        clientes.append(novocliente)
        


# fazer aparecer para o cliente o menu!!!

while True:
    # exibição do menu
    print("1. Novo Cliente")
    print("2. Apaga Cliente")
    print("3. Listar Clientes")
    print("4. Débito")
    print("5. Depósito")
    print("6. Extrato")
    print("7. Transferência entre contas")
    print("8. Cadastrar clientes")
    print("9. Sair")

    # Pedir um número do menu para o usuario:

    numero = int(input("Escolha uma opção e digite para confirmar: "))

    # Condições do menu:

    if numero==1:
        novocliente(clientes)
    if numero==2:
        apagacliente()
    if numero==3:
        listarcliente()
    if numero==4:
        debito()
    if numero==5:
        deposito()
    if numero==6:
        extrato()
    if numero==7:
        transferencia()
    if numero==8:
        cadastroclientes()
    if numero==9:
        #salva as informações adicionadas toda vez que o cliente clicar em "sair"
        salvar()
        break