def get_word_count(response):
    return len(response.split())


def get_ch_count(response):
    count = 0
    for ch in response:
        if ch != " ":
            count += 1
    return count


def round_thousand(number):
    return (number // 1000) * 1000


answer = input("문자열을 입력하세요 -> ")

print(get_word_count(answer))
print(get_ch_count(answer))
print(round_thousand(1234567))
