#!/usr/bin/python
# -*- coding: utf-8 -*-

import sympy as sp


def convert_to_sympy(k):
    if isinstance(k, int):
        return sp.Integer(k)
    elif isinstance(k, float):
        return sp.Float(k)

    return k
