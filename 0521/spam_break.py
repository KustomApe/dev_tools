while True:
    spam = input('Please type "spam" :  ')
    if spam == 'spam' or spam == 'Spam':
        print('You got a Spam.')
        break
    elif spam == 'nakanishi is cool':
        continue
    print('You need some Spam.')