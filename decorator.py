'''
	デコレータを使用する理由
		あらゆる処理には必ず本来の機能とは関係ない前後の処理が存在している
		その前後処理をデコレータで実現する
		よく使用される使われ方
		-> DB接続切断など、ファイルの読み込み開始切断
'''
def calc(func):
	def display(*args):
		print('start')
		print(func(*args))
		print('end')
	return display

def plus(x, y):
	return x + y

print('関数呼び出し開始')
calc(plus) (1, 2)
print('関数呼び出し終了')

print()

# @シンボルでの利用
@calc
def plus2(x, y):
	return x + y

print('@での関数呼び出し開始')
plus2(1, 2)
print('@での関数呼び出し終了')
