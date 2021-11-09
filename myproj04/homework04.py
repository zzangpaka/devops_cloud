"""
가수 별 곡수를 출력해보세요
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list  # 삭제해도 무관

singer_dict = {}

for song in song_list:
    if song["artist"] in singer_dict:
        singer_dict[song["artist"]] += 1
    else:
        singer_dict[song["artist"]] = 1
print(singer_dict)


# 교수님 풀이
# artist_dict = {}
# for song_dict in song_list:
# artist: str = song_dict["artist"]
# if artist not in artist_dict:
# artist_dict[artist] = 0
# artist_dict[artist] += 1
# print(artist_dict)

# 교수님 풀이2
# 맨 위에 -> from collections import Counter
# artist_list = []
# for song_dict in song_list:
# artist: str = song_dict["artist"]
# artist_list.append(artist)
# print(Counter(artist_list))

# 교수님 풀이3 - List Comprehension 문법. 2와 같다.
# 맨 위에 -> from collections import Counter
# artist_list = []
# artist_list = [
# song_dict["artist"]
# for song_dict in song_list]
# print(Counter(artist_list))

# 복잡한 방법
# artist_list.append(artist)
# print(artist_list)
# {
# "방탄소년단": 10,
# " 소미": 3,
# }
