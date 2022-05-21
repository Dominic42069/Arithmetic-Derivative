# Arithmetic-Derivative
Python Implementation of the arithmetic derivative for rational numbers.

The arithmetic derivative is defined for integers as:

$$
D: \hspace{1em} \mathbb{Z} \longrightarrow \mathbb{Z}
$$

with the following properties:

$$
D(0) \hspace{1em} = \hspace{1em}D(1) \hspace{1em} = \hspace{1em} 0\newline
D(p) \hspace{1em} = \hspace{1em} 1, \hspace{1em} p \hspace{1em} \text{is prime.}\newline
D(mn) \hspace{1em} = \hspace{1em} D(m)n \hspace{1em} + \hspace{1em} mD(n)\newwline
D(-n) \hspace{1em} = \hspace{1em} -D(n)
$$

For rational numbers:

$$
D(m/n) \hspace{1em} = \hspace{1em} (D(m)n - mD(n))/n^2
$$
