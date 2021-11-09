"""
곡명에 "가을"이 들어가는 곡명만 출력해보세요
hint: 포함여부 = "가을" in 곡명
"""


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list  # 삭제해도 무관

for song in song_list:
    if "가을" in song["title"]:
        print(song["title"])


# 교수님 풀이
# for song_dict in song_list:
# if "가을" in song_dict["title"]:
# print(song_dict["title"])
# 같습니다~~~ ^0^
