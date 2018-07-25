'''
    日付・時間
    datetimeクラス     : 日付と時間
    dateクラス         : 日付のみ
    timedeltaクラス    : 日付や時間差分
'''

from datetime import datetime

# datetimeクラス     : 日付と時間
print(datetime.now())

dt = datetime(2018, 7, 25)
print(dt)
print(type(dt))
print()

# pythonの曜日は0~6
weekday_dict = {
    0: '月曜', 1: '火曜', 2: '水曜', 3: '木曜',
    4: '金曜', 5: '土曜', 6: '日曜',
}
print(weekday_dict[dt.weekday()])
print()

# 日時の文字列変換 %wは日曜スタートなので注意が必要
dt_str = dt.strftime('%Y/%m/%d %w')
print(dt_str)
print(type(dt_str))
print()

# 文字列を日時に変換
str_dt = datetime.strptime('2019/07/25', '%Y/%m/%d')
print(str_dt)
print(type(str_dt))
print()

# date
from datetime import date
d = date.today()
print(d)
print(type(d))
print()

# 指定日付
d2 = date(2020, 7, 25) # 全て必要
print(d2)

# datetime同士を引き算するとtimedeltaインスタンスが作成される
td = datetime(2020, 7 , 25) - datetime.now()
print(td)
print(type(td))
print(td.days) # アクセスできるのはdaysのみ
print()

print(''' 今日から二週間後の日付が知りたい ''')
from datetime import timedelta
td2 = timedelta(weeks=2)
print(datetime.now() + td2)
print()

print(''' 今日から5日前の日付が知りたい ''')
print(datetime.now() - timedelta(days=5))
