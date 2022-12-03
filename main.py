#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# Projeto - Bolão da Copa do Mundo
# Novembro 2022

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# importanto bibliotecas
import streamlit as st
import sqlite3
import pandas as pd
import webbrowser
from datetime import date, datetime, time
from datetime import date, datetime, time,timedelta
from time import strftime
import time
import pytz
#import flag
#import emoji
import numpy as np # biblioteca Python usada para trabalhar com arrays
#import matplotlib.pyplot as plt # biblioteca para criar visualizações estáticas, animadas e interativas em Python
#from os import write
#from numpy.core.fromnumeric import size
#import Controllers.clientecontroller as clientecontroller
#import models.cliente as cliente
import pandas as pd
#import plotly.figure_factory as ff
from PIL import Image

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# funções

def grupos():
    
    '''
    
    Definição dos grupos da copa do mundo 2022
    
    '''
    
    grupos = np.array([['Catar','Equador','Senegal','Holanda','A'],
                       ['Inglaterra','Irã','Estados Unidos','País de Gales','B'],
                       ['Argentina','Arábia Saudita','México','Polônia','C'],
                       ['França','Austrália','Dinamarca','Tunísia','D'],
                       ['Espanha','Costa Rica','Alemanha','Japão','E'],
                       ['Bélgica','Canadá','Marrocos','Croácia','F'],
                       ['Brasil','Sérvia','Suíça','Camarões','G'],
                       ['Portugal','Gana','Uruguai','Coreia do Sul','H']]) # grupos da copa do mundo 2022
    
    return grupos

def listaSelecoes():

    '''

    Lista das seleções da copa do mundo 2022

    '''

    selecoes = ['Catar','Equador','Senegal','Holanda',
                'Inglaterra','Irã','Estados Unidos','País de Gales',
                'Argentina','Arábia Saudita','México','Polônia',
                'França','Austrália','Dinamarca','Tunísia',
                'Espanha','Costa Rica','Alemanha','Japão',
                'Bélgica','Canadá','Marrocos','Croácia',
                'Brasil','Sérvia','Suíça','Camarões',
                'Portugal','Gana','Uruguai','Coreia do Sul'] # seleções da copa do mundo 2022
    
    return selecoes

def cadastroApostador(login,senha):
    
    '''
    Cadastro do usuário e apostador:
    login, senha, pontos, cravadas, acertos, erros, nadas, não apostas, ...
    tabela do apostador.
    '''

    pontos     = 0
    cravadas   = 0
    acertos    = 0
    erros      = 0
    nadas      = 0
    naoapostas = 0

    apostador = [login, senha, pontos, cravadas, acertos, erros, nadas, naoapostas]
    numeroApostasIniciais = 20
    numeroApostasPrimeiraFase = 96
    numeroTotal = numeroApostasIniciais + numeroApostasPrimeiraFase
    for aposta in range(numeroTotal):
        apostador.append('')
    
    return apostador

def fazerApostaPrimeiraFase(cadastroApostador, nomeGrupo, nomeJogo, golMandante, golVisitante):

    # apostas - colocar botões
    '''
    
    Aposta em jogos da primeira fase:
    
    cadastro do apostador.
        
    nomes dos grupos: grupo A = 0; grupo B = 1; grupo C = 2; grupo D = 3; grupo E = 4; grupo F = 5; grupo G = 6; grupo H = 7.
    
    nomes dos jogos: jogo 1 = 0; jogo 2 = 1; jogo 3 = 2; jogo 4 = 3; jogo 5 = 4; jogo 6 = 5.
    
    gols do mandante e do visitante.    
    
    '''
    
    #-------------------------------------------------------------------------#        
    
    # rodada e jogo
    if nomeJogo == 0 or nomeJogo == 1:
        nomeRodada = 1
    elif nomeJogo == 2 or nomeJogo == 3:
        nomeRodada = 2
    elif nomeJogo == 4 or nomeJogo == 5:
        nomeRodada = 3
    
    
    if nomeRodada == 1:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 1: Time i1 x Time i2
        # rodada 1: Time i3 x Time i4
        time1 = 0
        time2 = 1
        time3 = 2
        time4 = 3
        if nomeJogo == 0:
            print('')
            print('Jogo 1')
            print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
        elif nomeJogo == 1:
            print('')
            print('Jogo 2')
            print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
    
    elif nomeRodada == 2:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 2: Time i1 x Time i3
        # rodada 2: Time i2 x Time i4
        time1 = 0
        time2 = 2
        time3 = 1
        time4 = 3
        if nomeJogo == 2:
            print('')
            print('Jogo 3')
            print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
        elif nomeJogo == 3:
            print('')
            print('Jogo 4')
            print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))

    elif nomeRodada == 3:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 3: Time i4 x Time i1
        # rodada 3: Time i2 x Time i3
        time1 = 3
        time2 = 0
        time3 = 1
        time4 = 2
        if nomeJogo == 4:
            print('')
            print('Jogo 5')
            print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
        elif nomeJogo == 5:
            print('')
            print('Jogo 6')
            print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))

    #-------------------------------------------------------------------------#

    # colocando o resultado no cadastro do usuário
    #cadastroApostador[-1][nomeGrupo][nomeJogo-1][0], cadastroApostador[-1][nomeGrupo][nomeJogo-1][1] = golMandante, golVisitante
    #cadastroApostador[-1][nomeGrupo][nomeJogo][0], cadastroApostador[-1][nomeGrupo][nomeJogo][1] = golMandante, golVisitante
    cadastroApostador[28+2*6*nomeGrupo+2*nomeJogo], cadastroApostador[28+2*6*nomeGrupo+2*nomeJogo+1] = golMandante, golVisitante
    
    print('')
    print('Aposta realizada!')
    if nomeJogo == 0 or nomeJogo == 2 or nomeJogo == 4:
        #print('%s %d X %d %s'%(selecoes()[nomeGrupo][time1][0],golMandante,golVisitante,selecoes()[nomeGrupo][time2][0]))
        print('%s %d X %d %s'%(grupos()[nomeGrupo][time1],golMandante,golVisitante,grupos()[nomeGrupo][time2]))
    elif nomeJogo == 1 or nomeJogo == 3 or nomeJogo == 5:
        #print('%s %d X %d %s'%(selecoes()[nomeGrupo][time3][0],golMandante,golVisitante,selecoes()[nomeGrupo][time4][0]))
        print('%s %d X %d %s'%(grupos()[nomeGrupo][time3],golMandante,golVisitante,grupos()[nomeGrupo][time4]))

    return cadastroApostador

def apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado):
    
    # apostas podio
    usuario[9] = listaSelecoes().index(apostaCampeao) #apostaCampeao
    usuario[10] = listaSelecoes().index(apostaViceCampeao) #apostaViceCampeao
    usuario[11] = listaSelecoes().index(apostaTerceiroColocado) #apostaTerceiroColocado

    return

def apostaGrupos(usuario,nomeGrupo,apostaPrimeiroGrupo,apostaSegundoGrupo):
    
    # apostas grupos
    if nomeGrupo == 0:
        usuario[12] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[13] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 1:
        usuario[14] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[15] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 2:
        usuario[16] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[17] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 3:
        usuario[18] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[19] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 4:
        usuario[20] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[21] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 5:
        usuario[22] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[23] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 6:
        usuario[24] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[25] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo
    elif nomeGrupo == 7:
        usuario[26] = listaSelecoes().index(apostaPrimeiroGrupo) #apostaPrimeiroGrupo
        usuario[27] = listaSelecoes().index(apostaSegundoGrupo) #apostaSegundoGrupo

    return

def horarioJogo(anoJogo,mesJogo,diaJogo,horaJogo,minutoJogo):
    # data e horário atual
    dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')
        
    #data_atual = datetime.now()
    #data_string = data_atual.strftime('%d/%m/%y %H:%M')
    #dataHoraMinutoAtual =datetime.strptime(data_string, '%d/%m/%y %H:%M')

    #print(dataHoraMinutoAtual)
    #print('')
    dataHoraMinutoJogo = datetime(anoJogo,mesJogo,diaJogo,horaJogo,minutoJogo)
    
    #print(dataHoraMinutoJogo)
    #print('')
    if dataHoraMinutoAtual >= dataHoraMinutoJogo:
        inicioJogo = False
        #print('acabou!')
    else:
        inicioJogo = True
        #print('Dá uma seguradinha ..')
    
    return inicioJogo

def horarioJogoGrupo(nomeGrupo,nomeJogo):
    
    # datas e horários dos jogos da primeira fase
    if nomeGrupo == 0:
        # Grupo A
        if nomeJogo == 0:
            # Catar x Equador
            inicioJogo = horarioJogo(2022,11,20,13,0)
        elif nomeJogo == 1:
            # Senegal X Holanda
            inicioJogo = horarioJogo(2022,11,21,13,0)
        elif nomeJogo == 2:
            # Catar X Senegal
            inicioJogo = horarioJogo(2022,11,25,10,0)
        elif nomeJogo == 3:
            # Holanda X Equador
            inicioJogo = horarioJogo(2022,11,25,13,0)
        elif nomeJogo == 4:
            # Holanda X Catar
            inicioJogo = horarioJogo(2022,11,29,12,0)
        elif nomeJogo == 5:
            # Equador X Senegal
            inicioJogo = horarioJogo(2022,11,29,12,0)
    
    elif nomeGrupo == 1:
        # Grupo B
        if nomeJogo == 0:
            # Inglaterra X Irã
            inicioJogo = horarioJogo(2022,11,21,10,0)
        elif nomeJogo == 1:
            # Estados Unidos X País de Gales
            inicioJogo = horarioJogo(2022,11,21,16,0)
        elif nomeJogo == 2:
            # Inglaterra X Estados Unidos
            inicioJogo = horarioJogo(2022,11,25,16,0)
        elif nomeJogo == 3:
            # País de Gales X Irã
            inicioJogo = horarioJogo(2022,11,25,7,0)
        elif nomeJogo == 4:
            # País de Gales X Inglaterra
            inicioJogo = horarioJogo(2022,11,29,16,0)
        elif nomeJogo == 5:
            # Irã X Estados Unidos
            inicioJogo = horarioJogo(2022,11,29,16,0)
    
    elif nomeGrupo == 2:
        # Grupo C
        if nomeJogo == 0:
            # Argentina X Arábia Saudita
            inicioJogo = horarioJogo(2022,11,22,7,0)
        elif nomeJogo == 1:
            # México X Polônia
            inicioJogo = horarioJogo(2022,11,22,13,0)
        elif nomeJogo == 2:
            # Argentina X México
            inicioJogo = horarioJogo(2022,11,26,16,0)
        elif nomeJogo == 3:
            # Polônia X Arábia Saudita
            inicioJogo = horarioJogo(2022,11,26,10,0)
        elif nomeJogo == 4:
            # Polônia X Argentina
            inicioJogo = horarioJogo(2022,11,30,16,0)
        elif nomeJogo == 5:
            # Arábia Saudita
            inicioJogo = horarioJogo(2022,11,30,16,0)
    
    elif nomeGrupo == 3:
        # Grupo D
        if nomeJogo == 0:
            # França X Austrália
            inicioJogo = horarioJogo(2022,11,22,16,0)
        elif nomeJogo == 1:
            # Dinamarca X Tunísia
            inicioJogo = horarioJogo(2022,11,22,10,0)
        elif nomeJogo == 2:
            # França X Dinamarca
            inicioJogo = horarioJogo(2022,11,26,13,0)
        elif nomeJogo == 3:
            # Tunísia X Austrália
            inicioJogo = horarioJogo(2022,11,26,7,0)
        elif nomeJogo == 4:
            # Tunísia X França
            inicioJogo = horarioJogo(2022,11,30,12,0)
        elif nomeJogo == 5:
            # Austrália X Dinamarca
            inicioJogo = horarioJogo(2022,11,30,12,0)
    
    elif nomeGrupo == 4:
        # Grupo E
        if nomeJogo == 0:
            # Espanha X Costa Rica
            inicioJogo = horarioJogo(2022,11,23,13,0)
        elif nomeJogo == 1:
            # Alemanha X Japão
            inicioJogo = horarioJogo(2022,11,23,10,0)
        elif nomeJogo == 2:
            # Espanha X Alemanha
            inicioJogo = horarioJogo(2022,11,27,16,0)
        elif nomeJogo == 3:
            # Japão X Costa Rica
            inicioJogo = horarioJogo(2022,11,27,7,0)
        elif nomeJogo == 4:
            # Japão X Espanha
            inicioJogo = horarioJogo(2022,12,1,16,0)
        elif nomeJogo == 5:
            # Costa Rica X Alemanha
            inicioJogo = horarioJogo(2022,12,1,16,0)
    
    elif nomeGrupo == 5:
        # Grupo F
        if nomeJogo == 0:
            # Bélgica X Canadá
            inicioJogo = horarioJogo(2022,11,23,16,0)
        elif nomeJogo == 1:
            # Marrocos X Croácia
            inicioJogo = horarioJogo(2022,11,23,7,0)
        elif nomeJogo == 2:
            # Bélgica X Marrocos
            inicioJogo = horarioJogo(2022,11,27,10,0)
        elif nomeJogo == 3:
            # Croácia X Canadá
            inicioJogo = horarioJogo(2022,11,27,13,0)
        elif nomeJogo == 4:
            # Croácia X Bélgica
            inicioJogo = horarioJogo(2022,12,1,12,0)
        elif nomeJogo == 5:
            # Canadá X Marrocos
            inicioJogo = horarioJogo(2022,12,1,12,0)
    
    elif nomeGrupo == 6:
        # Grupo G
        if nomeJogo == 0:
            # Brasil X Sérvia
            inicioJogo = horarioJogo(2022,11,24,16,0)
        elif nomeJogo == 1:
            # Suíça X Camarões
            inicioJogo = horarioJogo(2022,11,24,7,0)
        elif nomeJogo == 2:
            # Brasil X Suíça
            inicioJogo = horarioJogo(2022,11,28,13,0)
        elif nomeJogo == 3:
            # Camarões X Sérvia
            inicioJogo = horarioJogo(2022,11,28,7,0)
        elif nomeJogo == 4:
            # Camarões X Brasil
            inicioJogo = horarioJogo(2022,12,2,16,0)
        elif nomeJogo == 5:
            # Sérvia X Suíça
            inicioJogo = horarioJogo(2022,12,2,16,0)
    
    elif nomeGrupo == 7:
        # Grupo H
        if nomeJogo == 0:
            # Portugal x Gana
            inicioJogo = horarioJogo(2022,11,24,13,0)
        elif nomeJogo == 1:
            # Uruguai X Coreia do Sul
            inicioJogo = horarioJogo(2022,11,24,10,0)
        elif nomeJogo == 2:
            # Portugal X Uruguai
            inicioJogo = horarioJogo(2022,11,28,16,0)
        elif nomeJogo == 3:
            # Coreia do Sul X Gana
            inicioJogo = horarioJogo(2022,11,28,10,0)
        elif nomeJogo == 4:
            # Coreia do Sul x Portugal
            inicioJogo = horarioJogo(2022,12,2,12,0)
        elif nomeJogo == 5:
            # Gana X Uruguai
            inicioJogo = horarioJogo(2022,12,2,12,0)
    
    return inicioJogo

