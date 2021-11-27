from tkinter import *
from tkinter import messagebox

# 버튼을 사용하여 알림 창 띄우기
def clickButton() :
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.') # messagebox 타이틀, messagebox 내용

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text='요기 눌러요', command=clickButton)
button2 = Button(window, text='요기 눌러요', command=clickButton)
button3 = Button(window, text='요기 눌러요', command=clickButton)

# 정렬 : TOP, RIGHT, LEFT, BOTTOM
# 여백: padx/pady
button1.pack(side=LEFT, padx=10, pady=10)
button2.pack(side=LEFT, padx=10, pady=10)
button3.pack(side=LEFT, padx=10, pady=10)

window.mainloop()
