# def reorderLogFiles(self, logs: List[str]) -> List[str]:
#     letters, digits = [], []
#     for log in logs:
#         if log.split()[1].isdigit():
#             digits.append(log)
#         else:
#             letters.append(log)

#     letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

#     return letters + digits


def reorderLogFiles(logs):

    def get_key(log):
        _id, rest = log.split(" ", maxsplit=1)
        print(_id, rest)
        return (0, rest, _id) if rest[0].isalpha() else (1, )

    return sorted(logs, key=get_key)


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

print(reorderLogFiles(logs))
