퀴즈 = """코드 만들어보기 반복문을 활용하여, 
효과적으로 3단/6단/9단 구구단 출력하기"""

print(퀴즈)

for number in range(3, 10, 3):
    for i in range(1, 10):
        print(f"{number} * {i} = {number * i}")


# number =3
# for i in range(1, 10):
# print(f"{number} * {i} = {number * i})

# for number in [3, 6, 9]: / (3, 10, 3)
# for i in range(1, 10):
# print(f"{number} * {i} = {number * i})
