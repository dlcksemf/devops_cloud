# 멜론 TOP100 리스트에서 "좋아요" TOP10 곡명 출력

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# my answer

# def sort_fn(songs_list):
#     return int(songs_list["like"])


# top10_like_songs = sorted(song_list, key=sort_fn, reverse=True)[:10]

# for i in range(0, 10):
#     line = "[{title}], {like}".format(**top10_like_songs[i])
#     print(line)

# 교수님 answer


def 정렬기준값을_만들어줄_함수(song_dict):
    return song_dict["like"]


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

for song_dict in sorted_song_list[:10]:
    print("[{like}] {title} {artist}".format(**song_dict))
