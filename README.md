# Arithmetic-Derivative
Python Implementation of the arithmetic derivative for rational numbers.

The arithmetic derivative is defined for integers as:

$$
D: \hspace{0.5em} \mathbb{Z} \longrightarrow \mathbb{Z}
$$

with the following properties:

$$
D(0) \hspace{0.5em} = \hspace{0.5em}D(1) \hspace{0.5em} = \hspace{0.5em} 0
$$
$$
D(p) \hspace{0.5em} = \hspace{0.5em} 1, \hspace{0.5em} p \hspace{0.5em} \text{is prime.}\newline
D(mn) \hspace{0.5em} = \hspace{0.5em} D(m)n \hspace{0.5em} + \hspace{0.5em} mD(n)\newline
D(-n) \hspace{0.5em} = \hspace{0.5em} -D(n)
$$

For rational numbers:

$$
D(m/n) \hspace{0.5em} = \hspace{0.5em} (D(m)n - mD(n))/n^2
$$
