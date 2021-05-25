import random as rand
from random import choice as choi
import numpy as np
import pandas as pd

def car_col():
    cars = ['Nissan', 'Toyota', 'Lamborghini', 'Ferrari']
    opt1 = rand.choice(cars)
    opt2 = rand.randrange(1, 4)
    result = cars[opt2]
    print(result)
    return opt1