def dataHorarioJogoGrupo(nomeGrupo,nomeJogo):
    
    # datas e horários dos jogos da primeira fase
    if nomeGrupo == 0:
        # Grupo A
        if nomeJogo == 0:
            # Catar x Equador
            inicioJogo = datetime(2022,11,20,13,0)
        elif nomeJogo == 1:
            # Senegal X Holanda
            inicioJogo = datetime(2022,11,21,13,0)
        elif nomeJogo == 2:
            # Catar X Senegal
            inicioJogo = datetime(2022,11,25,10,0)
        elif nomeJogo == 3:
            # Holanda X Equador
            inicioJogo = datetime(2022,11,25,13,0)
        elif nomeJogo == 4:
            # Holanda X Catar
            inicioJogo = datetime(2022,11,29,12,0)
        elif nomeJogo == 5:
            # Equador X Senegal
            inicioJogo = datetime(2022,11,29,12,0)
    
    elif nomeGrupo == 1:
        # Grupo B
        if nomeJogo == 0:
            # Inglaterra X Irã
            inicioJogo = datetime(2022,11,21,10,0)
        elif nomeJogo == 1:
            # Estados Unidos X País de Gales
            inicioJogo = datetime(2022,11,21,16,0)
        elif nomeJogo == 2:
            # Inglaterra X Estados Unidos
            inicioJogo = datetime(2022,11,25,16,0)
        elif nomeJogo == 3:
            # País de Gales X Irã
            inicioJogo = datetime(2022,11,25,7,0)
        elif nomeJogo == 4:
            # País de Gales X Inglaterra
            inicioJogo = datetime(2022,11,29,16,0)
        elif nomeJogo == 5:
            # Irã X Estados Unidos
            inicioJogo = datetime(2022,11,29,16,0)
    
    elif nomeGrupo == 2:
        # Grupo C
        if nomeJogo == 0:
            # Argentina X Arábia Saudita
            inicioJogo = datetime(2022,11,22,7,0)
        elif nomeJogo == 1:
            # México X Polônia
            inicioJogo = datetime(2022,11,22,13,0)
        elif nomeJogo == 2:
            # Argentina X México
            inicioJogo = datetime(2022,11,26,16,0)
        elif nomeJogo == 3:
            # Polônia X Arábia Saudita
            inicioJogo = datetime(2022,11,26,10,0)
        elif nomeJogo == 4:
            # Polônia X Argentina
            inicioJogo = datetime(2022,11,30,16,0)
        elif nomeJogo == 5:
            # Arábia Saudita
            inicioJogo = datetime(2022,11,30,16,0)
    
    elif nomeGrupo == 3:
        # Grupo D
        if nomeJogo == 0:
            # França X Austrália
            inicioJogo = datetime(2022,11,22,16,0)
        elif nomeJogo == 1:
            # Dinamarca X Tunísia
            inicioJogo = datetime(2022,11,22,10,0)
        elif nomeJogo == 2:
            # França X Dinamarca
            inicioJogo = datetime(2022,11,26,13,0)
        elif nomeJogo == 3:
            # Tunísia X Austrália
            inicioJogo = datetime(2022,11,26,7,0)
        elif nomeJogo == 4:
            # Tunísia X França
            inicioJogo = datetime(2022,11,30,12,0)
        elif nomeJogo == 5:
            # Austrália X Dinamarca
            inicioJogo = datetime(2022,11,30,12,0)
    
    elif nomeGrupo == 4:
        # Grupo E
        if nomeJogo == 0:
            # Espanha X Costa Rica
            inicioJogo = datetime(2022,11,23,13,0)
        elif nomeJogo == 1:
            # Alemanha X Japão
            inicioJogo = datetime(2022,11,23,10,0)
        elif nomeJogo == 2:
            # Espanha X Alemanha
            inicioJogo = datetime(2022,11,27,16,0)
        elif nomeJogo == 3:
            # Japão X Costa Rica
            inicioJogo = datetime(2022,11,27,7,0)
        elif nomeJogo == 4:
            # Japão X Espanha
            inicioJogo = datetime(2022,12,1,16,0)
        elif nomeJogo == 5:
            # Costa Rica X Alemanha
            inicioJogo = datetime(2022,12,1,16,0)
    
    elif nomeGrupo == 5:
        # Grupo F
        if nomeJogo == 0:
            # Bélgica X Canadá
            inicioJogo = datetime(2022,11,23,16,0)
        elif nomeJogo == 1:
            # Marrocos X Croácia
            inicioJogo = datetime(2022,11,23,7,0)
        elif nomeJogo == 2:
            # Bélgica X Marrocos
            inicioJogo = datetime(2022,11,27,10,0)
        elif nomeJogo == 3:
            # Croácia X Canadá
            inicioJogo = datetime(2022,11,27,13,0)
        elif nomeJogo == 4:
            # Croácia X Bélgica
            inicioJogo = datetime(2022,12,1,12,0)
        elif nomeJogo == 5:
            # Canadá X Marrocos
            inicioJogo = datetime(2022,12,1,12,0)
    
    elif nomeGrupo == 6:
        # Grupo G
        if nomeJogo == 0:
            # Brasil X Sérvia
            inicioJogo = datetime(2022,11,24,16,0)
        elif nomeJogo == 1:
            # Suíça X Camarões
            inicioJogo = datetime(2022,11,24,7,0)
        elif nomeJogo == 2:
            # Brasil X Suíça
            inicioJogo = datetime(2022,11,28,13,0)
        elif nomeJogo == 3:
            # Camarões X Sérvia
            inicioJogo = datetime(2022,11,28,7,0)
        elif nomeJogo == 4:
            # Camarões X Brasil
            inicioJogo = datetime(2022,12,2,16,0)
        elif nomeJogo == 5:
            # Sérvia X Suíça
            inicioJogo = datetime(2022,12,2,16,0)
    
    elif nomeGrupo == 7:
        # Grupo H
        if nomeJogo == 0:
            # Portugal x Gana
            inicioJogo = datetime(2022,11,24,13,0)
        elif nomeJogo == 1:
            # Uruguai X Coreia do Sul
            inicioJogo = datetime(2022,11,24,10,0)
        elif nomeJogo == 2:
            # Portugal X Uruguai
            inicioJogo = datetime(2022,11,28,16,0)
        elif nomeJogo == 3:
            # Coreia do Sul X Gana
            inicioJogo = datetime(2022,11,28,10,0)
        elif nomeJogo == 4:
            # Coreia do Sul x Portugal
            inicioJogo = datetime(2022,12,2,12,0)
        elif nomeJogo == 5:
            # Gana X Uruguai
            inicioJogo = datetime(2022,12,2,12,0)

    return inicioJogo

def classificacaoInicial():
    
    '''
    
    Classificação antes do início da copa do mundo
    
    '''
    
    #numeroSelecoes = len(grupos()[0])-1 # Número de times por grupo
    selecoes = [] # array das seleções
    pontosSelecao = 0
    jogos         = 0
    vitorias      = 0
    empates       = 0
    derrotas      = 0
    golsPro       = 0
    golsContra    = 0
    saldoGols     = 0
    
    # looping para montar os grupos
    for grupo in range(len(grupos())):
        s = []
        #for selecao in range(1, numeroSelecoes+1, 1):
        for selecao in range(len(grupos()[0])):
            s.append([grupos()[grupo][selecao], pontosSelecao, jogos, vitorias, empates, derrotas, golsPro, golsContra, saldoGols])
        selecoes.append(s)
    
    return selecoes

