TS="a" or "b" or "ab" or "o"

S="f" or "m"
RH="+" or "-"

doações=[(("023.054.111-09",'f',27),"b",'-',(4,7,2012),500),(("021.054.111-09",'m',17),"a",'+',(4,7,2012),250),(("013.054.111-09",'m',37),"ab",'+',(4,7,2012),500)]
doações2=[(("023.054.111-09",'f',27),"b",'-',(4,7,2012),500),(("021.054.111-09",'m',17),"a",'+',(4,7,2012),250),(("013.054.111-09",'m',37),"ab",'+',(4,7,2012),500),(("523.054.111-09",'f',19),"b",'-',(4,7,2012),500),(("023.554.111-09",'m',17),"a",'+',(4,7,2012),500)]
doações4=[(("023.054.111-09",'f',27),"b",'-',(1,7,2012),500),(("123.054.111-09",'f',27),"a",'-',(1,7,2012),500),(("223.054.111-09",'f',27),"ab",'-',(2,7,2012),500),(("323.054.111-09",'f',27),"o",'-',(3,7,2012),500),(("423.054.111-09",'f',27),"a",'+',(3,7,2012),500),(("523.054.111-09",'f',27),"ab",'+',(4,7,2012),500),(("033.054.111-09",'f',27),"o",'+',(4,7,2012),500),(("083.054.111-09",'f',27),"b",'-',(5,7,2012),500),(("022.054.111-09",'f',27),"a",'+',(5,7,2012),500),(("023.024.111-09",'f',27),"a",'+',(5,7,2012),500),(("023.054.311-09",'f',27),"a",'-',(5,7,2012),500),(("020.054.111-09",'f',27),"ab",'+',(5,7,2012),500),(("023.254.111-09",'f',27),"ab",'+',(6,7,2012),500),(("023.554.111-09",'f',27),"o",'+',(7,7,2012),500),(("023.054.151-09",'f',27),"o",'+',(7,7,2012),500),(("923.054.111-09",'f',27),"b",'+',(8,7,2012),500),(("023.854.111-09",'f',27),"a",'-',(8,7,2012),500),(("023.454.111-09",'f',27),"b",'-',(9,7,2012),500),(("023.054.111-29",'f',27),"ab",'-',(10,7,2012),500),(("323.154.111-09",'f',27),"o",'+',(10,7,2012),500),(("023.054.181-09",'f',27),"ab",'+',(11,7,2012),500),(("023.054.011-09",'f',27),"a",'+',(12,7,2012),500),(("023.054.141-09",'f',27),"a",'-',(12,7,2012),500),(("023.054.911-09",'f',27),"ab",'+',(13,7,2012),500),(("023.954.111-09",'f',27),"b",'+',(14,7,2012),500),(("023.050.111-09",'f',27),"o",'-',(14,7,2012),500),(("023.054.121-09",'f',27),"ab",'+',(14,7,2012),500),(("023.054.111-19",'f',27),"b",'+',(14,7,2012),500),(("023.084.111-09",'f',27),"a",'-',(14,7,2012),500),(("023.054.111-89",'f',27),"o",'+',(14,7,2012),500),(("023.054.411-09",'f',27),"a",'+',(15,7,2012),250),(("333.054.111-09",'f',27),"b",'+',(15,7,2012),500),(("034.054.111-09",'f',27),"b",'+',(15,7,2012),500),(("023.054.123-09",'f',27),"b",'-',(16,7,2012),500),(("023.054.221-09",'f',27),"ab",'+',(17,7,2012),500),(("443.054.111-09",'f',27),"o",'-',(17,7,2012),500),(("023.434.111-09",'f',27),"o",'+',(18,7,2012),500),(("023.324.111-09",'f',27),"o",'+',(19,7,2012),250),(("322.054.111-09",'f',27),"o",'+',(20,7,2012),500),(("023.054.134-09",'f',27),"o",'+',(20,7,2012),500),(("023.054.361-09",'f',27),"o",'+',(20,7,2012),500),(("023.314.111-09",'f',27),"b",'-',(21,7,2012),500),(("023.054.111-02",'f',27),"b",'+',(21,7,2012),500),(("023.054.111-39",'f',27),"ab",'+',(22,7,2012),500),(("023.054.113-09",'f',27),"b",'-',(23,7,2012),500),(("023.054.551-09",'f',27),"a",'+',(24,7,2012),500),(("023.054.111-33",'f',27),"o",'+',(24,7,2012),500),(("023.054.111-59",'f',27),"o",'+',(24,7,2012),500),(("023.054.141-49",'f',27),"ab",'+',(25,7,2012),500),(("023.054.121-29",'f',27),"a",'-',(26,7,2012),500),(("023.054.111-03",'f',27),"o",'+',(27,7,2012),500),(("023.054.113-29",'f',27),"a",'-',(28,7,2012),500),(("993.054.111-09",'f',27),"a",'+',(29,7,2012),500),(("023.012.111-09",'f',27),"ab",'-',(30,7,2012),500),(("023.054.521-09",'f',27),"b",'+',(31,7,2012),500)]

