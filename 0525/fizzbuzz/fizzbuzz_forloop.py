fizz = []
buzz = []
fizzbuzz = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz!')
        fizzbuzz.append(i)
    elif i % 3 == 0:
        print('Fizz!')
        fizz.append(i)
    elif i % 5 == 0:
        print('Buzz!')
    else:
        print(i)