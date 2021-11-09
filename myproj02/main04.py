# 숫자 퀴즈
# 랜덤 숫자를 맞춰보세요.

# hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.

# 유저에게 10회의 기회를 줍니다. - for/range
# 그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는지 출력
# 입력한 숫자가 랜덤수보다 작다면, "더 큰 수를 입력해주세요."라고 출력
# 입력한 숫자가 랜덤수보다 크다면, "더 작은 수를 입력해주세요."라고 출력
# 횟수를 초과했다면, "다음 기회에 ..."라고 출력

import random

input("---숫자퀴즈---")

count = 0

number = random.randint(1, 100)

answer = int(number or 100)

for answer in range(10):
    number = int(input(">>>"))
    if answer < number:
        print("더 큰 수를 입력해주세요.")
        count += 1
    else:
        print("더 작은 수를 입력해주세요.")
        count += 1

    if answer == number:
        print(f"{count}번 만에 맞췄습니다.")
        print(answer)
    if answer >= 10:
        print(f"다음 기회에 ...")
