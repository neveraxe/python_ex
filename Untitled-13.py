t = (1, 2, 3)
t[0] = 'a'


'''
    # 실행시 나오는 에러메세지

    Traceback (most recent call last):
     File "d:\파이썬 예제\Untitled-13.py", line 2, in <module>
        t[0] = 'a'
    TypeError: 'tuple' object does not support item assignment
'''

# 이유 : tuple은 원소(element)의 값을 변경할 수 없습니다.