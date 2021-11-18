# 과제
import random


print("1~100사이 숫자가 주어집니다. 정답을 맞혀주세요.")

count = 0

a = random.randint(1, 100)

for number in range(10):
    number = int(input(">>>"))
    if a > number:
        print("더 큰 수를 입력해주세요.")
        count += 1
    if a < number:
        print("더 작은 수를 입력해주세요.")
        count += 1
    if a == number:
        print("정답입니다.")
        print(a)

    if count == 10:
        print("다음 기회에 ...")


# 교수님 방법
# from random import randint
# number = randint(1,100)
# is_pass = False
# for retry in range(1, 11):
# line = input(f"[{retry}] Try guess number : ")
# answer = int(line.strip() or 0) # strip = 좌우의 빈공간을 지워준다
# (Try/Except 썼을때 strip()뒤의 or 0을 없앤다)
# if answer == number:
# print(f"{retry}회 시도에 성공")
# is_pass = True
# break
# elif answer < number:
# print("더 큰 수를 입력해주세요")
# elif answer > number: (or else:)
# print("더 작은 수를 입력해주세요")
# if retry == False:
# print("다음 기회에 ...")

# else(for에):
# print("다음 기회에 ...")
