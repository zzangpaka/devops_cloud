# def check_even_number(number):
#     return number % 2 == 0


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in filter(check_even_number, numbers):
#     print(number)

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


print('<<<"방탄소년단" 곡명만 출력하기>>>')

# TODO
def filter_fn1(song_dict):
    return song_dict["artist"] == "방탄소년단"


def sort_fn1(song_dict):
    return song_dict["title"]


new_song_list = filter(filter_fn1, song_list)  # list 타입은 아닙니다.
new_song_list = sorted(new_song_list, key=sort_fn1)

for song_dict in new_song_list:
    print(song_dict["artist"], song_dict["title"])


print('<<<곡명에 "사랑"이 포함된 곡명만 출력하기>>>')

# TODO
def filter_fn2(song_dict):
    return "사랑" in song_dict["title"]


def sort_fn2(song_dict):
    return song_dict["artist"]


new_song_list = filter(filter_fn2, song_list)  # list 타입은 아닙니다.
new_song_list = sorted(new_song_list, key=sort_fn2)

for song_dict in new_song_list:
    print(song_dict["artist"], song_dict["title"])


print('<<<"좋아요" 수가 200,000 이상인 곡명만 출력하기>>>')


# TODO
def filter_fn3(song_dict):
    return song_dict["like"] > 200000


def sort_fn3(song_dict):
    return song_dict["like"]


new_song_list = filter(filter_fn3, song_list)  # list 타입은 아닙니다.
new_song_list = sorted(new_song_list, key=sort_fn3, reverse=True)

for song_dict in new_song_list:
    print(song_dict["like"], song_dict["title"], song_dict["artist"])
