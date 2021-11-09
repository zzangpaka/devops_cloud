퀴즈 = """1이상 100미만 범위에서 3과 5의 공배수(15의 배수)의 합을 출력하기"""

print(퀴즈)


i = 0


for number in range(1, 100):
    if number % 3 == 0:
        if number % 5 == 0:
            i += number

print(i)


# acc = 0
# for i in range(1, 100):
# if i % 3 == 0 and i % 5 == 0:
# acc += i
# print(acc)

# number_list = []
# for i in range(1, 100):
# if i % 3 == 0 and i % 5 == 0:
# number_list.append(i)
# print(sum(number_list))
