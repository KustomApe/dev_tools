def hoge(a, b): #デフォルト値
    result = a + b
    return result

def 関数名自由に付けられる(第一引数, 第二引数):
    result = a + b
    return result

def name(first_name, last_name):
    full_name = first_name + last_name
    return full_name

answer = name('eisuke', 'nakanishi')
answer1 = name(last_name = 'Mochida', first_name = 'Futa')
print(answer)
print(answer1)


# tashizan = hoge(b=5, a=9)
# tashizan = hoge(5, 9)
tashizan = hoge(3, 4)
tashizan = hoge(b=3, a=4)


print(tashizan)

# class クラス名
# def 関数名(引数1, 引数2, 引数3...):
