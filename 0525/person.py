class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print('Name:', self.name, 'AGE:', self.age)

class Engineer(Person):
    def __init__(self, name, age, speciality):
        super().__init__(name, age) #スーパークラスの機能を呼び出しています
        self.speciality = speciality

    def details(self):
        super().details()
        print('SPECIALITY : ', self.speciality)

steve = Person('Steve Jobs', 56)
steve.details()

dennis = Engineer('Dennis', 70, 'programmer')
dennis.details()