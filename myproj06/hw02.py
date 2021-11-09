"""
2번

멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
예) 단어수가 제일 큰 노래가 우선순위가 가장 높게
"""
# sorted/filter/map/max/min 되도록 사용


import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
