from tkinter import *
from tkinter import messagebox


def clickButton():
    messagebox.showinfo("버튼 클릭", "버튼을 클릭했습니다")


window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text="요기 눌러요", fg="red", bg="yellow", command=clickButton)
button2 = Button(window, text="요기 눌러요", fg="red", bg="yellow", command=clickButton)
button3 = Button(window, text="요기 눌러요", fg="red", bg="yellow", command=clickButton)

button1.pack(side=LEFT, padx=10, pady=10)  # RIGHT, TOP, BOTTOM
button2.pack(side=LEFT, padx=5, pady=10)
button3.pack(side=LEFT, padx=10, pady=10)

window.mainloop()
