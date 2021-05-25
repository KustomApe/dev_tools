# weather ver.2
import random

def forecast():
    possibilities = ['sunny', 'rain', 'snow', 'cloudy', 'hail', 'drizzle', 'unknown']
    return random.choice(possibilities)