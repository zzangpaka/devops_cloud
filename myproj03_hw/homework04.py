퀴즈 = """구구단 퀴즈 break 안 쓴 버전"""


print(퀴즈)


for number in range(2, 10):
    for i in range(1, 10):
        if number >= i:  # i를 앞에 쓰는게 가독성이 좋다.
            print(f"{number} * {i} = {number * i}")


# for number in range(2, 10):
# for i in range(1, number + 1):
# print(f"{number} * {i} = {number * i}")
