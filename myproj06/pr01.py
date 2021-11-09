"""
문제
artist 글자수가 3글자 이상인 곡에 대해서
각 곡의 좋아요 수와 제목글자수의 곱을 출력해보세요
"""

# 1) for/if로 구현
# 2) filter/map 위주로 구현


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
three_over = []

# new_song_list: List[dict] = []
for song_dict in song_list:
    if song_dict["artist"]:
        title: str = song_dict["title"]
        like: int = song_dict["like"]
        three_over.append([title, len(title), like])
# for song_dict in song_list:
# artist: str = song_dict["artist"]
# if len(artist) >= 3:
# value: int = song_dict["like"] * len(song_dict["artist"])
# new_song_list.append(dict(song_dict, value=value))

# for song_dict in new_song_list:
# print("{title} / {value}".format(**song_dict))

for title, length, like in three_over:
    if len(title) >= 3:
        print("곡명:", title, "글자수:", length, "좋아요:", like)


def title_length_like(three_over):
    len(title) >= 3
    return [like, len(title)]


for like, length in map(title_length_like, three_over):
    print(like * len(title))
