import gera_planilhas
import sobe_dado
import os

def cria_planilha():
    st = input('Setor: ')
    if not os.path.exists(f'C:/Users/topo/Desktop/setor_{st}'):
        os.makedirs(f'C:/Users/topo/Desktop/setor_{st}')
    print(gera_planilhas.gera_planilhas(st))


def menu():
    print('1 - GERA PLANILHA')
    print('2 - SOBE DADOS CAMPO')

    op = int(input('\nOpcao ->> '))
    if op == 1:
        cria_planilha()
    elif op == 2:
        print(sobe_dado.sobe_dados())

menu()