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


    registro_codigo = 'registro' + str(codigo)

    f = open("arquivo.txt", "r")

    if not registro_codigo in f.read():
        registros = {
            registro_codigo: {
                'Pessoa': {'Nome': nome, 'Data de Nacimento': data_nascimento, 'CPF': cpf, 'Endereco': endereco},
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
            for k, y in x.items():
                print('Codigo: ' + i)
                print('\n' + '          ' + k + '          ' + '\n')
                for t, u in y.items():
                    print(t + ':' + u)

        line = f.readline()
        cnt += 1
    # res = ast.literal_eval(f.read()) 
    # print(type(res))
    # res = json.loads(f.read())
    # print(res)
    # for i in res:
    #     print(res[i])

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
        criar_registro(
            codigo=2, nome='Paulo', 
            data_nascimento='12/09/1995', 
            cpf='04930907110', endereco='Quadra 1 Lote 1700', 
            placa='EJKC3', modelo='Captur', ano='2017', cor='pink')
    elif '2' in action:
        print('editar')
    elif '3' in action:
        print('excluir')
    elif '4' in action:
        ver_registros()
    elif '5' in action:
        exit(0)
    else:
        print('Não existe essa opção!')

