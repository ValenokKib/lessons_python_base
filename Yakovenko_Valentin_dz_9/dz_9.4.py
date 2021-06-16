class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"{self.name}: Машина поехала")
    def stop(self):
        print(f"{self.name}: Машина остановилась")
    def turn(self, direction):
        print(f"{self.name} поворот {'left' if direction == 1 else 'right'}")
    def show_speed(self):
        print(f"{self.name}: Скорость - {self.speed}")

class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: Speed - {self.speed} 'ПРЕВЫШЕНИЕ!!!'" if self.speed > 60 else f"{self.name} {self.speed}"

class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: Speed - {self.speed} 'ПРЕВЫШЕНИЕ!!!'" if self.speed > 40 else f"{self.name} {self.speed}"

class SportCar(Car):
    """Sport Car"""

class Police(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

work_Car = WorkCar('KAMAZ', 'yellow', 30)
work_Car.go()
work_Car.turn(1)
print(work_Car.show_speed())
work_Car.stop()

town_Car = TownCar('KIA', 'black', 70)
town_Car.go()
town_Car.turn(0)
print(town_Car.show_speed())
town_Car.stop()

sport = SportCar('Lamba', 'orange', 210)
sport.go()
sport.turn(1)
sport.turn(0)
sport.show_speed()
sport.stop()

police = Police('Ford (police)', 'grey/blue', 99999)
police.go()
police.turn(1)
police.turn(0)
police.show_speed()
police.stop()



