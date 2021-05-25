class Car():
    def run():
        print('run')

class NissanCar(Car):
    car = Car()
    car.run()

nissan_car = NissanCar()
nissan_car.run()