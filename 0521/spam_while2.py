count = int(input('Please order : '))

while count > 0:
    print('Spam, ' * count)
    count -= 1

else:
    print('Last but not least, NO SPAM.')