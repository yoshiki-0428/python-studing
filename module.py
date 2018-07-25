'''
    モジュール化について
        ソースファイルをまとめること
        同列パッケージでも使用は不可能、必ずimportして使用する

    パッケージについて
        パッケージを作成した場合 __init__.py を必ず作成する
'''

# パッケージ名.ファイル名 から 関数 をimportする
from module_calc import plus
# パッケージ名.ファイル名 自体をimport
import module_calc

print('module_calcから計算:', plus(1, 2))
# importしてないので失敗
# minus(1, 2))
print(module_calc.minus(1,2))
