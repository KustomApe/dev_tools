# ご自身の特技、ご自身の趣味→リスト
skill = ['ドリフト', '車いじり', 'エンジニアリング']

# 中西：プログラミングを教えること, メンバーお名前：特技、趣味、目標、おいしい食べ物
member_skill = {'中西' : 'すべる担当', '西先生' : 'フォロー担当'}

# forステータステイトメントを使って中身をそれぞれ表示
print('グループnはメンバー数' + str(len(member_skill)) + '人です。')
cnt = 0
for i in member_skill:
    if cnt == 0:
        print(i[cnt] + 'は' + member_skill[i] + 'になりたくて')
        cnt += 1
    elif cnt == 1:
        print(i[cnt] + 'は' + member_skill[i] +'になりたくて')
        cnt += 1
    else:
        print('done')