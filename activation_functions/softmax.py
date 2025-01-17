from base import ActivationFunction
import numpy as np


class Softmax(ActivationFunction):

    def __init__(self):
        super().__init__()
        self.name = "Softmax"
        self.description = "Softmax activation function"
        self.__function = lambda x: np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)
        self.__derivative = lambda x: self.__function(x) * (1 - self.__function(x))

    @property
    def function(self):
        return self.__function

    @property
    def derivative(self):
        return self.__derivative

    def forward(self, x):
        return self.__function(x)

    def gradient(self, x):
        return self.__derivative(x)
