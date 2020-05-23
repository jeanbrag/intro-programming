lista=[1,2,3,4,5,6,7,8,9,10]

# Lista com os k primeiros elementos de uma lista xs
def take(k,xs): return xs[0:k]

# Lista com os elementos de xs seguintes aos k primeiros
def drop(k,xs): return xs[k:]

# Primeiro elemento de uma lista xs
def head(xs): return xs[0]

# Sublista similar a xs mas sem o primeiro elemento
def tail(xs): return xs[1:]

# Ultimo elemento de uma lista xs
def last(xs): return xs[-1]

# Sublista similar a xs mas sem o ultimo elemento
def init(xs): return xs - xs[-1]






