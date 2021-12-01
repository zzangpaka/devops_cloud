import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk


def choiceData():
    conn = None
    cur = None

    Country = edt1.get()
    City = edt2.get()
    Land = edt3.get()

    (
        lCountry,
        lCity,
        lLand,
        lEmbassy,
        lAddr,
        lTelnum,
        lEmergTel,
        lWorkTime,
        lLunchTime,
        lMemo,
    ) = ([], [], [], [], [], [], [], [], [], [])

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )
    # 커서
    cur = conn.cursor()

    # 데이터 초기화

    lCountry.append("나라")
    lCountry.append("— - — - — - — - — - — - — - — - — - — - ")

    lCity.append("도시")
    lCity.append("— - — - — - — - — - — - — - — - — - — -")

    lLand.append("대륙")
    lLand.append("— - — - — - — - — - — - — - — - — - — -")

    lEmbassy.append("대사관")
    lEmbassy.append("— - — - — - — - — - — - — - — - — - — -")

    lAddr.append("주소")
    lAddr.append("— - — - — - — - — - — - — - — - — - — -")

    lTelnum.append("민원전화")
    lTelnum.append("— - — - — - — - — - — - — - — - — - — -")

    lEmergTel.append("응급전화")
    lEmergTel.append("— - — - — - — - — - — - — - — - — - — -")

    lWorkTime.append("운영시간")
    lWorkTime.append("— - — - — - — - — - — - — - — - — - — -")

    lLunchTime.append("점심시간")
    lLunchTime.append("— - — - — - — - — - — - — - — - — - — -")

    lMemo.append("기타사항")
    lMemo.append("— - — - — - — - — - — - — - — - — - — -")

    # Select 기능 구현
    sql = (
        "SELECT Country, City, Land, Embassy, Addr, Telnum, EmergTel, WorkTime, LunchTime, Memo FROM embassyTBL WHERE Country = '"
        + Country
        + "' OR City = '"
        + City
        + "' OR Land = '"
        + Land
        + "' ORDER BY Country, City, Land ASC"
    )
    cur.execute(sql)

    try:  # 오류가 발생하면 except 구문으로 들어감.
        cur.execute(sql)
    except:  # 오류가 났을 때 프로그램 강제 종류를 막고 유지하기 위해
        messagebox.showwarning("입력 오류", "아무것도 적히지 않았어요.")
    else:
        # 쿼리 실행이 완료(오류 없이)
        # 1) 메시지박스로 성공 알림
        messagebox.showinfo("조회 성공", "조회가 완료되었습니다!")

    while True:
        row = cur.fetchone()

        if row == None:
            break
        lCountry.append(row[0])
        lCity.append(row[1])
        lLand.append(row[2])
        lEmbassy.append(row[3])
        lAddr.append(row[4])
        lTelnum.append(row[5])
        lEmergTel.append(row[6])
        lWorkTime.append(row[7])
        lLunchTime.append(row[8])
        lMemo.append(row[9])

    # GUI ListBox에 insert
    # 1) 리스트 박스 초기화(기존 데이터 삭제)
    listCountry.delete(0, listCountry.size() - 1)
    listCity.delete(0, listCity.size() - 1)
    listLand.delete(0, listLand.size() - 1)
    listEmbassy.delete(0, listEmbassy.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)
    listTelnum.delete(0, listTelnum.size() - 1)
    listEmergTel.delete(0, listEmergTel.size() - 1)
    listWorkTime.delete(0, listWorkTime.size() - 1)
    listLunchTime.delete(0, listLunchTime.size() - 1)
    listMemo.delete(0, listMemo.size() - 1)

    # 2) select 해온 데이터 insert
    for (item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,) in zip(
        lCountry,
        lCity,
        lLand,
        lEmbassy,
        lAddr,
        lTelnum,
        lEmergTel,
        lWorkTime,
        lLunchTime,
        lMemo,
    ):
        listCountry.insert(END, item1)
        listCity.insert(END, item2)
        listLand.insert(END, item3)
        listEmbassy.insert(END, item4)
        listAddr.insert(END, item5)
        listTelnum.insert(END, item6)
        listEmergTel.insert(END, item7)
        listWorkTime.insert(END, item8)
        listLunchTime.insert(END, item9)
        listMemo.insert(END, item10)

    conn.close()


