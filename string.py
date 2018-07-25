'''
    String(文字列関係)
'''

# クォーテーションの種類
# '' 通常
print('abc')
# "" 通常
print("abc")
# """""" 改行含む
print("""a
      b
      c""")

# 文字列の生成（代入） ※使用は非推奨(可読性落ちる)
# フォーマット文字列
# %d : 10進数
print('%dの数です' %(100))

# %を使用した文字列生成は消える可能性がある
str = '%(name)sは%(type)sです。' %{
    'type': '哺乳類',
    'name': '犬'
}
print(str)

# formatメソッドを使用した文字生成
str2 = '{0}は{1}です。日本には{2:d}万匹以上存在します'.format('猫', '哺乳類', 100)
str3 = '{name}は{type}です。'.format(name='猫', type='哺乳類')
print(str2)
print(str3)
# 3.6~はf'{0}は{1}です'というf文字列で文字列生成が可能


# 文字列の操作
# 検索
print('猫' in '猫は哺乳類')
print(str3.index('哺乳類')) # 存在しない場合 実行エラー(ValueError)
print(str3.find('哺乳類'))  # 存在しない場合 -1
print(str3.startswith('猫')) # 初期文字が「猫」から始まっているか
print(str3.endswith('猫')) # 初期文字が「猫」で終わっているか

print(str3.isalpha()) # 英字か日本語（文字列ならOK）
print(str3.isdigit()) # 数字か判定
print('123'.isdigit()) # 数字か判定
print('1,2,3'.split(','))
