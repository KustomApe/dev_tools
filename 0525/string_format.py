# print('Spam')
# 'spam', 'bacon', 'ham'
# print('{0}'.format('Spam'))
# Spam

# name = input('name')
# age = str(input('age'))
# address = input('住所くれ')
# print('{2}という名のものは年齢が{0}歳で住処は{1}県らすい'.format(age, address, name))
# print('{0} {1} {2}'.format(100, 'Spam', 200))
# print('{1} {2} {1}'.format(100, 'Spam', 200))


# line = '{0}さんの身長は{1}cm、体重は{2}kgです。'.format('中西', 178, 80.3)
# print(line)

# # {インデックス番号:書式指定}
# # 身長と体重を小数点以下1桁で統一して表示したい
# line = '{0}さんの身長は{1:.1f}cm、体重は{2:.1f}kgです。'.format('中西', 178, 80.3)
# # {インデックス番号:</>文字寄せ / 最小幅 / , 千の位にカンマ / .3 小数点以下の桁数 / f 型}
print('{0:06.2f}'.format(12.3456))
# # 型の指定
# # s 文字列
# # d 整数
# # e / E 浮動小数点 / 指数表記
# # f / F 浮動小数点 / 小数点表記
# # 小数点以下n桁を指定するには {:.nf} と指定する
# '{:.1f}'.format(0.01)
# '{:.2f}'.format(0.01)
# '{:.5f}'.format(0.01)

# # 桁数指定を文字列型にすると文字数を最大何文字使用するか指定できる
# '{:.2}'.format('abcde')
# '{:.3}'.format('abcde')
# '{:.7}'.format('abcde')



# '{0:s}'.format('Spam')

# print('{0:06.2f}'.format(12.3456))