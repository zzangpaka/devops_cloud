# 리스트를 먼저 쓰고 사전으로 채워넣는게 일반적........?
"""
방탄소년단의 곡명만 출력해보세요
hint: for 루프 내에서 if 조건문을 통해 "가수"필드 체크
"""


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list  # 삭제해도 무관

# song = dict 사전이었다....^^....
for song in song_list:  # 리스트는 되도록 하나의 타입으로만 구성하도록
    if song["artist"] == "방탄소년단":
        # print(song["artist"], song["title"], song["like"])
        line = "{}, {}, {}".format(song["artist"], song["title"], song["like"])
        line = "{가수명}, {곡명}, {좋아요수}".format(
            가수명=song["artist"], 곡명=song["title"], 좋아요수=song["like"]
        )
        line = "{artist}, {title}, {like}".format(
            artist=song["artist"], title=song["title"], like=song["like"]
        )
        # unpack arguments (사전의 경우에만 가능) : 사전을 풀어서 인자를 넘겨주세용
        line = "{artist}, {title}, {like}".format(**song)
        print(line)
# fmt : off = 블랙 끄기 / fmt : on = 블랙 켜기

# counter = Counter(artist_list)
# for artist in counter # key만 가져옴
# print(artist)

# for song_count in counter.values(): # values
# print(song_count)

# for artist in counter:
# print (artist, counter[artist])

# for artist, song_count in counter.items():
# print(artist, song_count)
