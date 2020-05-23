doacao=[(("001.002.003-04",'F', 18),"O","+",("01","01","2017"),500),(("002.003.004-05",'M',19),"O","-",("01","02","2017"),250),(("003.004.005-06", 'F',20),"A","+",
("02","01","2017"),500),(("004.005.006-07",'M',21),"A","-",("02","01","2017"),250),(("005.006.007-08",'F',22),"AB","+",("03","01","2017"),500),
(("006.007.008-09",'M',23),"AB","-",("03","01","2017"),250)]

def estoque(doacao):
    if (doacao==[]):
        return []
    else:
        qtde = [e for (a,b,c,d,e) in doacao if(b=="O" and c=="+")]
        qtde2 = [e for (a,b,c,d,e) in doacao if(b=="O" and c=="-")]
        qtde3 = [e for (a,b,c,d,e) in doacao if(b=="A" and c=="+")]
        qtde4 = [e for (a,b,c,d,e) in doacao if(b=="A" and c=="-")]
        qtde5 = [e for (a,b,c,d,e) in doacao if(b=="B" and c=="+")]
        qtde6 = [e for (a,b,c,d,e) in doacao if(b=="B" and c=="-")]
        qtde7 = [e for (a,b,c,d,e) in doacao if(b=="AB" and c=="+")]
        qtde8 = [e for (a,b,c,d,e) in doacao if(b=="AB" and c=="-")]
        return (("O", "+", sum(qtde)), ("O","-",sum(qtde2)),("A","+",sum(qtde3)),("A","-",sum(qtde4)),("B","+",sum(qtde5)),("B","-",sum(qtde6)),("AB","+",sum(qtde7)),("AB","-",sum(qtde8)) )

def mediam(mes,ano,doacao):
    result = [e for (a,b,c,d,e) in doacao if d[1]==mes and d[2]==ano]
    quant= len([e for (a,b,c,d,e) in doacao if d[1]==mes and d[2]==ano])
    return sum(result)/quant

def dias_abaixo(mes,ano,doacao):
    result = [e for (a,b,c,d,e) in doacao if d[1]==mes and d[2]==ano]
    quant= len([e for (a,b,c,d,e) in doacao if d[1]==mes and d[2]==ano])
    total=sum(result)/quant
    dias = [d[0] for (a,b,c,d,e) in doacao if d[1]==mes and d[2]==ano and e<total]
    return dias
