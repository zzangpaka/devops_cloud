import random
import pymysql
from tkinter import *
from tkinter import messagebox

# 데이터베이스 연동 함수
def insertData():
    conn = None
    cur = None

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()

    # 회원 정보 insert 기능 구현
    # 사용자에게 입력 받은 회원 정보 초기화
    Menu, Member = "", ""

    # GUI에서 입력한 데이터 담기
    Menu = edt1.get()
    Member = edt2.get()

    # SQL 쿼리 만들기
    sql = ""
    sql = (
        "INSERT INTO randomTBL (Menu, Member) VALUES"
        "('" + Menu + "', '" + Member + "')"
    )
    # 쿼리 실행
    try:
        cur.execute(sql)
    except:
        messagebox.showerror("오잉?", "다시 한 번 써주세요.")
    else:
        # 쿼리 실행이 완료 (오류없이)
        # 1) 메시지박스로 성공 알림
        messagebox.showinfo("꿀꿀", "메뉴가 등록 되었습니다.")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")

    # DB 접속 종료
    conn.close()


def selectData():
    conn = None
    cur = None

    lMenu, lMember = [], []

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )
    # 커서
    cur = conn.cursor()

    # 데이터 초기화
    lMenu.append("메뉴명")
    lMenu.append("---------")

    lMember.append("추천인")
    lMember.append("---------")

    # Select 기능 구현
    sql = "SELECT Menu, Member FROM randomTBL ORDER BY Menu ASC"
    cur.execute(sql)

    while True:
        row = cur.fetchone()

        if row == None:
            break
        lMenu.append(row[0])
        lMember.append(row[1])

    # GUI ListBox에 insert
    # 1) 리스트 박스 초기화(기존 데이터 삭제)
    listMenu.delete(0, listMenu.size() - 1)
    listMember.delete(0, listMember.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2 in zip(lMenu, lMember):
        listMenu.insert(END, item1)
        listMember.insert(END, item2)

    conn.close()


def randomData():
    conn = None
    cur = None

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )
    # 커서
    cur = conn.cursor()

    # Select 기능 구현
    sql = "SELECT Menu FROM randomTBL"
    cur.execute(sql)

    random.choice(Menu)

    try:
        cur.execute(sql)
    except:
        messagebox.showerror("오류발생!", "껐다 켜주세요.")
    else:
        # 쿼리 실행이 완료 (오류없이)
        # 1) 메시지박스로 성공 알림
        messagebox.showinfo("냠냠", "'rMenu'로 정해졌어요!")
        # 2) 데이터 커밋 (진짜 저장)
        conn.commit()
        # 3) 테이블 조회 (새로고침)
        selectData()

    # GUI ListBox에 insert
    # 1) 리스트 박스 초기화(기존 데이터 삭제)
    listMenu.delete(0, listMenu.size() - 1)
    listMember.delete(0, listMember.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2 in zip(rMenu, rMember):
        listMenu.insert(END, item1)
        listMember.insert(END, item2)

    conn.close()


# GUI 화면 구성
window = Tk()
window.geometry("600x500")
window.resizable(width=FALSE, height=FALSE)
window.title("Random Menu 고르기!")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
# listFrame.pack_forget()

label1 = Label(editFrame, text="먹고 싶은 메뉴")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="먹고 싶은 사람")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)


# 버튼
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text="뽑기", command=randomData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

listMenu = Listbox(listFrame)
listMenu.pack(side=LEFT, fill=BOTH, expand=1)

listMember = Listbox(listFrame)
listMember.pack(side=LEFT, fill=BOTH, expand=1)


window.mainloop()
