#P01. Escreva uma definição recursiva para a função norep(xs), cuja avaliação associe 
# uma lista similar a xs porém sem nenhum elemento repetido.

def norep(xs):
    l = []
    for i in xs:
        if i not in l:
            l.append(i)
    l.sort()
    return l


# P02. Defina a função permuta(xs,ys) cuja avaliação resulta True 
# se xs e ys tem os mesmos elementos, os quais ocorrem o mesmo número de vezes em cada uma. 
# Por exemplo:
# >>> permuta([1,4,1,5],[5,4,1,1])
# True

def permuta(xs,ys):
    if sorted(set(xs))==sorted(set(ys)): return True
    else: return False

# P03. Defina a função codigo(xs,ys) onde ys é uma frase e xs é uma lista 
# de pares (pin,pout) onde pin e pout são palavras. A avaliação de codigo(xs,ys) 
# produz uma frase similar a ys onde todas as palavras pin foram substituídas pelas respectivas pout. 
# Por exemplo:
# >>> codigo( [(“dia”,“jogo”),(“vida”,“tabela”)] , “dia após dia a vida muda”)
# “jogo após jogo a tabela muda”

def codigo(xs,ys):
	a=[pin for (pin,pout) in xs]
	b=[pout for (pin,pout) in xs]
	c= a[0]
	d= a[1]
	e= b[0]
	f= b[1]
	ys2= ys.replace(c,e)
	return ys2.replace(d,f)

    
