class A:
    def show(self):
        print('A')

    def go(self):
        print('go')

class B:
    def show(self):
        print('B')

    def come(self):
        print('come')

'''
    同じ名前のメソッドがある場合どんな振る舞いになるのか
        左側に書いたクラスが優先される
        Aクラスのメソッドが優先
'''

class C(A, B):
    # どうしても呼びたいときはCクラスで上書きする ※非推奨な書き方
    # def show(self):
    #     print('B')
    pass

ins = C()
ins.show()
ins.go()
ins.come()
