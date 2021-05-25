def spam(a, b):
    result = a + b
    return result
# 関数=メソッド

# 変数ak
ak = spam(6, 9)

class Spam:
    def __init__(self, muscle): #self=わたくし自身, 仮引数1, 仮引数2...
        self.muscle = muscle
        self.protain = 100
    def hoge(self):
        print('Hello')
    def fuga(self):
        print('Goodbye')

# インスタンスclassspam
classspam = Spam('上腕二頭筋')
print(classspam.muscle)
# classspamインスタンス生成完了
# classspam.hoge()
# classspam.fuga()

# インスタンス変数
classspam.ak = 60