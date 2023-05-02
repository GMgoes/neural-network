import numpy
from math import exp
from matplotlib import pyplot


class Neuronio:
    def __init__(self, entradas):
        self.n = entradas + 1
        self.w = numpy.random.rand(entradas + 1)

    def forward(self, listaX):
        x = listaX.copy()
        x.append(1)
        y = sum(self.w * x)
        o = 1 / (1 + exp(-y))
        d = o * (1 - o)
        self.x, self.o, self.d = x, o, d
        return o, d

    def backward(self, erro):
        backerror = [erro * self.d * w for w in self.w]
        for i in range(self.n):
            self.w[i] += 0.2 * erro * self.d * self.x[i]
        return backerror


# testando
input = [[0, 0], [0, 1], [1, 0], [1, 1]]
output = [0, 0, 0, 1]

neuro = Neuronio(2)
erromedio = 1
cont = 0
X = []
Y = []

while erromedio > 0.1:
    soma = 0
    for i in range(4):
        o, d = neuro.forward(input[i])
        erro = output[i] - o
        soma += abs(output[i] - o)
        neuro.backward(erro)
    erromedio = soma / 4
    cont += 1
    X.append(cont)
    Y.append(erromedio)

pyplot.plot(X,Y)
pyplot.show()