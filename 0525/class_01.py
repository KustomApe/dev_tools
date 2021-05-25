class Spam: #クラス定義
    def manufacture(self): #引数なしのインスタンスメソッド(関数)の定義
        print('Hormel Foods Corporation')

    def echo(self, message): #引数ありのインスタンスメソッド(関数)の定義
        print(message)

lunch = Spam() #lunchインスタンス生成
lunch.manufacture() #lunchインスタンスにメッセージを送る(インスタンスメソッドを呼び出す)
lunch.echo('hello, python') #lunchインスタンスに別のメッセージを送る

supper = Spam() #supperインスタンス生成
supper.manufacture()
supper.echo('hello, guido')
