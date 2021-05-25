class Car():
    def run():
        print('run')

class NissanCar(Car):
    # car = Car()
    # car.run()
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

nissan_car = NissanCar()
nissan_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()