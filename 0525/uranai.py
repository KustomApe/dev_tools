import uranai_func

cars = ['Nissan', 'Toyota', 'Lamborghini', 'Ferrari']


fortune = uranai_func.car_col()
if fortune == 'Nissan':
    print(fortune + ' is your beloved car C35Laurel.')
elif fortune == 'Toyota':
    print(fortune + ' is your beloved Supra.')
elif fortune == 'Lamborghini':
    print(fortune + ' is your beloved Supercar.')
else:
    print(fortune + ' is your beloved jumping horse.')

