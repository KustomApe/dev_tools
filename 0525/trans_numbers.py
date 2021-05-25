import sys

try:
    f = open('numbers.txt')
    print(f)
    s = f.readline()
    while s:
        i = int(s.strip())
        print(i)
        s = f.readline()
except OSError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print('Error', sys.exc_info()[0])

finally:
    print('Done')
    f.close()