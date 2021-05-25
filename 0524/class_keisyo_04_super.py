class Car():
    def run():
        print('run')

class NissanCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

nissan_car = NissanCar()
nissan_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()