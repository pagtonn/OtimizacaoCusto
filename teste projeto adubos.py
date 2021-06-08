
"""
Created on Sat Jul 18 14:49:11 2020

''''
#   minimizar o custo da adubação com base nos custo de cada 
#   fertilizante que tem suas definições e quantidades abaixo
#   sempre atento a demanda de cada necessidade
#        Projeto analisado unicamente perante custos  de N-P-K
#        As quantidades foram ajustadas para a produção de milho 
#   grão mediante valores esperados de produtividade e inseridos na solicitação
'''

import numpy as np
from scipy.optimize import linprog

n = (float(input ('Qual a recomendação de N?    ')))/1000
p = (float(input ('Qual a recomendação de P2O5?   ')))/1000
k = (float(input ('Qual a recomendação de K?    ')))/1000


c = np.array([2100,1600,1700,2500,1970,1630,1250,2000,1850])


Ac = np.array([[0.45,   0.0,   0],
               [0.21,     0,   0],
               [0.32,     0,   0],
               [ 0.1,  0.52,   0],
               [0.16,  0.46,   0],
               [ 0.0,  0.44,   0],
               [ 0.0,  0.18,   0],
               [ 0.0,     0, 0.6],
               [ 0.2,     0, 0.2]])

Ae = np.transpose(Ac)

be = np.array([n, p, k])

res = linprog(c, A_eq = Ae, b_eq = be, method = 'simplex' )

#resultado = [{:8.2f}.format(res.x)]
# apresentando os resultados da otimização
print()
print('    Resultados Obtidos com o Problema de otimizaçao de custos ')
print()
print()
print('Custo total de adubação obtido (R$) = {:10.2f}'.format(res.fun))
print()
print('Utilização de Uréia (kg) = {:8.2f}'.format(res.x[0]*1000))
print()
print('Utilização de Sulfato de Amônia (kg) = {:8.2f}'.format(res.x[1]*1000))
print()
print('Utilização de Nitrato de Amônia (kg) = {:8.2f}'.format(res.x[2]*1000))
print()
print('Utilização de MAP (kg) = {:8.2f}'.format(res.x[3]*1000))
print()
print('Utilização de DAP (kg) = {:8.2f}'.format(res.x[4]*1000))
print()
print('Utilização de ST (kg) = {:8.2f}'.format(res.x[5]*1000))
print()
print('Utilização de SS (kg) = {:8.2f}'.format(res.x[6]*1000))
print()
print('Utilização de KCl (kg) = {:8.2f}'.format(res.x[7]*1000))
print()
print('Utilização de 20-00-20 (kg) = {:8.2f}'.format(res.x[8]*1000))






























































































