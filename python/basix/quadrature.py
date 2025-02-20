"""Functions to manipulate quadrature types."""

import typing as _typing

import numpy as _np
import numpy.typing as _npt

from basix._basixcpp import QuadratureType as _QT
from basix._basixcpp import make_quadrature as _mq
from basix.cell import CellType
from basix.polynomials import PolysetType
from basix.utils import Enum

__all__ = ["string_to_type", "make_quadrature"]


class QuadratureType(Enum):
    """Quadrature type."""
    Default = _QT.Default
    gauss_jacobi = _QT.gauss_jacobi
    gll = _QT.gll
    xiao_gimbutas = _QT.xiao_gimbutas


def string_to_type(rule: str) -> QuadratureType:
    """Convert a string to a Basix QuadratureType enum.

    Args:
        rule: Qquadrature rule as a string.

    Returns:
        The quadrature type.

    """
    if rule == "default":
        return QuadratureType.Default

    if rule in ["Gauss-Lobatto-Legendre", "GLL"]:
        return QuadratureType.gll
    if rule in ["Gauss-Legendre", "GL", "Gauss-Jacobi"]:
        return QuadratureType.gauss_jacobi
    if rule == "Xiao-Gimbutas":
        return QuadratureType.xiao_gimbutas

    if not hasattr(QuadratureType, rule):
        raise ValueError(f"Unknown quadrature rule: {rule}")
    return getattr(QuadratureType, rule)


def make_quadrature(
    cell: CellType, degree: int, rule: QuadratureType = QuadratureType.Default,
    polyset_type: PolysetType = PolysetType.standard
) -> _typing.Tuple[_npt.NDArray[_np.float64], _npt.NDArray[_np.float64]]:
    """Create a quadrature rule.

    Args:
        cell: Cell type
        degree: Maximum polynomial degree that will be integrated
            exactly.
        rule: Quadrature rule.
        polyset_type: Type of polynomial that will be integrated
            exactly.

    Returns:
        The quadrature points and weights.

    """
    return _mq(rule.value, cell.value, polyset_type.value, degree)
