# 問題1
lst = []
for i in range(1, 101):
    lst.append(i)

# 問題2
lst2 = []
for i in lst:
    lst2.append(i * 100)

# 問題3
lst3 = []
for i in lst:
    if i % 3 == 0:
        lst3.append(i)

# 問題4
lst4 = []
for i in lst:
    if i % 3 != 0:
        lst4.append(i)