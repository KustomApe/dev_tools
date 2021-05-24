def survey(message='questions'):
    answer = input('Please input' + message + ':')
    return answer

users = []
while True:
    first_name = survey('first name')
    last_name = survey('last name')
    if first_name == '' and last_name == '':
        break
    else:
        users.append(first_name + ' ' + last_name)

print('-' * 40)
for user in users:
    print(user)

print('Thank you for your cooperation.')

