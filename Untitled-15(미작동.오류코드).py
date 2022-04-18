#-*- coding: utf-8 -*-   // 한글깨짐 잡아주는 구문 // vs code에서는 미작동 
#number.py // EUC-KR로 전화하면 가능하나 vs code에서는 한글깨짐


def 입력():
    return input()
def 출력(변수):
    print(변수)
def 맵(함수,리스트):
    return map(함수,리스트)
def 정수화(변수):
    return int(변수)

에이,비 = 맵(정수화,입력().split())
출력(에이+비)