# Numerical Methods

This repository contains three academic projects developed as part of the **Numerical Methods** course, exploring computational techniques for solving mathematical problems, numerical approximation and error analysis.

The projects cover numerical precision, iterative methods for finding roots of nonlinear equations, and polynomial interpolation techniques.

## Project 1 – Numerical Precision & Series Convergence

**Programming Language:** C

This project explores machine precision, convergence of infinite series and numerical approximation of π.

**Main Topics:**

- **Machine Epsilon:** Determination of machine epsilon for `float`, `double` and `long double` data types.
- **Series Convergence:** Approximation of π using a series of positive terms and analysis of truncation errors.
- **Recursive Formulas:** Implementation of recursive expressions to avoid overflow and improve computational efficiency.
- **Leibniz Series:** Approximation of π using an alternating infinite series.
- **Euler Transformation:** Application of a convergence acceleration technique to improve the efficiency of the Leibniz series.
- **Error Analysis:** Comparison between theoretical error bounds and actual approximation errors.

The results demonstrate how convergence acceleration can significantly reduce the number of terms required to achieve a given precision.

## Project 2 – Numerical Methods for Root Finding

**Programming Language:** Python

This project focuses on iterative methods for approximating roots of nonlinear equations and analyzing their convergence and computational efficiency.

**Main Topics:**

- **Bisection Method:** Implementation of successive interval bisections to approximate equation roots.
- **Newton's Method:** Application of Newton's iterative method, including derivative calculations and error estimation.
- **Fixed-Point Iteration:** Analysis of different iterative formulations and their convergence behavior.
- **Convergence Analysis:** Comparison of iteration counts, approximation errors and convergence rates.
- **Error Estimation:** Evaluation of theoretical error bounds and stopping criteria.

The project compares different numerical approaches and highlights how the choice of iterative formulation and initial approximation affects convergence and efficiency.

## Project 3 – Polynomial Interpolation & Cubic Splines

**Programming Language:** Python

This project explores polynomial interpolation and cubic spline techniques, applying them to a mathematical function and real-world meteorological data.

**Main Topics:**

- **Lagrange Interpolation:** Construction of polynomial interpolators using Lagrange basis polynomials.
- **Newton Interpolation:** Implementation of Newton's divided differences method.
- **Natural Cubic Splines:** Construction of piecewise cubic polynomials by solving a system of linear equations.
- **Interpolation Error:** Analysis of interpolation errors and theoretical error bounds.
- **Runge Phenomenon:** Investigation of oscillations associated with high-degree polynomial interpolation using equally spaced nodes.
- **Real-World Data Modeling:** Application of interpolation methods to model monthly average evaporation recorded over 23 years at a meteorological station in Adelaide.

The results highlight the limitations of global polynomial interpolation and demonstrate the advantages of natural cubic splines when approximating smoothly varying data.

## Technologies & Tools

- C
- Python
- NumPy
- SymPy
- Numerical Analysis
- Mathematical Modeling
- Error Analysis
- Numerical Interpolation

## Repository Structure

- **Project 1:** Numerical precision, series convergence and approximation of π.
- **Project 2:** Iterative methods for solving nonlinear equations.
- **Project 3:** Polynomial interpolation, divided differences and cubic splines.

Each project includes its corresponding academic report. Python source code is provided for Projects 2 and 3.