def selectData():
    conn = None
    cur = None

    (
        lCountry,
        lCity,
        lLand,
        lEmbassy,
        lAddr,
        lTelnum,
        lEmergTel,
        lWorkTime,
        lLunchTime,
        lMemo,
    ) = ([], [], [], [], [], [], [], [], [], [])

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )
    # 커서
    cur = conn.cursor()

    # 데이터 초기화

    lCountry.append("나라")
    lCountry.append("— - — - — - — - — - — - — - — - — - — - ")

    lCity.append("도시")
    lCity.append("— - — - — - — - — - — - — - — - — - — -")

    lLand.append("대륙")
    lLand.append("— - — - — - — - — - — - — - — - — - — -")

    lEmbassy.append("대사관")
    lEmbassy.append("— - — - — - — - — - — - — - — - — - — -")

    lAddr.append("주소")
    lAddr.append("— - — - — - — - — - — - — - — - — - — -")

    lTelnum.append("민원전화")
    lTelnum.append("— - — - — - — - — - — - — - — - — - — -")

    lEmergTel.append("응급전화")
    lEmergTel.append("— - — - — - — - — - — - — - — - — - — -")

    lWorkTime.append("운영시간")
    lWorkTime.append("— - — - — - — - — - — - — - — - — - — -")

    lLunchTime.append("점심시간")
    lLunchTime.append("— - — - — - — - — - — - — - — - — - — -")

    lMemo.append("기타사항")
    lMemo.append("— - — - — - — - — - — - — - — - — - — -")

    # Select 기능 구현
    sql = (
        "SELECT Country, City, Land, Embassy, Addr, Telnum, EmergTel, WorkTime, LunchTime, Memo FROM embassyTBL "
        "ORDER BY Country, City, Land ASC"
    )
    cur.execute(sql)

    while True:
        row = cur.fetchone()

        if row == None:
            break
        lCountry.append(row[0])
        lCity.append(row[1])
        lLand.append(row[2])
        lEmbassy.append(row[3])
        lAddr.append(row[4])
        lTelnum.append(row[5])
        lEmergTel.append(row[6])
        lWorkTime.append(row[7])
        lLunchTime.append(row[8])
        lMemo.append(row[9])

    # GUI ListBox에 insert
    # 1) 리스트 박스 초기화(기존 데이터 삭제)
    listCountry.delete(0, listCountry.size() - 1)
    listCity.delete(0, listCity.size() - 1)
    listLand.delete(0, listLand.size() - 1)
    listEmbassy.delete(0, listEmbassy.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)
    listTelnum.delete(0, listTelnum.size() - 1)
    listEmergTel.delete(0, listEmergTel.size() - 1)
    listWorkTime.delete(0, listWorkTime.size() - 1)
    listLunchTime.delete(0, listLunchTime.size() - 1)
    listMemo.delete(0, listMemo.size() - 1)

    # 2) select 해온 데이터 insert
    for (item1, item2, item3, item4, item5, item6, item7, item8, item9, item10,) in zip(
        lCountry,
        lCity,
        lLand,
        lEmbassy,
        lAddr,
        lTelnum,
        lEmergTel,
        lWorkTime,
        lLunchTime,
        lMemo,
    ):
        listCountry.insert(END, item1)
        listCity.insert(END, item2)
        listLand.insert(END, item3)
        listEmbassy.insert(END, item4)
        listAddr.insert(END, item5)
        listTelnum.insert(END, item6)
        listEmergTel.insert(END, item7)
        listWorkTime.insert(END, item8)
        listLunchTime.insert(END, item9)
        listMemo.insert(END, item10)

    conn.close()


def backFrame():
    editFrame.pack()
    listFrame3.pack_forget()


