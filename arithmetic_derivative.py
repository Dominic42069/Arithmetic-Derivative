from numbers import Number
from numpy import sqrt
from sqlalchemy import Float

class PrimeFactoredInteger:
    def primefactorise(self):
        n = self.abs_n
        if n == 0:
            return [(0, 1)]
        primes = []
        powers = []
        while n % 2 == 0:
            primes.append(2)
            n /= 2
        for k in range(3, self.abs_n+1, 2):
            while n % k == 0:
                primes.append(k)
                n /= k
        for i in set(primes):
            powers.append(primes.count(i))
        primes = list(set(primes))
        factorisation = list(zip(primes, powers))
        return factorisation

    def __init__(self, n):
        if isinstance(n, Number):
            if n < 0:
                self.minus = True
                self.abs_n = -n
            else:
                self.abs_n = n
                self.minus = False
            self.factorisation = self.primefactorise()
        else:
            self.factorisation = n
            self.minus = False
            self.abs_n = self.evaluate()

    def evaluate(self):
        val = 0
        for factor in self.factorisation:
            val += factor[0]**factor[1]
        return val

    def __repr__(self):
        output = ""
        if self.minus:
            output += "-"
        for factor in self.factorisation:
            if factor[1] == 1:
                output += f"{factor[0]} * "
            else:
                output += f"{factor[0]}^{factor[1]} * "
        output = output[:-3]
        return output

    def __mul__(self, other):
        return self.abs_n*other

    def __rmul__(self, other):
        return other*self.abs_n

    def __pow__(self, other):
        return self.abs_n**other


class IntegerWithDerivative(PrimeFactoredInteger):
    def __init__(self, n):
        super().__init__(n)

    def derivative(self):
        if self.minus:
            m = IntegerWithDerivative(self.abs_n)
            return -m.derivative()
        elif self.abs_n == 0 or self.abs_n == 1:
            return 0
        else:
            end_factor = self.factorisation.pop()
            if not self.factorisation:
                return end_factor[1]*end_factor[0]**(end_factor[1]-1)
            else:
                nfac = list()
                nfac.append(end_factor)
                n = IntegerWithDerivative(nfac)
                m = IntegerWithDerivative(self.factorisation)
                return m.derivative()*n + m*n.derivative()


class RationalWithDerivative(IntegerWithDerivative):
    def __init__(self, n):
        self.num, self.den = n.as_integer_ratio()
        self.num = IntegerWithDerivative(self.num)
        self.den = IntegerWithDerivative(self.den)

    def derivative(self):
        return (self.num.derivative()*self.den - self.num*self.den.derivative())/((self.den)**2)
