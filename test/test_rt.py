# Copyright (c) 2020 Chris Richardson & Matthew Scroggs
# FEniCS Project
# SPDX-License-Identifier: MIT

import numpy
import pytest
import sympy

import basix


def sympy_rt(celltype, n):
    # These basis functions were computed using symfem. They can be recomputed
    # by running (eg):
    #    import symfem
    #    e = symfem.create_element("triangle", "Raviart-Thomas", 2)
    #    print(e.get_basis_functions())
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    z = sympy.Symbol("z")

    if celltype == basix.CellType.triangle:
        if n == 1:
            return [[-x, -y], [x - 1, y], [-x, 1 - y]]
        if n == 2:
            return [[-8*x**2 + 4*x, -8*x*y + 2*y],
                    [-8*x*y + 2*x, -8*y**2 + 4*y],
                    [-8*x**2 - 8*x*y + 12*x + 6*y - 4, -8*x*y - 8*y**2 + 6*y],
                    [8*x*y - 2*x - 6*y + 2, 8*y**2 - 4*y],
                    [8*x**2 + 8*x*y - 6*x, 8*x*y - 6*x + 8*y**2 - 12*y + 4],
                    [-8*x**2 + 4*x, -8*x*y + 6*x + 2*y - 2],
                    [-16*x**2 - 8*x*y + 16*x, -16*x*y - 8*y**2 + 8*y],
                    [-8*x**2 - 16*x*y + 8*x, -8*x*y - 16*y**2 + 16*y]]
        if n == 3:
            return [
                [-45*x**3 + 45*x**2 - 9*x, -45*x**2*y + 30*x*y - 3*y],
                [-45*x*y**2 + 30*x*y - 3*x, -45*y**3 + 45*y**2 - 9*y],
                [-45*x**3/4 - 45*x**2*y + 75*x**2/4 - 45*x*y**2/4 + 45*x*y/2 - 6*x, -45*x**2*y/4 - 45*x*y**2 + 45*x*y/2 - 45*y**3/4 + 75*y**2/4 - 6*y],  # noqa: E501
                [45*x**3 + 90*x**2*y - 90*x**2 + 45*x*y**2 - 120*x*y + 54*x - 30*y**2 + 36*y - 9, 45*x**2*y + 90*x*y**2 - 60*x*y + 45*y**3 - 60*y**2 + 18*y],  # noqa: E501
                [45*x*y**2 - 30*x*y + 3*x - 30*y**2 + 24*y - 3, 45*y**3 - 45*y**2 + 9*y],
                [45*x**3/4 - 45*x**2*y/2 - 15*x**2 - 45*x*y**2/2 + 75*x*y/2 + 9*x/4 + 15*y**2 - 15*y + 3/2, 45*x**2*y/4 - 45*x*y**2/2 - 45*y**3/2 + 105*y**2/4 - 21*y/4],  # noqa: E501
                [-45*x**3 - 90*x**2*y + 60*x**2 - 45*x*y**2 + 60*x*y - 18*x, -45*x**2*y + 30*x**2 - 90*x*y**2 + 120*x*y - 36*x - 45*y**3 + 90*y**2 - 54*y + 9],  # noqa: E501
                [-45*x**3 + 45*x**2 - 9*x, -45*x**2*y + 30*x**2 + 30*x*y - 24*x - 3*y + 3],
                [45*x**3/2 + 45*x**2*y/2 - 105*x**2/4 - 45*x*y**2/4 + 21*x/4, 45*x**2*y/2 - 15*x**2 + 45*x*y**2/2 - 75*x*y/2 + 15*x - 45*y**3/4 + 15*y**2 - 9*y/4 - 3/2],  # noqa: E501
                [270*x**3 + 360*x**2*y - 450*x**2 + 90*x*y**2 - 300*x*y + 180*x, 270*x**2*y + 360*x*y**2 - 300*x*y + 90*y**3 - 150*y**2 + 60*y],  # noqa: E501
                [90*x**3 + 360*x**2*y - 150*x**2 + 270*x*y**2 - 300*x*y + 60*x, 90*x**2*y + 360*x*y**2 - 300*x*y + 270*y**3 - 450*y**2 + 180*y],  # noqa: E501
                [-270*x**3 - 180*x**2*y + 360*x**2 + 60*x*y - 90*x, -270*x**2*y - 180*x*y**2 + 240*x*y + 30*y**2 - 30*y],  # noqa: E501
                [-180*x**3 - 360*x**2*y + 240*x**2 + 120*x*y - 60*x, -180*x**2*y - 360*x*y**2 + 360*x*y + 60*y**2 - 60*y],  # noqa: E501
                [-360*x**2*y + 60*x**2 - 180*x*y**2 + 360*x*y - 60*x, -360*x*y**2 + 120*x*y - 180*y**3 + 240*y**2 - 60*y],  # noqa: E501
                [-180*x**2*y + 30*x**2 - 270*x*y**2 + 240*x*y - 30*x, -180*x*y**2 + 60*x*y - 270*y**3 + 360*y**2 - 90*y]
            ]
    if celltype == basix.CellType.tetrahedron:
        if n == 1:
            return [[2*x, 2*y, 2*z],
                    [2 - 2*x, -2*y, -2*z],
                    [2*x, 2*y - 2, 2*z],
                    [-2*x, -2*y, 2 - 2*z]]
        if n == 2:
            return [
                [30*x**2 - 12*x, 30*x*y - 6*y, 30*x*z - 6*z],
                [30*x*y - 6*x, 30*y**2 - 12*y, 30*y*z - 6*z],
                [30*x*z - 6*x, 30*y*z - 6*y, 30*z**2 - 12*z],
                [30*x**2 + 30*x*y + 30*x*z - 48*x - 24*y - 24*z + 18, 30*x*y + 30*y**2 + 30*y*z - 24*y, 30*x*z + 30*y*z + 30*z**2 - 24*z],  # noqa: E501
                [-30*x*y + 6*x + 24*y - 6, -30*y**2 + 12*y, -30*y*z + 6*z],
                [-30*x*z + 6*x + 24*z - 6, -30*y*z + 6*y, -30*z**2 + 12*z],
                [-30*x**2 - 30*x*y - 30*x*z + 24*x, -30*x*y + 24*x - 30*y**2 - 30*y*z + 48*y + 24*z - 18, -30*x*z - 30*y*z - 30*z**2 + 24*z],  # noqa: E501
                [30*x**2 - 12*x, 30*x*y - 24*x - 6*y + 6, 30*x*z - 6*z],
                [30*x*z - 6*x, 30*y*z - 6*y - 24*z + 6, 30*z**2 - 12*z],
                [30*x**2 + 30*x*y + 30*x*z - 24*x, 30*x*y + 30*y**2 + 30*y*z - 24*y, 30*x*z - 24*x + 30*y*z - 24*y + 30*z**2 - 48*z + 18],  # noqa: E501
                [-30*x**2 + 12*x, -30*x*y + 6*y, -30*x*z + 24*x + 6*z - 6],
                [-30*x*y + 6*x, -30*y**2 + 12*y, -30*y*z + 24*y + 6*z - 6],
                [-60*x**2 - 30*x*y - 30*x*z + 60*x, -60*x*y - 30*y**2 - 30*y*z + 30*y, -60*x*z - 30*y*z - 30*z**2 + 30*z],  # noqa: E501
                [-30*x**2 - 60*x*y - 30*x*z + 30*x, -30*x*y - 60*y**2 - 30*y*z + 60*y, -30*x*z - 60*y*z - 30*z**2 + 30*z],  # noqa: E501
                [-30*x**2 - 30*x*y - 60*x*z + 30*x, -30*x*y - 30*y**2 - 60*y*z + 30*y, -30*x*z - 30*y*z - 60*z**2 + 60*z]  # noqa: E501
            ]
        if n == 3:
            return [
                [252*x**3 - 216*x**2 + 36*x, 252*x**2*y - 144*x*y + 12*y, 252*x**2*z - 144*x*z + 12*z],
                [252*x*y**2 - 144*x*y + 12*x, 252*y**3 - 216*y**2 + 36*y, 252*y**2*z - 144*y*z + 12*z],
                [252*x*z**2 - 144*x*z + 12*x, 252*y*z**2 - 144*y*z + 12*y, 252*z**3 - 216*z**2 + 36*z],
                [63*x*y**2 + 252*x*y*z - 72*x*y + 63*x*z**2 - 72*x*z + 12*x, 63*y**3 + 252*y**2*z - 90*y**2 + 63*y*z**2 - 108*y*z + 24*y, 63*y**2*z + 252*y*z**2 - 108*y*z + 63*z**3 - 90*z**2 + 24*z],  # noqa: E501
                [63*x**3 + 252*x**2*z - 90*x**2 + 63*x*z**2 - 108*x*z + 24*x, 63*x**2*y + 252*x*y*z - 72*x*y + 63*y*z**2 - 72*y*z + 12*y, 63*x**2*z + 252*x*z**2 - 108*x*z + 63*z**3 - 90*z**2 + 24*z],  # noqa: E501
                [63*x**3 + 252*x**2*y - 90*x**2 + 63*x*y**2 - 108*x*y + 24*x, 63*x**2*y + 252*x*y**2 - 108*x*y + 63*y**3 - 90*y**2 + 24*y, 63*x**2*z + 252*x*y*z - 72*x*z + 63*y**2*z - 72*y*z + 12*z],  # noqa: E501
                [-252*x**3 - 504*x**2*y - 504*x**2*z + 540*x**2 - 252*x*y**2 - 504*x*y*z + 720*x*y - 252*x*z**2 + 720*x*z - 360*x + 180*y**2 + 360*y*z - 240*y + 180*z**2 - 240*z + 72, -252*x**2*y - 504*x*y**2 - 504*x*y*z + 360*x*y - 252*y**3 - 504*y**2*z + 360*y**2 - 252*y*z**2 + 360*y*z - 120*y, -252*x**2*z - 504*x*y*z - 504*x*z**2 + 360*x*z - 252*y**2*z - 504*y*z**2 + 360*y*z - 252*z**3 + 360*z**2 - 120*z],  # noqa: E501
                [-252*x*y**2 + 144*x*y - 12*x + 180*y**2 - 120*y + 12, -252*y**3 + 216*y**2 - 36*y, -252*y**2*z + 144*y*z - 12*z],  # noqa: E501
                [-252*x*z**2 + 144*x*z - 12*x + 180*z**2 - 120*z + 12, -252*y*z**2 + 144*y*z - 12*y, -252*z**3 + 216*z**2 - 36*z],  # noqa: E501
                [-63*x*y**2 - 252*x*y*z + 72*x*y - 63*x*z**2 + 72*x*z - 12*x + 45*y**2 + 180*y*z - 60*y + 45*z**2 - 60*z + 12, -63*y**3 - 252*y**2*z + 90*y**2 - 63*y*z**2 + 108*y*z - 24*y, -63*y**2*z - 252*y*z**2 + 108*y*z - 63*z**3 + 90*z**2 - 24*z],  # noqa: E501
                [-63*x**3 - 126*x**2*y + 126*x**2*z + 99*x**2 - 63*x*y**2 + 126*x*y*z + 144*x*y + 126*x*z**2 - 216*x*z - 33*x + 45*y**2 - 90*y*z - 30*y - 90*z**2 + 90*z - 3, -63*x**2*y - 126*x*y**2 + 126*x*y*z + 54*x*y - 63*y**3 + 126*y**2*z + 54*y**2 + 126*y*z**2 - 126*y*z - 3*y, -63*x**2*z - 126*x*y*z + 126*x*z**2 + 18*x*z - 63*y**2*z + 126*y*z**2 + 18*y*z + 126*z**3 - 144*z**2 + 21*z],  # noqa: E501
                [-63*x**3 + 126*x**2*y - 126*x**2*z + 99*x**2 + 126*x*y**2 + 126*x*y*z - 216*x*y - 63*x*z**2 + 144*x*z - 33*x - 90*y**2 - 90*y*z + 90*y + 45*z**2 - 30*z - 3, -63*x**2*y + 126*x*y**2 - 126*x*y*z + 18*x*y + 126*y**3 + 126*y**2*z - 144*y**2 - 63*y*z**2 + 18*y*z + 21*y, -63*x**2*z + 126*x*y*z - 126*x*z**2 + 54*x*z + 126*y**2*z + 126*y*z**2 - 126*y*z - 63*z**3 + 54*z**2 - 3*z],  # noqa: E501
                [252*x**3 + 504*x**2*y + 504*x**2*z - 360*x**2 + 252*x*y**2 + 504*x*y*z - 360*x*y + 252*x*z**2 - 360*x*z + 120*x, 252*x**2*y - 180*x**2 + 504*x*y**2 + 504*x*y*z - 720*x*y - 360*x*z + 240*x + 252*y**3 + 504*y**2*z - 540*y**2 + 252*y*z**2 - 720*y*z + 360*y - 180*z**2 + 240*z - 72, 252*x**2*z + 504*x*y*z + 504*x*z**2 - 360*x*z + 252*y**2*z + 504*y*z**2 - 360*y*z + 252*z**3 - 360*z**2 + 120*z],  # noqa: E501
                [252*x**3 - 216*x**2 + 36*x, 252*x**2*y - 180*x**2 - 144*x*y + 120*x + 12*y - 12, 252*x**2*z - 144*x*z + 12*z],  # noqa: E501
                [252*x*z**2 - 144*x*z + 12*x, 252*y*z**2 - 144*y*z + 12*y - 180*z**2 + 120*z - 12, 252*z**3 - 216*z**2 + 36*z],  # noqa: E501
                [63*x**3 + 252*x**2*z - 90*x**2 + 63*x*z**2 - 108*x*z + 24*x, 63*x**2*y - 45*x**2 + 252*x*y*z - 72*x*y - 180*x*z + 60*x + 63*y*z**2 - 72*y*z + 12*y - 45*z**2 + 60*z - 12, 63*x**2*z + 252*x*z**2 - 108*x*z + 63*z**3 - 90*z**2 + 24*z],  # noqa: E501
                [63*x**3 + 126*x**2*y - 126*x**2*z - 54*x**2 + 63*x*y**2 - 126*x*y*z - 54*x*y - 126*x*z**2 + 126*x*z + 3*x, 63*x**2*y - 45*x**2 + 126*x*y**2 - 126*x*y*z - 144*x*y + 90*x*z + 30*x + 63*y**3 - 126*y**2*z - 99*y**2 - 126*y*z**2 + 216*y*z + 33*y + 90*z**2 - 90*z + 3, 63*x**2*z + 126*x*y*z - 126*x*z**2 - 18*x*z + 63*y**2*z - 126*y*z**2 - 18*y*z - 126*z**3 + 144*z**2 - 21*z],  # noqa: E501
                [-126*x**3 - 126*x**2*y - 126*x**2*z + 144*x**2 + 63*x*y**2 + 126*x*y*z - 18*x*y + 63*x*z**2 - 18*x*z - 21*x, -126*x**2*y + 90*x**2 - 126*x*y**2 - 126*x*y*z + 216*x*y + 90*x*z - 90*x + 63*y**3 + 126*y**2*z - 99*y**2 + 63*y*z**2 - 144*y*z + 33*y - 45*z**2 + 30*z + 3, -126*x**2*z - 126*x*y*z - 126*x*z**2 + 126*x*z + 63*y**2*z + 126*y*z**2 - 54*y*z + 63*z**3 - 54*z**2 + 3*z],  # noqa: E501
                [-252*x**3 - 504*x**2*y - 504*x**2*z + 360*x**2 - 252*x*y**2 - 504*x*y*z + 360*x*y - 252*x*z**2 + 360*x*z - 120*x, -252*x**2*y - 504*x*y**2 - 504*x*y*z + 360*x*y - 252*y**3 - 504*y**2*z + 360*y**2 - 252*y*z**2 + 360*y*z - 120*y, -252*x**2*z + 180*x**2 - 504*x*y*z + 360*x*y - 504*x*z**2 + 720*x*z - 240*x - 252*y**2*z + 180*y**2 - 504*y*z**2 + 720*y*z - 240*y - 252*z**3 + 540*z**2 - 360*z + 72],  # noqa: E501
                [-252*x**3 + 216*x**2 - 36*x, -252*x**2*y + 144*x*y - 12*y, -252*x**2*z + 180*x**2 + 144*x*z - 120*x - 12*z + 12],  # noqa: E501
                [-252*x*y**2 + 144*x*y - 12*x, -252*y**3 + 216*y**2 - 36*y, -252*y**2*z + 180*y**2 + 144*y*z - 120*y - 12*z + 12],  # noqa: E501
                [-63*x**3 - 252*x**2*y + 90*x**2 - 63*x*y**2 + 108*x*y - 24*x, -63*x**2*y - 252*x*y**2 + 108*x*y - 63*y**3 + 90*y**2 - 24*y, -63*x**2*z + 45*x**2 - 252*x*y*z + 180*x*y + 72*x*z - 60*x - 63*y**2*z + 45*y**2 + 72*y*z - 60*y - 12*z + 12],  # noqa: E501
                [-63*x**3 + 126*x**2*y - 126*x**2*z + 54*x**2 + 126*x*y**2 + 126*x*y*z - 126*x*y - 63*x*z**2 + 54*x*z - 3*x, -63*x**2*y + 126*x*y**2 - 126*x*y*z + 18*x*y + 126*y**3 + 126*y**2*z - 144*y**2 - 63*y*z**2 + 18*y*z + 21*y, -63*x**2*z + 45*x**2 + 126*x*y*z - 90*x*y - 126*x*z**2 + 144*x*z - 30*x + 126*y**2*z - 90*y**2 + 126*y*z**2 - 216*y*z + 90*y - 63*z**3 + 99*z**2 - 33*z - 3],  # noqa: E501
                [126*x**3 + 126*x**2*y + 126*x**2*z - 144*x**2 - 63*x*y**2 - 126*x*y*z + 18*x*y - 63*x*z**2 + 18*x*z + 21*x, 126*x**2*y + 126*x*y**2 + 126*x*y*z - 126*x*y - 63*y**3 - 126*y**2*z + 54*y**2 - 63*y*z**2 + 54*y*z - 3*y, 126*x**2*z - 90*x**2 + 126*x*y*z - 90*x*y + 126*x*z**2 - 216*x*z + 90*x - 63*y**2*z + 45*y**2 - 126*y*z**2 + 144*y*z - 30*y - 63*z**3 + 99*z**2 - 33*z - 3],  # noqa: E501
                [1512*x**3 + 2016*x**2*y + 2016*x**2*z - 2592*x**2 + 504*x*y**2 + 1008*x*y*z - 1728*x*y + 504*x*z**2 - 1728*x*z + 1080*x, 1512*x**2*y + 2016*x*y**2 + 2016*x*y*z - 1728*x*y + 504*y**3 + 1008*y**2*z - 864*y**2 + 504*y*z**2 - 864*y*z + 360*y, 1512*x**2*z + 2016*x*y*z + 2016*x*z**2 - 1728*x*z + 504*y**2*z + 1008*y*z**2 - 864*y*z + 504*z**3 - 864*z**2 + 360*z],  # noqa: E501
                [504*x**3 + 2016*x**2*y + 1008*x**2*z - 864*x**2 + 1512*x*y**2 + 2016*x*y*z - 1728*x*y + 504*x*z**2 - 864*x*z + 360*x, 504*x**2*y + 2016*x*y**2 + 1008*x*y*z - 1728*x*y + 1512*y**3 + 2016*y**2*z - 2592*y**2 + 504*y*z**2 - 1728*y*z + 1080*y, 504*x**2*z + 2016*x*y*z + 1008*x*z**2 - 864*x*z + 1512*y**2*z + 2016*y*z**2 - 1728*y*z + 504*z**3 - 864*z**2 + 360*z],  # noqa: E501
                [504*x**3 + 1008*x**2*y + 2016*x**2*z - 864*x**2 + 504*x*y**2 + 2016*x*y*z - 864*x*y + 1512*x*z**2 - 1728*x*z + 360*x, 504*x**2*y + 1008*x*y**2 + 2016*x*y*z - 864*x*y + 504*y**3 + 2016*y**2*z - 864*y**2 + 1512*y*z**2 - 1728*y*z + 360*y, 504*x**2*z + 1008*x*y*z + 2016*x*z**2 - 1728*x*z + 504*y**2*z + 2016*y*z**2 - 1728*y*z + 1512*z**3 - 2592*z**2 + 1080*z],  # noqa: E501
                [-1512*x**3 - 1008*x**2*y - 1008*x**2*z + 1944*x**2 + 288*x*y + 288*x*z - 432*x, -1512*x**2*y - 1008*x*y**2 - 1008*x*y*z + 1296*x*y + 144*y**2 + 144*y*z - 144*y, -1512*x**2*z - 1008*x*y*z - 1008*x*z**2 + 1296*x*z + 144*y*z + 144*z**2 - 144*z],  # noqa: E501
                [-1008*x**3 - 2016*x**2*y - 1008*x**2*z + 1296*x**2 + 576*x*y + 288*x*z - 288*x, -1008*x**2*y - 2016*x*y**2 - 1008*x*y*z + 2016*x*y + 288*y**2 + 144*y*z - 288*y, -1008*x**2*z - 2016*x*y*z - 1008*x*z**2 + 1152*x*z + 288*y*z + 144*z**2 - 144*z],  # noqa: E501
                [-1008*x**3 - 1008*x**2*y - 2016*x**2*z + 1296*x**2 + 288*x*y + 576*x*z - 288*x, -1008*x**2*y - 1008*x*y**2 - 2016*x*y*z + 1152*x*y + 144*y**2 + 288*y*z - 144*y, -1008*x**2*z - 1008*x*y*z - 2016*x*z**2 + 2016*x*z + 144*y*z + 288*z**2 - 288*z],  # noqa: E501
                [-2016*x**2*y + 288*x**2 - 1008*x*y**2 - 1008*x*y*z + 2016*x*y + 144*x*z - 288*x, -2016*x*y**2 + 576*x*y - 1008*y**3 - 1008*y**2*z + 1296*y**2 + 288*y*z - 288*y, -2016*x*y*z + 288*x*z - 1008*y**2*z - 1008*y*z**2 + 1152*y*z + 144*z**2 - 144*z],  # noqa: E501
                [-1008*x**2*y + 144*x**2 - 1512*x*y**2 - 1008*x*y*z + 1296*x*y + 144*x*z - 144*x, -1008*x*y**2 + 288*x*y - 1512*y**3 - 1008*y**2*z + 1944*y**2 + 288*y*z - 432*y, -1008*x*y*z + 144*x*z - 1512*y**2*z - 1008*y*z**2 + 1296*y*z + 144*z**2 - 144*z],  # noqa: E501
                [-1008*x**2*y + 144*x**2 - 1008*x*y**2 - 2016*x*y*z + 1152*x*y + 288*x*z - 144*x, -1008*x*y**2 + 288*x*y - 1008*y**3 - 2016*y**2*z + 1296*y**2 + 576*y*z - 288*y, -1008*x*y*z + 144*x*z - 1008*y**2*z - 2016*y*z**2 + 2016*y*z + 288*z**2 - 288*z],  # noqa: E501
                [-2016*x**2*z + 288*x**2 - 1008*x*y*z + 144*x*y - 1008*x*z**2 + 2016*x*z - 288*x, -2016*x*y*z + 288*x*y - 1008*y**2*z + 144*y**2 - 1008*y*z**2 + 1152*y*z - 144*y, -2016*x*z**2 + 576*x*z - 1008*y*z**2 + 288*y*z - 1008*z**3 + 1296*z**2 - 288*z],  # noqa: E501
                [-1008*x**2*z + 144*x**2 - 2016*x*y*z + 288*x*y - 1008*x*z**2 + 1152*x*z - 144*x, -1008*x*y*z + 144*x*y - 2016*y**2*z + 288*y**2 - 1008*y*z**2 + 2016*y*z - 288*y, -1008*x*z**2 + 288*x*z - 2016*y*z**2 + 576*y*z - 1008*z**3 + 1296*z**2 - 288*z],  # noqa: E501
                [-1008*x**2*z + 144*x**2 - 1008*x*y*z + 144*x*y - 1512*x*z**2 + 1296*x*z - 144*x, -1008*x*y*z + 144*x*y - 1008*y**2*z + 144*y**2 - 1512*y*z**2 + 1296*y*z - 144*y, -1008*x*z**2 + 288*x*z - 1008*y*z**2 + 288*y*z - 1512*z**3 + 1944*z**2 - 432*z]  # noqa: E501
            ]
    raise NotImplementedError


