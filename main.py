import sys
from sys import exit

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


    registro_codigo = 'registro' + str(codigo)

    f = open("arquivo.txt", "r")

    if not registro_codigo in f.read():
        registros = {
            registro_codigo: {
                'Pessoa': {'Nome': nome, 'Data de Nacimento': data_nascimento, 'CPF': cpf, 'Endereço': endereco},
                'Automóvel': {'Placa': placa, 'Modelo': modelo, 'Ano': ano, 'Cor': cor},
            }
        }
        
        arquivo = open("arquivo.txt", "a")
        arquivo.write(str(registros) + '\n')
        arquivo.close()
        return registros
    else:
        print('Esse código já existe, use outro código!')
        
while True:
    print('--------------------------')
    print('O que deseja fazer ?')
    print('1 - Inserir um registro')
    print('2 - Editar um registro')
    print('3 - Excluir um registro')
    print('4 - Sair')
    print('---------------------------')
    action = input("\n> ")
    if '1' in action:
        criar_registro(
            codigo=2, nome='Taynara', 
            data_nascimento='12/09/1995', 
            cpf='04930907110', endereco='Quadra 1 Lote 1700', 
            placa='EJKC3', modelo='Captur', ano='2017', cor='pink')
    elif '2' in action:
        print('editar')
    elif '3' in action:
        print('excluir')
    elif '4' in action:
        exit(0)

