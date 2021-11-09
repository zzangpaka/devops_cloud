"""
1번

멜론TOP100 리스트에서 "곡명" 단어수 출력
예) Dynamite -> 1
"""
# sorted/filter/map/max/min 되도록 사용

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
title_length = []


def title_name(song_dict):
    """
    곡명을 모음
    """
    return song_dict["title"]


for song_dict in filter(title_name, song_list):
    title: str = song_dict["title"]
    title_length.append(title, len(title))

for title, length in title_length:
    print("곡명: {title}, 단어수: {length}".format(**song_dict))