def classificacaoFaseGrupos(selecoes, nomeGrupo, nomeJogo, golMandante, golVisitante):

    '''
    
    Classificação primeira fase:
    
    nomes dos grupos: grupo A = 0; grupo B = 1; grupo C = 2; grupo D = 3; grupo E = 4; grupo F = 5; grupo G = 6; grupo H = 7.
    
    nomes dos jogos: jogo 1 = 0; jogo 2 = 1; jogo 3 = 2; jogo 4 = 3; jogo 5 = 4; jogo 6 = 5.
    
    '''
    
    #-------------------------------------------------------------------------#        
    
    # rodada e jogo
    #nomeRodada = int(input('Qual rodada você quer apostar? '))
    if nomeJogo == 0 or nomeJogo == 1:
        nomeRodada = 1
    elif nomeJogo == 2 or nomeJogo == 3:
        nomeRodada = 2
    elif nomeJogo == 4 or nomeJogo == 5:
        nomeRodada = 3
    
    if nomeRodada == 1:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 1: Time i1 x Time i2
        # rodada 1: Time i3 x Time i4
        time1 = 0
        time2 = 1
        time3 = 2
        time4 = 3
        if nomeJogo == 0:
            
            # gols
            selecoes[nomeGrupo][time1].append(golMandante)
            selecoes[nomeGrupo][time2].append(golVisitante)

            # Número de jogos
            selecoes[nomeGrupo][time1][2] = selecoes[nomeGrupo][time1][2]+1 # número de jogos que o time i1 fez
            selecoes[nomeGrupo][time2][2] = selecoes[nomeGrupo][time2][2]+1 # número de jogos que o time i2 fez
            # Gols pró
            selecoes[nomeGrupo][time1][6] = selecoes[nomeGrupo][time1][6]+selecoes[nomeGrupo][time1][-1] # gols que o time i1 fez
            selecoes[nomeGrupo][time2][6] = selecoes[nomeGrupo][time2][6]+selecoes[nomeGrupo][time2][-1] # gols que o time i2 fez
            # Gols contra
            selecoes[nomeGrupo][time1][7] = selecoes[nomeGrupo][time1][7]+selecoes[nomeGrupo][time2][-1] # gols que o time i1 tomou
            selecoes[nomeGrupo][time2][7] = selecoes[nomeGrupo][time2][7]+selecoes[nomeGrupo][time1][-1] # gols que o time i2 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time1][8] = selecoes[nomeGrupo][time1][6]-selecoes[nomeGrupo][time1][7] # saldo de gols do time i1
            selecoes[nomeGrupo][time2][8] = selecoes[nomeGrupo][time2][6]-selecoes[nomeGrupo][time2][7] # saldo de gols do time i2

            # Jogo 1
            if selecoes[nomeGrupo][time1][-1]==selecoes[nomeGrupo][time2][-1]: # empate
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+1 # soma um ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+1 # soma um ponto
                selecoes[nomeGrupo][time1][4] = selecoes[nomeGrupo][time1][4]+1 # mais um empate
                selecoes[nomeGrupo][time2][4] = selecoes[nomeGrupo][time2][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time1][-1]>selecoes[nomeGrupo][time2][-1]: # vitoria mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+3 # soma três pontos
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time1][3] = selecoes[nomeGrupo][time1][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][5] = selecoes[nomeGrupo][time2][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time1][-1]<selecoes[nomeGrupo][time2][-1]: # derrota mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+3 # soma três pontos
                selecoes[nomeGrupo][time1][5] = selecoes[nomeGrupo][time1][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][3] = selecoes[nomeGrupo][time2][3]+1 # mais uma derrota

            print('')
            print('Fim de jogo!')
            print('Jogo 1')
            print('%s %d X %d %s'%(selecoes[nomeGrupo][time1][0], golMandante, golVisitante, selecoes[nomeGrupo][time2][0]))

        elif nomeJogo == 1:
            
            # gols
            selecoes[nomeGrupo][time3].append(golMandante)
            selecoes[nomeGrupo][time4].append(golVisitante)
            
            # Número de jogos
            selecoes[nomeGrupo][time3][2] = selecoes[nomeGrupo][time3][2]+1 # número de jogos que o time i3 fez
            selecoes[nomeGrupo][time4][2] = selecoes[nomeGrupo][time4][2]+1 # número de jogos que o time i4 fez
            # Gols pró
            selecoes[nomeGrupo][time3][6] = selecoes[nomeGrupo][time3][6]+selecoes[nomeGrupo][time3][-1] # gols que o time i3 fez
            selecoes[nomeGrupo][time4][6] = selecoes[nomeGrupo][time4][6]+selecoes[nomeGrupo][time4][-1] # gols que o time i4 fez
            # Gols contra
            selecoes[nomeGrupo][time3][7] = selecoes[nomeGrupo][time3][7]+selecoes[nomeGrupo][time4][-1] # gols que o time i3 tomou
            selecoes[nomeGrupo][time4][7] = selecoes[nomeGrupo][time4][7]+selecoes[nomeGrupo][time3][-1] # gols que o time i4 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time3][8] = selecoes[nomeGrupo][time3][6]-selecoes[nomeGrupo][time3][7] # saldo de gols do time i3
            selecoes[nomeGrupo][time4][8] = selecoes[nomeGrupo][time4][6]-selecoes[nomeGrupo][time4][7] # saldo de gols do time i4

            # Jogo 2
            if selecoes[nomeGrupo][time3][-1]==selecoes[nomeGrupo][time4][-1]: # empate
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+1 # soma um ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+1 # soma um ponto
                selecoes[nomeGrupo][time3][4] = selecoes[nomeGrupo][time3][4]+1 # mais um empate
                selecoes[nomeGrupo][time4][4] = selecoes[nomeGrupo][time4][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time3][-1]>selecoes[nomeGrupo][time4][-1]: # vitoria mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+3 # soma três pontos
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time3][3] = selecoes[nomeGrupo][time3][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][5] = selecoes[nomeGrupo][time4][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time3][-1]<selecoes[nomeGrupo][time4][-1]: # derrota mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+3 # soma três pontos
                selecoes[nomeGrupo][time3][5] = selecoes[nomeGrupo][time3][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][3] = selecoes[nomeGrupo][time4][3]+1 # mais uma derrota

            print('')
            print('Fim de jogo!')
            print('Jogo 2')
            print('%s %d X %d %s'%(selecoes[nomeGrupo][time3][0], golMandante, golVisitante, selecoes[nomeGrupo][time4][0]))
    
    elif nomeRodada == 2:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 2: Time i1 x Time i3
        # rodada 2: Time i2 x Time i4
        time1 = 0
        time2 = 2
        time3 = 3
        time4 = 1
        if nomeJogo == 2:
            
            # gols
            selecoes[nomeGrupo][time1].append(golMandante)
            selecoes[nomeGrupo][time2].append(golVisitante)

            # Número de jogos
            selecoes[nomeGrupo][time1][2] = selecoes[nomeGrupo][time1][2]+1 # número de jogos que o time i1 fez
            selecoes[nomeGrupo][time2][2] = selecoes[nomeGrupo][time2][2]+1 # número de jogos que o time i2 fez
            # Gols pró
            selecoes[nomeGrupo][time1][6] = selecoes[nomeGrupo][time1][6]+selecoes[nomeGrupo][time1][-1] # gols que o time i1 fez
            selecoes[nomeGrupo][time2][6] = selecoes[nomeGrupo][time2][6]+selecoes[nomeGrupo][time2][-1] # gols que o time i2 fez
            # Gols contra
            selecoes[nomeGrupo][time1][7] = selecoes[nomeGrupo][time1][7]+selecoes[nomeGrupo][time2][-1] # gols que o time i1 tomou
            selecoes[nomeGrupo][time2][7] = selecoes[nomeGrupo][time2][7]+selecoes[nomeGrupo][time1][-1] # gols que o time i2 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time1][8] = selecoes[nomeGrupo][time1][6]-selecoes[nomeGrupo][time1][7] # saldo de gols do time i1
            selecoes[nomeGrupo][time2][8] = selecoes[nomeGrupo][time2][6]-selecoes[nomeGrupo][time2][7] # saldo de gols do time i2

            # Jogo 1
            if selecoes[nomeGrupo][time1][-1]==selecoes[nomeGrupo][time2][-1]: # empate
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+1 # soma um ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+1 # soma um ponto
                selecoes[nomeGrupo][time1][4] = selecoes[nomeGrupo][time1][4]+1 # mais um empate
                selecoes[nomeGrupo][time2][4] = selecoes[nomeGrupo][time2][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time1][-1]>selecoes[nomeGrupo][time2][-1]: # vitoria mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+3 # soma três pontos
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time1][3] = selecoes[nomeGrupo][time1][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][5] = selecoes[nomeGrupo][time2][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time1][-1]<selecoes[nomeGrupo][time2][-1]: # derrota mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+3 # soma três pontos
                selecoes[nomeGrupo][time1][5] = selecoes[nomeGrupo][time1][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][3] = selecoes[nomeGrupo][time2][3]+1 # mais uma derrota

            print('')
            print('Fim de jogo!')
            print('Jogo 3')
            print('%s %d X %d %s'%(selecoes[nomeGrupo][time1][0], golMandante, golVisitante, selecoes[nomeGrupo][time2][0]))

        elif nomeJogo == 3:
            
            # gols
            selecoes[nomeGrupo][time3].append(golMandante)
            selecoes[nomeGrupo][time4].append(golVisitante)
            
            # Número de jogos
            selecoes[nomeGrupo][time3][2] = selecoes[nomeGrupo][time3][2]+1 # número de jogos que o time i3 fez
            selecoes[nomeGrupo][time4][2] = selecoes[nomeGrupo][time4][2]+1 # número de jogos que o time i4 fez
            # Gols pró
            selecoes[nomeGrupo][time3][6] = selecoes[nomeGrupo][time3][6]+selecoes[nomeGrupo][time3][-1] # gols que o time i3 fez
            selecoes[nomeGrupo][time4][6] = selecoes[nomeGrupo][time4][6]+selecoes[nomeGrupo][time4][-1] # gols que o time i4 fez
            # Gols contra
            selecoes[nomeGrupo][time3][7] = selecoes[nomeGrupo][time3][7]+selecoes[nomeGrupo][time4][-1] # gols que o time i3 tomou
            selecoes[nomeGrupo][time4][7] = selecoes[nomeGrupo][time4][7]+selecoes[nomeGrupo][time3][-1] # gols que o time i4 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time3][8] = selecoes[nomeGrupo][time3][6]-selecoes[nomeGrupo][time3][7] # saldo de gols do time i3
            selecoes[nomeGrupo][time4][8] = selecoes[nomeGrupo][time4][6]-selecoes[nomeGrupo][time4][7] # saldo de gols do time i4

            # Jogo 2
            if selecoes[nomeGrupo][time3][-1]==selecoes[nomeGrupo][time4][-1]: # empate
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+1 # soma um ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+1 # soma um ponto
                selecoes[nomeGrupo][time3][4] = selecoes[nomeGrupo][time3][4]+1 # mais um empate
                selecoes[nomeGrupo][time4][4] = selecoes[nomeGrupo][time4][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time3][-1]>selecoes[nomeGrupo][time4][-1]: # vitoria mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+3 # soma três pontos
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time3][3] = selecoes[nomeGrupo][time3][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][5] = selecoes[nomeGrupo][time4][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time3][-1]<selecoes[nomeGrupo][time4][-1]: # derrota mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+3 # soma três pontos
                selecoes[nomeGrupo][time3][5] = selecoes[nomeGrupo][time3][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][3] = selecoes[nomeGrupo][time4][3]+1 # mais uma derrota

            print('')
            print('Fim de jogo!')
            print('Jogo 4')
            print('%s %d X %d %s'%(selecoes[nomeGrupo][time3][0], golMandante, golVisitante, selecoes[nomeGrupo][time4][0]))

    elif nomeRodada == 3:
        # Time i1 = 0
        # Time i2 = 1
        # Time i3 = 2
        # Time i4 = 3
        # rodada 3: Time i4 x Time i1
        # rodada 3: Time i2 x Time i3
        time1 = 3
        time2 = 0
        time3 = 1
        time4 = 2
        if nomeJogo == 4:
            
            # gols
            selecoes[nomeGrupo][time1].append(golMandante)
            selecoes[nomeGrupo][time2].append(golVisitante)

            # Número de jogos
            selecoes[nomeGrupo][time1][2] = selecoes[nomeGrupo][time1][2]+1 # número de jogos que o time i1 fez
            selecoes[nomeGrupo][time2][2] = selecoes[nomeGrupo][time2][2]+1 # número de jogos que o time i2 fez
            # Gols pró
            selecoes[nomeGrupo][time1][6] = selecoes[nomeGrupo][time1][6]+selecoes[nomeGrupo][time1][-1] # gols que o time i1 fez
            selecoes[nomeGrupo][time2][6] = selecoes[nomeGrupo][time2][6]+selecoes[nomeGrupo][time2][-1] # gols que o time i2 fez
            # Gols contra
            selecoes[nomeGrupo][time1][7] = selecoes[nomeGrupo][time1][7]+selecoes[nomeGrupo][time2][-1] # gols que o time i1 tomou
            selecoes[nomeGrupo][time2][7] = selecoes[nomeGrupo][time2][7]+selecoes[nomeGrupo][time1][-1] # gols que o time i2 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time1][8] = selecoes[nomeGrupo][time1][6]-selecoes[nomeGrupo][time1][7] # saldo de gols do time i1
            selecoes[nomeGrupo][time2][8] = selecoes[nomeGrupo][time2][6]-selecoes[nomeGrupo][time2][7] # saldo de gols do time i2

            # Jogo 1
            if selecoes[nomeGrupo][time1][-1]==selecoes[nomeGrupo][time2][-1]: # empate
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+1 # soma um ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+1 # soma um ponto
                selecoes[nomeGrupo][time1][4] = selecoes[nomeGrupo][time1][4]+1 # mais um empate
                selecoes[nomeGrupo][time2][4] = selecoes[nomeGrupo][time2][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time1][-1]>selecoes[nomeGrupo][time2][-1]: # vitoria mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+3 # soma três pontos
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time1][3] = selecoes[nomeGrupo][time1][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][5] = selecoes[nomeGrupo][time2][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time1][-1]<selecoes[nomeGrupo][time2][-1]: # derrota mandante
                selecoes[nomeGrupo][time1][1] = selecoes[nomeGrupo][time1][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time2][1] = selecoes[nomeGrupo][time2][1]+3 # soma três pontos
                selecoes[nomeGrupo][time1][5] = selecoes[nomeGrupo][time1][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time2][3] = selecoes[nomeGrupo][time2][3]+1 # mais uma derrota

            print('')
            print('Fim de jogo!')
            print('Jogo 5')
            print('%s %d X %d %s'%(selecoes[nomeGrupo][time1][0], golMandante, golVisitante, selecoes[nomeGrupo][time2][0]))
            
        elif nomeJogo == 5:
            
            # gols
            selecoes[nomeGrupo][time3].append(golMandante)
            selecoes[nomeGrupo][time4].append(golVisitante)
            
            # Número de jogos
            selecoes[nomeGrupo][time3][2] = selecoes[nomeGrupo][time3][2]+1 # número de jogos que o time i3 fez
            selecoes[nomeGrupo][time4][2] = selecoes[nomeGrupo][time4][2]+1 # número de jogos que o time i4 fez
            # Gols pró
            selecoes[nomeGrupo][time3][6] = selecoes[nomeGrupo][time3][6]+selecoes[nomeGrupo][time3][-1] # gols que o time i3 fez
            selecoes[nomeGrupo][time4][6] = selecoes[nomeGrupo][time4][6]+selecoes[nomeGrupo][time4][-1] # gols que o time i4 fez
            # Gols contra
            selecoes[nomeGrupo][time3][7] = selecoes[nomeGrupo][time3][7]+selecoes[nomeGrupo][time4][-1] # gols que o time i3 tomou
            selecoes[nomeGrupo][time4][7] = selecoes[nomeGrupo][time4][7]+selecoes[nomeGrupo][time3][-1] # gols que o time i4 tomou
            # Saldo de gols
            selecoes[nomeGrupo][time3][8] = selecoes[nomeGrupo][time3][6]-selecoes[nomeGrupo][time3][7] # saldo de gols do time i3
            selecoes[nomeGrupo][time4][8] = selecoes[nomeGrupo][time4][6]-selecoes[nomeGrupo][time4][7] # saldo de gols do time i4

            # Jogo 2
            if selecoes[nomeGrupo][time3][-1]==selecoes[nomeGrupo][time4][-1]: # empate
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+1 # soma um ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+1 # soma um ponto
                selecoes[nomeGrupo][time3][4] = selecoes[nomeGrupo][time3][4]+1 # mais um empate
                selecoes[nomeGrupo][time4][4] = selecoes[nomeGrupo][time4][4]+1 # mais um empate
            elif selecoes[nomeGrupo][time3][-1]>selecoes[nomeGrupo][time4][-1]: # vitoria mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+3 # soma três pontos
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time3][3] = selecoes[nomeGrupo][time3][3]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][5] = selecoes[nomeGrupo][time4][5]+1 # mais uma derrota
            elif selecoes[nomeGrupo][time3][-1]<selecoes[nomeGrupo][time4][-1]: # derrota mandante
                selecoes[nomeGrupo][time3][1] = selecoes[nomeGrupo][time3][1]+0 # nenhum ponto
                selecoes[nomeGrupo][time4][1] = selecoes[nomeGrupo][time4][1]+3 # soma três pontos
                selecoes[nomeGrupo][time3][5] = selecoes[nomeGrupo][time3][5]+1 # mais uma vitória
                selecoes[nomeGrupo][time4][3] = selecoes[nomeGrupo][time4][3]+1 # mais uma derrota

            print('')
            print('Fim de jogo!')
            print('Jogo 6')
            print('%s %d X %d %s'%(selecoes[nomeGrupo][time3][0], golMandante, golVisitante, selecoes[nomeGrupo][time4][0]))

    return selecoes

