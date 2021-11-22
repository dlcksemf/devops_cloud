import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 문제
# artist 글자수가 3글자 이상인 곡에 대해서
# 좋아요 수와 제목글자수의 곱을 출력해보세요.


def check_artist_length(song_dict):
    return len(song_dict["artist"]) > 2


def like_times_title_length(song_dict):
    title: str = song_dict["title"]
    like: int = song_dict["like"]
    artist: str = song_dict["artist"]
    return [title, artist, like, len(title) * like]


# 1) for/if로 구현
artist_length = []
for song_dict in song_list:
    if len(song_dict["artist"]) > 2:
        title: str = song_dict["title"]
        like: int = song_dict["like"]
        result: int = len(song_dict["title"]) * like
        artist_length.append([title, like, result])

for title, like, result in artist_length:
    print(f"{title} / {like}, {result}")


# 2) filter/ map 위주로 구현
# for title, like, result in map(
#     like_times_title_length, filter(check_artist_length, song_list)
# ):
#     print(f"{title} / {like} / {result}")
