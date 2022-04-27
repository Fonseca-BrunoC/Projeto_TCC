#Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


#Definindo as EDO's
def edo(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  Yxs = args[2]  # coeficiente estequiométrico
  kd = args[3]  # constante de morte celular
  alfa = args[4]  # constante do produto associado ao crescimento

  mi = mimax * (C[1] / (Ks + C[1])) #Monod
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = - (1/Yxs) * (mi - kd) * C[0] #eq para o substrato
  dCpdt = alfa * mi * C[0] #eq do produto associado ao crescimento
  return dCxdt, dCsdt, dCpdt

def edo2(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  Yxs = args[2]  # coeficiente estequiométrico
  kd = args[3]  # constante de morte celular
  beta = args[5]  # constante do produto não associado ao crescimento

  mi = mimax * (C[1] / (Ks + C[1])) #Monod
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = - (1/Yxs) * (mi - kd) * C[0] #eq para o substrato
  dCpdt = beta * C[0] #eq do produto não associado ao crescimento
  return dCxdt, dCsdt, dCpdt

def edo3(C, t, *args):
  mimax = args[0]  # unidade 1/hora - taxa específica de crescimento
  Ks = args[1]  # constante de semi-saturação
  Yxs = args[2]  # coeficiente estequiométrico
  kd = args[3]  # constante de morte celular
  alfa = args[4]  # constante do produto associado ao crescimento
  beta = args[5]  # constante do produto não associado ao crescimento

  mi = mimax * (C[1] / (Ks + C[1])) #Monod
  dCxdt = (mi - kd) * C[0] #eq para célula
  dCsdt = - (1/Yxs) * (mi - kd) * C[0] #eq para o substrato
  dCpdt = ((alfa * mi) + beta ) * C[0] #eq do produto parcialmente associado ao crescimento
  return dCxdt, dCsdt, dCpdt