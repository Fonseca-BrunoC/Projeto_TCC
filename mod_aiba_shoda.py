import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution
from scipy.integrate import odeint
import pandas as pd

#Importando os dados
df = pd.read_excel('Dados.xlsx')
data = df.to_numpy() #Covertendo os dados em np
t = data[:,0] #tempo
Cexp = data[:,1:4] #Concentrações experimentais
Ci = (Cexp[0,0], Cexp[0,1], Cexp[0,2]) #condições iniciais


def edo1(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  Ki = args[2] #constante de inibição por substrato
  Yxs = args[3]  # coeficiente estequiométrico
  kd = args[4]  # constante de morte celular
  alfa = args[5]  # constante do produto associado ao crescimento

  d1 = np.exp(-Ki * C[2])
  d2 = C[1] / (Ks + C[1])
  mi = mimax * d2 * d1 #Aiba Shoda
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = -((1/Yxs) * (mi - kd) * C[0]) #eq para o substrato
  dCpdt = alfa * mi * C[0] #eq do produto associado ao crescimento
  return dCxdt, dCsdt, dCpdt

def edo2(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  Ki = args[2] #constante de inibição por substrato
  Yxs = args[3]  # coeficiente estequiométrico
  kd = args[4]  # constante de morte celular
  beta = args[5]  # constante do produto não associado ao crescimento

  d1 = np.exp(-Ki * C[2])
  d2 = C[1] / (Ks + C[1])
  mi = mimax * d2 * d1 #Aiba Shoda
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = -((1/Yxs) * (mi - kd) * C[0]) #eq para o substrato
  dCpdt = beta * C[0] #eq do produto não associado ao crescimento
  return dCxdt, dCsdt, dCpdt

def edo3(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  Ki = args[2] # constante de inibição por substrato
  Yxs = args[3]  # coeficiente estequiométrico
  kd = args[4]  # constante de morte celular
  alfa = args[5]  # constante do produto associado ao crescimento
  beta = args[6]  # constante do produto não associado ao crescimento

  d1 = np.exp(-Ki * C[2])
  d2 = C[1] / (Ks + C[1])
  mi = mimax * d2 * d1 #Aiba Shoda
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = -((1/Yxs) * (mi - kd) * C[0]) #eq para o substrato
  dCpdt = ((alfa * mi) + beta ) * C[0] #eq do produto parcialmente associado ao crescimento
  return dCxdt, dCsdt, dCpdt

lista = [1,1,1]

def rmse1(parametros, *data):
  t, Cexp = data
  p = tuple(parametros)
  simulacao = odeint(edo1, Ci, t, args = p)
  residuo = simulacao - Cexp
  for i in range(0,3):
    residuo[:,i] = residuo[:,i] / lista[i]
  residuo = residuo.flatten()
  residuo = sum(residuo ** 2)
  return residuo

def rmse2(parametros, *data):
  t, Cexp = data
  p = tuple(parametros)
  simulacao = odeint(edo2, Ci, t, args = p)
  residuo = simulacao - Cexp
  for i in range(0,3):
    residuo[:,i] = residuo[:,i] / lista[i]
  residuo = residuo.flatten()
  residuo = sum(residuo ** 2)
  return residuo

def rmse3(parametros, *data):
  t, Cexp = data
  p = tuple(parametros)
  simulacao = odeint(edo3, Ci, t, args = p)
  residuo = simulacao - Cexp
  for i in range(0,3):
    residuo[:,i] = residuo[:,i] / lista[i]
  residuo = residuo.flatten()
  residuo = sum(residuo ** 2)
  return residuo

def parametros1():
  limites1 = [(0, 1), (0, 50), (0, 100), (0.01, 5), (0, 1), (0, 2)]
  args = (t, Cexp)

  novos_parametros1 = differential_evolution(rmse1, limites1, args=args, popsize=5, tol=0.01, mutation=(0.5, 1),
                                             recombination=0.7,
                                             updating='immediate')  # aplicando a evolução diferencial
  P1 = novos_parametros1.x
  return P1

def result1():
  return parametros1()

def parametros2():
  limites2 = [(0, 1), (0, 50), (0, 100), (0.01, 5), (0, 1), (0, 2)]
  args = (t, Cexp)

  novos_parametros2 = differential_evolution(rmse2, limites2, args=args, popsize=5, tol=0.01, mutation=(0.5, 1),
                                               recombination=0.7,
                                               updating='immediate')  # aplicando a evolução diferencial
  P2 = novos_parametros2.x
  return P2

def result2():
  return parametros2()

def parametros3():
  limites3 = [(0, 1), (0, 50), (0, 100), (0.01, 5), (0, 1), (0, 2), (0, 2)]
  args = (t, Cexp)

  novos_parametros3 = differential_evolution(rmse3, limites3, args=args, popsize=5, tol=0.01, mutation=(0.5, 1),
                                               recombination=0.7,
                                               updating='immediate')  # aplicando a evolução diferencial
  P3 = novos_parametros3.x
  return P3

def result3():
  return parametros3()

P1 = parametros1()
P1 = tuple(P1)
sol1 = odeint(edo1, Ci, t, args = P1)
Cx1 = sol1[:,0]
Cs1 = sol1[:,1]
Cp1 = sol1[:,2]

P2 = parametros2()
P2 = tuple(P2)
sol2 = odeint(edo2, Ci, t, args = P2)
Cx2 = sol2[:,0]
Cs2 = sol2[:,1]
Cp2 = sol2[:,2]

P3 = parametros3()
P3 = tuple(P3)
sol3 = odeint(edo3, Ci, t, args = P3)
Cx3 = sol3[:,0]
Cs3 = sol3[:,1]
Cp3 = sol3[:,2]
#Comparando os valores
Cxe = Cexp[:,0]
Cse = Cexp[:,1]
Cpe = Cexp[:,2]

def plot1():
  f_MP1 = plt.figure()
  ax = f_MP1.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  m_cx = ax.plot(t, Cx1, 'r-', linewidth=1, label='Cx_Modelo')
  m_cs = ax.plot(t, Cs1, 'b-', linewidth=1, label='Cs_Modelo')
  m_cp = ax.plot(t, Cp1, 'g-', linewidth=1, label='Cp_Modelo')
  d_cx = ax.plot(t, Cxe, marker = 'o', markersize = 2, color = 'red', linestyle='', label='Cx_Dados')
  d_cs = ax.plot(t, Cse, marker = 'o', markersize = 2, color = 'blue', linestyle='', label='Cs_Dados')
  d_cp = ax.plot(t, Cpe, marker = 'o', markersize = 2, color = 'green', linestyle='', label='Cp_Dados')
  ax.set_title("Comparação entre dados e modelo", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Concentração (g/L)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center',ncol=2, shadow=True)
  f_MP1.set_figheight(5)
  f_MP1.set_figwidth(8)
  return plt.show()

def plot2():
  f_MP2 = plt.figure()
  ax = f_MP2.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  m_cx = ax.plot(t, Cx2, 'r-', linewidth=1, label='Cx_Modelo')
  m_cs = ax.plot(t, Cs2, 'b-', linewidth=1, label='Cs_Modelo')
  m_cp = ax.plot(t, Cp2, 'g-', linewidth=1, label='Cp_Modelo')
  d_cx = ax.plot(t, Cxe, marker='o', markersize = 2, color='red', linestyle='', label='Cx_Dados')
  d_cs = ax.plot(t, Cse, marker='o', markersize = 2, color='blue', linestyle='', label='Cs_Dados')
  d_cp = ax.plot(t, Cpe, marker='o', markersize = 2, color='green', linestyle='', label='Cp_Dados')
  ax.set_title("Comparação entre dados e modelo", weight='bold')
  ax.set_xlabel('Tempo (h)', weight='bold')
  ax.set_ylabel('Concentração (g/L)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center', ncol=2, shadow=True)
  f_MP2.set_figheight(5)
  f_MP2.set_figwidth(8)
  return plt.show()

def plot3():
  f_MP3 = plt.figure()
  ax = f_MP3.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  m_cx = ax.plot(t, Cx3, 'r-', linewidth=1, label='Cx_Modelo')
  m_cs = ax.plot(t, Cs3, 'b-', linewidth=1, label='Cs_Modelo')
  m_cp = ax.plot(t, Cp3, 'g-', linewidth=1, label='Cp_Modelo')
  d_cx = ax.plot(t, Cxe, marker='o', markersize = 2 , color='red', linestyle='', label='Cx_Dados')
  d_cs = ax.plot(t, Cse, marker='o', markersize= 2, color='blue', linestyle='', label='Cs_Dados')
  d_cp = ax.plot(t, Cpe, marker='o', markersize = 2, color='green', linestyle='', label='Cp_Dados')
  ax.set_title("Comparação entre dados e modelo", weight='bold')
  ax.set_xlabel('Tempo (h)', weight='bold')
  ax.set_ylabel('Concentração (g/L)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center', ncol=2, shadow=True)
  f_MP3.set_figheight(5)
  f_MP3.set_figwidth(8)
  return plt.show()

#Produtividades

Produtividadex_exp = Cxe[1:] / t[1:]
Produtividadex_exp[Produtividadex_exp<0] = 0

Produtividadex1_mod = Cx1[1:] / t[1:]
Produtividadex1_mod[Produtividadex1_mod<0] = 0

Produtividadep_exp = Cpe[1:] / t[1:]
Produtividadep_exp[Produtividadep_exp<0] = 0

Produtividadep1_mod = Cp1[1:] / t[1:]
Produtividadep1_mod[Produtividadep1_mod<0] = 0

Produtividadex2_mod = Cx2[1:] / t[1:]
Produtividadex2_mod[Produtividadex2_mod<0] = 0

Produtividadep2_mod = Cp2[1:] / t[1:]
Produtividadep2_mod[Produtividadep2_mod<0] = 0

Produtividadex3_mod = Cx3[1:] / t[1:]
Produtividadex3_mod[Produtividadex3_mod<0] = 0

Produtividadep3_mod = Cp3[1:] / t[1:]
Produtividadep3_mod[Produtividadep3_mod<0] = 0

def grafico_produtividade1():
  f_produtividade_exp = plt.figure()
  ax = f_produtividade_exp.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t[1:], Produtividadex1_mod, 'r-', linewidth=1, label='Produtividade celular\nmodelo')
  l2 = ax.plot(t[1:], Produtividadep1_mod, 'b-', linewidth=1, label='Produtividade do produto\nmodelo')
  l3 = ax.plot(t[1:], Produtividadex_exp, marker = 'o', markersize = 2, color = 'red', linestyle='', label='Produtividade celular\ndados')
  l4 = ax.plot(t[1:], Produtividadep_exp, marker = 'o', markersize = 2, color = 'blue', linestyle='', label='Produtividade do produto\ndados')
  ax.set_title("PRODUTIVIDADE CELULAR E DO PRODUTO", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Produtividade (g/L.h)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center',ncol=2, shadow=True)
  f_produtividade_exp.set_figheight(6)
  f_produtividade_exp.set_figwidth(8)
  return plt.show()

def grafico_produtividade2():
  f_produtividade_exp = plt.figure()
  ax = f_produtividade_exp.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t[1:], Produtividadex2_mod, 'r-', linewidth=1, label='Produtividade celular\nmodelo')
  l2 = ax.plot(t[1:], Produtividadep2_mod, 'b-', linewidth=1, label='Produtividade do produto\nmodelo')
  l3 = ax.plot(t[1:], Produtividadex_exp, marker = 'o', markersize = 2, color = 'red', linestyle='', label='Produtividade celular\ndados')
  l4 = ax.plot(t[1:], Produtividadep_exp, marker = 'o', markersize = 2, color = 'blue', linestyle='', label='Produtividade do produto\ndados')
  ax.set_title("PRODUTIVIDADE CELULAR E DO PRODUTO", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Produtividade (g/L.h)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center',ncol=2, shadow=True)
  f_produtividade_exp.set_figheight(6)
  f_produtividade_exp.set_figwidth(8)
  return plt.show()

def grafico_produtividade3():
  f_produtividade_exp = plt.figure()
  ax = f_produtividade_exp.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t[1:], Produtividadex3_mod, 'r-', linewidth=1, label='Produtividade celular\nmodelo')
  l2 = ax.plot(t[1:], Produtividadep3_mod, 'b-', linewidth=1, label='Produtividade do produto\nmodelo')
  l3 = ax.plot(t[1:], Produtividadex_exp, marker = 'o', markersize = 2, color = 'red', linestyle='', label='Produtividade celular\ndados')
  l4 = ax.plot(t[1:], Produtividadep_exp, marker = 'o', markersize = 2, color = 'blue', linestyle='', label='Produtividade do produto\ndados')
  ax.set_title("PRODUTIVIDADE CELULAR E DO PRODUTO", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Produtividade (g/L.h)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center',ncol=2, shadow=True)
  f_produtividade_exp.set_figheight(6)
  f_produtividade_exp.set_figwidth(8)
  return plt.show()

#Calculando os valores de mi
mimax1 = P1[0]
ks1 = P1[1]
mi1 = mimax1 * (Cs1 / (ks1 + Cs1))

mimax2 = P2[0]
ks2 = P2[1]
mi2 = mimax2 * (Cs2 / (ks2 + Cs2))

mimax3 = P3[0]
ks3 = P3[1]
mi3 = mimax3 * (Cs3 / (ks3 + Cs3))

def grafico_mi1():
  f_mi = plt.figure()
  ax = f_mi.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t, mi1, 'r-', linewidth=1)
  ax.set_title("Velocidade específica de crescimento - Aiba Shoda", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Velocidade específica de crescimento', weight='bold')
  ax.grid(True)
  f_mi.set_figheight(5)
  f_mi.set_figwidth(8)
  return plt.show()

def grafico_mi2():
  f_mi = plt.figure()
  ax = f_mi.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t, mi2, 'r-', linewidth=1)
  ax.set_title("Velocidade específica de crescimento - Aiba Shoda", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Velocidade específica de crescimento', weight='bold')
  ax.grid(True)
  f_mi.set_figheight(5)
  f_mi.set_figwidth(8)
  return plt.show()

def grafico_mi3():
  f_mi = plt.figure()
  ax = f_mi.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t, mi3, 'r-', linewidth=1)
  ax.set_title("Velocidade específica de crescimento - Aiba Shoda", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Velocidade específica de crescimento', weight='bold')
  ax.grid(True)
  f_mi.set_figheight(5)
  f_mi.set_figwidth(8)
  return plt.show()