"""
4번

멜론TOP100 리스트에서
리스트에 랭크된 가수는 총 몇 팀인가요? (중복 제거한 가수명 리스트의 크기)
2곡 이상 랭크된 가수는 몇 팀인가요?
"방탄소년단"의 좋아요 총 합은?
"""
# sorted/filter/map/max/min 되도록 사용


from collections import Counter

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


print("<<<멜론TOP100 리스트에 총 몇팀의 가수가 랭크되었나?>>>")

singer_list = []
numbers = ["artist"]
even_numbers = []

for song_dict in song_list:
    artist: str = song_dict["artist"]
    singer_list.append(artist)

print(Counter(singer_list))


def check_even_number(number):
    return number == "artist"


print("<<<멜론TOP100 리스트에 2곡 이상 랭크된 가수는 몇팀인가?>>>")


print("<<<멜론TOP100 리스트에서 방탄소년단의 좋아요수 총 합은?>>>")

like_number = []

for song in song_list:
    if song["like"]:
