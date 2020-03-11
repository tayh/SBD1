from sys import exit
import json 
import ast 


def criar_registro(**kwargs):
    codigo = kwargs.get('codigo')
    nome = kwargs.get('nome')
    data_nascimento = kwargs.get('data_nascimento')
    cpf = kwargs.get('cpf')
    endereco = kwargs.get('endereco')
    placa = kwargs.get('placa')
    modelo = kwargs.get('modelo')
    ano = kwargs.get('ano')
    cor = kwargs.get('cor')


    registro_codigo = str(codigo)

    f = open("arquivo.txt", "r")

    if not registro_codigo in f.read():
        registros = {
            registro_codigo: {
                'Pessoa': {'Nome': nome, 'Data de Nascimento': data_nascimento, 'CPF': cpf, 'Endereco': endereco},
                'Automovel': {'Placa': placa, 'Modelo': modelo, 'Ano': ano, 'Cor': cor},
            }
        }
        
        arquivo = open("arquivo.txt", "a")
        arquivo.write(str(registros) + '\n')
        arquivo.close()
        return registros
    else:
        print('Esse código já existe, use outro código!')

def ver_registros():
    f = open("arquivo.txt", "r")
    line = f.readline()
    cnt = 1
    while line:
        res = ast.literal_eval(line)
        for i, x in res.items():
            print('-----------------------------')
            print('Código: ' + i)
            for k, y in x.items():
                print('\n' + '          ' + k + '          ' + '\n')
                for t, u in y.items():
                    print(t + ':' + u)

        line = f.readline()
        cnt += 1

def remover_registro():
    print('Insira o código registro que deseja remover: ')
    codigo = input()
    with open("arquivo.txt", "r") as f:
        lines = f.readlines()
    with open("arquivo.txt", "w") as f:
        for line in lines:
            if not codigo in line.strip("\n"):
                f.write(line)

def editar_registro():
    print('Insira o código do registro que deseja editar: ')
    codigo = input()
    print('Insira um novo Nome: ')
    nome = input()
    print('Insira uma nova Data de Nascimento: ')
    data_nascimento = input()
    print('Insira um novo o Endereço: ')
    endereco = input()
    print('Insira o novo CPF: ')
    cpf = input()
    print('Insira a nova placa do automovel: ')
    placa = input()
    print('Insira o novo modelo do automovel: ')
    modelo = input()
    print('Insira o novo ano do automovel: ')
    ano = input()
    print('Insira a nova cor do carro: ')
    cor = input()

    with open("arquivo.txt", "r") as f:
        lines = f.readlines()
    with open("arquivo.txt", "w") as f:
        for line in lines:
            if not codigo in line.strip("\n"):
                f.write(line)
    
    criar_registro(
        codigo=codigo, nome=nome, 
        data_nascimento=data_nascimento, 
        cpf=cpf, endereco=endereco, 
        placa=placa, modelo=modelo, ano=ano, cor=cor)

while True:
    print('--------------------------')
    print('O que deseja fazer ?')
    print('1 - Inserir um registro')
    print('2 - Editar um registro')
    print('3 - Excluir um registro')
    print('4 - Ver todos registros')
    print('5 - Sair')
    print('---------------------------')
    action = input("\n> ")
    if '1' in action:
        print('Insira o código: ')
        codigo = input()
        print('Insira o Nome: ')
        nome = input()
        print('Insira a Data de Nascimento: ')
        data_nascimento = input()
        print('Insira o Endereço: ')
        endereco = input()
        print('Insira o CPF: ')
        cpf = input()
        print('Insira a placa do automovel: ')
        placa = input()
        print('Insira o modelo do automovel: ')
        modelo = input()
        print('Insira o ano do automovel: ')
        ano = input()
        print('Insira a cor do carro: ')
        cor = input()
        criar_registro(
            codigo=codigo, nome=nome, 
            data_nascimento=data_nascimento, 
            cpf=cpf, endereco=endereco, 
            placa=placa, modelo=modelo, ano=ano, cor=cor)
    elif '2' in action:
        editar_registro()
    elif '3' in action:
        remover_registro()
    elif '4' in action:
        ver_registros()
    elif '5' in action:
        exit(0)
    else:
        print('Não existe essa opção!')

