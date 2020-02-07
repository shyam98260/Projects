from datetime import date
from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from mysql.connector import Error
from student import student
from admin import admin




admin_login = 0
admin_username = 0
admin_password = 0

student_login = 0
student_username = 0
studnet_password = 0

try:
    tdate = date.today()
    day = tdate.day
    month = tdate.month
    year = tdate.year
    print(day, ' ', month, " ", year)
    dddd = "" + str(day) + "-" + str(month) + "-" + str(year) + ""
    connection = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
    if connection.is_connected():
        cursor = connection.cursor()
        f_date = date(int(year), int(month), int(day))



        query = "select * from issue_book"
        cursor.execute(query)
        details = cursor.fetchall()
        for cc in details:
            llll = cc[9]
            c = llll[len(llll) - 4:]
            a = ''
            b = ''
            for x in llll[0:2]:
                if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
                    a = a + x
            for x in llll[len(llll) - 7:len(llll) - 4]:
                if x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '0':
                    b = b + x
            no_late = 0
            l_date = date(int(c), int(b), int(a))
            delta = l_date - f_date
            kkk = delta.days
            kkk = abs(kkk)
            if l_date < f_date:
                query = "update issue_book set fine_amount=\'"+str((int(kkk)*5))+"\' where enrollment_no=\'"+str(cc[0])+"\' and b_id=\'"+str(cc[3])+"\'"
                cursor.execute(query)
                connection.commit()







        t = Tk()
        t.geometry('500x300')
        t.resizable(False, False)

        label_1 = Label(t, text="UserName", width=20, font=("Arial", 10))
        label_1.place(x=80, y=130)
        entry_1 = Entry(t, font=('Arial'))
        entry_1.place(x=240, y=130)

        label_2 = Label(t, text="Password", width=20, font=("Arial", 10))
        label_2.place(x=80, y=170)
        entry_2 = Entry(t, font=('Arial'), show='*')
        entry_2.place(x=240, y=170)

        v = IntVar()

        rb = Radiobutton(t, text='Admin', variable=v, value=1, anchor=CENTER)
        rb.pack(anchor=CENTER)

        rbb = Radiobutton(t, text='Student', variable=v, value=2, anchor=CENTER)
        rbb.pack(anchor=CENTER)



        def submit():
            who = int(v.get())
            if who == 0:
                print(showerror('ShowError', 'Please Select Admin Or Student'))
                llll = len(entry_1.get())
                entry_1.delete(0, llll)
                llll = len(entry_2.get())
                entry_2.delete(0, llll)
            elif who == 1:
                if entry_1.get()!='':
                    if entry_2.get()!='':
                        query = "select * from admin where username=\'" + str(entry_1.get()) + "\' "
                        cursor.execute(query)
                        all_details = cursor.fetchall()
                        if len(all_details)>0:
                            query = "select * from admin where username=\'" + str(entry_1.get()) + "\' and password=  \'" + str(entry_2.get()) + "\' "
                            cursor.execute(query)
                            all_details = cursor.fetchall()
                            if len(all_details)>0:
                                all_details = all_details[0]
                                t.destroy()
                                admin(all_details[0],all_details[1])
                            else:
                                print(showerror('ShowError', 'Please Enter Right Password'))
                                llll = len(entry_2.get())
                                entry_2.delete(0, llll)
                        else:
                            print(showerror('ShowError', 'Please Enter valid username'))
                            llll = len(entry_1.get())
                            entry_1.delete(0, llll)
                            llll = len(entry_2.get())
                            entry_2.delete(0, llll)
                    else:
                        print(showerror('ShowError', 'Please Enter Password'))
                else:
                    print(showerror('ShowError', 'Please Enter Username'))
            elif who == 2:
                if entry_1.get() != '':
                    if entry_2.get() != '':
                        query = "select * from student where enrollment_no=\'" + str(entry_1.get()) + "\' "
                        cursor.execute(query)
                        all_details = cursor.fetchall()
                        if len(all_details) > 0:
                            query = "select * from student where enrollment_no=\'" + str(entry_1.get()) + "\' and password=  \'" + str(entry_2.get()) + "\' "
                            cursor.execute(query)
                            all_details = cursor.fetchall()
                            if len(all_details) > 0:
                                all_details = all_details[0]
                                t.destroy()
                                student(all_details[0],all_details[6])
                            else:
                                print(showerror('ShowError', 'Please Enter Right Password'))
                                llll = len(entry_2.get())
                                entry_2.delete(0, llll)
                        else:
                            print(showerror('ShowError', 'Please Enter valid username'))
                            llll = len(entry_1.get())
                            entry_1.delete(0, llll)
                            llll = len(entry_2.get())
                            entry_2.delete(0, llll)
                    else:
                        print(showerror('ShowError', 'Please Enter Password'))
                else:
                    print(showerror('ShowError', 'Please Enter Username'))




        Button(t, text='Submit', width=15, bg='brown', fg='white',command=submit).place(x=260, y=220)

        label_0 = Label(t, text="Login", width=20, font=("bold", 20))

        label_0.place(x=90, y=53)
        t.mainloop()


except Error as e:
    print('This is not opeating',e)

