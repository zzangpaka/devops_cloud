from tkinter import *
from tkinter import messagebox


def clickButton():
    messagebox.showinfo("버튼 클릭", "버튼을 클릭했습니다")


window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("500x500")

upFrame = Frame(window)
upFrame.pack()

midFrame = Frame(window)
midFrame.pack()

downFrame = Frame(window)
downFrame.pack()


editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

button = Button(window, text="요기 눌러요", fg="red", bg="yellow", command=clickButton)

listBox = Listbox(downFrame)
listBox.pack()


editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

button = Button(midFrame, text="중간")
button.pack(padx=20, pady=20)

listBox = Listbox(downFrame)
listBox.pack()

listBox.insert(END, "하나")
listBox.insert(END, "둘")
listBox.insert(END, "셋")

# window.title("윈도창 연습")
# window.geometry("400x100")  # 넓이 * 높이
# window.resizable(width=FALSE, height=FALSE) # 윈도우 사이즈 고정

# 라벨 연습
label1 = Label(window, text="This is MariaDB를")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")
label3 = Label(window, text="공부 중입니다.", bg="magenta", width=20, height=5, anchor=SE)
# # 부모 윈도우, 출력될 글, 설정 : Font, fg=글자색, bg=배경색, anchor=글자의 위치(N, NE, E, SE, S, SW, W, NW, CENTER)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
