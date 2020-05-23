# Exercício 1: Defina a função intersec(x1,y1,x2,y2,x3,y3,x4,y4) que sucede se, no plano cartesiano,
# há intersecção entre dois retângulos definidos pelos pontos superior esquerdo e inferior direito: (x1,y1) e (x2,y2)
# para o primeiro retângulo e (x3,y3) e (x4,y4) para o segundo.

def intersec(x1,y1,x2,y2,x3,y3,x4,y4):
	return intersecx(x1,x2,x3,x4) and intersecy(y1,y2,y3,y4)
def intersecx(x1,x2,x3,x4):
		if x3>=x1 and x3<=x2 or x4>=x1 and x4<=x2: return True
		else: return False
def intersecy(y1,y2,y3,y4):
		if y3<=y1 and y3>=y2 or y4<=y1 and y4>=y2: return True 
		else: return False 

# Exercício 2: A tarifação de uma ligação telefônica internacional é feita do seguinte modo: O valor mínimo é de R$5,
# que dá direito a uma ligação de até 5 minutos. Quando a duração é de até 10 minutos, são cobrados R$7. 
# Ligações com mais de 10 minutos pagam R$1 por cada minuto adicional (somados aos R$7 iniciais). 
# Defina a função tarifa(m) que associa o valor do custo da ligação com duração de m minutos.﻿ 
# Por exemplo:
# >>> tarifa(12)
# 9


def tarifa(m):
    if m<0: return False 
    if m<5: return 5
    elif m>5 and m<10: return 7
    else: return 7+(m-10)

# Exercício 3: Um torcedor fanático deseja confeccionar uma bandeira do Brasil "estilizada" para usar durante os jogos olímpicos de 2016. 
# Ele já tem a quantidade de panos verde e azul exatas e precisa saber quantos metros de pano amarelo vai precisar comprar. 
# Calcule a quantidade de pano amarelo (em metros quadrados), considerando que a bandeira está no plano cartesiano, 
# e que sabemos os valores dos pontos superior esquerdo (x1, y1) e inferior direito (x2, y2)

from math import*
def pano_amarelo(x1,y1,x2,y2):return area_quad(y1,y2)-area_circ(y1,y2)
def quad(x):return x*x
def lado_quad(y1,y2):return sqrt(area_quad(y1,y2))
def area_quad(y1,y2):return (quad(abs(y1-y2)))/2
def raio (x):return (x)/2
def area_circ(y1,y2):return pi*(quad(raio(lado_quad(y1,y2))))

