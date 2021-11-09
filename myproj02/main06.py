def gugudan(number):
    # number = 2
    print(f"--- {number}단 ---")
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")


for number in range(2, 10):
    gugudan(number)


# 함수의 구성 요소
# 함수의 이름 : 1개
# 함수의 인자(Arguments) : 0개 이상
# 함수의 반환값(Return Value) : 1개
