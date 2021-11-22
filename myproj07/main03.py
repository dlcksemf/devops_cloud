"""
QUIZ : 멜론TOP100 리스트에서 ...
"""
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# "좋아요" 수가 가장 많은 곡은? 가장 작은 곡은?
def peek_like_for_song(song_dict):
    return song_dict["like"]


# 오류 대응 1
song_dict = max(song_list, key=peek_like_for_song, default=None)
if song_dict == None:
    print("노래목록이 비었습니다.")
else:
    print(song_dict)

# 오류 대응 2 -> python에서 사용 많이 함
try:
    song_dict = max(song_list, key=peek_like_for_song)
except ValueError:
    print("노래목록이 비었습니다.")
else:
    print(song_dict)

# 오류 대응 3 -> c언어에서 사용 많이 함
if song_list:
    song_dict = max(song_list, key=peek_like_for_song)
    print(song_dict)
else:
    print("노래목록이 비었습니다.")


# "곡명" 단어수가 가장 많은 곡은? 가장 작은 곡은?


# "곡명" 글자수가 가장 많은 곡은? 가장 적은 곡은?
