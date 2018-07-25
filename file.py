
# ファイル操作
f = open('readme.md', encoding='utf-8')
# データの取得（未指定: 全部, 数字指定: 数字分読み込む）
print(f.read(10)) # サイズ（省略可能）
print('ファイル情報:', f.name ,f.mode, f.encoding)
print(type(f))

# すべての内容を取得
file_str = f.readlines()
print(file_str[0])
# 一行分だけ取得
file_str2 = f.readline()
print(file_str2)

f.close() # 開いたら閉じる

# ファイル書き込みの処理
# r: 読み込み w: 書き込み a: 追加書き込み r+: 読み書き
fw = open('write_file.md', 'w', encoding='utf-8')
# 改行が含まれないので注意
fw.write('こんにちは\n')
fw.writelines('おはよう\n')
fw.writelines('さよなら\n')
fw.close()

# ファイルオープン closeメソッドいらないパターン
with open('readme.md') as f:
    print(f.read(40))
