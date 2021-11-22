import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


# 멜론 TOP100 리스트에서 "곡명"단어수 출력
def map_fn1(song_list):
    count_words = lambda song_dict: len(song_dict["title"].split())
    return list(map(count_words, song_list))


print(map_fn1(song_list))


# 멜론TOP100 리스트에서 "곡명" 단어수로 TOP10 곡명 출력
def sort_fn2(song_list):
    count_words = lambda song_dict: len(song_dict["title"].split())
    return count_words(song_list)


counted_dict = sorted(song_list, reverse=True, key=sort_fn2)[:10]

for song_dict in counted_dict:
    print(song_dict["title"])


# "좋아요" 수가 가장 많은 곡은? 가장 작은 곡은?
def max_min_fn3(song_list):
    return song_list["like"]


print(max(song_list, key=max_min_fn3)["title"])
print(min(song_list, key=max_min_fn3)["title"])


# "곡명" 단어수가 가장 많은 곡은? 가장 작은 곡은?
def max_min_fn4(song_list):
    count_words2 = lambda song_dict: len(song_dict["title"].split())
    return count_words2(song_list)


print(max(song_list, key=max_min_fn4)["title"])
print(min(song_list, key=max_min_fn4)["title"])


# "곡명" 글자수가 가장 많은 곡은? 가장 작은 곡은?
def max_min_fn5(song_list):
    count_letters = lambda song_dict: len(song_dict["title"])
    return count_letters(song_list)


print(max(song_list, key=max_min_fn5)["title"])
print(min(song_list, key=max_min_fn5)["title"])


# 멜론 TOP100 리스트에서 리스트에 랭크된 가수는 총 몇 팀인가요?
def map_fn6(song_list):
    artist = lambda song_dict: song_dict["artist"]
    return list(map(artist, song_list))


song_set = set(map_fn6(song_list))

print(len(song_set))


# 멜론 TOP100 리스트에서 2곡 이상 랭크된 가수는 몇 팀인가요?
def map_fn7(song_list):
    artist = lambda song_dict: song_dict["artist"]
    return list(map(artist, song_list))


TOP100_artist_list = map_fn7(song_list)

artist_dict = {
    artist: TOP100_artist_list.count(artist) for artist in TOP100_artist_list
}

filter_artist_dict = {
    artist: artist_dict[artist]
    for artist in artist_dict
    if int(artist_dict[artist]) > 1
}

print(len(filter_artist_dict))


# 멜론 TOP100 리스트에서 "방탄소년단"의 좋아요 총 합은?
def filter_fn8(song_list):
    return song_list["artist"] == "방탄소년단"


BTS_song_list = filter(filter_fn8, song_list)

acc8 = 0

for song_dict in BTS_song_list:
    acc8 += song_dict["like"]

print(acc8)
