# 문자열을 인자로 받아 공백을 제외한 글자수를 반환하는 함수를 작성하세요
# "우리는 파이썬을 즐겨요"를 인자로 받아 10을 반환(예
# def get_count(s): for ch in s: 문자열
# 힌트 문자열은 순회가능한 객채
# " " 공백 => ==, != 사용


def get_ch_count_except_space(s):
    count = 0
    for ch in s:
        if ch != " ":
            count += 1
    return count


print(get_ch_count_except_space("우리는 파이썬을 즐겨요"))


# acc -> 함수밖(전역변수 = global variable) / 함수안(지역변수 = local variable)