@pytest.mark.parametrize("degree", [1, 2, 3])
def test_tri(degree):
    celltype = basix.CellType.triangle
    g = sympy_rt(celltype, degree)
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    rt = basix.create_element(basix.ElementFamily.RT, basix.CellType.triangle, degree, basix.LagrangeVariant.equispaced)
    pts = basix.create_lattice(celltype, 1, basix.LatticeType.equispaced, True)
    nderiv = 3
    wtab = rt.tabulate(nderiv, pts)

    for kx in range(nderiv + 1):
        for ky in range(nderiv + 1 - kx):
            wsym = numpy.zeros_like(wtab[0])
            for i, gi in enumerate(g):
                for j, gij in enumerate(gi):
                    wd = sympy.diff(gij, x, kx, y, ky)
                    for k, p in enumerate(pts):
                        wsym[k, i, j] = wd.subs([(x, p[0]), (y, p[1])])

            assert numpy.isclose(wtab[basix.index(kx, ky)], wsym).all()


@pytest.mark.parametrize("degree", [1, 2, 3])
def test_tet(degree):
    celltype = basix.CellType.tetrahedron
    g = sympy_rt(celltype, degree)
    x = sympy.Symbol("x")
    y = sympy.Symbol("y")
    z = sympy.Symbol("z")
    rt = basix.create_element(
        basix.ElementFamily.RT, basix.CellType.tetrahedron, degree, basix.LagrangeVariant.equispaced)

    pts = basix.create_lattice(celltype, 5, basix.LatticeType.equispaced, True)
    nderiv = 1
    wtab = rt.tabulate(nderiv, pts)

    for kx in range(nderiv + 1):
        for ky in range(nderiv + 1 - kx):
            for kz in range(nderiv + 1 - kx - ky):
                wsym = numpy.zeros_like(wtab[0])
                for i, gi in enumerate(g):
                    for j, gij in enumerate(gi):
                        wd = sympy.diff(gij, x, kx, y, ky, z, kz)
                        for k, p in enumerate(pts):
                            wsym[k, i, j] = wd.subs([(x, p[0]), (y, p[1]), (z, p[2])])

                assert numpy.isclose(wtab[basix.index(kx, ky, kz)], wsym).all()
