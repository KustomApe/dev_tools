#問題1
lst = []
for i in range(1, 101):
    lst.append(i)
print(lst)
print(lst[0])
print(lst[99])

# 問題2
lst2 = []
for i in lst:
    lst2.append(i * 100)
print(lst2)
print(lst2[0])
print(lst2[99])

# 問題3
lst3 = []
for i in lst:
    if i % 3 == 0:
        lst3.append(i)
print(lst3)
print(lst3[0])
print(lst3[1])
print(len(lst3))

#問題4
lst4 = []
for i in lst:
    if i % 3 != 0:
        lst4.append(i)
print('####################')
print(lst4[0])
print(lst4[2])
print(lst4)
print(len(lst4) - 1)
max_value = max(lst4)
print(max_value)
max_index = lst4.index(max_value)
print(max_index)

#問題5
lst5 = lst.copy()
lst5.reverse()
print(lst5)