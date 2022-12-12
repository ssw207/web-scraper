from random import randint # randint 모듈에서 random 함수 임포트

def print_hi(name="empty"):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.

def if_condition(val):
    if val > 0:
        print("0보다 크다")
    elif val == 0:
        print("0이다")
    else:
        print("그외")

def inputTest():
    # input에서 사용자 입력을 받고 int를 이용해 문자열을 숫자로 변환
    age = int(input("how old are you"))
    print(age)

def random():
    print(randint(1,50))

def testWhile():
    while 1 < 20:
        print()

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    # print_hi()
    # if_condition(0)
    # inputTest()
    random()
