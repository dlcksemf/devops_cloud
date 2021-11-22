import pandas as pd
from collections import Counter

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 방탄소년단의 곡명만 출력해보세요.

for song_dict in song_list:
    if song_dict["artist"] == "방탄소년단":
        print(song_dict["title"])


# 곡명에 "가을"이 들어가는 곡명만 출력해보세요.

for song_dict in song_list:
    if "가을" in song_dict["title"]:
        print(song_dict["title"])


# 좋아요 수가 200000이 넘는 곡수는?

song_count = 0
for song_dict in song_list:
    if song_dict["like"] > 200000:
        song_count += 1
print(f"좋아요가 200,0000이 넘는 곡은 {song_count}곡입니다.")


# 가수 별 곡수를 출력해보세요.

# 01. List 활용
# artist_dict = {}
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     if artist not in artist_dict:
#         artist_dict[artist] = 0
#     artist_dict[artist] += 1
# print(artist_dict)

# 02. counter 활용
# artist_list = []
# for song_dict in song_list:
#     artist: str = song_dict["artist"]
#     artist_list.append(artist)
# print(Counter(artist_list))

# 03. List Comprehension
artist_list = [song_dict["artist"] for song_dict in song_list]
counter = Counter(artist_list)

# for artist in counter: # keys
#   print(artist)

# for song_count in counter.values():  # values
#     print(song_count)

# for artist in counter:
#     print(artist, counter[artist])

for artist, song_count in counter.items():
    print(artist, song_count)
