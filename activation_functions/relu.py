from base import ActivationFunction


class ReLU(ActivationFunction):

    def __init__(self):
        super().__init__()
        self.name = 'ReLU'
        self.description = 'Rectified Linear Unit'
        self.__function = lambda x: max(0, x)
        self.__derivative = lambda x: 1 if x > 0 else 0

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
