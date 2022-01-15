class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


Ferrari = SportCar(100, 'Red', 'Ferrari', False)
Kia = TownCar(30, 'Black', 'Kia', False)
VAZ = WorkCar(70, 'Green', 'VAZ', True)
Hyundai = PoliceCar(110, 'Blue',  'hyundai', True)
print(VAZ.turn_left())
print(f'When {Kia.turn_right()}, then {Ferrari.stop()}')
print(f'{VAZ.go()} with speed exactly {VAZ.show_speed()}')
print(f'{VAZ.name} is {VAZ.color}')
print(f'Is {Ferrari.name} a police car? {Ferrari.is_police}')
print(f'Is {VAZ.name}  a police car? {VAZ.is_police}')
print(Ferrari.show_speed())
print(Kia.show_speed())
print(Hyundai.police())
print(VAZ.show_speed())
