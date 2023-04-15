import tkinter
import mysql.connector
from pathlib import Path
from sql_connector import select_sub
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox


def page3(result,subcode='23CPP'):
    no_corr_ans=0
    ques_no = 1
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/parthagarwal/Desktop/build/assets3/frame0")
    def update(j):
        canvas2.itemconfig(ques,text=questions[j][0])
        str1.set(questions[j][1])
        str2.set(questions[j][2])
        str3.set(questions[j][3])
        str4.set(questions[j][4])

    def next(ans,j):
        if j<6:
            if j != 0:
                corr_ans = questions[j - 1][5][-1]
            nonlocal ques_no,no_corr_ans
            ques_no+=1
            if ans==corr_ans:
                print("correct")
                no_corr_ans+=1
            else:
                print("wrong")
        if j<5:
            update(j)


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    questions=select_sub(sub_code=subcode)

    canvas2 = Canvas(
        window,
        bg="#FFFFFF",
        height=832,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas2.place(x=0, y=0)
    canvas2.create_rectangle(
        0.0,
        0.0,
        1280.0,
        99.0,
        fill="#4292F3",
        outline="")

    canvas2.create_text(
        33.0,
        19.0,
        anchor="nw",
        text=result[1],
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 32 * -1)
    )
    if result[0]=='stu': desig = 'Student'
    else: desig = 'Teacher'
    canvas2.create_text(
        33.0,
        61.0,
        anchor="nw",
        text=desig,
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas2.create_text(
        1131.0,
        61.0,
        anchor="nw",
        text=subcode,
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas2.create_text(
        1131.0,
        24.0,
        anchor="nw",
        text=f"STD -{result[2]}",
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 28 * -1)
    )

    ques = canvas2.create_text(
        92.0,
        151.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("RobotoRoman Regular", 32 * -1),
        width=1120

    )

    str1=tkinter.StringVar(value='')
    button_1 = Button(
        canvas2,
        textvariable=str1,
        borderwidth=0,
        font=("RobotoRoman Regular", 20 * -1),
        highlightthickness=0,
        wraplength=1050,
        command=lambda: next('1',j=ques_no),
        relief="flat"
    )
    button_1.place(
        x=68.0,
        y=346.0,
        width=1143.0,
        height=94.0
    )
    str3 = tkinter.StringVar(value="")
    button_3 = Button(
        canvas2,
        textvariable=str3,
        borderwidth=0,
        highlightthickness=0,
        font=("RobotoRoman Regular", 20 * -1),
        command=lambda: next('3',j=ques_no),
        wraplength=1050,
        relief="flat"
    )
    button_3.place(
        x=68.0,
        y=584.0,
        width=1143.0,
        height=94.0
    )
    str4 = tkinter.StringVar(value="")
    button_4 = Button(
        canvas2,
        borderwidth=0,
        textvariable=str4,
        highlightthickness=0,
        font=("RobotoRoman Regular", 20 * -1),
        command=lambda: next('4',j=ques_no),
        wraplength=1050,
        relief="flat"
    )
    button_4.place(
        x=68.0,
        y=703.0,
        width=1143.0,
        height=94.0
    )
    str2 = tkinter.StringVar(value="")
    button_2 = Button(
        canvas2,
        borderwidth=0,
        textvariable=str2,
        highlightthickness=0,
        font=("RobotoRoman Regular", 20 * -1),
        command=lambda: next('2',j=ques_no),
        wraplength=1050,
        relief="flat"
    )
    button_2.place(
        x=68.0,
        y=465.0,
        width=1143.0,
        height=94.0
    )

    update(0)



    window.resizable(False, False)
    window.mainloop()


def page2(result):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/parthagarwal/Desktop/build/assets2/frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas1 = Canvas(
        window,
        bg="#FFFFFF",
        height=832,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas1.place(x=0, y=0)
    canvas1.create_rectangle(
        0.0,
        0.0,
        1280.0,
        99.0,
        fill="#4292F3",
        outline="")

    canvas1.create_text(
        33.0,
        19.0,
        anchor="nw",
        text=result[1],
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 32 * -1)
    )
    if result[0]=='stu': desig = 'Student'
    else: desig = 'Teacher'
    canvas1.create_text(
        33.0,
        61.0,
        anchor="nw",
        text=desig,
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 20 * -1)
    )

    canvas1.create_text(
        33.0,
        175.0,
        anchor="nw",
        text="Welcome to the Exam Genie!",
        fill="#343434",
        font=("RobotoRoman Regular", 64 * -1)
    )

    canvas1.create_text(
        385.0,
        416.0,
        anchor="nw",
        text="Which subject u wanna study",
        fill="#343434",
        font=("RobotoItalic Regular", 40 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas1.create_image(
        183.0,
        595.25,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        canvas1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page3(result,subcode="23CPP"),
        relief="flat"
    )
    button_1.place(
        x=193.0,
        y=509.0,
        width=245.0,
        height=245.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        canvas1,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page3(result,subcode='23PYPY'),
        relief="flat"
    )
    button_2.place(
        x=518.0,
        y=509.0,
        width=245.0,
        height=245.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        canvas1,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: page3(result,subcode='23MA'),
        relief="flat"
    )
    button_3.place(
        x=843.0,
        y=509.0,
        width=245.0,
        height=245.0
    )

    canvas1.create_text(
        33.0,
        264.0,
        anchor="nw",
        text="Your exam preparation journey begins here",
        fill="#343434",
        font=("RobotoRoman Regular", 32 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas1.create_image(
        1089.0,
        291.5,
        image=image_image_2
    )
    canvas1.create_text(
        1131.0,
        40.0,
        anchor="nw",
        text=f"STD -{result[2]}",
        fill="#FFFFFF",
        font=("RobotoRoman Regular", 28 * -1)
    )
    window.resizable(False, False)
    window.mainloop()


def login(event):
    conn = mysql.connector.connect(host = 'localhost',user ='root',passwd = "Qseytak144469@",database='ques_data')
    cur = conn.cursor()
    uname = entry_2.get()
    pswd = entry_1.get()
    qry = "SELECT * FROM login WHERE username = %s AND password1=%s AND desig=%s"
    cur.execute(qry,(uname,pswd,event))
    result = cur.fetchall()
    if result:
        if event=='stu':
            page2(result[0][2:])
        else:
            messagebox.showinfo("Status", "Login successful")
        window.destroy()
        return True
    else:
        messagebox.showinfo("Status","Login Unsuccessful")
        return False


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/parthagarwal/Desktop/build/assets1/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def on_enter_user(event):
    if entry_2.get()=='Username':
        entry_2.delete(0,tkinter.END)
def on_enter_pass(event):
    if entry_1.get()=='Password':
        entry_1.delete(0,tkinter.END)



window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1280.0,
    832.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    945.0,
    416.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    376.0,
    419.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    986.0,
    377.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    986.0,
    470.0,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    967.5,
    471.0,
    image=entry_image_1
)
entry_1 = Entry(#password
    window,
    bd=0,
    bg="#FFFFFF",
    font=("Roboto",16),
    fg="#000716",
    highlightthickness=0,
    show='*'
)
entry_1.place(
    x=847.0,
    y=453.0,
    width=241.0,
    height=34.0
)
entry_1.insert(
    0,
    'Password'
)
entry_1.bind(
    '<FocusIn>',
    on_enter_pass
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    967.5,
    378.0,
    image=entry_image_2
)
entry_2 = Entry(#username
    window,
    bd=0,
    bg="#FFFFFF",
    font=("Roboto",16),
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=847.0,
    y=360.0,
    width=241.0,
    height=34.0
)
entry_2.insert(
    0,
    'Username'
)
entry_2.bind(
    '<FocusIn>',
    on_enter_user
)

button_image_1 = PhotoImage(#login as teacher
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login('teach'),
    relief="flat",
    cursor='hand2'
)
button_1.place(
    x=995.0,
    y=551.0,
    width=149.0,
    height=55.0
)

button_image_2 = PhotoImage(#login as student
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login('stu'),
    relief="flat",
    cursor='hand2'
)
button_2.place(
    x=826.0,
    y=553.0,
    width=148.16162109375,
    height=54.42034912109375
)

canvas.create_text(
    882.0,
    224.0,
    anchor="nw",
    text="Log In",
    fill="#2C2C2C",
    font=("Helvetica Bold", 58 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1117.0,
    378.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1117.0,
    472.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
