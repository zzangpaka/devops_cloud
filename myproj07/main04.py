"""
리스트에 랭크된 가수는 총 몇 팀인가요? (중복 제거한 가수명 리스트의 크기)
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 1

artist_list = []
for song_dict in song_list:
    song_dict["artist"]
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.append(artist)
print(len(artist_list))
# not in -> 없을 때


# 2

artist_set = set()
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)
print(len(artist_set))
# 집합(set)은 순서의 개념이 없어서 add, 리스트는 순서의 개념이 있기때문에 append
# 집합(set)은 알아서 중복 제거가 됨


# 3

artist_set = set([song_dict["artist"] for song_dict in song_list])
print(len(artist_set))


# 4 (Set Comprehension)

artist_set = {song_dict["artist"] for song_dict in song_list}
print(len(artist_set))
