#Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import odeint


#Importando os dados
df = pd.read_excel('Parâmetros_Levenspinel_Sim.xlsx')
data = df.to_numpy() #Covertendo os dados em np
data = data[0:,1]

#Definindo as EDO's
def edo(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  n = args[2] #constante de inibição por substrato
  Yxs = args[3]  # coeficiente estequiométrico
  kd = args[4]  # constante de morte celular
  alfa = args[5]  # constante do produto associado ao crescimento
  Cpmax = args[6]

  d = 1 - (C[2]/Cpmax)
  d1 = d ** n
  d2 = C[1] / (Ks + C[1])
  mi = mimax * d2 * d1 #Levenspinel
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt =  -((1/Yxs) * (mi - kd) * C[0]) #eq para o substrato
  dCpdt = alfa * mi * C[0] #eq do produto associado ao crescimento
  return dCxdt, dCsdt, dCpdt

def edo2(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  n = args[2] #constante de inibição por substrato
  Yxs = args[3]  # coeficiente estequiométrico
  kd = args[4]  # constante de morte celular
  beta = args[5]  # constante do produto não associado ao crescimento
  Cpmax = args[6]

  d = 1 - (C[2]/Cpmax)
  d1 = d ** n
  d2 = C[1] / (Ks + C[1])
  mi = mimax * d2 * d1 #Levenspinel
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = -((1/Yxs) * (mi - kd) * C[0]) #eq para o substrato
  dCpdt = beta * C[0] #eq do produto não associado ao crescimento
  return dCxdt, dCsdt, dCpdt

def edo3(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  n = args[2] # constante de inibição por substrato
  Yxs = args[3]  # coeficiente estequiométrico
  kd = args[4]  # constante de morte celular
  alfa = args[5]  # constante do produto associado ao crescimento
  beta = args[6]  # constante do produto não associado ao crescimento
  Cpmax = args[7]

  d = 1 - (C[2]/Cpmax)
  d1 = d ** n
  d2 = C[1] / (Ks + C[1])
  mi = mimax * d2 * d1 #Levenspinel
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = -((1/Yxs) * (mi - kd) * C[0]) #eq para o substrato
  dCpdt = ((alfa * mi) + beta ) * C[0] #eq do produto parcialmente associado ao crescimento
  return dCxdt, dCsdt, dCpdt

t_s = np.linspace(0, int(data[0]), (int(data[0]) * 10))

def p_s1():
  Ci1 = data[1], data[2], 0
  s_p1 = data[3], data[4], data[5], data[6], data[7], data[8], data[9]
  s_p1 = tuple(s_p1)
  sol1 = odeint(edo, Ci1, t_s, args = s_p1)
  return sol1

sol1 = p_s1()

Cx1 = sol1[:, 0]
Cs1 = sol1[:, 1]
Cp1 = sol1[:, 2]

def p_s2():
  Ci2 = data[1], data[2], 0
  s_p2 = data[3], data[4], data[5], data[6], data[7], data[8], data[9]
  s_p2 = tuple(s_p2)
  sol2 = odeint(edo2, Ci2, t_s, args = s_p2)
  return sol2

sol2 = p_s2()

Cx2 = sol2[:, 0]
Cs2 = sol2[:, 1]
Cp2 = sol2[:, 2]

def plot_sim_Levenspinel1():
  f_S1 = plt.figure()
  ax = f_S1.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  func = ax.plot(t_s, Cx1, 'r-', linewidth=2, label='Cx')
  func2 = ax.plot(t_s, Cs1, 'b-', linewidth=2, label='Cs')
  func3 = ax.plot(t_s, Cp1, 'g-', linewidth=2, label='Cp')
  ax.set_title("SIMULAÇÃO - PRODUTO ASSOCIADO AO CRESCIMENTO", weight='bold')
  ax.set_xlabel('Tempo (h)', weight='bold')
  ax.set_ylabel('Concentração (g/L)', weight='bold')
  ax.grid(True)
  ax.legend(loc='upper center', ncol=2, shadow=True)
  f_S1.set_figheight(5)
  f_S1.set_figwidth(8)
  return plt.show()

def plot_sim_Levenspinel2():
  f_S2 = plt.figure()
  ax = f_S2.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  func = ax.plot(t_s, Cx2, 'r-', linewidth=2, label='Cx')
  func2 = ax.plot(t_s, Cs2, 'b-', linewidth=2, label='Cs')
  func3 = ax.plot(t_s, Cp2, 'g-', linewidth=2, label='Cp')
  ax.set_title("SIMULAÇÃO - PRODUTO NÃO ASSOCIADO AO CRESCIMENTO", weight='bold')
  ax.set_xlabel('Tempo (h)', weight='bold')
  ax.set_ylabel('Concentração (g/L)', weight='bold')
  ax.grid(True)
  ax.legend(loc='upper center', ncol=2, shadow=True)
  f_S2.set_figheight(5)
  f_S2.set_figwidth(8)
  return plt.show()

mimax = data[1]
ks = data[2]

if len(data) == 11:
  def p_s3():
    Ci3 = data[1], data[2], 0
    s_p3 = data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]
    s_p3 = tuple(s_p3)
    sol3 = odeint(edo3, Ci3, t_s, args=s_p3)
    return sol3


  sol3 = p_s3()

  Cx3 = sol3[:, 0]
  Cs3 = sol3[:, 1]
  Cp3 = sol3[:, 2]


  def plot_sim_Levenspinel3():
    f_S3 = plt.figure()
    ax = f_S3.add_subplot(111)
    plt.rc('axes', titlesize=15)
    plt.rc('axes', labelsize=10)
    func = ax.plot(t_s, Cx3, 'r-', linewidth=2, label='Cx')
    func2 = ax.plot(t_s, Cs3, 'b-', linewidth=2, label='Cs')
    func3 = ax.plot(t_s, Cp3, 'g-', linewidth=2, label='Cp')
    ax.set_title("SIMULAÇÃO - PRODUTO PARCIALMENTE ASSOCIADO AO CRESCIMENTO", weight='bold')
    ax.set_xlabel('Tempo (h)', weight='bold')
    ax.set_ylabel('Concentração (g/L)', weight='bold')
    ax.grid(True)
    ax.legend(loc='upper center', ncol=2, shadow=True)
    f_S3.set_figheight(5)
    f_S3.set_figwidth(8)
    return plt.show()


  Produtividadex3 = Cx3[1:] / t_s[1:]
  Produtividadex3[Produtividadex3 < 0] = 0

  Produtividadep3 = Cp3[1:] / t_s[1:]
  Produtividadep3[Produtividadep3 < 0] = 0


  def grafico_produtividade_s3():
    f_produtividade_exp = plt.figure()
    ax = f_produtividade_exp.add_subplot(111)
    plt.rc('axes', titlesize=15)
    plt.rc('axes', labelsize=10)
    l1 = ax.plot(t_s[1:], Produtividadex3, 'r-', linewidth=1, label='Produtividade celular')
    l2 = ax.plot(t_s[1:], Produtividadep3, 'b-', linewidth=1, label='Produtividade do produto')
    ax.set_title("PRODUTIVIDADE CELULAR E DO PRODUTO", weight='bold')
    ax.set_xlabel('Tempo (h)', weight='bold')
    ax.set_ylabel('Produtividade (g/L.h)', weight='bold')
    ax.grid(True)
    plt.rc('legend', fontsize=13)
    ax.legend(loc='upper center', ncol=2, shadow=True)
    f_produtividade_exp.set_figheight(6)
    f_produtividade_exp.set_figwidth(8)
    return plt.show()

  mi3 = mimax * (Cs3 / (ks + Cs3))


  def mi_Levenspinel_s3():
    f_mi = plt.figure()
    ax = f_mi.add_subplot(111)
    plt.rc('axes', titlesize=15)
    plt.rc('axes', labelsize=10)
    l1 = ax.plot(t_s, mi3, 'r-', linewidth=1)
    ax.set_title("Velocidade específica de crescimento - Levenspinel", weight='bold')
    ax.set_xlabel('Tempo (h)', weight='bold')
    ax.set_ylabel('Velocidade específica de crescimento', weight='bold')
    ax.grid(True)
    f_mi.set_figheight(5)
    f_mi.set_figwidth(8)
    return plt.show()

#Produtividades

Produtividadex1 = Cx1[1:] / t_s[1:]
Produtividadex1[Produtividadex1<0] = 0

Produtividadep1 = Cp1[1:] / t_s[1:]
Produtividadep1[Produtividadep1<0] = 0

Produtividadex2 = Cx2[1:] / t_s[1:]
Produtividadex2[Produtividadex2<0] = 0

Produtividadep2 = Cp2[1:] / t_s[1:]
Produtividadep2[Produtividadep2<0] = 0

Produtividadex2 = Cx2[1:] / t_s[1:]
Produtividadex2[Produtividadex2<0] = 0



def grafico_produtividade_s1():
  f_produtividade_exp = plt.figure()
  ax = f_produtividade_exp.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t_s[1:], Produtividadex1, 'r-', linewidth=1, label='Produtividade celular')
  l2 = ax.plot(t_s[1:], Produtividadep1, 'b-', linewidth=1, label='Produtividade do produto')
  ax.set_title("PRODUTIVIDADE CELULAR E DO PRODUTO", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Produtividade (g/L.h)', weight='bold')
  ax.grid(True)
  plt.rc('legend', fontsize=13)
  ax.legend(loc='upper center',ncol=2, shadow=True)
  f_produtividade_exp.set_figheight(6)
  f_produtividade_exp.set_figwidth(8)
  return plt.show()

def grafico_produtividade_s2():
  f_produtividade_exp = plt.figure()
  ax = f_produtividade_exp.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t_s[1:], Produtividadex2, 'r-', linewidth=1, label='Produtividade celular')
  l2 = ax.plot(t_s[1:], Produtividadep2, 'b-', linewidth=1, label='Produtividade do produto')
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

mi1 = mimax * (Cs1 / (ks + Cs1))
mi2 = mimax * (Cs2 / (ks + Cs2))

def mi_Levenspinel_s1():
  f_mi = plt.figure()
  ax = f_mi.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t_s, mi1, 'r-', linewidth=1)
  ax.set_title("Velocidade específica de crescimento - Levenspinel", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Velocidade específica de crescimento', weight='bold')
  ax.grid(True)
  f_mi.set_figheight(5)
  f_mi.set_figwidth(8)
  return plt.show()

def mi_Levenspinel_s2():
  f_mi = plt.figure()
  ax = f_mi.add_subplot(111)
  plt.rc('axes', titlesize=15)
  plt.rc('axes', labelsize=10)
  l1 = ax.plot(t_s, mi2, 'r-', linewidth=1)
  ax.set_title("Velocidade específica de crescimento - Levenspinel", weight ='bold')
  ax.set_xlabel('Tempo (h)',weight='bold')
  ax.set_ylabel('Velocidade específica de crescimento', weight='bold')
  ax.grid(True)
  f_mi.set_figheight(5)
  f_mi.set_figwidth(8)
  return plt.show()

def save_s1():
  df_concents_dados_sim_Levenspinel_s1 = pd.DataFrame(
    {'Tempo': t_s,'Cx': Cx1, 'Cs':Cs1, 'Cp':Cp1})
  df_concents_dados_produtividade_Levenspinel_s1 = pd.DataFrame(
    {'Tempo': t_s[1:],'Produtividade Celualr': Produtividadex1, 'Produtividade Produto': Produtividadep1})
  df_concents_dados_mi_Levenspinel_s1 = pd.DataFrame(
    {'Tempo': t_s,'Mi': mi1})
  with pd.ExcelWriter('Dados_simulação_Levenspinel_associado.xlsx') as writer:
    df_concents_dados_sim_Levenspinel_s1.to_excel(writer, sheet_name="Simulação")
    df_concents_dados_produtividade_Levenspinel_s1.to_excel(writer, sheet_name="Produtividade")
    df_concents_dados_mi_Levenspinel_s1.to_excel(writer, sheet_name="Mi")
    writer.save()

def save_s2():
  df_concents_dados_sim_Levenspinel_s2 = pd.DataFrame(
    {'Tempo': t_s,'Cx': Cx2, 'Cs':Cs2, 'Cp':Cp2})
  df_concents_dados_produtividade_Levenspinel_s2 = pd.DataFrame(
    {'Tempo': t_s[1:],'Produtividade Celualr': Produtividadex2, 'Produtividade Produto': Produtividadep2})
  df_concents_dados_mi_Levenspinel_s2 = pd.DataFrame(
    {'Tempo': t_s,'Mi': mi2})
  with pd.ExcelWriter('Dados_simulação_Levenspinel_não_associado.xlsx') as writer:
    df_concents_dados_sim_Levenspinel_s2.to_excel(writer, sheet_name="Simulação")
    df_concents_dados_produtividade_Levenspinel_s2.to_excel(writer, sheet_name="Produtividade")
    df_concents_dados_mi_Levenspinel_s2.to_excel(writer, sheet_name="Mi")
    writer.save()

def save_s3():
  df_concents_dados_sim_Levenspinel_s3 = pd.DataFrame(
    {'Tempo': t_s,'Cx': Cx3, 'Cs':Cs3, 'Cp':Cp3})
  df_concents_dados_produtividade_Levenspinel_s3 = pd.DataFrame(
    {'Tempo': t_s[1:],'Produtividade Celualr': Produtividadex3, 'Produtividade Produto': Produtividadep3})
  df_concents_dados_mi_Levenspinel_s3 = pd.DataFrame(
    {'Tempo': t_s,'Mi': mi3})
  with pd.ExcelWriter('Dados_simulação_Levenspinel_parcialmente_associado.xlsx') as writer:
    df_concents_dados_sim_Levenspinel_s3.to_excel(writer, sheet_name="Simulação")
    df_concents_dados_produtividade_Levenspinel_s3.to_excel(writer, sheet_name="Produtividade")
    df_concents_dados_mi_Levenspinel_s3.to_excel(writer, sheet_name="Mi")
    writer.save()