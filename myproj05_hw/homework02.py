"""
2번

멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
예) 단어수가 제일 큰 노래가 우선순위가 가장 높게
"""
# sorted/filter/map/max/min 되도록 사용


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


print('<<<멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 출력하기>>>')
# 단어수가 큰 노래가 우선순위가 높게
# TODO
def filter_fn1(song_dict):
    return song_dict["title"]


def sort_fn1(song_dict):
    return song_dict["title"]


new_song_list = filter(filter_fn1, song_list)
new_song_list = sorted(new_song_list, key=sort_fn1)
title_list = sorted(new_song_list, key=sort_fn1)


for song_dict in new_song_list:
    title_list.append(song_dict["title"])
    print(song_dict["title"])
    print(len(song_dict["title"].split(" ")))
