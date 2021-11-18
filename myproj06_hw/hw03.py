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
