from sympy import Symbol, symbols
import sympy as sp

i = Symbol('i')
j = Symbol('j')
k = Symbol('k')

def convert_to_sympy(k):
    if isinstance(k, int):
        return sp.Integer(k)
    elif isinstance(k, float):
        return sp.Float(k)
    
    return k


class Vector:
    vector = 0
    
    def __init__(self, x=0, y=0, z=0):
        x = convert_to_sympy(x)
        y = convert_to_sympy(y)
        z = convert_to_sympy(z)
        
        self.vector = x*i + y*j + z*k
        
    def __add__(self, u):
        return Vector.from_symbols(self.vector+u.vector)
        
    def __mul__(self, u):
        if isinstance(u, Vector):
            return self.dot(u)
        else:
            return Vector.from_symbols(u*self.vector)
        
    def __or__(self, u):
        return sp.acos(self*u/(self.module*u.module))
            
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
    
    def __xor__(self, u):
        return sp.asin((self**u).module/(self.module*u.module))

    @property
    def azimuthal(self):
        return sp.atan2(self.vector.coeff(j), self.vector.coeff(i))

    def cross(self, u):
        return Vector.from_symbols(
            sp.Matrix([[i, j, k],
                       [self.vector.coeff(i), self.vector.coeff(j),
                        self.vector.coeff(k)],
                       [u.vector.coeff(i), u.vector.coeff(j),
                        u.vector.coeff(k)]]).det())

    def dot(self, u):
        return (self.vector.coeff(i)*u.vector.coeff(i) +
                self.vector.coeff(j)*u.vector.coeff(j) +
                self.vector.coeff(k)*u.vector.coeff(k))
        
    @staticmethod
    def from_polar(r, theta, phi):
        r = convert_to_sympy(r)
        theta = convert_to_sympy(theta)
        phi = convert_to_sympy(phi)
        
        return Vector(
            r*sp.sin(theta)*sp.cos(phi),
            r*sp.sin(theta)*sp.sin(phi),
            r*sp.cos(theta)
        )
        
    @staticmethod
    def from_symbols(v):
        v = v.expand()
        return Vector(v.coeff(i), v.coeff(j), v.coeff(k))    

    @property
    def module(self):
        return sp.sqrt(self.vector.coeff(i)**2 +
                       self.vector.coeff(j)**2 +
                       self.vector.coeff(k)**2)
        
    @property
    def polar(self):
        return sp.asin(
            sp.sqrt(self.vector.coeff(i)**2 +
                    self.vector.coeff(j)**2)/self.module)


v_x, v_y, v_z = symbols('v_x, v_y, v_z')
u_x, u_y, u_z = symbols('u_x, u_y, u_z')

v = Vector(v_x, v_y, v_z)
u = Vector(u_x, u_y, u_z)
