from sympy import Symbol, symbols
import numpy as np
import sympy as sp

i = Symbol('i')
j = Symbol('j')
k = Symbol('k')

class Vector:
    vector = 0
    
    def __init__(self, x=0, y=0, z=0):
        self.vector = x*i + y*j + z*k
        
    def __add__(self, u):
        return Vector.from_symbols(self.vector+u.vector)
        
    def __mul__(self, u):
        if isinstance(u, Vector):
            return self.dot(u)
        else:
            return Vector.from_symbols(u*self.vector)
            
    def __pow__(self, u):
        return self.cross(u)   
        
    def __rmul__(self, u):
        if isinstance(u, Vector):
            return self.dot(u)
        else:
            return Vector.from_symbols(u*self.vector)
    
    def __repr__(self):
        return ("Vector(" + str(self.vector.coeff(i)) +
                ", " + str(self.vector.coeff(j)) +
                ", " + str(self.vector.coeff(k)) +
                ")")
            
    def __str__(self):
        return str(self.vector)
    
    def __sub__(self, u):
        return Vector.from_symbols(self.vector-u.vector)

    def bi_angle(self):
        return sp.atan(sp.Rational(self.vector.coeff(j), self.vector.coeff(i)))

    def cross(self, u):
        matrix = np.array([[i, j, k],
                        [self.vector.coeff(i), self.vector.coeff(j),
                         self.vector.coeff(k)],
                        [u.vector.coeff(i), u.vector.coeff(j),
                         u.vector.coeff(k)]])
        return Vector.from_symbols(sp.Matrix(matrix).det())


    def dot(self, u):
        return (self.vector.coeff(i)*u.vector.coeff(i) +
                self.vector.coeff(j)*u.vector.coeff(j) +
                self.vector.coeff(k)*u.vector.coeff(k))
        
    @staticmethod
    def from_symbols(v):
        v = v.expand()
        return Vector(v.coeff(i), v.coeff(j), v.coeff(k))    

    def module(self):
        return sp.sqrt(self.vector.coeff(i)**2 +
                       self.vector.coeff(j)**2 +
                       self.vector.coeff(k)**2)
        
v_x, v_y, v_z = symbols('v_x, v_y, v_z')
u_x, u_y, u_z = symbols('u_x, u_y, u_z')

v = Vector(v_x, v_y, v_z)
u = Vector(u_x, u_y, u_z)
