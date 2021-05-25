class Spam: #クラス定義
    def __init__(self, amount):
        self.salt = 2.2
        self.amount = amount

    def manufacture(self): #引数なしのインスタンスメソッド(関数)の定義
        print('Hormel Foods Corporation')

    def echo(self, message): #引数ありのインスタンスメソッド(関数)の定義
        print(message)


lunch = Spam(340) #lunchインスタンス生成
lunch.manufacture() #lunchインスタンスにメッセージを送る(インスタンスメソッドを呼び出す)
lunch.echo('hello, python') #lunchインスタンスに別のメッセージを送る
print(lunch.amount)
print(lunch.salt)

supper = Spam(220) #supperインスタンス生成
supper.manufacture()
supper.echo('hello, guido')
print(supper.amount)
print(supper.salt)

lunch.amount = 340 #インスタンス変数
print(lunch.amount)

supper.amount = 280 #インスタンス変数
print(supper.amount)