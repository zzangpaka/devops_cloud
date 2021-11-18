# 다섯번째 과제
"""
1번

멜론TOP100 리스트에서 "곡명" 단어수 출력
예) Dynamite -> 1
"""
# sorted/filter/map/max/min 되도록 사용

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
title_list = []

print("<<<곡명 단어수 출력하기>>>")

# TODO
def title_name(song_dict):
    return song_dict["title"]


new_song_list = filter(title_name, song_list)
new_song_list = sorted(new_song_list, key=title_name)
# title_list = sorted(new_song_list, key=filter_fn1)

for song_dict in new_song_list:
    title_list.append(song_dict["title"])
    print(f"[곡명]", song_dict["title"])
    print(f"[단어수]", len(song_dict["title"].split(" ")))
