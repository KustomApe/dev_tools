fizz = []
buzz = []
fizzbuzz = []

i = 1
while i < 101:
    if i % 15 == 0:
        print('Fizz Buzz!')
        fizzbuzz.append(i)
    elif i % 3 == 0:
        print('Fizz!')
        fizz.append(i)
    elif i % 5 == 0:
        print('Buzz!')
    else:
        print(i)