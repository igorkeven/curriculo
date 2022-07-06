

from time import sleep
from datetime import date, datetime
anoAtual = date.today().year
idade = f'{anoAtual - 1993} anos'
tempoAmor = f'{anoAtual - 2012} anos'
idadejoao = f'{anoAtual - 2014} anos'
print(f'\33[33m{"CURRÍCULO":^30}\33[m')
dados = {}
dados['experiencias'] = {'site': 'https://www.kevenaom.com'}
dados['Qualificações'] = {'formação Acadêmica' : {'nome':'UNIVESP','conclusão':2026 , 'curso': 'Engenharia da Computação'}, 'cursos com certificado' : {'curso 1 ': 'Python', 'curso 2':'Javascript', 'curso 3 ':'HTML e CSS'}, 'Informações adicionais': 'Programador com conhecimentos de Javascript, node JS, HTML, CSS e Python. Estudante de TI e com experiência de trabalho voluntário em criação de sites.' }
dados['dados pessoais'] = {'nome completo':'igor keven de moraes da silva'.upper(), 'idade': idade ,'aniverssario':'02/12/1992','email':'igorkeven@hotmail.com','instagram':'https://www.instagram.com/kevenigor/','celular':'(13)997273701','whatsapp':'https://wa.me/+5513997273701','endereco':'Rua Fileta presgrave do Amaral', 'numero': 241, 'bairro':'Ana Dias','cidade':'Itariri','estado':'SÃO PAULO'}


def linha(len):
    """
    mostra uma linha ( -= )
    e usa-se o parâmetro "len" para dizer o tamanho da linha.
    """
    print()
    print('-='*len)
    print()


def code0():
    print(f'\33[34mEste é o currículo de Igor Keven\33[m')
    print(f'\33[31m{"Digite o codigo do dado que deseja:":^30}\33[m')
    print(f"\33[7m{'cod':<5} {'dados':>17}\33[m")
    i = 0
    for c  in dados.keys():
        i +=1
        print(f"{i:>2}{c:>25} ")

    cod = int(input('Cod: '))
    if cod == 1:
        code1()
    elif cod == 2:
        code2()
    elif cod == 3:
        code3()


def code1():
    linha(60)
    print(f'\33[33m{"EXPERIÊNCIAS":^35}\33[m')
    print(f"criei um site para meu irmão '{dados['experiencias']['site']}' mas atualmente esta fora do ar ")
    print('Fora isso ainda não trabalhei na area.')
    print('Mas estou muito empolgado para uma oportunidade!')
    print('Meu github https://github.com/igorkeven')
    linha(60)


def code2():
    while True:
        i = 0
        print(f'\33[31m{"Digite o codigo do dado que deseja saber":^30}\33[m')
        print(f"\33[33m{'QUALIFICAÇÕES':^25}\33[m")
        print(f"\33[7m{'cod':<5} {'dados':>17}\33[m")
        for c  in dados['Qualificações'].keys():
            i +=1
            print(f"{i:>2}{c:>25} ")
        cod = int(input('Cod: '))
        if cod == 1:
            linha(50)
            print(f'Estudo {dados["Qualificações"]["formação Acadêmica"]["curso"]} na {dados["Qualificações"]["formação Acadêmica"]["nome"]} com conclusão em {dados["Qualificações"]["formação Acadêmica"]["conclusão"]}')
            linha(50)
        elif cod == 2:
            linha(30)
            print(f'\33[33m{"CURSOS COM CERTIFICADOS":^35}\33[m')
            print(f'Fiz os cursos de :')
            for c in dados['Qualificações']['cursos com certificado'].values():
                print(f'{c:^15}')
            print()
            print('todos com conclusão em 2022')
            linha(30)
        elif cod == 3:
            linha(50)
            print(f'\33[33m{"QUALIFICAÇÕES":^25}\33[m')
            print(dados['Qualificações']['Informações adicionais'])
            linha(50)
        cont = str(input('Se deseja voltar para o primeiro menu aperte (V) ou (C) para ver outro dado: ')).strip()[0]
        if cont in 'Vv':
            code0()
            break


def code3():
    linha(50)
    print(f"\33[33m{'DADOS PESSOAIS':^25}\33[m")
    print('AGUARDE OS DADOS IRÃO APARECER COM INTERVALO DE 2 SEGUNDOS')
    sleep(2)
    print(f'Me chamo {dados["dados pessoais"]["nome completo"]}')
    sleep(2)
    print(f'tenho {dados["dados pessoais"]["idade"]}')
    sleep(2)
    print(f'nasci em {dados["dados pessoais"]["aniverssario"]}')
    sleep(2)
    print(f'Moro com minha companheira RAIZA EMANOELE há {tempoAmor} ')
    sleep(2)
    print(f'Temos um filho JOÃO KEVEN  de {idadejoao} ')
    sleep(2)
    print(f'Moro na {dados["dados pessoais"]["endereco"]} nº{dados["dados pessoais"]["numero"]}')
    sleep(2)
    print(f'Cidade de {dados["dados pessoais"]["cidade"]}')
    sleep(2)
    print(f'bairro de {dados["dados pessoais"]["bairro"]}')
    sleep(2)
    print(f'Estado de {dados["dados pessoais"]["estado"]}')
    sleep(2.5)
    print(f'Telefone para contato: {dados["dados pessoais"]["celular"]}')
    sleep(2.5)
    print(f'Instagram: {dados["dados pessoais"]["instagram"]}')
    sleep(2.5)
    print(f'Whatsapp: {dados["dados pessoais"]["whatsapp"]}')
    sleep(2.5)
    linha(50)

while True:
    code0()
    cont = str(input('Deseja consultar outro dado? [S/N] ')).strip()[0]
    if cont in 'Nn':
        break
print()
print(' << \33[1;31m Agradeço a oportunidade e não vou decepcionar!! \33[m >>')
print()


