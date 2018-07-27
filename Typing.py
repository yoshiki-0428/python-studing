import time
import keyword
import random

# 実行時間を計るデコレータ
def timer(func):
    def time_count(*args, **keys):
        startTime = time.time()
        result = func(*args, **keys)
        processingTime = time.time() - startTime
        print(str(inputTime) + '秒かかりました')   # 時間を表示したい場合は追記
        if processingTime >= 4:
            print('時間がかかりすぎです！')
        elif processingTime >= 2:
            print('まあまあです')
        else :
            print('素晴らしいスピードです！')
        return result
    return time_count

# pythonのキーワードを取得し、入力値と同じかどうかチェックする関数
# この関数については実行時間を計る
@timer
def typing(outputKey):
    inputKey = input('入力してください：' + outputKey + '\n')
    if inputKey == outputKey :
        return True
    else :
        return False

# キーワードをランダムで取得する関数
def get_keyword():
    keyList = keyword.kwlist
    index = random.randint(0, len(keyList) - 1)
    return keyList[index]

# 実行内容
if __name__ == '__main__':
    print('タイピング練習を行います。')
    check = 0   # 正解数をカウントするための変数
    for i in range(10):
        print(str(i + 1) + '問目です')
        msg = 'NGです・・・'
        if typing(get_keyword()) :
            check += 1
            msg = 'OKです！'
        print(msg)
        print()

    print(str(check) + '/10問正解しました')
