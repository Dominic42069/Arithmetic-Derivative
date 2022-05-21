# Arithmetic-Derivative
Python Implementation of the arithmetic derivative for rational numbers.

The arithmetic derivative is defined for integers as:

$$
D: \hspace{0.5em} \mathbb{Z} \hspace{0.25em} \longrightarrow \hspace{0.25em} \mathbb{Z}
$$

with the following properties:

$$
D(0) \hspace{0.5em} = \hspace{0.5em} D(1) \hspace{0.5em} = \hspace{0.5em} 0
$$

$$
D(p) \hspace{0.5em} = \hspace{0.5em} 1, \hspace{0.5em} p \hspace{0.5em} \text{is prime.}
$$

$$
D(mn) \hspace{0.5em} = \hspace{0.5em} D(m)n \hspace{0.5em} + \hspace{0.5em} mD(n)
$$

$$
D(-n) \hspace{0.5em} = \hspace{0.5em} -D(n)
$$

For rational numbers:

$$
D \left(\frac{m}{n}\right) \hspace{0.5em} = \hspace{0.5em} \frac{D(m)n - mD(n)}{n^2}
$$