def noticeData():
    conn = None
    cur = None

    editFrame.pack_forget()
    listFrame3.pack(fill=BOTH, expand=1)

    lfocus, lcallNum = [], []

    # 데이터베이스 접속
    conn = pymysql.connect(
        host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8"
    )

    # 커서
    cur = conn.cursor()
    # 데이터 초기화
    lfocus.append("공지사항")
    lfocus.append(
        "— - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — -"
    )

    lcallNum.append("24시간 영사콜센터")
    lcallNum.append(
        "— - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — - — -"
    )

    # select 기능 구현
    sql = "SELECT focus, callNum from noticeTBL"
    cur.execute(sql)

    while True:
        row = cur.fetchone()  # db에서 가져온 값

        if row == None:
            break
        lfocus.append(row[0])  # db에서 가져온 값
        lcallNum.append(row[1])

    # GUI ListBox에 insert
    # 1) 리스트 박스 초기화(기존 데이터 삭제)
    listfocus.delete(0, listfocus.size() - 1)  # listUserID는 gui
    listcallNum.delete(0, listcallNum.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2 in zip(lfocus, lcallNum):
        listfocus.insert(END, item1)
        listcallNum.insert(END, item2)

    conn.close()


# GUI 화면 구성
window = Tk()
window.geometry("1300x700")
window.title("해외 주재 대한민국 대사관 정보")

editFrame = Frame(window)
editFrame.pack()


listFrame1 = Frame(window)
listFrame1.pack(side=TOP, fill=BOTH, expand=1)

listFrame2 = Frame(window)
listFrame2.pack(side=BOTTOM, fill=BOTH, expand=1)

listFrame3 = Frame(window)
listFrame3.pack(fill=BOTH, expand=1)
listFrame3.pack_forget()

label1 = Label(editFrame, text="나라")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=30)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="도시")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=30)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="대륙")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=30)
edt3.pack(side=LEFT, padx=10, pady=10)


# 버튼
btnSelect = Button(editFrame, text="선택", command=choiceData)
btnSelect.pack(side=LEFT, padx=15, pady=15)

btnSelect = Button(editFrame, text="전체", command=selectData)
btnSelect.pack(side=LEFT, padx=15, pady=15)

btnSelect = Button(editFrame, text="공지", command=noticeData)
btnSelect.pack(side=LEFT, padx=15, pady=15)


listCountry = Listbox(listFrame1)
listCountry.pack(side=LEFT, fill=BOTH, expand=1)

listEmbassy = Listbox(listFrame2)
listEmbassy.pack(side=LEFT, fill=BOTH, expand=1)

listCity = Listbox(listFrame1)
listCity.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame2)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

listLand = Listbox(listFrame1)
listLand.pack(side=LEFT, fill=BOTH, expand=1)

listTelnum = Listbox(listFrame2)
listTelnum.pack(side=LEFT, fill=BOTH, expand=1)

listWorkTime = Listbox(listFrame1)
listWorkTime.pack(side=LEFT, fill=BOTH, expand=1)

listEmergTel = Listbox(listFrame2)
listEmergTel.pack(side=LEFT, fill=BOTH, expand=1)

listLunchTime = Listbox(listFrame1)
listLunchTime.pack(side=LEFT, fill=BOTH, expand=1)

listMemo = Listbox(listFrame2)
listMemo.pack(side=LEFT, fill=BOTH, expand=1)

listfocus = Listbox(listFrame3)
listfocus.pack(side=LEFT, fill=BOTH, expand=1)

listcallNum = Listbox(listFrame3)
listcallNum.pack(side=LEFT, fill=BOTH, expand=1)


btnBack = Button(listFrame3, text="뒤로가기", command=backFrame)
btnBack.pack(side=LEFT, padx=10, pady=10)


def createNewWindow():
    notice = tk.Toplevel(app)
    labelExample = tk.Label(notice, text="공지사항")
    buttonExample = tk.Button(notice, text="공지")

    labelExample.pack()
    buttonExample.pack()


app = tk.Tk()
buttonExample = tk.Button(app, text="공지", command=createNewWindow)
buttonExample.pack()

app.mainloop()


window.mainloop()
