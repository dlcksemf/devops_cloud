import collections

# 1 리스트로 변환


def isPalindrome(self, s: str) -> bool:
    strs = [char.lower() for char in s if char.isalnum()]

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

# 2 데크 자료형을 이용


def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 3 슬라이싱 사용


def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


def Palindrome(word: str) -> bool:
    char_list = [char.lower() for char in word if char.isalnum()]
    return char_list == char_list[::-1]


word = "A man, a plan, a canal: Panama"
if Palindrome(word):
    print("It's a Palindrome!")
else:
    print("It's not a Palindrome..")
