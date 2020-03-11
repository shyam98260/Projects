from datetime import date
from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from mysql.connector import Error
from student import student
from admin import admin
# from PIL import Image,ImageTk
import datetime
import calendar
from datetime import datetime as pappu
from get_pakka_time import mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
from Captcha import generate_captcha




admin_login = 0
admin_username = 0
admin_password = 0

student_login = 0
student_username = 0
studnet_password = 0

try:
    this_is_main_part = generate_captcha()
    tdate = date.today()
    day = tdate.day
    month = tdate.month
    year = tdate.year
    print(day, ' ', month, " ", year)

    kkkkkkkkkk = "" + str(day) + " " + str(month) + " " + str(year) + ""
    def findDay(date):
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])

    mmmmmmmmm = {1:' Jan',2:' Feb',3:' Mar',4:' Apr',5:' May',6:' June',7:' July',8:' Aug',9:' Sep',10:' Oct',11:' Nov',12:' Dec'}
    dddd = str(findDay(kkkkkkkkkk))+" , " + str(day) + mmmmmmmmm[int(month)]#"-" + str(month) + "-" + str(year) + ""
    connection = mysql.connector.connect(host='localhost',database='library',user='root',password='root')
    if connection.is_connected():
        cursor = connection.cursor()
        f_date = date(int(year), int(month), int(day))


        # This would genrate the fine automatically when it will run
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




        # This Would Calculate the age of student automattically when it will run
        query = "select * from student"
        cursor.execute(query)
        details_of_student = cursor.fetchall()
        for x in details_of_student:
            llll = x[9]
            c = llll[len(llll) - 4:]
            a = ''
            b = ''
            for xx in llll[0:2]:
                if xx == '1' or xx == '2' or xx == '3' or xx == '4' or xx == '5' or xx == '6' or xx == '7' or xx == '8' or xx == '9' or xx == '0':
                    a = a + xx
            for yy in llll[len(llll) - 7:len(llll) - 4]:
                if yy == '1' or yy == '2' or yy == '3' or yy == '4' or yy == '5' or yy == '6' or yy == '7' or yy == '8' or yy == '9' or yy == '0':
                    b = b + yy

            l_date = date(int(c), int(b), int(a))
            delta = l_date - f_date
            new_year = (delta.days + delta.seconds / 86400) / 365.2425
            best_age = int(abs(new_year))
            print(best_age)
            query = "update student set age=\'" + str(best_age) + "\' where enrollment_no=\'" + str(x[0]) + "\'"
            cursor.execute(query)
            connection.commit()








        t = Tk()
        t.geometry('500x380')

        label_11 = Label(t, text=dddd,bg='#8FBC8F',fg='black', width=0, font=("bold", 11))
        label_11.place(x=390, y=0)
        t.resizable(False, False)




        label_1 = Label(t, text="UserName",bg='#8FBC8F',fg='black', width=20, font=("Arial", 10))
        label_1.place(x=80, y=130)
        entry_1 = Entry(t, font=('Arial'),bg='#F5DEB3',fg='#800080',insertbackground='red',bd=3)
        # entry_1.config(state=DISABLED)
        entry_1.place(x=240, y=130)




        label_2 = Label(t, text="Password",bg='#8FBC8F',fg='black', width=20, font=("Arial", 10))
        label_2.place(x=80, y=170)
        entry_2 = Entry(t, font=('Arial'), show='*',bg='#F5DEB3',fg='#800080',insertbackground='red',bd=3)
        entry_2.place(x=240, y=170)

        label_3 = Label(t, text="Captcha", bg='#8FBC8F', fg='black', width=20, font=("Arial", 10))
        label_3.place(x=80, y=260)
        entry_3 = Entry(t, font=('Arial'), bg='#F5DEB3', fg='#800080', insertbackground='red', bd=3)
        entry_3.place(x=240, y=260)




        v = IntVar()
        rb = Radiobutton(t, text='Admin',bg='#8FBC8F',fg='black', variable=v, value=1, anchor=CENTER,cursor='hand2')
        rb.pack(anchor=CENTER)
        rbb = Radiobutton(t, text='Student',bg='#8FBC8F',fg='black', variable=v, value=2, anchor=CENTER,cursor='hand2')
        rbb.pack(anchor=CENTER)

        def papa():
            global photo
            global this_is_main_part
            this_is_main_part = generate_captcha()
            photo = PhotoImage(file='shyam.png')
            Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                   image=photo).place(
                x=230, y=210)

        photo = PhotoImage(file='shyam.png')
        # label_2 = Label(t, bg='#8FBC8F', fg='black', width=200, font=("Arial", 10),image=photo)
        # label_2.place(x=230, y=210)
        Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
               image=photo).place(
            x=230, y=210)





        def submit(event):
            global photo
            global this_is_main_part
            who = int(v.get())
            if who == 0:
                print(showerror('ShowError', 'Please Select Admin Or Student'))
                llll = len(entry_1.get())
                entry_1.delete(0, llll)
                llll = len(entry_2.get())
                entry_2.delete(0, llll)
                this_is_main_part = generate_captcha()
                photo = PhotoImage(file='shyam.png')
                Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                       image=photo).place(
                    x=230, y=210)
                entry_3.delete(0, len(entry_3.get()))
                entry_1.delete(0, len(entry_1.get()))
                entry_2.delete(0, len(entry_2.get()))

            elif who == 1:
                if entry_1.get()!='':
                    if entry_2.get()!='':


                        query = "select * from admin where username=\'" + str(entry_1.get()) + "\' "
                        cursor.execute(query)
                        all_details = cursor.fetchall()
                        if len(all_details) <= 0:
                            query = "select * from librarian where username=\'" + str(entry_1.get()) + "\' "
                            cursor.execute(query)
                            all_details = cursor.fetchall()



                        if len(all_details)>0:
                            query = "select * from admin where username=\'" + str(entry_1.get()) + "\' and password=  \'" + str(entry_2.get()) + "\' "
                            cursor.execute(query)
                            all_details = cursor.fetchall()
                            if len(all_details)<=0:
                                query = "select * from librarian where username=\'" + str(
                                    entry_1.get()) + "\' and password=  \'" + str(entry_2.get()) + "\' "
                                cursor.execute(query)
                                all_details = cursor.fetchall()


                            if len(all_details)>0:
                                if entry_3.get()!='':
                                    if str(entry_3.get())==str(this_is_main_part):
                                        all_details = all_details[0]
                                        t.destroy()
                                        admin(all_details[0], all_details[1])
                                    else:
                                        entry_3.delete(0,len(entry_3.get()))
                                        entry_1.delete(0,len(entry_1.get()))
                                        entry_2.delete(0,len(entry_2.get()))
                                        this_is_main_part = generate_captcha()
                                        photo = PhotoImage(file='shyam.png')
                                        Button(t, width=190, bg='#BDB76B', fg='black', command=papa,
                                               cursor='hand2',
                                               image=photo).place(
                                            x=230, y=210)
                                else:
                                    showwarning('Warning','Please Write The Captcha')
                                    this_is_main_part = generate_captcha()
                                    photo = PhotoImage(file='shyam.png')
                                    Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                           image=photo).place(
                                        x=230, y=210)
                                    entry_3.delete(0, len(entry_3.get()))
                                    entry_1.delete(0, len(entry_1.get()))
                                    entry_2.delete(0, len(entry_2.get()))
                            else:
                                print(showerror('ShowError', 'Please Enter Right Password'))
                                llll = len(entry_2.get())
                                entry_2.delete(0, llll)
                                this_is_main_part = generate_captcha()
                                photo = PhotoImage(file='shyam.png')
                                Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                       image=photo).place(
                                    x=230, y=210)
                                entry_3.delete(0, len(entry_3.get()))
                                entry_1.delete(0, len(entry_1.get()))
                                entry_2.delete(0, len(entry_2.get()))
                        else:
                            print(showerror('ShowError', 'Please Enter valid username'))
                            llll = len(entry_1.get())
                            entry_1.delete(0, llll)
                            llll = len(entry_2.get())
                            entry_2.delete(0, llll)
                            this_is_main_part = generate_captcha()
                            photo = PhotoImage(file='shyam.png')
                            Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                   image=photo).place(
                                x=230, y=210)
                            entry_3.delete(0, len(entry_3.get()))
                            entry_1.delete(0, len(entry_1.get()))
                            entry_2.delete(0, len(entry_2.get()))
                    else:
                        print(showerror('ShowError', 'Please Enter Password'))
                        this_is_main_part = generate_captcha()
                        photo = PhotoImage(file='shyam.png')
                        Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                               image=photo).place(
                            x=230, y=210)
                        entry_3.delete(0, len(entry_3.get()))
                        entry_1.delete(0, len(entry_1.get()))
                        entry_2.delete(0, len(entry_2.get()))
                else:
                    print(showerror('ShowError', 'Please Enter Username'))
                    this_is_main_part = generate_captcha()
                    photo = PhotoImage(file='shyam.png')
                    Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                           image=photo).place(
                        x=230, y=210)
                    entry_3.delete(0, len(entry_3.get()))
                    entry_1.delete(0, len(entry_1.get()))
                    entry_2.delete(0, len(entry_2.get()))
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
                                if entry_3.get()!='':
                                    if str(entry_3.get())==str(this_is_main_part):
                                        all_details = all_details[0]
                                        t.destroy()
                                        student(all_details[0], all_details[6])
                                    else:
                                        entry_3.delete(0, len(entry_3.get()))
                                        entry_1.delete(0, len(entry_1.get()))
                                        entry_2.delete(0, len(entry_2.get()))
                                        this_is_main_part = generate_captcha()
                                        this_is_main_part = generate_captcha()
                                        photo = PhotoImage(file='shyam.png')
                                        Button(t, width=190, bg='#BDB76B', fg='black', command=papa,
                                               cursor='hand2',
                                               image=photo).place(
                                            x=230, y=210)
                                else:
                                    showwarning('Warning', 'Please Write The Captcha')
                                    this_is_main_part = generate_captcha()
                                    photo = PhotoImage(file='shyam.png')
                                    Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                           image=photo).place(
                                        x=230, y=210)
                                    entry_3.delete(0, len(entry_3.get()))
                                    entry_1.delete(0, len(entry_1.get()))
                                    entry_2.delete(0, len(entry_2.get()))
                            else:
                                print(showerror('ShowError', 'Please Enter Right Password'))
                                llll = len(entry_2.get())
                                entry_2.delete(0, llll)
                                this_is_main_part = generate_captcha()
                                photo = PhotoImage(file='shyam.png')
                                Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                       image=photo).place(
                                    x=230, y=210)
                                entry_3.delete(0, len(entry_3.get()))
                                entry_1.delete(0, len(entry_1.get()))
                                entry_2.delete(0, len(entry_2.get()))
                        else:
                            print(showerror('ShowError', 'Please Enter valid username'))
                            llll = len(entry_1.get())
                            entry_1.delete(0, llll)
                            llll = len(entry_2.get())
                            entry_2.delete(0, llll)
                            this_is_main_part = generate_captcha()
                            photo = PhotoImage(file='shyam.png')
                            Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                   image=photo).place(
                                x=230, y=210)
                            entry_3.delete(0, len(entry_3.get()))
                            entry_1.delete(0, len(entry_1.get()))
                            entry_2.delete(0, len(entry_2.get()))
                    else:
                        print(showerror('ShowError', 'Please Enter Password'))
                        this_is_main_part = generate_captcha()
                        photo = PhotoImage(file='shyam.png')
                        Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                               image=photo).place(
                            x=230, y=210)
                        entry_3.delete(0, len(entry_3.get()))
                        entry_1.delete(0, len(entry_1.get()))
                        entry_2.delete(0, len(entry_2.get()))
                else:
                    print(showerror('ShowError', 'Please Enter Username'))
                    this_is_main_part = generate_captcha()
                    photo = PhotoImage(file='shyam.png')
                    Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                           image=photo).place(
                        x=230, y=210)
                    entry_3.delete(0, len(entry_3.get()))
                    entry_1.delete(0, len(entry_1.get()))
                    entry_2.delete(0, len(entry_2.get()))

            elif who == 3:
                if entry_1.get()!='':
                    if entry_2.get()!='':
                        query = "select * from librarian where username=\'" + str(entry_1.get()) + "\' "
                        cursor.execute(query)
                        all_details = cursor.fetchall()
                        if len(all_details)>0:
                            query = "select * from librarian where username=\'" + str(entry_1.get()) + "\' and password=  \'" + str(entry_2.get()) + "\' "
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
                                this_is_main_part = generate_captcha()
                                photo = PhotoImage(file='shyam.png')
                                Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                       image=photo).place(
                                    x=230, y=210)
                                entry_3.delete(0, len(entry_3.get()))
                                entry_1.delete(0, len(entry_1.get()))
                                entry_2.delete(0, len(entry_2.get()))
                        else:
                            print(showerror('ShowError', 'Please Enter valid username'))
                            llll = len(entry_1.get())
                            entry_1.delete(0, llll)
                            llll = len(entry_2.get())
                            entry_2.delete(0, llll)
                            this_is_main_part = generate_captcha()
                            photo = PhotoImage(file='shyam.png')
                            Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                                   image=photo).place(
                                x=230, y=210)
                            entry_3.delete(0, len(entry_3.get()))
                            entry_1.delete(0, len(entry_1.get()))
                            entry_2.delete(0, len(entry_2.get()))
                    else:
                        print(showerror('ShowError', 'Please Enter Password'))
                        this_is_main_part = generate_captcha()
                        photo = PhotoImage(file='shyam.png')
                        Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                               image=photo).place(
                            x=230, y=210)
                        entry_3.delete(0, len(entry_3.get()))
                        entry_1.delete(0, len(entry_1.get()))
                        entry_2.delete(0, len(entry_2.get()))
                else:
                    print(showerror('ShowError', 'Please Enter Username'))
                    this_is_main_part = generate_captcha()
                    photo = PhotoImage(file='shyam.png')
                    Button(t, width=190, bg='#BDB76B', fg='black', command=papa, cursor='hand2',
                           image=photo).place(
                        x=230, y=210)
                    entry_3.delete(0, len(entry_3.get()))
                    entry_1.delete(0, len(entry_1.get()))
                    entry_2.delete(0, len(entry_2.get()))




        Button(t, text='Submit', width=15, bg='#BDB76B', fg='black',command=lambda :submit(''),cursor='hand2').place(x=260, y=320)

        # Button(t, text='', width=1, bg='#8FBC8F', fg='black', command=submit, cursor='hand2').place(x=440, y=170)

        label_0 = Label(t, text="Login", width=20,bg='#8FBC8F',fg='black', font=("Algerian", 20))
        label_0.place(x=90, y=73)
        t.title('Library Management System')
        # label_5 = Label(t, text="Login Page",bg='#8FBC8F',fg='black', width=20, font=("bold", 9))
        # label_5.place(x=390, y=280)
        p = PhotoImage(file="icon-login.png")
        t.iconphoto(False,p)
        t.configure(bg='#8FBC8F')

        t.bind('<Return>', submit)


        def update():  # take process bar for example
            gggg = str()
            now = pappu.now()
            current_time = now.strftime("%H:%M:%S")
            if int(current_time[:2]) > 12:
                gggg += str(int(current_time[:2]) - 12) + str(current_time[2:])
            else:
                gggg = current_time
            label_5 = Label(t, text=gggg, bg='#8FBC8F', fg='black', font=("bold", 15))
            label_5.place(x=0, y=0)
            t.after(1000, update)


        update()


        def mmmmmmmmmmmmm():
            print(mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm())
            label_11 = Label(t, text=mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm(), bg='#8FBC8F', fg='black', width=0,
                             font=("bold", 11))
            label_11.place(x=380 - len(mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm()), y=0)

            t.after(1000, mmmmmmmmmmmmm)


        mmmmmmmmmmmmm()


        t.mainloop()


except Error as e:
    print('This is not opeating',e)


