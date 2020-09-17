// Copyright (c) 2020 Chris Richardson
// FEniCS Project
// SPDX-License-Identifier:    MIT

#include "finite-element.h"

//-----------------------------------------------------------------------------
FiniteElement::FiniteElement(int dim, int degree) : _dim(dim), _degree(degree)
{
  // Do nothing in base class
}
//-----------------------------------------------------------------------------
Eigen::Array<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>
FiniteElement::tabulate_basis(
    const Eigen::Array<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>&
        pts) const
{
  if (pts.cols() != _dim)
    throw std::runtime_error(
        "Point dimension does not match element dimension");

  Eigen::Array<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> result(
      pts.rows(), poly_set.size());
  for (std::size_t j = 0; j < poly_set.size(); ++j)
    result.col(j) = poly_set[j].tabulate(pts);

  return result;
}
//-----------------------------------------------------------------------------
void FiniteElement::apply_dualmat_to_basis(
    const Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic,
                        Eigen::RowMajor>& coeffs,
    const Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic,
                        Eigen::RowMajor>& dualmat,
    const std::vector<Polynomial>& basis, int ndim)
{
  auto A = coeffs * dualmat.transpose();

  Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>
      new_coeffs(coeffs.rows(), coeffs.cols());

  // auto Ainv = A.inverse();
  // new_coeffs = Ainv * coeffs;
  // faster to use solve()
  new_coeffs = A.colPivHouseholderQr().solve(coeffs);

#ifndef NDEBUG
  std::cout << "Initial coeffs = \n[" << coeffs << "]\n";
  std::cout << "Dual matrix = \n[" << dualmat << "]\n";
  std::cout << "New coeffs = \n[" << new_coeffs << "]\n";
#endif

  int psize = basis.size();
  int ndofs = dualmat.rows();

  // Create polynomial sets for x, y (and z) components
  // stacking x0, x1, x2,... y0, y1, y2,... z0, z1, z2...
  poly_set.resize(ndofs * ndim, Polynomial::zero());
  for (int j = 0; j < ndim; ++j)
    for (int i = 0; i < ndofs; ++i)
      for (int k = 0; k < psize; ++k)
        poly_set[i + ndofs * j] += basis[k] * new_coeffs(i, k + psize * j);
}
//-----------------------------------------------------------------------------
