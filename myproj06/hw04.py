"""
4번

멜론TOP100 리스트에서
리스트에 랭크된 가수는 총 몇 팀인가요? (중복 제거한 가수명 리스트의 크기)
2곡 이상 랭크된 가수는 몇 팀인가요?
"방탄소년단"의 좋아요 총 합은?
"""
# sorted/filter/map/max/min 되도록 사용

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