def resultadoJogo(golMandante, golVisitante):

    '''
    
    Resultado jogo
        
    '''
    
    #-------------------------------------------------------------------------#        
    
    vitoria = False
    empate  = False
    derrota = False

    if golMandante != '':    
        if golMandante == golVisitante: # empate
            empate = True
        elif golMandante > golVisitante: # vitoria mandante
            vitoria = True
        elif golMandante < golVisitante: # derrota mandante
            derrota = True

    return vitoria, empate, derrota

def resultadoApostadorFaseGrupos(usuario,pontuacao,golMandanteApostador,golVisitanteApostador,golMandanteJogo,golVisitanteJogo):
    
    '''
    
    Função que contabiliza os pontos do usuario para um jogo na fase de grupos
    
    '''
    
    vitoria, empate, derrota = resultadoJogo(golMandanteJogo,golVisitanteJogo)
    vitoriaApostador, empateApostador, derrotaApostador = resultadoJogo(golMandanteApostador,golVisitanteApostador)
    if vitoria:
        if vitoriaApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 10
                pontuacao += 10
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 7
                pontuacao += 7
        elif derrotaApostador:
            # erro
            usuario[5] = int(usuario[5]) + 1
            usuario[2] = int(usuario[2]) - 7
            pontuacao += -7
        elif empateApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 10
            pontuacao += -10
            
    #-------------------------------------------------------------------------#
            
    elif empate:
        if vitoriaApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        elif derrotaApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        elif empateApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 10
                pontuacao += 10
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 7
                pontuacao += 7
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 10
            pontuacao += -10
    
    #-------------------------------------------------------------------------#
    
    elif derrota:
        if vitoriaApostador:
            # erro
            usuario[5] = int(usuario[5]) + 1
            usuario[2] = int(usuario[2]) - 7
            pontuacao += -7
        elif derrotaApostador:
            if golMandanteJogo == golMandanteApostador and golVisitanteJogo == golVisitanteApostador:
                # cravada
                usuario[3] = int(usuario[3]) + 1
                usuario[2] = int(usuario[2]) + 10
                pontuacao += 10
            else:
                # acerto
                usuario[4] = int(usuario[4]) + 1
                usuario[2] = int(usuario[2]) + 7
                pontuacao += 7
        elif empateApostador:
            # nada
            usuario[6] = int(usuario[6]) + 1
            usuario[2] = int(usuario[2]) + 0
            pontuacao += 0
        if golMandanteApostador == '':
            # não apostou
            usuario[7] = int(usuario[7]) + 1
            usuario[2] = int(usuario[2]) - 10
            pontuacao += -10
            
    return usuario, pontuacao

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#

# DB Management
dados = sqlite3.connect('dados10.db')
d = dados.cursor()

def cria_tabela_usuarios():
    d.execute("CREATE TABLE IF NOT EXISTS tabela(login TEXT, senha TEXT)")

def adicionar_dados_usuarios(login, senha):
    d.execute("INSERT INTO tabela(login, senha) VALUES(?, ?)", (login, senha))
    dados.commit()

def login_usuario(username,password):
    d.execute('SELECT * FROM tabela WHERE login = ? AND senha = ?',(username,password))
    dado = d.fetchall()
    return dado

def todos_os_usuarios():
    d.execute('SELECT * FROM tabela')
    dado = d.fetchall()
    return dado

#-----------------------------------------------------------------------------#

def usuarioMestre():
    cria_tabela_usuarios()
    usuariosLista = []
    # definindo a lista de usuarios e o usuario mestre
    if len(todos_os_usuarios()) == 0:
        cadastro = cadastroApostador('usuarioMestre','appBolao')
        np.save('usuarioMestre',cadastro)
        usuariosLista.append(cadastro)
        adicionar_dados_usuarios('usuarioMestre','appBolao')
        st.success('O usuário mestre foi criado.')
    else:
        for i in range(len(todos_os_usuarios())):
            usuario = np.load(str(np.array(todos_os_usuarios())[:,0][i])+'.npy')
            usuariosLista.append(usuario)

    return usuariosLista

#-----------------------------------------------------------------------------#

# criando o usuario mestre
usuariosLista = usuarioMestre()

