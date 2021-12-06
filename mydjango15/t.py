# 포스팅 : 제목, 내용, 글쓴이

# 튜플 -> 인덱스로 접근 -> 인덱스에 대한 정보 필요 (가장 1차원적)
# 정보 수정 불가능 -> 정보 중간에 넣기 불가 (순서 의미있게 지정 불가)
post = ("제목", "내용", "글쓴이")
post[0]
post[1] # ...


# 네임드 튜플
from collections import namedtuple

Post = namedtuple('Post', 'title content author_name')
post = Post("제목", "내용", "글쓴이")
post[0] / post[1] / post[2] / ...
post.title / post.content / post.author_name

def check_content(content:str) -> bool:
	if len(content) == 0:
		# error ...
		pass
	# ...

# 클래스 / CapitalCase
class Post:
	# 생성자 (Constructor)
	def __init__(self, title, content, author_name):
		self.title = title # 둘이 다른 변수
		self.content = content
		self.author_name = author_name

	def check_content(self):
		if len(self.content) == 0:
			# error ...
			pass


post = Post("제목", "내용", "글쓴이")
post.title
post.content
post.author_name
post.check_content()
