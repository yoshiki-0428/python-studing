class Solider():
    def __init__(self, name=None):
        self.name = name
        self.hp = 100

    def hurt(self, attacked):
        self.hp -= attacked

class MagicSolider(Solider):
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def fire(self):
        self.mp -= 10 #mp減らす
        return 100    #攻撃

    def hurt(self, attacked):
        super().hurt(attacked)


sol = Solider('敵')
print(sol.name, 'HP:', sol.hp)

msol = MagicSolider('主人公', 120, 100)
print(msol.name, 'HP:', msol.hp, 'MP:', msol.mp)

print('主人公の魔法攻撃！！')
sol.hurt(msol.fire())
print(msol.name, 'HP:', msol.hp, 'MP:', msol.mp)
print(sol.name, 'HP:', sol.hp)
