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
  mimax = args[0]
  Ks = args[1]
  Yxs = args[2]
  kd = args[3]
  alfa = args[4]

  mi = mimax * (C[1] / (Ks + C[1]))
  dCxdt = (mi - kd) * C[0]
  dCsdt = - (1/Yxs) * (mi - kd) * (C[0])
  dCpdt = alfa * mi * C[0]
  return dCxdt, dCsdt, dCpdt

def edo2(C, t, *args):
  mimax = args[0]
  Ks = args[1]
  Yxs = args[2]
  kd = args[3]
  beta = args[4]

  mi = mimax * (C[1] / (Ks + C[1]))
  dCxdt = (mi - kd) * C[0]
  dCsdt = - (1/Yxs) * (mi - kd) * (C[0])
  dCpdt = beta * C[0]
  return dCxdt, dCsdt, dCpdt

def edo3(C, t, *args):
  mimax = args[0]
  Ks = args[1]
  Yxs = args[2]
  kd = args[3]
  alfa = args[4]
  beta = args[5]

  mi = mimax * (C[1] / (Ks + C[1]))
  dCxdt = (mi - kd) * C[0]
  dCsdt = - (1/Yxs) * (mi - kd) * (C[0])
  dCpdt = ((alfa * mi) + beta ) * (C[0])
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

limites1 = [(0, 1),(0, 100),(0, 1),(0, 1),(0, 1)]
limites2 = [(0, 1),(0, 100),(0, 1),(0, 1),(0, 1)]
limites3 = [(0, 1),(0, 100),(0, 1),(0, 1),(0, 1),(0, 1)]
args = (t, Cexp)
novos_parametros1 = differential_evolution(rmse1, limites1, args = args, popsize=5,  tol=0.01, mutation=(0.5, 1), recombination=0.7, updating='immediate') #aplicando a evolução diferencial
P1 = novos_parametros1.x
novos_parametros2 = differential_evolution(rmse2, limites2, args = args, popsize=5,  tol=0.01, mutation=(0.5, 1), recombination=0.7, updating='immediate') #aplicando a evolução diferencial
P2 = novos_parametros2.x
novos_parametros3 = differential_evolution(rmse3, limites3, args = args, popsize=5,  tol=0.01, mutation=(0.5, 1), recombination=0.7, updating='immediate') #aplicando a evolução diferencial
P3 = novos_parametros3.x

def result1():
  return P1

def result2():
  return P2

def result3():
  return P3

P1 = tuple(P1)
sol1 = odeint(edo1, Ci, t, args = P1)
Cx1 = sol1[:,0]
Cs1 = sol1[:,1]
Cp1 = sol1[:,2]

P2 = tuple(P2)
sol2 = odeint(edo2, Ci, t, args = P2)
Cx2 = sol2[:,0]
Cs2 = sol2[:,1]
Cp2 = sol2[:,2]

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