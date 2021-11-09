import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""
멜론TOP100 리스트에서 "곡명 / 단어수" 리스트를 만들어봅시다.
총 100줄 중에 한 줄 출력 의 예 : Dynamite ➡ 1
"""

# for song_dict in song_list:
#     title: str = song_dict["title"]
#     title_length = len(title)
#     print(title, title_length)


# def get_title_for_song(song_dict):
#     return song_dict["title"]


# title_list = list(map(get_title_for_song, song_list))
# print(title_list)

# for title in map(get_title_for_song, song_list):
#     print(f"{title} - {len(title)}")


def get_title_and_length_for_song(song_dict):
    title: str = song_dict["title"]
    title_length: int = len(song_dict["title"].split(" "))
    return [title, title_length]


for title, length in map(get_title_and_length_for_song, song_list):
    print(title, ":", length)


# 방탄소년단의 노래에 대해서만 곡명과 곡명의 글자수를 출력

# bts_list = []
# for song_dict in song_list:
#     if song_dict["artist"] == "방탄소년단":
#         title: str = song_dict["title"]
#         bts_list.append([title, len(title)])

# for title, length in bts_list:
#     print(title, length)


# filter/map version


def check_bts_song(song_dict):
    return song_dict["artist"] == "방탄소년단"


for title, length in map(
    get_title_and_length_for_song, filter(check_bts_song, song_list)
):
    print(title, ":", length)

"""
멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
단어수가 제일 큰 노래가 우선순위가 가장 높겠죠.
"""

new_song_list = []


def check_long_name(song_dict):
    title: str = song_dict["title"]
    title_length: int = len(song_dict["title"])
    return [title, title_length]


new_song_list = sorted(song_list, reverse=True, key=check_long_name)

for song_dict in new_song_list[:10]:
    print(song_dict["title"])
