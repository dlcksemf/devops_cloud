from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("입력관련 연습")

# 프레임 : 영역을 나누기
# 엔트리 : 입력상자 (사용자에게 입력 받는 <input type=text>)
# 리스트박스 : 목록 (겨로가 화면 여러개의 row를 표현해야 할 때)

# 프레임으로 upFrame, downFrame으로 나눠서 영역을 사용
# background, relief/bd(border)
upFrame = Frame(window)
upFrame.pack()

midFrame = Frame(window)
midFrame.pack()

downFrame = Frame(window)
downFrame.pack()

# 입력상자를 upFrame에 배치
editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

# 버튼을 midFrame에 배치
button = Button(midFrame, text='중간')
button.pack(padx=20, pady=20)

# 리스트박스는 downFrame에 배치
listBox = Listbox(downFrame)
listBox.pack()

# 리스트 박스에 값 입력
listBox.insert(END, "하나")
listBox.insert(END, "둘")
listBox.insert(END, "셋")

window.mainloop()
