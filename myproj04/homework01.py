# 리스트를 먼저 쓰고 사전으로 채워넣는게 일반적........?
"""
방탄소년단의 곡명만 출력해보세요
hint: for 루프 내에서 if 조건문을 통해 "가수"필드 체크
"""


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list  # 삭제해도 무관

# song = dict 사전이었다....^^....
for song in song_list:  # 리스트는 되도록 하나의 타입으로만 구성하도록
    if song["artist"] == "방탄소년단":
        print(song["title"])


# 교수님 풀이
# for song_dict in song_list:
# if song_dict["artist"] == "방탄소년단":
# print(song_dict["title"])
# 같아서 너무 좋다~~~~
