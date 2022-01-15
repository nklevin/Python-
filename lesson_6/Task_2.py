class road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width

class road_mass(road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume

r = road_mass(25, 10000, 125)
print(r.mass())