##funções de estoque por tipo sanguíneo 
def estoqueapos(doações): ## estoque de A+
    def somaQDapos(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="a" and RH=="+"])
    def estoqueapos2(doações): return [(TS,RH,somaQDapos(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="a" and RH=="+"]
    if estoqueapos2(doações)==[]: return ("a","+",0)
    else: return estoqueapos2(doações)[0]
def estoqueaneg(doações): ## estoque de A-
    def somaQDaneg(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="a" and RH=="-"])
    def estoqueaneg2(doações): return [(TS,RH,somaQDaneg(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="a" and RH=="-"]
    if estoqueaneg2(doações)==[]: return ("a","-",0)
    else: return estoqueaneg2(doações)[0]
def estoquebpos(doações): ## estoque de B+
    def somaQDbpos(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="b" and RH=="+"])
    def estoquebpos2(doações): return [(TS,RH,somaQDbpos(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="b" and RH=="+"]
    if estoquebpos2(doações)==[]: return ("b","+",0)
    else: return estoquebpos2(doações)[0]
def estoquebneg(doações): ## estoque de B-
    def somaQDbneg(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="b" and RH=="-"])
    def estoquebneg2(doações): return [(TS,RH,somaQDbneg(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="b" and RH=="-"]
    if estoquebneg2(doações)==[]: return ("b","-",0)
    else: return estoquebneg2(doações)[0]
def estoqueabpos(doações): ## estoque de AB+
    def somaQDabpos(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="ab" and RH=="+"])
    def estoqueabpos2(doações): return [(TS,RH,somaQDabpos(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="ab" and RH=="+"]
    if estoqueabpos2(doações)==[]: return ("ab","+",0)
    else: return estoqueabpos2(doações)[0]
def estoqueabneg(doações): ## estoque de AB-
    def somaQDabneg(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="ab" and RH=="-"])
    def estoqueabneg2(doações): return [(TS,RH,somaQDabneg(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="ab" and RH=="-"]
    if estoqueabneg2(doações)==[]: return ("ab","-",0)
    else: return estoqueabneg2(doações)[0]
def estoqueopos(doações): ## estoque de O+
    def somaQDopos(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="o" and RH=="+"])
    def estoqueopos2(doações): return [(TS,RH,somaQDopos(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="o" and RH=="+"]
    if estoqueopos2(doações)==[]: return ("o","+",0)
    else: return estoqueopos2(doações)[0]
def estoqueoneg(doações): ## estoque de O-
    def somaQDoneg(doações): return sum([QD for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="o" and RH=="-"])
    def estoqueoneg2(doações): return [(TS,RH,somaQDoneg(doações)) for ((CPF,S,I),TS,RH,DD,QD) in doações if TS=="o" and RH=="-"]
    if estoqueoneg2(doações)==[]: return ("o","-",0)
    else: return estoqueoneg2(doações)[0]
                                                    
## PROBLEMA 1 - função estoque(doações)

def estoque(doações): return [estoqueapos(doações),estoqueaneg(doações),estoquebpos(doações),estoquebneg(doações),estoqueabpos(doações),estoqueabneg(doações),estoqueopos(doações),estoqueoneg(doações)]


## PROBLEMA 2 - função mediam(mês,ano,doações)

def mediam(mês,ano,doações):
    def somaQDmes(mês,ano,doações):
        return sum([QD for ((CPF,S,I),TS,RH,(d,m,a),QD) in doações if mês==m and ano==a]) ### SOMA DA QUANTIDADE DE SANGUE DOADA NAQUELE MÊS
    if mês==1: return somaQDmes(mês,ano,doações)/31 ##janeiro
    elif mês==2 and ano%4==0: return somaQDmes(mês,ano,doações)/29 ### PARA O CASO DO ANO SER BISSEXTO
    elif mês==2: return somaQDmes(mês,ano,doações)/28 ##fevereiro
    elif mês==3: return somaQDmes(mês,ano,doações)/31 ##março
    elif mês==4: return somaQDmes(mês,ano,doações)/30 ##abril
    elif mês==5: return somaQDmes(mês,ano,doações)/31 ##maio
    elif mês==6: return somaQDmes(mês,ano,doações)/30 ##junho
    elif mês==7: return somaQDmes(mês,ano,doações)/31 ##julho
    elif mês==8: return somaQDmes(mês,ano,doações)/31 ##agosto
    elif mês==9: return somaQDmes(mês,ano,doações)/30 ##setembro
    elif mês==10: return somaQDmes(mês,ano,doações)/31 ##outubro
    elif mês==11: return somaQDmes(mês,ano,doações)/30 ##novembro
    elif mês==12: return somaQDmes(mês,ano,doações)/31 ##dezembro


## PROBLEMA 3 - função dias_abaixo(mês,ano,doações)

def dias_abaixo(mês,ano,doações):
    def somaQDdma(dia,mês,ano,doações): return sum([QD for ((CPF,S,I),TS,RH,(d,m,a),QD) in doações if dia==d and mês==m and ano==a]) ##soma da quantidade de sangue por data(dia,mês,ano)
    def dias_abaixo2(mês,ano,doações): return [d for ((CPF,S,I),TS,RH,(d,m,a),QD) in doações if somaQDdma(d,mês,ano,doações)<mediam(mês,ano,doações)] ##dias em que a soma de sangue foi menor que a média mensal 
    return sorted(set(dias_abaixo2(mês,ano,doações))) ##lista dos dias com a função sorted(set()) para não haver repetição de dias













