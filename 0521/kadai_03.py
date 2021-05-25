'''
準備) ./python_train/kadai_03.pyファイルを作成する
ユーザーが成人か否かを判定するプログラムに他条件分岐を追記してください
'''

user = int(input('年齢を入力してください：'))
if  user >= 20 and user < 30:
    print('お酒はほどほどに。')
elif user >= 30 and user < 40:
    print('健康診断結果によって飲酒は考えてくださいね')
elif user >= 40 and user < 50:
    print('家庭のことを考えて飲酒は楽しく')
elif user >= 50 and user < 60:
    print('寝る前のワイン1ショットぐらいがいいんじゃないですか？')
elif user >= 60:
    print('わたくしの祖父は言いました、飲みすぎると目覚めたとき現実か天国か迷う、と')
else:
    print('お酒はだめです。')