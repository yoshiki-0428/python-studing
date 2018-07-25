
def set_price(price):
    def get_price(cnt):
        return price * cnt
    return get_price

# この時点でset_priceが設定される(get_priceの関数を持っているイメージ)
adult = set_price(1000)
child = set_price(800)

# adult = get_price(xx)なので数値を入れると計算された結果が返る
print(adult(3))
print(child(2))
