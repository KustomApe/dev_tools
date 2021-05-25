class Car():
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class NissanCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print('#################')
nissan_car = NissanCar('Nismo')
print(nissan_car.model)
nissan_car.run()
print('#################')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()