def main():
    
    ''' Simple Login App '''
    menu = ['Home','Cadastro','Login']
    choice = st.sidebar.selectbox('Menu',menu)

    #-----------------------------------------------------------------------------#

    if choice == 'Home':
        st.subheader('Acesso do administrador')
        username = st.text_input('Nome de usuário')
        password = st.text_input('Senha', type = 'password')

        if username == 'usuarioMestre' and password == 'appBolao':
            #task = st.sidebar.selectbox('Task',['Conexão','Testes','Fase de grupos','Usuários'])
            task = st.sidebar.selectbox('Task',['Conexão','Testes','Fase de grupos','Fase Eliminatórias','Usuários'])

            if task == 'Conexão':
                st.subheader('Conectado')
                
            elif task == 'Testes':
                st.subheader('Testes')

                usuarioMestre = np.load('usuarioMestre.npy')
                opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
                opcoes = [0,1,2,3,4]
                for contadorUsuario in range(1, len(usuariosLista), 1):
                    st.subheader(usuariosLista[contadorUsuario][0])
                    with st.form(key = 'includebolao'+str(contadorUsuario)):
                        apostaBolao = st.selectbox('Selecione a posição que ficará no bolão', options = opcoesBolao, index = 3)
                        botaoBolao = st.form_submit_button(label = 'Apostar')
                    if botaoBolao:# and inicioCopa:
                        #usuario[8] = opcoes[opcoesBolao.index(apostaBolao)]
                        usuariosLista[contadorUsuario][8] = opcoes[opcoesBolao.index(apostaBolao)]
                        np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                    if usuariosLista[contadorUsuario][8] != '':
                        st.subheader('Aposta registrada!')
                        st.write(f'Você vai ser o {opcoesBolao[int(usuariosLista[contadorUsuario][8])]} !')

                        #-----------------------------------------------------------------------------#

                        st.title('Apostas iniciais - 13:00 20/11/2022')
                        with st.form(key = 'include_campeao'+str(contadorUsuario)):
                            apostaCampeao = st.selectbox('Quem será o campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            apostaViceCampeao = st.selectbox('Quem será o vice campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            apostaTerceiroColocado = st.selectbox('Quem será o terceiro colocado da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            botaoApostaCampeao = st.form_submit_button(label = 'Apostar')
                        if botaoApostaCampeao:# and inicioCopa:
                            apostaPodio(usuariosLista[contadorUsuario],apostaCampeao,apostaViceCampeao,apostaTerceiroColocado)
                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                        if usuariosLista[contadorUsuario][9] != '':
                            st.subheader('Apostas registradas!')
                            st.write(f'Aposta campeão: {listaSelecoes()[int(usuariosLista[contadorUsuario][9])]}')
                            st.write(f'Aposta vice campeão: {listaSelecoes()[int(usuariosLista[contadorUsuario][10])]}')
                            st.write(f'Aposta terceiro colocado: {listaSelecoes()[int(usuariosLista[contadorUsuario][11])]}')

                        #-----------------------------------------------------------------------------#

                        for nomeGrupo in range(len(grupos()[:,0])):
                            st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
                            with st.form(key = 'include_aposta_grupo_'+str(grupos()[nomeGrupo][-1])+str(contadorUsuario)):
                                apostaPrimeiro = st.selectbox('Quem será o primeiro colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
                                apostaSegundo  = st.selectbox('Quem será o segundo colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
                                botaoApostaGrupos = st.form_submit_button(label = 'Apostar no grupo '+str(grupos()[nomeGrupo][-1]))
                            if botaoApostaGrupos:# and inicioCopa:
                                apostaGrupos(usuariosLista[contadorUsuario],nomeGrupo,apostaPrimeiro,apostaSegundo)
                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                            if usuariosLista[contadorUsuario][2*nomeGrupo+12] != '':
                                st.subheader('Apostas registradas!')
                                st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuariosLista[contadorUsuario][2*nomeGrupo+12])]}')
                                st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuariosLista[contadorUsuario][2*nomeGrupo+13])]}')

                        #-----------------------------------------------------------------------------#

                    classificacao = classificacaoInicial()
                    st.subheader(usuariosLista[contadorUsuario][0])
                    for nomeGrupo in range(len(grupos()[:,0])):
                        st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')

                        # Datas e horários dos jogos
                        for nomeJogo in range(6):
                            with st.form(key = 'include_aposta_jogo_'+str(nomeJogo+1)+'do_grupo_'+str(grupos()[nomeGrupo][-1])+str(contadorUsuario)):
                                st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - {dataHorarioJogoGrupo(nomeGrupo,nomeJogo)}')

                                # rodada e jogo
                                if nomeJogo == 0 or nomeJogo == 1:
                                    nomeRodada = 1
                                elif nomeJogo == 2 or nomeJogo == 3:
                                    nomeRodada = 2
                                elif nomeJogo == 4 or nomeJogo == 5:
                                    nomeRodada = 3

                                if nomeRodada == 1:
                                    # Time i1 = 0
                                    # Time i2 = 1
                                    # Time i3 = 2
                                    # Time i4 = 3
                                    # rodada 1: Time i1 x Time i2
                                    # rodada 1: Time i3 x Time i4
                                    time1 = 0
                                    time2 = 1
                                    time3 = 2
                                    time4 = 3
                                    if nomeJogo == 0:
                                        #print('')
                                        #print('Jogo 1')
                                        #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                        aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        botao_jogo_1 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                        #if botao_jogo_1:
                                        if botao_jogo_1:# and inicioJogo:
                                            fazerApostaPrimeiraFase(usuariosLista[contadorUsuario],nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                                        if usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Aposta registrada!')
                                            st.write(f'{grupos()[nomeGrupo][time1]} {usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo]} X {usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Fim de jogo!')
                                            st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                    elif nomeJogo == 1:
                                        #print('')
                                        #print('Jogo 2')
                                        #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                        aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        botao_jogo_2 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                        #if botao_jogo_2:
                                        if botao_jogo_2:# and inicioJogo:
                                            fazerApostaPrimeiraFase(usuariosLista[contadorUsuario],nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                                        if usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Aposta registrada!')
                                            #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                            st.write(f'{grupos()[nomeGrupo][time3]} {usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo]} X {usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Fim de jogo!')
                                            st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                elif nomeRodada == 2:
                                    # Time i1 = 0
                                    # Time i2 = 1
                                    # Time i3 = 2
                                    # Time i4 = 3
                                    # rodada 2: Time i1 x Time i3
                                    # rodada 2: Time i2 x Time i4
                                    # rodada 2: Time i4 x Time i2 ALTERADA
                                    time1 = 0
                                    time2 = 2
                                    time3 = 3
                                    time4 = 1
                                    if nomeJogo == 2:
                                        #print('')
                                        #print('Jogo 3')
                                        #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                        aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        botao_jogo_3 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                        #if botao_jogo_3:
                                        if botao_jogo_3:# and inicioJogo:
                                            fazerApostaPrimeiraFase(usuariosLista[contadorUsuario],nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                                        if usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Aposta registrada!')
                                            #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                            st.write(f'{grupos()[nomeGrupo][time1]} {usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo]} X {usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Fim de jogo!')
                                            st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                    elif nomeJogo == 3:
                                        #print('')
                                        #print('Jogo 4')
                                        #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                        aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        botao_jogo_4 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                        #if botao_jogo_4:
                                        if botao_jogo_4:# and inicioJogo:
                                            fazerApostaPrimeiraFase(usuariosLista[contadorUsuario],nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                                        if usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Aposta registrada!')
                                            #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                            st.write(f'{grupos()[nomeGrupo][time3]} {usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo]} X {usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Fim de jogo!')
                                            st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                elif nomeRodada == 3:
                                    # Time i1 = 0
                                    # Time i2 = 1
                                    # Time i3 = 2
                                    # Time i4 = 3
                                    # rodada 3: Time i4 x Time i1
                                    # rodada 3: Time i2 x Time i3
                                    time1 = 3
                                    time2 = 0
                                    time3 = 1
                                    time4 = 2
                                    if nomeJogo == 4:
                                        #print('')
                                        #print('Jogo 5')
                                        #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                        aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        botao_jogo_5 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                        #if botao_jogo_5:
                                        if botao_jogo_5:# and inicioJogo:
                                            fazerApostaPrimeiraFase(usuariosLista[contadorUsuario],nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                                        if usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Aposta registrada!')
                                            #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                            st.write(f'{grupos()[nomeGrupo][time1]} {usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo]} X {usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Fim de jogo!')
                                            st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                    elif nomeJogo == 5:
                                        #print('')
                                        #print('Jogo 6')
                                        #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                        aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                        botao_jogo_6 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                        inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                        #if botao_jogo_6:
                                        if botao_jogo_6:# and inicioJogo:
                                            fazerApostaPrimeiraFase(usuariosLista[contadorUsuario],nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                            np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])
                                        if usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Aposta registrada!')
                                            #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                            st.write(f'{grupos()[nomeGrupo][time3]} {usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo]} X {usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                        if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                            st.subheader('Fim de jogo!')
                                            st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))


            elif task == 'Fase de grupos':
                st.title('Fase de Grupos')
                classificacao = classificacaoInicial()
                indiceUsuario = np.where(np.array(todos_os_usuarios())[:,0] == username)[0][0]
                usuario = usuariosLista[indiceUsuario]
                for contadorUsuario in range(1, len(usuariosLista), 1):
                    usuariosLista[contadorUsuario][2] = 0
                    usuariosLista[contadorUsuario][3] = 0
                    usuariosLista[contadorUsuario][4] = 0
                    usuariosLista[contadorUsuario][5] = 0
                    usuariosLista[contadorUsuario][6] = 0
                    usuariosLista[contadorUsuario][7] = 0
                    np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                classificadosGrupos = np.array(['Holanda','Senegal',
                                                'Inglaterra','Estados Unidos',
                                                'Argentina','Polônia',
                                                'França','Austrália',
                                                'Japão','Espanha',
                                                'Marrocos','Croácia',
                                                'Brasil','Suíça',
                                                'Portugal','Coreia do Sul'])
                
                for contadorUsuario in range(1, len(usuariosLista), 1):
                    pontuacaoGrupos = 0
                    for apostaGrupo in range(12, 28, 2):
                        if np.array(usuariosLista)[contadorUsuario][apostaGrupo] != '':
                            if listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                                pontuacaoGrupos += 60
                            elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                                pontuacaoGrupos += 30
                            elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                                pontuacaoGrupos += 42
                            elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo-12]:
                                pontuacaoGrupos += 21
                            elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                                pontuacaoGrupos += 30
                            elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                                pontuacaoGrupos += 21
                            elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                                pontuacaoGrupos += 0

                    usuariosLista[contadorUsuario][2] = int(usuariosLista[contadorUsuario][2]) + pontuacaoGrupos
                    np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])


                for nomeGrupo in range(len(grupos()[:,0])):
                    st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
                    
                    # Datas e horários dos jogos
                    for nomeJogo in range(6):
                        with st.form(key = 'include_aposta_jogo_'+str(nomeJogo+1)+'do_grupo_'+str(grupos()[nomeGrupo][-1])):
                            st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - {dataHorarioJogoGrupo(nomeGrupo,nomeJogo)}')

                            # rodada e jogo
                            if nomeJogo == 0 or nomeJogo == 1:
                                nomeRodada = 1
                            elif nomeJogo == 2 or nomeJogo == 3:
                                nomeRodada = 2
                            elif nomeJogo == 4 or nomeJogo == 5:
                                nomeRodada = 3

                            if nomeRodada == 1:
                                # Time i1 = 0
                                # Time i2 = 1
                                # Time i3 = 2
                                # Time i4 = 3
                                # rodada 1: Time i1 x Time i2
                                # rodada 1: Time i3 x Time i4
                                time1 = 0
                                time2 = 1
                                time3 = 2
                                time4 = 3
                                if nomeJogo == 0:
                                    #print('')
                                    #print('Jogo 1')
                                    #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                    placar_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    placar_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    botao_jogo_1 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                                    inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                    if botao_jogo_1 and not inicioJogo:
                                        fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_1,placar_selecao_2)
                                        np.save(str(username),usuario)
                                        st.subheader(f'Registrou.')
                                    if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                        st.subheader('Fim de jogo!')
                                        st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                        classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                                        if not inicioJogo:
                                            for contadorUsuario in range(1, len(usuariosLista), 1):
                                                pontuacaoJogo = 0
                                                usuariosLista[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(usuariosLista[contadorUsuario],pontuacaoJogo,usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                                st.subheader(f'A sua pontuação do {usuariosLista[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                                elif nomeJogo == 1:
                                    #print('')
                                    #print('Jogo 2')
                                    #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                    placar_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    placar_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    botao_jogo_2 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                                    inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                    if botao_jogo_2 and not inicioJogo:
                                        fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_3,placar_selecao_4)
                                        np.save(str(username),usuario)
                                        st.subheader(f'Registrou.')
                                    if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                        st.subheader('Fim de jogo!')
                                        st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                        classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                                        if not inicioJogo:
                                            for contadorUsuario in range(1, len(usuariosLista), 1):
                                                pontuacaoJogo = 0
                                                usuariosLista[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(usuariosLista[contadorUsuario],pontuacaoJogo,usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                                st.subheader(f'A sua pontuação do {usuariosLista[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                            elif nomeRodada == 2:
                                # Time i1 = 0
                                # Time i2 = 1
                                # Time i3 = 2
                                # Time i4 = 3
                                # rodada 2: Time i1 x Time i3
                                # rodada 2: Time i2 x Time i4
                                # rodada 2: Time i4 x Time i2 ALTERADA
                                time1 = 0
                                time2 = 2
                                time3 = 3
                                time4 = 1
                                if nomeJogo == 2:
                                    #print('')
                                    #print('Jogo 3')
                                    #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                    placar_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    placar_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    botao_jogo_3 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                                    inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                    if botao_jogo_3 and not inicioJogo:
                                        fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_1,placar_selecao_2)
                                        np.save(str(username),usuario)
                                        st.subheader(f'Registrou.')
                                    if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                        st.subheader('Fim de jogo!')
                                        st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                        classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                                        if not inicioJogo:
                                            for contadorUsuario in range(1, len(usuariosLista), 1):
                                                pontuacaoJogo = 0
                                                usuariosLista[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(usuariosLista[contadorUsuario],pontuacaoJogo,usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                                st.subheader(f'A sua pontuação do {usuariosLista[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                                elif nomeJogo == 3:
                                    #print('')
                                    #print('Jogo 4')
                                    #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                    placar_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    placar_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    botao_jogo_4 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                                    inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                    if botao_jogo_4 and not inicioJogo:
                                        fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_3,placar_selecao_4)
                                        np.save(str(username),usuario)
                                        st.subheader(f'Registrou.')
                                    if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                        st.subheader('Fim de jogo!')
                                        st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                        classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                                        if not inicioJogo:
                                            for contadorUsuario in range(1, len(usuariosLista), 1):
                                                pontuacaoJogo = 0
                                                usuariosLista[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(usuariosLista[contadorUsuario],pontuacaoJogo,usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                                st.subheader(f'A sua pontuação do {usuariosLista[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                            elif nomeRodada == 3:
                                # Time i1 = 0
                                # Time i2 = 1
                                # Time i3 = 2
                                # Time i4 = 3
                                # rodada 3: Time i4 x Time i1
                                # rodada 3: Time i2 x Time i3
                                time1 = 3
                                time2 = 0
                                time3 = 1
                                time4 = 2
                                if nomeJogo == 4:
                                    #print('')
                                    #print('Jogo 5')
                                    #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                    placar_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    placar_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    botao_jogo_5 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                                    inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                    if botao_jogo_5 and not inicioJogo:
                                        fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_1,placar_selecao_2)
                                        np.save(str(username),usuario)
                                        st.subheader(f'Registrou.')
                                    if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                        st.subheader('Fim de jogo!')
                                        st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                        classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                                        if not inicioJogo:
                                            for contadorUsuario in range(1, len(usuariosLista), 1):
                                                pontuacaoJogo = 0
                                                usuariosLista[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(usuariosLista[contadorUsuario],pontuacaoJogo,usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                                st.subheader(f'A sua pontuação do {usuariosLista[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                                elif nomeJogo == 5:
                                    #print('')
                                    #print('Jogo 6')
                                    #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                    placar_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    placar_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                    botao_jogo_6 = st.form_submit_button(label = f'Postar placar do jogo {nomeJogo+1}')
                                    inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                    if botao_jogo_6 and not inicioJogo:
                                        fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,placar_selecao_3,placar_selecao_4)
                                        np.save(str(username),usuario)
                                        st.subheader(f'Registrou.')
                                    if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                        st.subheader('Fim de jogo!')
                                        st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                        classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuario[28+2*6*nomeGrupo+2*nomeJogo]),int(usuario[29+2*6*nomeGrupo+2*nomeJogo]))
                                        if not inicioJogo:
                                            for contadorUsuario in range(1, len(usuariosLista), 1):
                                                pontuacaoJogo = 0
                                                usuariosLista[contadorUsuario], pontuacao = resultadoApostadorFaseGrupos(usuariosLista[contadorUsuario],pontuacaoJogo,usuariosLista[contadorUsuario][28+2*6*nomeGrupo+2*nomeJogo],usuariosLista[contadorUsuario][29+2*6*nomeGrupo+2*nomeJogo],usuario[28+2*6*nomeGrupo+2*nomeJogo],usuario[29+2*6*nomeGrupo+2*nomeJogo])
                                                st.subheader(f'A sua pontuação do {usuariosLista[contadorUsuario][0]} foi: {pontuacao} ponto(s)')
                                                np.save(str(usuariosLista[contadorUsuario][0]),usuariosLista[contadorUsuario])

                rotuloColuna = ['P',  # pontuação
                                'J',  # jogos
                                'V',  # vitórias
                                'E',  # empates
                                'D',  # derrotas
                                'GP', # gols pró
                                'GC', # gols contra
                                'SG'] # saldo de gols
                for contadorClassificacao in range(len(classificacao)):
                    classificacao[contadorClassificacao].pop(-1)
                    df = pd.DataFrame(np.array([[classificacao[contadorClassificacao][0][1],classificacao[contadorClassificacao][0][2],classificacao[contadorClassificacao][0][3],classificacao[contadorClassificacao][0][4],classificacao[contadorClassificacao][0][5],classificacao[contadorClassificacao][0][6],classificacao[contadorClassificacao][0][7],classificacao[contadorClassificacao][0][8]],
                                                [classificacao[contadorClassificacao][1][1],classificacao[contadorClassificacao][1][2],classificacao[contadorClassificacao][1][3],classificacao[contadorClassificacao][1][4],classificacao[contadorClassificacao][1][5],classificacao[contadorClassificacao][1][6],classificacao[contadorClassificacao][1][7],classificacao[contadorClassificacao][1][8]],
                                                [classificacao[contadorClassificacao][2][1],classificacao[contadorClassificacao][2][2],classificacao[contadorClassificacao][2][3],classificacao[contadorClassificacao][2][4],classificacao[contadorClassificacao][2][5],classificacao[contadorClassificacao][2][6],classificacao[contadorClassificacao][2][7],classificacao[contadorClassificacao][2][8]],
                                                [classificacao[contadorClassificacao][3][1],classificacao[contadorClassificacao][3][2],classificacao[contadorClassificacao][3][3],classificacao[contadorClassificacao][3][4],classificacao[contadorClassificacao][3][5],classificacao[contadorClassificacao][3][6],classificacao[contadorClassificacao][3][7],classificacao[contadorClassificacao][3][8]]
                                                ]),
                                columns = tuple(rotuloColuna)
                    )
                    df.index = [classificacao[contadorClassificacao][0][0],classificacao[contadorClassificacao][1][0],classificacao[contadorClassificacao][2][0],classificacao[contadorClassificacao][3][0]]
                    st.table(df)
                
                st.subheader(usuariosLista)
                classificacaoBolao = []
                dadosClassificacao = []
                for contadorUsuario in range(1, len(usuariosLista), 1):
                    classificacaoBolao.append([usuariosLista[contadorUsuario][0],usuariosLista[contadorUsuario][2],usuariosLista[contadorUsuario][3],usuariosLista[contadorUsuario][4],usuariosLista[contadorUsuario][5],usuariosLista[contadorUsuario][6],usuariosLista[contadorUsuario][7]])
                    dadosClassificacao.append(np.delete(np.array(classificacaoBolao[contadorUsuario-1]),0,0))
                df0 = pd.DataFrame(np.array(dadosClassificacao),
                                   columns = ('Pontos','Cravadas','Acertos','Erros','Nadas','Não apostas'))
                df0.index = np.delete(np.array(usuariosLista)[:,0],0)
                st.table(df0)
                
            elif task == 'Fase Eliminatórias':
                st.title('Fase Eliminatórias')

            elif task == 'Usuários':
                st.subheader('Usuários')
                
                ##for contadorUsuarios in range(len(usuariosLista)):
                    ##usuariosLista[contadorUsuarios] = np.append(usuariosLista[contadorUsuarios], 48*[''])
                    ##st.subheader(usuariosLista[contadorUsuarios][0])
                    ##st.subheader(len(usuariosLista[contadorUsuarios]))
                    ##np.save(str(usuariosLista[contadorUsuarios][0]),usuariosLista[contadorUsuarios])
                
                clean_db = pd.DataFrame(todos_os_usuarios())
                st.dataframe(clean_db)
                st.subheader(usuariosLista)
        else:
            st.subheader('Você não tem acesso')

    #-----------------------------------------------------------------------------#

    elif choice == 'Cadastro':
        st.subheader('Criar nova conta')
        new_user = st.text_input('Nome de usuário')
        new_password = st.text_input('Senha', type = 'password')

        if st.button('Cadastrar'):
            cria_tabela_usuarios()
            #create_usertable()
            #add_userdata(new_user,new_password)
            #st.success('You have sucessfully created an valid Account')
            #st.info('Go to login Menu to login')
            if new_user == '' or new_password == '':
                st.error('Preencha todos os campos para realizar o cadastro.')
            else:
                for usuarios in range(len(todos_os_usuarios())):
                    if new_user == np.array(todos_os_usuarios())[:,0][usuarios]:
                        st.error('Esse usuário já existe.')
                        st.warning('Tente outro nome de usuário')
                        break
                    elif usuarios == len(todos_os_usuarios())-1:
                        cadastro = cadastroApostador(new_user,new_password)
                        np.save(str(new_user),cadastro)
                        usuariosLista.append(cadastro)
                        adicionar_dados_usuarios(new_user,new_password)
                        
                        st.success('Você criou uma conta válida com sucesso')
                        st.info('Vá ao Menu para fazer login')

    #-----------------------------------------------------------------------------#

    elif choice == 'Login':
        username = st.sidebar.text_input('Nome de usuário')
        password = st.sidebar.text_input('Senha', type = 'password')

        if st.sidebar.checkbox('Login'):
            # pegar o índice do usuario
            indiceUsuario = np.where(np.array(todos_os_usuarios())[:,0] == username)[0][0]
            usuario = usuariosLista[indiceUsuario]
            usuarioMestre = np.load('usuarioMestre.npy')

            result = login_usuario(username,password)
            if result:
                st.sidebar.success('Você está logado como {}'.format(username))
                task = st.sidebar.selectbox(label = 'Selecionar o campeonato', options = ['Copa do Mundo 2022','Outros'], index = 1)
                
                if task == 'Copa do Mundo 2022':
                    st.title('Bolão da Copa do Mundo 2022')
                    task1 = st.sidebar.selectbox(label = 'Opções', options = ['Apostas iniciais','Apostas fase de grupos','Apostas nas fases eliminatórias','Resumo das apostas','Links externos'], index = 0)
                    
                    if task1 == 'Apostas iniciais':                        
                        inicioCopa = horarioJogo(2022,11,22,10,0)
                        opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
                        opcoes = [0,1,2,3,4]

                        with st.form(key = 'include_bolao'):
                            apostaBolao = st.selectbox('Selecione a posição que ficará no bolão', options = opcoesBolao, index = 3)
                            botaoBolao = st.form_submit_button(label = 'Apostar')
                        if botaoBolao and inicioCopa:
                            usuario[8] = opcoes[opcoesBolao.index(apostaBolao)]
                            np.save(str(username),usuario)
                        if usuario[8] != '':
                            st.subheader('Aposta registrada!')
                            st.write(f'Você vai ser o {opcoesBolao[int(usuario[8])]} !')
                        
                        #-----------------------------------------------------------------------------#

                        st.title('Apostas iniciais - 13:00 20/11/2022')
                        with st.form(key = 'include_campeao'):
                            apostaCampeao = st.selectbox('Quem será o campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            apostaViceCampeao = st.selectbox('Quem será o vice campeão da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            apostaTerceiroColocado = st.selectbox('Quem será o terceiro colocado da Copa do Mundo 2022?', options = listaSelecoes(), index = 0)
                            botaoApostaCampeao = st.form_submit_button(label = 'Apostar')
                        #if botaoApostaCampeao and inicioCopa:
                        if botaoApostaCampeao and not inicioCopa:
                            apostaPodio(usuario,apostaCampeao,apostaViceCampeao,apostaTerceiroColocado)
                            np.save(str(username),usuario)
                        if usuario[9] != '':
                            st.subheader('Apostas registradas!')
                            st.write(f'Aposta campeão: {listaSelecoes()[int(usuario[9])]}')
                            st.write(f'Aposta vice campeão: {listaSelecoes()[int(usuario[10])]}')
                            st.write(f'Aposta terceiro colocado: {listaSelecoes()[int(usuario[11])]}')
 
                        #-----------------------------------------------------------------------------#

                        for nomeGrupo in range(len(grupos()[:,0])):
                            st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
                            with st.form(key = 'include_aposta_grupo_'+str(grupos()[nomeGrupo][-1])):
                                apostaPrimeiro = st.selectbox('Quem será o primeiro colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
                                apostaSegundo  = st.selectbox('Quem será o segundo colocado?', options = np.delete(grupos()[nomeGrupo],-1), index = 0)
                                botaoApostaGrupos = st.form_submit_button(label = 'Apostar no grupo '+str(grupos()[nomeGrupo][-1]))
                            if botaoApostaGrupos and inicioCopa:
                                apostaGrupos(usuario,nomeGrupo,apostaPrimeiro,apostaSegundo)
                                np.save(str(username),usuario)
                            if usuario[2*nomeGrupo+12] != '':
                                st.subheader('Apostas registradas!')
                                st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+12])]}')
                                st.write(f'Aposta primeiro colocado: {listaSelecoes()[int(usuario[2*nomeGrupo+13])]}')

                        #-----------------------------------------------------------------------------#

                    elif task1 == 'Apostas fase de grupos':
                        st.title('Fase de Grupos')
                        classificacao = classificacaoInicial()

                        for nomeGrupo in range(len(grupos()[:,0])):
                            st.subheader(f'Grupo {grupos()[nomeGrupo][-1]}')
                            
                            # Datas e horários dos jogos
                            for nomeJogo in range(6):
                                with st.form(key = 'include_aposta_jogo_'+str(nomeJogo+1)+'do_grupo_'+str(grupos()[nomeGrupo][-1])):
                                    st.subheader(f'Grupo {grupos()[nomeGrupo][-1]} - Jogo {nomeJogo+1} - {dataHorarioJogoGrupo(nomeGrupo,nomeJogo)}')
                                    
                                    # rodada e jogo
                                    if nomeJogo == 0 or nomeJogo == 1:
                                        nomeRodada = 1
                                    elif nomeJogo == 2 or nomeJogo == 3:
                                        nomeRodada = 2
                                    elif nomeJogo == 4 or nomeJogo == 5:
                                        nomeRodada = 3
                                    
                                    if nomeRodada == 1:
                                        # Time i1 = 0
                                        # Time i2 = 1
                                        # Time i3 = 2
                                        # Time i4 = 3
                                        # rodada 1: Time i1 x Time i2
                                        # rodada 1: Time i3 x Time i4
                                        time1 = 0
                                        time2 = 1
                                        time3 = 2
                                        time4 = 3
                                        if nomeJogo == 0:
                                            #print('')
                                            #print('Jogo 1')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                            aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_1 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_1:
                                            if botao_jogo_1 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                            if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Fim de jogo!')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                                classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                        elif nomeJogo == 1:
                                            #print('')
                                            #print('Jogo 2')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                            aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_2 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_2:
                                            if botao_jogo_2 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Fim de jogo!')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                                classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                    elif nomeRodada == 2:
                                        # Time i1 = 0
                                        # Time i2 = 1
                                        # Time i3 = 2
                                        # Time i4 = 3
                                        # rodada 2: Time i1 x Time i3
                                        # rodada 2: Time i2 x Time i4
                                        # rodada 2: Time i4 x Time i2 ALTERADA
                                        time1 = 0
                                        time2 = 2
                                        time3 = 3
                                        time4 = 1
                                        if nomeJogo == 2:
                                            #print('')
                                            #print('Jogo 3')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                            aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_3 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_3:
                                            if botao_jogo_3 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                            if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Fim de jogo!')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                                classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                        elif nomeJogo == 3:
                                            #print('')
                                            #print('Jogo 4')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                            aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_4 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_4:
                                            if botao_jogo_4 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Fim de jogo!')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                                classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                    elif nomeRodada == 3:
                                        # Time i1 = 0
                                        # Time i2 = 1
                                        # Time i3 = 2
                                        # Time i4 = 3
                                        # rodada 3: Time i4 x Time i1
                                        # rodada 3: Time i2 x Time i3
                                        time1 = 3
                                        time2 = 0
                                        time3 = 1
                                        time4 = 2
                                        if nomeJogo == 4:
                                            #print('')
                                            #print('Jogo 5')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time1], grupos()[nomeGrupo][time2]))
                                            aposta_selecao_1 = st.number_input(label = grupos()[nomeGrupo][time1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_2 = st.number_input(label = grupos()[nomeGrupo][time2], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_5 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_5:
                                            if botao_jogo_5 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_1,aposta_selecao_2)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time1]} {aposta_selecao_1} X {aposta_selecao_2} {grupos()[nomeGrupo][time2]}')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                            if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Fim de jogo!')
                                                st.write(f'{grupos()[nomeGrupo][time1]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time2]}')
                                                classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))

                                        elif nomeJogo == 5:
                                            #print('')
                                            #print('Jogo 6')
                                            #print('%s X %s'%(grupos()[nomeGrupo][time3], grupos()[nomeGrupo][time4]))
                                            aposta_selecao_3 = st.number_input(label = grupos()[nomeGrupo][time3], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            aposta_selecao_4 = st.number_input(label = grupos()[nomeGrupo][time4], min_value = 0, max_value = 10, step = 1, format = '%d')
                                            botao_jogo_6 = st.form_submit_button(label = f'Apostar no jogo {nomeJogo+1}')
                                            inicioJogo = horarioJogoGrupo(nomeGrupo,nomeJogo)
                                            #if botao_jogo_6:
                                            if botao_jogo_6 and inicioJogo:
                                                fazerApostaPrimeiraFase(usuario,nomeGrupo,nomeJogo,aposta_selecao_3,aposta_selecao_4)
                                                np.save(str(username),usuario)
                                            if usuario[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Aposta registrada!')
                                                #st.write(f'{grupos()[nomeGrupo][time3]} {aposta_selecao_3} X {aposta_selecao_4} {grupos()[nomeGrupo][time4]}')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuario[28+2*6*nomeGrupo+2*nomeJogo]} X {usuario[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                            if usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo] != '':
                                                st.subheader('Fim de jogo!')
                                                st.write(f'{grupos()[nomeGrupo][time3]} {usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]} X {usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]} {grupos()[nomeGrupo][time4]}')
                                                classificacao = classificacaoFaseGrupos(classificacao,nomeGrupo,nomeJogo,int(usuarioMestre[28+2*6*nomeGrupo+2*nomeJogo]),int(usuarioMestre[29+2*6*nomeGrupo+2*nomeJogo]))
                                                
                        rotuloColuna = ['P',  # pontuação
                                        'J',  # jogos
                                        'V',  # vitórias
                                        'E',  # empates
                                        'D',  # derrotas
                                        'GP', # gols pró
                                        'GC', # gols contra
                                        'SG'] # saldo de gols
                        for contadorClassificacao in range(len(classificacao)):
                            classificacao[contadorClassificacao].pop(-1)
                            df = pd.DataFrame(np.array([[classificacao[contadorClassificacao][0][1],classificacao[contadorClassificacao][0][2],classificacao[contadorClassificacao][0][3],classificacao[contadorClassificacao][0][4],classificacao[contadorClassificacao][0][5],classificacao[contadorClassificacao][0][6],classificacao[contadorClassificacao][0][7],classificacao[contadorClassificacao][0][8]],
                                                        [classificacao[contadorClassificacao][1][1],classificacao[contadorClassificacao][1][2],classificacao[contadorClassificacao][1][3],classificacao[contadorClassificacao][1][4],classificacao[contadorClassificacao][1][5],classificacao[contadorClassificacao][1][6],classificacao[contadorClassificacao][1][7],classificacao[contadorClassificacao][1][8]],
                                                        [classificacao[contadorClassificacao][2][1],classificacao[contadorClassificacao][2][2],classificacao[contadorClassificacao][2][3],classificacao[contadorClassificacao][2][4],classificacao[contadorClassificacao][2][5],classificacao[contadorClassificacao][2][6],classificacao[contadorClassificacao][2][7],classificacao[contadorClassificacao][2][8]],
                                                        [classificacao[contadorClassificacao][3][1],classificacao[contadorClassificacao][3][2],classificacao[contadorClassificacao][3][3],classificacao[contadorClassificacao][3][4],classificacao[contadorClassificacao][3][5],classificacao[contadorClassificacao][3][6],classificacao[contadorClassificacao][3][7],classificacao[contadorClassificacao][3][8]]
                                                        ]),
                                        columns = tuple(rotuloColuna)
                            )
                            df.index = [classificacao[contadorClassificacao][0][0],classificacao[contadorClassificacao][1][0],classificacao[contadorClassificacao][2][0],classificacao[contadorClassificacao][3][0]]
                            st.table(df)

                            
                    elif task1 == 'Apostas nas fases eliminatórias':
                        st.title('Apostas nas fases eliminatórias')
                        
                        st.header('Oitavas de final')
                        #-----------------------------
                        opcoesOitavas1 = ['Holanda','Estados Unidos']
                        opcoesOitavas2 = ['Argentina','Austrália']
                        opcoesOitavas3 = ['Japão','Croácia']
                        opcoesOitavas4 = ['Brasil','Coreia do Sul']
                        opcoesOitavas5 = ['Inglaterra','Senegal']
                        opcoesOitavas6 = ['França','Polônia']
                        opcoesOitavas7 = ['Marrocos','Espanha']
                        opcoesOitavas8 = ['Portugal','Suíça']
                        opcoesOitavas  = [opcoesOitavas1,
                                          opcoesOitavas2,
                                          opcoesOitavas3,
                                          opcoesOitavas4,
                                          opcoesOitavas5,
                                          opcoesOitavas6,
                                          opcoesOitavas7,
                                          opcoesOitavas8]
                        #-----------------------------
                        horarioOitavas1 = horarioJogo(2022,12,3,12,0)
                        horarioOitavas2 = horarioJogo(2022,12,3,16,0)
                        horarioOitavas3 = horarioJogo(2022,12,5,12,0)
                        horarioOitavas4 = horarioJogo(2022,12,5,16,0)
                        horarioOitavas5 = horarioJogo(2022,12,4,12,0)
                        horarioOitavas6 = horarioJogo(2022,12,4,16,0)
                        horarioOitavas7 = horarioJogo(2022,12,6,12,0)
                        horarioOitavas8 = horarioJogo(2022,12,6,16,0)
                        horarioOitavas  = [horarioOitavas1,
                                           horarioOitavas2,
                                           horarioOitavas3,
                                           horarioOitavas4,
                                           horarioOitavas5,
                                           horarioOitavas6,
                                           horarioOitavas7,
                                           horarioOitavas8]
                        #-----------------------------
                        dataOitavas1 = datetime(2022,12,3,12,0)
                        dataOitavas2 = datetime(2022,12,3,16,0)
                        dataOitavas3 = datetime(2022,12,5,12,0)
                        dataOitavas4 = datetime(2022,12,5,16,0)
                        dataOitavas5 = datetime(2022,12,4,16,0)
                        dataOitavas6 = datetime(2022,12,4,12,0)
                        dataOitavas7 = datetime(2022,12,6,12,0)
                        dataOitavas8 = datetime(2022,12,6,16,0)
                        dataOitavas  = [dataOitavas1,
                                        dataOitavas2,
                                        dataOitavas3,
                                        dataOitavas4,
                                        dataOitavas5,
                                        dataOitavas6,
                                        dataOitavas7,
                                        dataOitavas8]
                        #-----------------------------
                        for nomeJogo in range(8):
                            st.subheader(f'Jogo {nomeJogo+1} - {opcoesOitavas[nomeJogo][0]} x {opcoesOitavas[nomeJogo][1]} - {dataOitavas[nomeJogo]}')
                            with st.form(key = 'incluirApostaFaseEliminatoriasOitavasJogo'+str(nomeJogo+1)):
                                apostaOitavas = st.selectbox('Qual será a seleção classificada?', options = opcoesOitavas[nomeJogo], index = 0)
                                apostaOitavasSelecao1 = st.number_input(label = opcoesOitavas[nomeJogo][0], min_value = 0, max_value = 10, step = 1, format = '%d')
                                apostaOitavasSelecao2 = st.number_input(label = opcoesOitavas[nomeJogo][1], min_value = 0, max_value = 10, step = 1, format = '%d')
                                botaoApostaOitavas = st.form_submit_button(label = 'Apostar')
                            if botaoApostaOitavas and horarioOitavas[nomeJogo]:
                                if apostaOitavas == opcoesOitavas[nomeJogo][0] and apostaOitavasSelecao1 < apostaOitavasSelecao2 or apostaOitavas == opcoesOitavas[nomeJogo][1] and apostaOitavasSelecao2 < apostaOitavasSelecao1:
                                    st.subheader('Apostas INVÁLIDAS!')
                                    st.write(f'Tente realizar as apostas novamente.')
                                else:
                                    usuario[124+3*nomeJogo], usuario[125+3*nomeJogo] = apostaOitavasSelecao1, apostaOitavasSelecao2
                                    usuario[126+3*nomeJogo] = apostaOitavas
                                    np.save(str(username),usuario)
                            elif botaoApostaOitavas and not horarioOitavas[nomeJogo]:
                                st.subheader('O jogo já começou!')
                                st.write(f'Você NÃO pode realizar as apostas.')
                            if usuario[124+3*nomeJogo] != '' and usuario[126+3*nomeJogo] != '':
                                st.subheader('Aposta registrada!')
                                st.write(f'{opcoesOitavas[nomeJogo][0]} {usuario[124+3*nomeJogo]} X {usuario[125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
                                st.write(f'Aposta classificação: {usuario[126+3*nomeJogo]}')
                            if usuarioMestre[124+3*nomeJogo] != '' and usuarioMestre[126+3*nomeJogo] != '':
                                st.subheader('Fim de jogo!')
                                st.write(f'{opcoesOitavas[nomeJogo][0]} {usuarioMestre[124+3*nomeJogo]} X {usuarioMestre[125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
                                st.write(f'Seleção classificada: {usuarioMestre[126+3*nomeJogo]}')

                    elif task1 == 'Resumo das apostas':
                        st.header('Resumo das apostas')
                        
                        tabs = []
                        for tab in range(len(usuariosLista)):
                            tabs.append(np.array(usuariosLista)[tab][0])
                        tabs[0] = 'Classificação do Bolão'
                        tabs = st.tabs(tabs)
                        dataHoraMinutoAtual = datetime.strptime(datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%y %H:%M'), '%d/%m/%y %H:%M')
                        opcoesBolao = ['Campeão do mundo','Vice de nada','cara que não sabe de futebol, mas não vai ser o pior do bolão','Pangaré do futebol']
                        for usuario in range(len(usuariosLista)):
                            if usuario == 0:
                                with tabs[usuario]:
                                    st.header(f'Resumo das apostas do Bolão')
                                    st.image("https://static.streamlit.io/examples/owl.jpg", width = 200)
                                    
                                    st.subheader(f'Classificação do Bolão - {dataHoraMinutoAtual}')
                                    classificacaoBolao = []
                                    dadosClassificacao = []
                                    for contadorUsuario in range(1, len(usuariosLista), 1):
                                        classificacaoBolao.append([usuariosLista[contadorUsuario][0],usuariosLista[contadorUsuario][2],usuariosLista[contadorUsuario][3],usuariosLista[contadorUsuario][4],usuariosLista[contadorUsuario][5],usuariosLista[contadorUsuario][6],usuariosLista[contadorUsuario][7]])
                                        dadosClassificacao.append(np.delete(np.array(classificacaoBolao[contadorUsuario-1]),0,0))
                                    df0 = pd.DataFrame(np.array(dadosClassificacao),
                                                       columns = ('Pontos','Cravadas','Acertos','Erros','Nadas','Não apostas'))
                                    df0.index = np.delete(np.array(usuariosLista)[:,0],0)
                                    st.table(df0)
                                    
                                    #------------------                                    
                                    colunas = []
                                    opcoes = []
                                    apostasCampeao = []
                                    apostasViceCampeao = []
                                    apostasTerceiroColocado = []
                                    apostasGrupos = []
                                    for contadorUsuario in range(1, len(usuariosLista), 1):
                                        
                                        # Apostas Iniciais bolão, campeão, vice e terceiro
                                        colunas.append(np.array(usuariosLista)[contadorUsuario][0])
                                        if usuariosLista[contadorUsuario][8] != '':
                                            opcoes.append(f'Acha que vai ser o {opcoesBolao[int(usuariosLista[contadorUsuario][8])]} !')
                                        else:
                                            opcoes.append(f'Não acha nada.')

                                        if np.array(usuariosLista)[contadorUsuario][9] != '':
                                            apostasCampeao.append(listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][9])])
                                        else:
                                            apostasCampeao.append('Não apostou no campeão')

                                        if np.array(usuariosLista)[contadorUsuario][10] != '':
                                            apostasViceCampeao.append(listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][10])])
                                        else:
                                            apostasViceCampeao.append('Não apostou no vice-campeão')

                                        if np.array(usuariosLista)[contadorUsuario][11] != '':
                                            apostasTerceiroColocado.append(listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][11])])
                                        else:
                                            apostasTerceiroColocado.append('Não apostou no terceiro colocado')

                                        # apostas Iniciais Grupos
                                        listaApostasGruposUsuario = []
                                        for apostaGrupo in range(12, 28, 2):
                                            if np.array(usuariosLista)[contadorUsuario][apostaGrupo] != '':
                                                listaApostasGruposUsuario.append([listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])],listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])]])
                                            else:
                                                listaApostasGruposUsuario.append(['Não apostou','Não apostou'])
                                        apostasGrupos.append(listaApostasGruposUsuario)
                                        
                                    #--------------------------------

                                    classificadosGrupos = np.array(['Holanda','Senegal',
                                                                    'Inglaterra','Estados Unidos',
                                                                    'Argentina','Polônia',
                                                                    'França','Austrália',
                                                                    'Japão','Espanha',
                                                                    'Marrocos','Croácia',
                                                                    'Brasil','Suíça',
                                                                    'Portugal','Coreia do Sul'])
                                    
                                    apostadorPontuacaoApostasGrupos = []
                                    apostadorPontuacaoGrupos = []
                                    for contadorUsuario in range(1, len(usuariosLista), 1):
                                        pontuacaoApostasGrupos = []
                                        pontuacaoGrupos = 0
                                        for apostaGrupo in range(12, 28, 2):
                                            if np.array(usuariosLista)[contadorUsuario][apostaGrupo] != '':
                                                #pontuacaoApostasGrupos.append([listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])],listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])]])
                                                if listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                                                    pontuacaoApostasGrupos.append([30,30])
                                                    pontuacaoGrupos += 60
                                                elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                                                    pontuacaoApostasGrupos.append([30,0])
                                                    pontuacaoGrupos += 30
                                                elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                                                    pontuacaoApostasGrupos.append([21,21])
                                                    pontuacaoGrupos += 42
                                                elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo-12]:
                                                    pontuacaoApostasGrupos.append([21,0])
                                                    pontuacaoGrupos += 21
                                                elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                                                    pontuacaoApostasGrupos.append([0,30])
                                                    pontuacaoGrupos += 30
                                                elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                                                    pontuacaoApostasGrupos.append([0,21])
                                                    pontuacaoGrupos += 21
                                                elif listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[contadorUsuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                                                    pontuacaoApostasGrupos.append([0,0])
                                                    pontuacaoGrupos += 0
                                            else:
                                                #pontuacaoApostasGrupos.append(['Não apostou','Não apostou'])
                                                pontuacaoApostasGrupos.append([0,0])
                                        apostadorPontuacaoApostasGrupos.append(pontuacaoApostasGrupos)
                                        apostadorPontuacaoGrupos.append(pontuacaoGrupos)
                                    
                                    #-------------------------------------------
                                    

                                    st.subheader(f'Apostas campeão, final e terceiro colocado')
                                    colunas = tuple(colunas)
                                    dfa = pd.DataFrame(np.array([opcoes,apostasCampeao,apostasViceCampeao,apostasTerceiroColocado,]),
                                                      columns = colunas)
                                    dfa.index = ['Bolão','Campeão','Vice-campeão','Terceiro colocado']
                                    st.table(dfa)

                                    #-------------------------------------------
                                    
                                    st.subheader(f'Apostas classificados nos grupos')
                                    dfb = pd.DataFrame(np.array([np.array(apostadorPontuacaoGrupos),
                                                                 np.array(apostasGrupos)[:,0][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,0][:,0]),
                                                                 np.array(apostasGrupos)[:,0][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,0][:,1]), # grupo A
                                                                 np.array(apostasGrupos)[:,1][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,1][:,0]),
                                                                 np.array(apostasGrupos)[:,1][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,1][:,1]), # grupo B
                                                                 np.array(apostasGrupos)[:,2][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,2][:,0]),
                                                                 np.array(apostasGrupos)[:,2][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,2][:,1]), # grupo C
                                                                 np.array(apostasGrupos)[:,3][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,3][:,0]),
                                                                 np.array(apostasGrupos)[:,3][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,3][:,1]), # grupo D
                                                                 np.array(apostasGrupos)[:,4][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,4][:,0]),
                                                                 np.array(apostasGrupos)[:,4][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,4][:,1]), # grupo E
                                                                 np.array(apostasGrupos)[:,5][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,5][:,0]),
                                                                 np.array(apostasGrupos)[:,5][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,5][:,1]), # grupo F
                                                                 np.array(apostasGrupos)[:,6][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,6][:,0]),
                                                                 np.array(apostasGrupos)[:,6][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,6][:,1]), # grupo G
                                                                 np.array(apostasGrupos)[:,7][:,0],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,7][:,0]),
                                                                 np.array(apostasGrupos)[:,7][:,1],np.array(np.array(apostadorPontuacaoApostasGrupos)[:,7][:,1])]), # grupo H
                                                      columns = colunas)
                                    dfb.index = ['Pontuação total',
                                                 '1° Grupo A','1° Grupo A - Pontuação',
                                                 '2° Grupo A','2° Grupo A - Pontuação',
                                                 '1° Grupo B','1° Grupo B - Pontuação',
                                                 '2° Grupo B','2° Grupo B - Pontuação',
                                                 '1° Grupo C','1° Grupo C - Pontuação',
                                                 '2° Grupo C','2° Grupo C - Pontuação',
                                                 '1° Grupo D','1° Grupo D - Pontuação',
                                                 '2° Grupo D','2° Grupo D - Pontuação',
                                                 '1° Grupo E','1° Grupo E - Pontuação',
                                                 '2° Grupo E','2° Grupo E - Pontuação',
                                                 '1° Grupo F','1° Grupo F - Pontuação',
                                                 '2° Grupo F','2° Grupo F - Pontuação',
                                                 '1° Grupo G','1° Grupo G - Pontuação',
                                                 '2° Grupo G','2° Grupo G - Pontuação',
                                                 '1° Grupo H','1° Grupo H - Pontuação',
                                                 '2° Grupo H','2° Grupo H - Pontuação']
                                    st.table(dfb)
                                    
                                    #-------------------------------------------
                            
                            else:
                                with tabs[usuario]:
                                    st.header(f'Resumo das apostas - {np.array(usuariosLista)[usuario][0]}')                                    

                                    #-----------------------------
                                    st.subheader('Oitavas de final')
                                    #-----------------------------
                                    opcoesOitavas1 = ['Holanda','Estados Unidos']
                                    opcoesOitavas2 = ['Argentina','Austrália']
                                    opcoesOitavas3 = ['Japão','Croácia']
                                    opcoesOitavas4 = ['Brasil','Coreia do Sul']
                                    opcoesOitavas5 = ['Inglaterra','Senegal']
                                    opcoesOitavas6 = ['França','Polônia']
                                    opcoesOitavas7 = ['Marrocos','Espanha']
                                    opcoesOitavas8 = ['Portugal','Suíça']
                                    opcoesOitavas  = [opcoesOitavas1,
                                                      opcoesOitavas2,
                                                      opcoesOitavas3,
                                                      opcoesOitavas4,
                                                      opcoesOitavas5,
                                                      opcoesOitavas6,
                                                      opcoesOitavas7,
                                                      opcoesOitavas8]
                                    #-----------------------------
                                    horarioOitavas1 = horarioJogo(2022,12,3,12,0)
                                    horarioOitavas2 = horarioJogo(2022,12,3,16,0)
                                    horarioOitavas3 = horarioJogo(2022,12,5,12,0)
                                    horarioOitavas4 = horarioJogo(2022,12,5,16,0)
                                    horarioOitavas5 = horarioJogo(2022,12,4,12,0)
                                    horarioOitavas6 = horarioJogo(2022,12,4,16,0)
                                    horarioOitavas7 = horarioJogo(2022,12,6,12,0)
                                    horarioOitavas8 = horarioJogo(2022,12,6,16,0)
                                    horarioOitavas  = [horarioOitavas1,
                                                       horarioOitavas2,
                                                       horarioOitavas3,
                                                       horarioOitavas4,
                                                       horarioOitavas5,
                                                       horarioOitavas6,
                                                       horarioOitavas7,
                                                       horarioOitavas8]
                                    #-----------------------------
                                    for nomeJogo in range(8):
                                        st.write(f'Jogo {nomeJogo+1} - {np.array(usuariosLista)[usuario][0]}')
                                        if not horarioOitavas[nomeJogo]:
                                        #if horarioOitavas[nomeJogo]:
                                            if np.array(usuariosLista)[usuario][124+3*nomeJogo] != '':
                                                st.write(f'{opcoesOitavas[nomeJogo][0]} {np.array(usuariosLista)[usuario][124+3*nomeJogo]}x{np.array(usuariosLista)[usuario][125+3*nomeJogo]} {opcoesOitavas[nomeJogo][1]}')
                                                st.write(f'Classificado: {np.array(usuariosLista)[usuario][126+3*nomeJogo]}')
                                            else:
                                                st.write(f'Aposta NÃO realizada.')
                                    #-------------------------------------------
                                    
                                    if usuariosLista[usuario][8] != '':
                                        st.subheader(f'Acha que vai ser o {opcoesBolao[int(usuariosLista[usuario][8])]} !')
                                    
                                    if np.array(usuariosLista)[usuario][9] != '':
                                        apostaCampeao = listaSelecoes()[int(np.array(usuariosLista)[usuario][9])]
                                    else:
                                        apostaCampeao = 'Não apostou no campeão'
                                        
                                    if np.array(usuariosLista)[usuario][10] != '':
                                        apostaViceCampeao = listaSelecoes()[int(np.array(usuariosLista)[usuario][10])]
                                    else:
                                        apostaViceCampeao = 'Não apostou no vice-campeão'
                                        
                                    if np.array(usuariosLista)[usuario][11] != '':
                                        apostaTerceiroColocado = listaSelecoes()[int(np.array(usuariosLista)[usuario][11])]
                                    else:
                                        apostaTerceiroColocado = 'Não apostou no terceiro colocado'
                                        
                                    df1 = pd.DataFrame(np.array([[apostaCampeao,apostaViceCampeao,apostaTerceiroColocado],
                                                        ['Fase de grupos','Fase de grupos','Fase de grupos']]),
                                                        columns = ('Campeão','Vice-campeão','Terceiro colocado'))
                                    df1.index = [f'Aposta - {np.array(usuariosLista)[usuario][0]}','Periodo da aposta']
                                    st.table(df1)

                                    st.subheader(f'Apostas grupos - {dataHoraMinutoAtual}:')
                                    classificadosGrupos = np.array(['Holanda','Senegal',
                                                                    'Inglaterra','Estados Unidos',
                                                                    'Argentina','Polônia',
                                                                    'França','Austrália',
                                                                    'Japão','Espanha',
                                                                    'Marrocos','Croácia',
                                                                    '','',
                                                                    '',''])
                                    pontuacaoApostasGrupos = []
                                    pontuacaoGrupos = 0
                                    for apostaGrupo in range(12, 28, 2):
                                        if np.array(usuariosLista)[usuario][apostaGrupo] != '':
                                            pontuacaoApostasGrupos.append([listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])],listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])]])
                                            if listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                                                pontuacaoApostasGrupos.append([30,30])
                                                pontuacaoGrupos += 60
                                            elif listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] == classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                                                pontuacaoApostasGrupos.append([30,0])
                                                pontuacaoGrupos += 30
                                            elif listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                                                pontuacaoApostasGrupos.append([21,21])
                                                pontuacaoGrupos += 42
                                            elif listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] == classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo-12]:
                                                pontuacaoApostasGrupos.append([21,0])
                                                pontuacaoGrupos += 21
                                            elif listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo+1-12]:
                                                pontuacaoApostasGrupos.append([0,30])
                                                pontuacaoGrupos += 30
                                            elif listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] != classificadosGrupos[apostaGrupo+1-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] == classificadosGrupos[apostaGrupo-12]:
                                                pontuacaoApostasGrupos.append([0,21])
                                                pontuacaoGrupos += 21
                                            elif listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo])] != classificadosGrupos[apostaGrupo-12] and listaSelecoes()[int(np.array(usuariosLista)[usuario][apostaGrupo+1])] != classificadosGrupos[apostaGrupo+1-12]:
                                                pontuacaoApostasGrupos.append([0,0])
                                                pontuacaoGrupos += 0
                                        else:
                                            pontuacaoApostasGrupos.append(['Não apostou','Não apostou'])
                                            pontuacaoApostasGrupos.append([0,0])

                                    df2 = pd.DataFrame(np.array(pontuacaoApostasGrupos),
                                                       columns = ('Primeiro colocado','Segundo colocado'))
                                    df2.index = ['Grupo A - aposta',
                                                 'Grupo A - pontuação',
                                                 'Grupo B - aposta',
                                                 'Grupo B - pontuação',
                                                 'Grupo C - aposta',
                                                 'Grupo C - pontuação',
                                                 'Grupo D - aposta',
                                                 'Grupo D - pontuação',
                                                 'Grupo E - aposta',
                                                 'Grupo E - pontuação',
                                                 'Grupo F - aposta',
                                                 'Grupo F - pontuação',
                                                 'Grupo G - aposta',
                                                 'Grupo G - pontuação',
                                                 'Grupo H - aposta',
                                                 'Grupo H - pontuação']
                                    st.table(df2)
                                    st.subheader(f'Apostas dos classificados dos grupos: {pontuacaoGrupos} ponto(s)')
                                    #-------------------------------------------
                                    
                                    st.subheader(f'Apostas jogos primeira fase - {dataHoraMinutoAtual}:')
                                    for contadorGrupo in range(8):
                                        st.write(f'Grupo {grupos()[:,4][contadorGrupo]} - {np.array(usuariosLista)[usuario][0]}')
                                        for contadorJogo in range(6):
                                            # rodada e jogo
                                            if contadorJogo == 0 or contadorJogo == 1:
                                                nomeRodada = 1
                                            elif contadorJogo == 2 or contadorJogo == 3:
                                                nomeRodada = 2
                                            elif contadorJogo == 4 or contadorJogo == 5:
                                                nomeRodada = 3

                                            if nomeRodada == 1:
                                                # Time i1 = 0
                                                # Time i2 = 1
                                                # Time i3 = 2
                                                # Time i4 = 3
                                                # rodada 1: Time i1 x Time i2
                                                # rodada 1: Time i3 x Time i4
                                                time1 = 0
                                                time2 = 1
                                                time3 = 2
                                                time4 = 3
                                                if contadorJogo == 0:
                                                    timeMandante  = time1
                                                    timeVisitante = time2
                                                elif contadorJogo == 1:
                                                    timeMandante  = time3
                                                    timeVisitante = time4

                                            elif nomeRodada == 2:
                                                # Time i1 = 0
                                                # Time i2 = 1
                                                # Time i3 = 2
                                                # Time i4 = 3
                                                # rodada 2: Time i1 x Time i3
                                                # rodada 2: Time i2 x Time i4
                                                time1 = 0
                                                time2 = 2
                                                time3 = 3
                                                time4 = 1
                                                if contadorJogo == 2:
                                                    timeMandante  = time1
                                                    timeVisitante = time2
                                                elif contadorJogo == 3:
                                                    timeMandante  = time3
                                                    timeVisitante = time4

                                            elif nomeRodada == 3:
                                                # Time i1 = 0
                                                # Time i2 = 1
                                                # Time i3 = 2
                                                # Time i4 = 3
                                                # rodada 3: Time i4 x Time i1
                                                # rodada 3: Time i2 x Time i3
                                                time1 = 3
                                                time2 = 0
                                                time3 = 1
                                                time4 = 2
                                                if contadorJogo == 4:
                                                    timeMandante  = time1
                                                    timeVisitante = time2
                                                elif contadorJogo == 5:
                                                    timeMandante  = time3
                                                    timeVisitante = time4

                                            if not horarioJogoGrupo(contadorGrupo,contadorJogo):
                                                if np.array(usuariosLista)[usuario][28+2*6*contadorGrupo+2*contadorJogo] != '':
                                                    st.write(f'Jogo {contadorJogo+1}: {grupos()[contadorGrupo][timeMandante]} {np.array(usuariosLista)[usuario][28+2*6*contadorGrupo+2*contadorJogo]} x {np.array(usuariosLista)[usuario][29+2*6*contadorGrupo+2*contadorJogo]} {grupos()[contadorGrupo][timeVisitante]}')
                                                else:
                                                    st.write(f'Jogo {contadorJogo+1}: Aposta NÃO realizada.')

                    elif task1 == 'Links externos':

                        classificacaoGE = 'https://ge.globo.com/futebol/copa-do-mundo/2022/'
                        if st.button('Classificação Globo Esporte'):
                            webbrowser.open_new_tab(classificacaoGE)
                        
                        simuladorGE = 'https://interativos.ge.globo.com/futebol/copa-do-mundo/especial/simulador-da-copa-do-mundo-2022'
                        if st.button('Simulador Globo Esporte'):
                            webbrowser.open_new_tab(simuladorGE)

                elif task == 'Outros':
                    st.title('Dá uma seguradinha que estamos começando ainda ... 🎈')

            else:
                st.error('Usuário/senha inválidos')
            
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#
#=============================================================================#
#-----------------------------------------------------------------------------#
