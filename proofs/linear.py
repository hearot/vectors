from vectors import u, v
from sympy import symbols

# Thesis: u**v is orthogonal to all the linear combinations of u and v.

w, z = symbols('w, z')

a = u**v
b = w*u + z*v

assert (a*b).expand() == 0
