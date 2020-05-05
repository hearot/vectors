#!/usr/bin/python
# -*- coding: utf-8 -*-

from sympy import symbols
from .units import i, j, k
from .vector import Vector

v_x, v_y, v_z = symbols('v_x, v_y, v_z')
u_x, u_y, u_z = symbols('u_x, u_y, u_z')

v = Vector(v_x, v_y, v_z)
u = Vector(u_x, u_y, u_z)
