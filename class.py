'''
    クラスの作成方法
        クラスに何も書きたくない場合は pass を指定する
        インスタンス生成時に __init__ が呼び出される
        private属性 という考え方はない
        3系からは属性を隠蔽するような使い方も存在する
'''
# 引数なしコンストラクタ
class Sample:
    def __init__(self):
        self.name = None
        self.price = None

sam = Sample() # インスタンスの生成
print(type(sam))
# 属性の呼出、代入はJavaと変わらない
sam.name = 'John'
sam.price = 100
print(sam.name, sam.price)
print()

# 引数付きコンストラクタ
class Sample2:
    rate = 0.08
    # selfというキーワードを必ず使うことが条件
    # Javaはthisはあってもなくても良い
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_detail(self):
        print('クラスメソッドからの呼出:', self.name)

    def get_price(self):
        return self.price

    @classmethod
    def calcTax(cls, price):
        return int(price + price * cls.rate)

    @staticmethod
    def plus(x, y):
        return x + y

sam = Sample2('John', 1000) # インスタンスの生成
print(type(sam))
print(sam.name, sam.price)
sam.show_detail()
print('クラスメソッドからの数値返却:', sam.get_price())

print('クラスメソッドの実行', Sample2.calcTax(1000))
print('スタティッククラスメソッドの実行', Sample2.plus(500, 500))
