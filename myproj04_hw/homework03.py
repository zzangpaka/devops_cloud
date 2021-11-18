"""
좋아요 수가 200000이 넘는 곡수는?
hint: int(좋아요) > 200000
"""


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
song_list  # 삭제해도 무관
result = 0


for song in song_list:
    if song["like"] > 200000:
        result += 1
print(result)


# 교수님 풀이
# song_count = 0
# for song_dict in song_list:
# if song_dict["like"] > 200000:
# song_count += 1
# print(f"좋아요가 200,0000이 넘는 곡은 {song_count}곡입니다.")
# 마지막 보기 좋게 설명문을 써줄 것! 참조! 나머지는 같았다 >0<
