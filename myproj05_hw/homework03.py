"""
3번

좋아요수가 가장 많은 곡은? 가장 작은곡은?
곡명 단어수가 가장 많은 곡은? 가장 작은곡은?
곡명 글자수가 가장 많은 곡은? 가장 작은곡은?
예) 값 = max(iterable)
"""
# sorted/filter/map/max/min 되도록 사용


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


print("<<<좋아요 수가 가장 많은 곡과 작은 곡은?>>>")

# TODO
def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)
for song_dict in sorted_song_list[0:1]:
    print("[가장 많은 곡] {artist} {title} [{like}]".format(**song_dict))

for song_dict in sorted_song_list[99:100]:
    print("[가장 적은 곡] {artist} {title} [{like}]".format(**song_dict))


print("<<<곡명 단어수가 가장 많은 곡과 작은 곡은?>>>")


print("<<<곡명 글자수가 가장 많은 곡과 작은 곡은?>>>")
