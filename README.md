# Arithmetic-Derivative
Python Implementation of the arithmetic derivative for rational numbers.

The arithmetic derivative is defined for integers as:

$$
D: \mathbb{Z} \longrightarrow \mathbb{Z}
$$

with the following properties:

$$
D(0) = D(1) = 0\\
D(p) = 1, p \text{is prime.}\\
D(mn) = D(m)n + mD(n)\\
D(-n) = -D(n)
$$

For rational numbers:

$$
D(m/n) = (D(m)n - mD(n))/n^2
$$
