class Road:
    def __init__(self, length, wigth):
        self._length = length
        self._width = wigth

    def weight_asphalt(self, weight = 25, thickness = 5):
        return f'{self._length} м * {self._width} м * {weight} кг * {thickness} см = ' \
               f'{(self._length * self._width * weight * thickness) / 1000} тонн'

a = Road(5000, 20)
print(a.weight_asphalt())