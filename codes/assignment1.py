import sympy as sp
x=sp.symbol('x')
f=sp.(x**2 - 9)/(x-3)
s=sp.limit(f,x,3)
print("the limit is:",s)
