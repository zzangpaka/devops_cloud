# 문자열과 인덱스

# 문자열(str 타입) = 저장된 순서를 유지한다
# 0부터 시작해 1씩 증가하는 일련번호를 통해 개별 문자에 접근할 수 있다 = 인덱스
# 언어에 상관없이 모든 글자는 하나의 인덱스를 가진다 = 파이썬은 유니코드를 지원하기 때문
# 인덱스/슬라이싱 문법은 순서를 유지하는 대다수의 자료구조에서 지원 = 문자열, 리스트, 튜플 등
# [0] / [0:3] = 0이상 3미만
# 변경 불가능한 객체(리스트는 변경가능 Mutable, 튜플은 불가능 Immutable)

# 범위 밖의 인덱스를 지정하면 인덱스 에러가 뜸

# Immutable은 변수에 할당된 후 변경 불가
# 좋아하는_언어 = "파이썬" (O)
# 좋아하는_언어[0] = "자" (X)
# 다만 변수에 새로운 문자열을 할당하는 것은 가능
# 좋아하는_언어 = "파이썬" -> 좋아하는_언어 = "자이썬"(O)

# 음수 인덱스를 지원
#  h  e  l  l  o
#  0  1  2  3  4
# -5 -4 -3 -2 -1

# 슬라이싱
# 인덱스 = 개별 값을 하나씩 참조 -> 문자열[2]
# 슬라이싱 = 연속된 다수 값을 한 번에 참조 -> 문자열[0:2]
# s[0:5:1] -> 0이상, 5미만, 1씩 증가

# 자료구조(Data Structures)
# 데이터를 효율적으로 저장/관리하는 방법
# 데이터 성격에 따라 다양하고 효율적인 자료구조
# 파이썬에서 지원하는 자료구조 = 리스트(list), 튜플(tuple), 집합(set), 사전(dict)
# 이 외에 deque, fronzensets, defaultdict, Counter, namedtuple 등이 있다.

# 시퀀스 = 순서를 가지는 성격
# 파이썬은 ABC의 특징을 계승
# 시퀀스의 공통 인터페이스에 따라 여러 시퀀스에 반복, 슬라이싱, 정렬, 연결 등 공통된 연산을 적용할 수 있다
# 단일 자료형 지원 여부에 따른 분류 = 컨테이너 시퀀스(서로 다른 자료 항목 담음), 균일 시퀀스(단일 자료형만 담을수있다)
# 가변성에 따른 분류 = 가변 시퀀스, 불변 시퀀스(tuple, str, bytes)
