"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 리스트를 만들어봅시다.
단어수가 제일 큰 노래가 우선순위가 가장 높게 해봅시다.
"""
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def pick_word_count_for_title(song_dict):
    title: str = song_dict["title"]
    word_list = title.split(" ")
    return len(word_list)


sorted_song_list = sorted(song_list, key=pick_word_count_for_title, reverse=True)
top10_song_list = sorted_song_list[:10]

for song_dict in top10_song_list:
    print("{like} {title}".format(**song_dict))
# 첫 인자는 목록(리스트, 튜플, 집합, 사전), 키는 함수 -> sorted의 결과는 항상 리스트
# 정렬 기준값을 for 루프에서 가져오고 싶을 때 map으로 정렬 기준값을 가진 함수를 먼저 만들어서 불러온다
