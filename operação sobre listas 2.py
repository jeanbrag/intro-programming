# 1) Dado uma lista de triplas contendo o número de matrícula, a nota final (0-10) 
# e a frequência (0-100) de alunos de certa disciplina, defina a função rfinal(nfs) 
# cuja avaliação associe uma tupla formada por 4 listas onde: a primeira lista contém 
# as tuplas com alunos aprovados, a segunda com alunos reprovados por nota, a terceira 
# com alunos reprovados por falta, a quarta com alunos reprovados por nota e por falta.


nfs=[(1,5.9,77),(45,4.8,100),(22,3.4,70),(103,8.8,40),(334,1.2,34),(7,9.9,100),(87,5.9,45)]

def reprovad2(nfs):
    return [(matricula) for (matricula,nf,freq) in nfs if nf<5 and freq<75]

def aprovado(nfs):
    return [(matricula) for (matricula,nf,freq) in nfs if nf>=5 and freq>=75]

def reprovadnf(nfs):
    return [(matricula) for (matricula,nf,freq) in nfs if nf<5 and freq>=75]

def reprovadfreq(nfs):
    return [(matricula) for (matricula,nf,freq) in nfs if nf>=5 and freq<75]

def rfinal(nfs):
    return [aprovado(nfs),reprovadnf(nfs),reprovadfreq(nfs),reprovad2(nfs)]

# 2) Usando a definição de listas por compreensão, defina a função sem argumentos domino()
# cuja avaliação associe uma lista com duplas que representam as 28 pedras do dominó.

def domino():
    return[(a,b) for a in range(7) for b in range(7)if a<=b]

