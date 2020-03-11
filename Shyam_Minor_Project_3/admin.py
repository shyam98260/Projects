from datetime import date ,time,timedelta,datetime
from tkinter import *
from pyzbar.pyzbar import decode
import cv2
import numpy as np
from tkinter.messagebox import *
import mysql.connector
from mysql.connector import Error
from random import randint
import pyqrcode
import os
import cv2
from pyqrcode import QRCode
from twilio.rest import Client
import time
from barcode import generate
from open_in_web_browser import open_web_browser
from Scan_Qr_Code import scan
from print_all_book_not_in_library import print_all_details_book_not_in_library
from know_student_id_password import know_student_id_password
from Date_Validate import validate
from get_bok_details import get_book_detailss
from students_haing_fine import student_having_fine
from get_all_student_issued_book import get_all_student_who_issue_book
from admin_see_all_fine_history import admin_fine_history
import pandas as pd
import datetime as lakhan
import calendar
from datetime import datetime as pappu
from get_pakka_time import mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
from search_using_qr_code import search_book_qr_code




def admin(username,password):
    count = 0
    tdate = date.today()
    day = tdate.day
    month = tdate.month
    year = tdate.year
    # print(day, ' ', month, " ", year)
    dddd = "" + str(day) + "-" + str(month) + "-" + str(year) + ""

    kkkkkkkkkk = "" + str(day) + " " + str(month) + " " + str(year) + ""
    chacha_date =  str(day) + "-" + str(month) + "-" + str(year)
    def findDay(date):
        born = lakhan.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])

    mmmmmmmmm = {1: ' Jan', 2: ' Feb', 3: ' Mar', 4: ' Apr', 5: ' May', 6: ' June', 7: ' July', 8: ' Aug', 9: ' Sep',
                 10: ' Oct', 11: ' Nov', 12: ' Dec'}
    dddddddddd = str(findDay(kkkkkkkkkk)) + " , " + str(day) + mmmmmmmmm[int(month)]  # "-" + str(month) + "-" + str(year) + ""



    try:
        connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
        if connection.is_connected():
            cursor = connection.cursor()
            # Completed


            # def genrate_qrcode():
            #     l = int(len(os.listdir('BarCode/')))
            #     l = l + 1
            #     filename = ('BarCode/' + str(l))
            #     sss = True
            #     while sss:
            #         s = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))+ str(randint(0, 9))+ str(randint(0, 9))+ str(randint(0, 9))+ str(randint(0, 9))
            #         query = "select * from add_book where b_id= \'"+str(s)+"\' "
            #         cursor.execute(query)
            #         details = cursor.fetchall()
            #         if len(details)>0:
            #             pass
            #         elif len(details)<=0:
            #             sss = False
            #     print(s)
            #     # url = pyqrcode.create(s)
            #     # url.svg(filename + '.svg', scale=8)
            #     name = generate('code128', str(s), output=filename)
            #     return s,name

            def genrate_qrcode():
                l = int(len(os.listdir('BarCode/')))
                l = l + 1
                filename = ('BarCode/' + str(l))
                sss = True
                while sss:
                    s = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(
                        randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                    query = "select * from add_book where b_id= \'" + str(s) + "\' "
                    cursor.execute(query)
                    details = cursor.fetchall()
                    if len(details) > 0:
                        pass
                    elif len(details) <= 0:
                        sss = False
                print(s)
                url = pyqrcode.create(s)
                url.svg(filename + '.svg', scale=8)
                return s, filename + '.svg'





            def kkkk():
                add = Tk()
                label_1 = Label(add, text="Add Book", width=10, font=("bold", 20))
                label_1.place(x=57, y=5)
                add.title(string='Select the mode of adding the book')
                label_11 = Label(add, text=dddd, width=0, font=("bold", 11))
                label_11.place(x=0, y=0)

                def add_book():
                    add.destroy()
                    adb = Tk()
                    label_1 = Label(adb, text="Add Book", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    adb.geometry('500x400')
                    label_1 = Label(adb, text="Book Title", width=20, font=("Arial", 10))
                    label_1.place(x=80, y=130)
                    entry_1 = Entry(adb, font=('Arial'))
                    entry_1.place(x=240, y=130)
                    label_2 = Label(adb, text="Book Author", width=20, font=("Arial", 10))
                    label_2.place(x=80, y=170)
                    entry_2 = Entry(adb, font=('Arial'))
                    entry_2.place(x=240, y=170)
                    label_3 = Label(adb, text="Book Publication", width=20, font=("Arial", 10))
                    label_3.place(x=80, y=210)
                    entry_3 = Entry(adb, font=('Arial'))
                    entry_3.place(x=240, y=210)
                    label_4 = Label(adb, text="No Of Books", width=20, font=("Arial", 10))
                    label_4.place(x=80, y=250)
                    entry_4 = Entry(adb, font=('Arial'))
                    entry_4.place(x=240, y=250)
                    label_5 = Label(adb, text="Edition", width=20, font=("Arial", 10))
                    label_5.place(x=80, y=290)
                    editiom = []
                    for x in range(1, 21):
                        editiom.append(int(x))
                    c = StringVar(adb)
                    droplist = OptionMenu(adb, c, *editiom)
                    droplist.config(width=20)
                    c.set('Select Book Edition')
                    droplist.place(x=240, y=290)

                    def submiitt(c):
                        if entry_1.get() != '':
                            if entry_2.get() != '':
                                if entry_3.get() != '':
                                    if entry_4.get() != '':
                                        try:
                                            nobs = int(entry_4.get())
                                        except:
                                            print(showerror('PLEASE USE DIGIT',
                                                            'Enter no of books in digit \n not in letter'))
                                            entry_4.delete(0, len(entry_4.get()))
                                            return ''

                                        if c != '':
                                            c = int(c)
                                            query = "select * from add_book where b_name= \'" + str(
                                                entry_1.get()) + "\' and b_author=\'" + str(
                                                entry_2.get()) + "\' and b_publication=\'" + str(
                                                entry_3.get()) + "\' and b_edition=\'" + str(c) + "\'"
                                            cursor.execute(query)
                                            alll = cursor.fetchall()
                                            if len(alll) > 0:
                                                print(showwarning('ALREADY IN LIBRARY',
                                                                  'This Book is already added in the library'))
                                                adb.destroy()
                                            else:
                                                s, filename = genrate_qrcode()
                                                query = "insert into add_book values(\'" + str(s) + "\',\'" + str(
                                                    entry_1.get()) + "\',\'" + str(entry_2.get()) + "\',\'" + str(
                                                    entry_3.get()) + "\',\'" + str(c) + "\',\'" + str(
                                                    entry_4.get()) + "\')"
                                                cursor.execute(query)
                                                connection.commit()
                                                query = "select * from add_book where b_name= \'" + str(
                                                entry_1.get()) + "\' and b_author=\'" + str(
                                                entry_2.get()) + "\' and b_publication=\'" + str(
                                                entry_3.get()) + "\' and b_edition=\'" + str(c) + "\'"
                                                cursor.execute(query)
                                                alll = cursor.fetchall()
                                                if len(alll) > 0:
                                                    print(showinfo('CONGRATULATIONS', 'Book added Succesfully'))
                                                    vvvv = askokcancel(title='Want to see qr code',
                                                                       message='Do you cant to see qr code or not yes/no')
                                                    if vvvv == True:
                                                        wd = os.getcwd()
                                                        print(wd)
                                                        wwd = ''
                                                        for x in wd:
                                                            if x == '\\':
                                                                x = '\\\\'
                                                                wwd = wwd + x
                                                        wd = wd + '\\' + filename
                                                        open_web_browser(wd)
                                                    adb.destroy()
                                                else:
                                                    print(showerror('CAUSING SOME PROBLEM',
                                                                    'Book Can\'t be added Becaues of some problem'))
                                        else:
                                            print(showwarning('EDITION', 'Select the Edition'))

                                    else:
                                        print(showwarning('NO OF BOOK', 'Enter no of books'))
                                else:
                                    print(showwarning('PUBLICATION', 'Enter book Publication'))
                            else:
                                print(showwarning('AUTHOR', 'Enter book Author'))
                        else:
                            print(showwarning('TITLE', 'Enter book Title'))

                    def kk():
                        if c.get() == 'Select Book Edition':
                            c.set('')
                        submiitt(c.get())

                    Button(adb, text='Submit', width=15, bg='brown', fg='white', command=kk).place(x=260, y=350)
                    adb.resizable(False, False)
                    adb.mainloop()
                def kkkkkk():
                    add.destroy()
                    def increase_no_of_book():
                        add = Tk()
                        label_1 = Label(add, text="Increase Book", width=10, font=("bold", 20))
                        label_1.place(x=57, y=5)
                        add.title(string='Select the mode of Increasing the book')
                        label_11 = Label(add, text=dddd, width=0, font=("bold", 11))
                        label_11.place(x=0, y=0)

                        def second_mode():
                            add.destroy()
                            barcode = scan()
                            if barcode != None:
                                addd = Tk()
                                label_1 = Label(addd, text="Increase Book", width=20, font=("bold", 20))
                                label_1.place(x=120, y=5)
                                label_4 = Label(addd, text="No Of Books", width=20, font=("Arial", 10))
                                label_4.place(x=80, y=100)
                                entry_4 = Entry(addd, font=('Arial'))
                                entry_4.place(x=240, y=100)

                                def kk():
                                    print(barcode)
                                    if entry_4.get() != '':
                                        try:
                                            kkkkkk = int(entry_4.get())
                                            query = "select no_of_books from add_book where b_id= \'" + str(
                                                barcode) + "\' "
                                            cursor.execute(query)
                                            details = cursor.fetchall()
                                            details = details[0]
                                            details = int(details[0]) + int(entry_4.get())
                                            query = "update add_book set no_of_books=\'" + str(
                                                details) + "\' where b_id= \'" + str(barcode) + "\' "
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select no_of_books from add_book where b_id= \'" + str(
                                                barcode) + "\' "
                                            cursor.execute(query)
                                            detailss = cursor.fetchall()
                                            detailss = detailss[0]
                                            detailss = int(detailss[0])
                                            if int(details) == int(detailss):
                                                print(showinfo('Congratulation\'s', 'Book increassed Succesfully'))
                                                addd.destroy()
                                            else:
                                                print(showerror('ERROR',
                                                                'Book Can\'t be increassed just because of \n some probplem'))
                                        except:
                                            print(showwarning('ERROR',
                                                              'Please enter the no of books in digit not in character'))
                                            entry_4.delete(0, len(entry_4.get()))
                                    else:
                                        print(showwarning('ERROR', 'Please enter the no of books'))

                                addd.geometry('500x300')
                                Button(addd, text='Submit', width=15, bg='brown', fg='white', command=kk).place(x=260,
                                                                                                                y=140)
                                addd.resizable(False, False)
                                addd.mainloop()
                            else:
                                print(showwarning('SCAN QR CODE', 'Please scan the qr code first'))

                        def first_mode():
                            add.destroy()
                            adb = Tk()
                            label_1 = Label(adb, text="Increase Book", width=20, font=("bold", 20))
                            label_1.place(x=90, y=5)
                            adb.geometry('500x400')
                            label_11 = Label(adb, text=dddd, width=0, font=("bold", 11))
                            label_11.place(x=0, y=0)
                            label_1 = Label(adb, text="Book Title", width=20, font=("Arial", 10))
                            label_1.place(x=80, y=130)
                            entry_1 = Entry(adb, font=('Arial'))
                            entry_1.place(x=240, y=130)

                            label_4 = Label(adb, text="Book Author", width=20, font=("Arial", 10))
                            label_4.place(x=80, y=170)
                            entry_4 = Entry(adb, font=('Arial'))
                            entry_4.place(x=240, y=170)

                            label_5 = Label(adb, text="Book Publication", width=20, font=("Arial", 10))
                            label_5.place(x=80, y=210)
                            entry_5 = Entry(adb, font=('Arial'))
                            entry_5.place(x=240, y=210)

                            label_5 = Label(adb, text="Edition", width=20, font=("Arial", 10))
                            label_5.place(x=80, y=250)
                            editiom = []
                            for x in range(1, 21):
                                editiom.append(int(x))
                            c = StringVar(adb)
                            droplist = OptionMenu(adb, c, *editiom)
                            droplist.config(width=20)
                            c.set('Select Book Edition')
                            droplist.place(x=240, y=250)

                            label_9 = Label(adb, text="No Of Books To Increase", width=20, font=("Arial", 10))
                            label_9.place(x=80, y=290)
                            entry_9 = Entry(adb, font=('Arial'))
                            entry_9.place(x=240, y=290)

                            # def auto_update():
                            #     if len(entry_4.get())>=3 and len(entry_1.get())>=3:
                            #         query = "select * from add_book where b_author=\'" + str(
                            #             entry_4.get()) + "\' and b_name=\'" + str(entry_1.get()) + "\' or b_publication like \'%" + str(entry_5.get()) + "%\'"
                            #         cursor.execute(query)
                            #         book_author = cursor.fetchall()
                            #         if len(book_author) > 0:
                            #             book_author = book_author[0]
                            #             print(book_author)
                            #             if str(entry_4.get())!=str(book_author[2]):
                            #                 entry_4.insert(len(entry_4.get()), str(str(book_author[2])[len(entry_4.get()):]))
                            #             if str(book_author[3])!=str(entry_5.get()):
                            #                 entry_5.insert(0,book_author[3])
                            #             if str(c.get())!=str(book_author[4]):
                            #                 c.set(book_author[4])
                            #
                            #
                            # # adb.bind("<Enter>",auto_update)

                            # Button(adb, text='Submit', width=15, bg='brown', fg='white', command=auto_update).place(x=260,
                            #                                                                                    y=370)

                            def submit():
                                if c.get()=='Select Book Edition':
                                    c.set('')
                                if str(entry_1.get())!='':
                                    if str(entry_4.get())!='':
                                        if str(entry_5.get()) != '':
                                            if str(c.get()) != '':
                                                if str(entry_9.get())!='':
                                                    if str(entry_9.get()).isnumeric():
                                                        query = "select * from add_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_4.get()) + "\' and b_publication=\'" + str(
                                                            entry_5.get()) + "\' and b_edition=\'" + str(c.get()) + "\'"
                                                        cursor.execute(query)
                                                        details = cursor.fetchall()
                                                        if len(details) > 0:
                                                            details = details[0]
                                                            no_of_booooooo = int(details[5])
                                                            ohhhhh =  no_of_booooooo + int(entry_9.get())
                                                            query = "update add_book set no_of_books=\'" + str(ohhhhh) + "\' where b_id=\'"+str(details[0])+"\'"
                                                            cursor.execute(query)
                                                            connection.commit()
                                                            query = "select no_of_books from add_book where b_id=\'"+str(details[0])+"\'"
                                                            cursor.execute(query)
                                                            details = cursor.fetchall()
                                                            details = details[0]
                                                            details = int(details[0])
                                                            if details==ohhhhh:
                                                                showinfo('Successfully','Books Increased Successfully')
                                                                adb.destroy()
                                                            else:
                                                                showwarning('warning','Books Can\'t Increased Because Of Some Reason')
                                                        else:
                                                            showwarning('warning', 'This Book Is Not In Library')
                                                    else:
                                                        showwarning('warning','No Of Books Must be In Integer')
                                                else:
                                                    showwarning('warning','Please Enter The No Of Books To Increase')
                                            else:
                                                showwarning('warning', 'Please select The Book Edition')
                                        else:
                                            showwarning('warning', 'Please Enter The Book Publication')
                                    else:
                                        showwarning('warning','Please Enter The Book Author')

                                else:
                                    showwarning('Warning','Please Enter the Book Title')

                            Button(adb, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=260,
                                                                                                               y=330)
                            adb.resizable(False, False)
                            adb.mainloop()

                        Button(add, text='Scan Qr Code', width=15, height=2, bg='brown', fg='white',
                               command=second_mode).place(x=10, y=50)
                        Button(add, text='Or By Book Name', width=15, height=2, bg='brown', fg='white',
                               command=first_mode).place(x=150, y=50)
                        add.geometry('300x200')
                        add.resizable(False, False)
                        add.mainloop()

                    increase_no_of_book()

                def import_csv_for_books():
                    add.destroy()
                    filename = []
                    a = os.listdir()
                    for x in a:
                        if len(x) > 5:
                            if x[-5:] == '.xlsx':
                                print('yes')
                                filename.append(x)

                    if len(filename) > 0:
                        llll = Tk()
                        label_1 = Label(llll, text="Select The Excel File", width=20, font=("bold", 20))
                        label_1.place(x=90, y=5)

                        llll.title(string='Select File')
                        # label_11 = Label(llll, text=dddd, width=0, font=("bold", 11))
                        # label_11.place(x=0, y=0)

                        label_5 = Label(llll, text="Select File", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=100)
                        c = StringVar(llll)
                        droplist = OptionMenu(llll, c, *filename)
                        droplist.config(width=20)
                        c.set('Select The Excel File')
                        droplist.place(x=240, y=100)
                        llll.geometry('500x300')
                        llll.resizable(False, False)

                        def ggggggggg():
                            if c.get() == 'Select The Excel File':
                                c.set('')
                            if c.get() != '':
                                s = pd.read_excel(str(c.get()))
                                a = s[['b_name', 'b_author', 'b_publication','b_edition','no_of_books']].to_numpy().tolist()
                                print(len(a))
                                i = 2
                                b = str()
                                print(a)
                                if len(a) > 0:
                                    query = "select * from add_book"
                                    cursor.execute(query)
                                    bef_len = cursor.fetchall()
                                    bef_len = len(bef_len)
                                    no_of_book_updated = 0
                                    ppp = None
                                    for x in a:
                                        if str(x[0]) == 'nan' or str(x[1]) == 'nan' or str(x[2]) == 'nan' or str(
                                                x[3]) == 'nan' or str(x[4]) == 'nan':
                                            b += 'Row ' + str(i) + ' some data is missing\n'
                                        else:
                                            if str(x[3]).isdigit():
                                                if str(x[4]).isdigit():
                                                    query = "select * from add_book where b_name=\'" + str(
                                                        x[0]) + "\' and b_author=\'" + str(
                                                        x[1]) + "\' and b_publication=\'" + str(
                                                        x[2]) + "\' and b_edition=\'" + str(x[3]) + "\' "
                                                    print(str(i)+'  '+str(x[3])+'    '+str(x[0]))
                                                    cursor.execute(query)

                                                    details = cursor.fetchall()
                                                    if len(details) > 0:
                                                        details = details[0]
                                                        if int(details[5]) < int(x[4]):
                                                            query = "update add_book set no_of_books=\'" + str(
                                                                int(details[5]) + int(x[4])) + "\' where b_id=\'" + str(
                                                                details[0]) + "\'"
                                                            cursor.execute(query)
                                                            connection.commit()
                                                            no_of_book_updated += 1
                                                    else:
                                                        s, name = genrate_qrcode()
                                                        query = "insert into add_book values(\'" + str(
                                                            s) + "\',\'" + str(x[0]) + "\',\'" + str(
                                                            x[1]) + "\',\'" + str(x[2]) + "\',\'" + str(
                                                            x[3]) + "\',\'" + str(x[4]) + "\')"
                                                        cursor.execute(query)
                                                        connection.commit()
                                            else:
                                                b += 'Row ' + str(i) + ' b_edition is not digit\n'

                                        i += 1


                                    query = "select * from add_book"
                                    cursor.execute(query)
                                    af_len = cursor.fetchall()
                                    af_len = len(af_len)
                                    if af_len > bef_len:
                                        showinfo('Information', 'Data Inserted successfully')
                                        llll.destroy()
                                        if b == '':
                                            pass
                                        else:
                                            showerror('error', b)
                                    elif af_len == bef_len:
                                        showerror('error', 'This all Data Is Already Available')
                                        llll.destroy()
                                        if b == '':
                                            pass
                                        else:
                                            showerror('error', b)
                                    else:
                                        if b == '':
                                            pass
                                        else:
                                            showerror('error', b)
                                    if no_of_book_updated > 0:
                                        showinfo('Information', str(no_of_book_updated) + ' Books Updated')
                                else:
                                    showwarning('warning', 'There is not any entry in this file')

                        Button(llll, text='Submit', width=15, bg='brown', fg='white', command=ggggggggg).place(x=260,
                                                                                                               y=190)
                        llll.mainloop()
                    else:
                        showwarning('warning', 'There is No any file with the extension \'.xlsx\'')

                    # showwarning('Warning','This is under progress ')


                Button(add, text='Add New Book', width=15, height=2, bg='brown', fg='white', command=add_book).place(x=10,
                                                                                                                y=50)
                Button(add, text='Increase Book', width=15, height=2, bg='brown', fg='white',command=kkkkkk).place(x=150, y=50)
                Button(add, text='Import CSV', width=15, height=2, bg='brown', fg='white',command=import_csv_for_books).place(x=75, y=100)
                add.geometry('280x200')
                add.resizable(False, False)
                add.mainloop()

            # Completed
            def calling():
                account_sid = "ACe36c77e6302d6870ebd91d83fbb2b28a"
                auth_token = "abe3760c7c33f11c29779409afdcc1a9"
                client = Client(account_sid, auth_token)
                aaa = askyesno("askyesno", "Do You Want to Call or Not")
                if aaa == True:
                    call = client.calls.create(to="+918223859046", from_="+12015617688",url="http://demo.twilio.com/docs/voice.xml")
                    if call.sid != None:
                        print(showinfo('ShowError', 'Call Has Been Sent to the Provided Mobile Number'))
                    else:
                        print(showerror('ShowError', 'There is some issue while calling'))
                elif aaa == 'False':
                    print(showerror('ShowError', 'Call is cancled'))




            def calling_librarian():
                query = "select * from librarian"
                cursor.execute(query)
                details = cursor.fetchall()
                if len(details)>0:
                    llll = Tk()
                    label_1 = Label(llll, text="Select The Book", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    llll.title(string='Select Book')
                    label_11 = Label(llll, text=dddd, width=0, font=("bold", 11))
                    label_11.place(x=0, y=0)
                    label_5 = Label(llll, text="Select book", width=20, font=("Arial", 10))
                    label_5.place(x=80, y=100)
                    query = "select username from librarian"
                    cursor.execute(query)
                    details = cursor.fetchall()
                    editiom = []
                    for x in details:
                        editiom.append(x[0])
                    c = StringVar(llll)
                    droplist = OptionMenu(llll, c, *editiom)
                    droplist.config(width=20)
                    c.set('Select Name For Calling')
                    droplist.place(x=240, y=100)
                    llll.geometry('500x300')
                    llll.resizable(False, False)

                    def ppp():
                        if c.get()=='Select Name For Calling':
                            c.set('')
                        query = "select mobile_no from librarian where username=\'"+str(c.get())+"\'"
                        cursor.execute(query)
                        kkkkkkkkkkkkkkkkkkk = cursor.fetchall()
                        kkkkkkkkkkkkkkkkkkk = kkkkkkkkkkkkkkkkkkk[0]
                        kkkkkkkkkkkkkkkkkkk = kkkkkkkkkkkkkkkkkkk[0]
                        account_sid = "ACe36c77e6302d6870ebd91d83fbb2b28a"
                        auth_token = "abe3760c7c33f11c29779409afdcc1a9"
                        client = Client(account_sid, auth_token)
                        aaa = askyesno("askyesno", "Do You Want to Call or Not")
                        if aaa == True:
                            try:
                                call = client.calls.create(to='+91'+str(kkkkkkkkkkkkkkkkkkk), from_="+12015617688",url="http://demo.twilio.com/docs/voice.xml")
                            except:
                                showwarning('warning','Please Verify The Number First')
                                return ''
                            if call.sid != None:
                                print(showinfo('ShowError', 'Call Has Been Sent to the Provided Mobile Number'))
                            else:
                                print(showerror('ShowError', 'There is some issue while calling'))
                        elif aaa == 'False':
                            print(showerror('ShowError', 'Call is cancled'))
                    Button(llll, text='Submit', width=15, bg='brown', fg='white', command=ppp).place(x=260, y=190)
                    llll.mainloop()
                else:
                    showwarning('Warning','There librarian are in the database')










            # Completed
            def no_of_book_not_in_library():
                print_all_details_book_not_in_library()

            # Completed
            def student_id_password():
                aaa = askyesno("askyesno", "Do You Want Search for particular user yes/no")
                if aaa == True:
                    kkk = Tk()
                    label_1 = Label(kkk, text="Know Student Details", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    kkk.geometry('500x200')
                    label_1 = Label(kkk, text="Enter Name of Student", width=20, font=("Arial", 10))
                    label_1.place(x=80, y=130)
                    entry_1 = Entry(kkk, font=('Arial'))
                    entry_1.place(x=240, y=130)
                    def gett():
                        if entry_1.get() != '':
                            ah = entry_1.get()
                            query = "select * from student where name like \'%" + str(ah) + "%\'"
                            cursor.execute(query)
                            kh = cursor.fetchall()
                            if len(kh) > 0:
                                know_student_id_password(entry_1.get())
                                kkk.destroy()
                            else:
                                print(showerror('ShowError', 'There is no student with this name'))
                        else:
                            print(showwarning('ShowError', 'Please Enter Name'))
                    Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=gett).place(x=260, y=170)
                    kkk.mainloop()
                else:
                    know_student_id_password('False')

            # Completed
            def add_student():
                age = None
                print(showinfo('ShowError','Username Must be the Enrollment No of Student \n And Password must be Default for everyone\n if the student wants to change their password'))
                ads = Tk()
                ads.resizable(False, False)
                label_1 = Label(ads, text="Student Information", width=20, font=("bold", 20))
                label_1.place(x=120, y=5)
                ads.geometry('600x500')
                label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                label_0.place(x=80, y=90)
                entry_0 = Entry(ads, font=('Arial'))
                entry_0.place(x=240, y=90)
                label_1 = Label(ads, text="Name", width=20, font=("Arial", 10))
                label_1.place(x=80, y=130)
                entry_1 = Entry(ads, font=('Arial'))
                entry_1.place(x=240, y=130)
                label_2 = Label(ads, text="Mobile No", width=20, font=("Arial", 10))
                label_2.place(x=80, y=170)
                entry_2 = Entry(ads, font=('Arial'))
                entry_2.place(x=240, y=170)
                label_3 = Label(ads, text="Branch", width=20, font=("Arial", 10))
                label_3.place(x=80, y=210)
                x = 250
                Branch = ['CSE', 'EE', 'EC', 'ME', 'CE','IT']
                c = StringVar(ads)
                droplist = OptionMenu(ads, c, *Branch)
                droplist.config(width=20)
                c.set('select your Branch')
                droplist.place(x=240, y=210)
                label_4 = Label(ads, text="SEM", width=20, font=("Arial", 10))
                label_4.place(x=80, y=x)
                x = 250
                sem = ['1', '2', '3', '4', '5', '6', '7', '8']
                d = StringVar(ads)
                droplist = OptionMenu(ads, d, *sem)
                droplist.config(width=20)
                d.set('select sem')
                droplist.place(x=240, y=250)
                label_5 = Label(ads, text="DOB", width=20, font=("Arial", 10))
                label_5.place(x=80, y=290)
                entry_5 = Entry(ads, font=('Arial'))
                entry_5.place(x=240, y=290)
                label_6 = Label(ads, text="Address", width=20, font=("Arial", 10))
                label_6.place(x=80, y=330)
                entry_6 = Entry(ads, font=('Arial'))
                entry_6.place(x=240, y=330)
                def submit():
                    if c.get()=='select your Branch':
                        c.set('')
                    if d.get()=='select sem':
                        d.set('')
                    if entry_0.get()!='':
                        if entry_1.get()!='':
                            if entry_2.get()!='':
                                try:
                                    mn = int(entry_2.get())
                                except:
                                    showwarning('Warning', 'Please enter the Mobile No in digit\n not in character')
                                    entry_2.delete(0, len(entry_2.get()))
                                    return ''
                                if len(entry_2.get()) == 10:
                                    if c.get() != '':
                                        if d.get() != '':
                                            if entry_5.get() != '':
                                                if len(entry_5.get()) == 10:
                                                    try:
                                                        mmmm = entry_5.get()
                                                        mmmm = mmmm[3:5]
                                                        yyyy = entry_5.get()
                                                        yyyy = yyyy[0:2]
                                                        dob = entry_5.get()
                                                        dob = dob[6:10]
                                                        age = str(int(year) - int(dob))
                                                        date_string = "" + dob + "-" + mmmm + "-" + yyyy + ""
                                                        date_format = '%Y-%m-%d'
                                                        cheack_validate = validate(date_string, date_format)
                                                    except:
                                                        showwarning('Warning', 'Please enter the valid DOB')
                                                        entry_5.delete(0, len(entry_5.get()))
                                                        return ''
                                                    if cheack_validate == True:
                                                        if int(age) > 13:
                                                            if entry_6.get() != '':
                                                                query = "select * from student where enrollment_no=\'" + str(
                                                                    entry_0.get()) + "\'"
                                                                cursor.execute(query)
                                                                details = cursor.fetchall()
                                                                if len(details) == 0:
                                                                    date_string = "" + yyyy + "-" + mmmm + "-" + dob + ""
                                                                    query = "select * from issue_book where enrollment_no =\'"+str(entry_0.get())+"\'"
                                                                    cursor.execute(query)
                                                                    llllll = cursor.fetchall()
                                                                    llllll = len(llllll)
                                                                    query = "insert into student values(\'" + str(
                                                                        entry_0.get()) + "\',\'" + str(
                                                                        entry_1.get()) + "\',\'" + str(
                                                                        c.get()) + "\',\'" + str(
                                                                        d.get()) + "\',\'" + str(
                                                                        age) + "\',\'" + str(
                                                                        entry_6.get()) + "\',\'" + str(
                                                                        'shyam') + "\',\'" + str(llllll) + "\',\'" + str(
                                                                        entry_2.get()) + "\',\'" + str(
                                                                        date_string) + "\')"
                                                                    cursor.execute(query)
                                                                    connection.commit()
                                                                    query = "select * from student where enrollment_no=\'" + str(
                                                                        entry_0.get()) + "\'"
                                                                    cursor.execute(query)
                                                                    details = cursor.fetchall()
                                                                    if len(details) > 0:
                                                                        showinfo('Congratulation\s',
                                                                                 'Student added successfully')
                                                                        ads.destroy()
                                                                    else:
                                                                        showerror('Error',
                                                                                  'Student Can\'t be added just because of some issue')
                                                                else:
                                                                    showinfo('Warning', 'Student is already added')
                                                            else:
                                                                showwarning('Warning', 'Please enter the Address')
                                                        else:
                                                            showwarning('Warning',
                                                                        'Student must be greater than the age of 13')
                                                            entry_5.delete(0, len(entry_5.get()))
                                                    else:
                                                        showwarning('Warning','Please enter the valid DOB this DOB \n does\'t exist')
                                                        entry_5.delete(0, len(entry_5.get()))

                                                else:
                                                    showwarning('Warning', 'Please Enter DOB in \'dd-mm-yyyy\ format')
                                                    entry_5.delete(0, len(entry_5.get()))
                                            else:
                                                showwarning('Warning', 'Please Enter DOB in \'dd-mm-yyyy\ format')
                                        else:
                                            showwarning('Warning', 'Please select the Semester')
                                    else:
                                        showwarning('Warning', 'Please select the branch')
                                else:
                                    showwarning('Warning', 'Please enter the 10 digit mobile no \n "xxxxxxxxxx"')
                                    entry_2.delete(0, len(entry_2.get()))

                            else:
                                showwarning('Warning', 'Please enter the Mobile No')
                        else:
                            showwarning('Warning', 'Please enter the Name')
                    else:
                        showwarning('Warning','Please enter the enrollment no')

                Button(ads, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=280, y=380)
                ads.mainloop()

            # Completed
            def remove_book():
                query = "select * from add_book"
                cursor.execute(query)
                vvvvvv = cursor.fetchall()
                if len(vvvvvv)>0:

                    rmb = Tk()
                    label_1 = Label(rmb, text="Remove Book", width=0, font=("bold", 20))
                    label_1.place(x=7, y=5)
                    rmb.geometry('250x200')

                    def qr():
                        barcode = None

                        def scan():
                            def barcodeReader(image, bgr):
                                gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                barcodes = decode(gray_img)

                                for decodedObject in barcodes:
                                    points = decodedObject.polygon

                                    pts = np.array(points, np.int32)
                                    pts = pts.reshape((-1, 1, 2))
                                    cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                                cv2.putText(frame, 'Press Q For Exit', (30, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                            (0, 255, 0), 4)
                                for bc in barcodes:
                                    cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30),
                                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                                bgr, 2)

                                    return bc.data.decode("utf-8")

                            bgr = (8, 70, 208)
                            cap = cv2.VideoCapture(0)
                            ok = True
                            while ok:
                                ret, frame = cap.read()
                                barcode = barcodeReader(frame, bgr)
                                if barcode != None:
                                    ok = False
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    return barcode
                                cv2.imshow('Barcode reader', frame)
                                code = cv2.waitKey(10)
                                if code == ord('q'):
                                    break

                        barcode = scan()
                        query = "select * from add_book where b_id=\'" + str(barcode) + "\'"
                        cursor.execute(query)
                        all_details = cursor.fetchall()
                        if len(all_details) == 0:
                            print(showerror('ShowError', 'This Book is not in library'))
                            rmb.destroy()
                        else:
                            query = "delete from add_book where b_id=\'" + str(barcode) + "\'"
                            cursor.execute(query)
                            connection.commit()
                            query = "select * from add_book where b_id=\'" + str(barcode) + "\'"
                            cursor.execute(query)
                            all_details = cursor.fetchall()
                            if len(all_details) == 0:
                                print(showinfo('ShowError', 'Book Deleted SuccessFully'))
                                rmb.destroy()
                            else:
                                print(showerror('ShowError', 'Book Not Deleted'))
                                rmb.destroy()

                    Button(rmb, text='Scan Qr\nCode', width=8, height=2, bg='brown', fg='white', command=qr).place(x=10,
                                                                                                                   y=50)

                    def submit_book():
                        rmb.destroy()
                        gg = Tk()
                        label_1 = Label(gg, text="Delete Book By Name", width=0, font=("bold", 20))
                        label_1.place(x=80, y=5)
                        gg.geometry('600x400')

                        label_2 = Label(gg, text="Book Title", width=20, font=("Arial", 10))
                        label_2.place(x=80, y=130)
                        entry_2 = Entry(gg, font=('Arial'))
                        entry_2.place(x=240, y=130)

                        label_4 = Label(gg, text="Book Author", width=20, font=("Arial", 10))
                        label_4.place(x=80, y=170)
                        entry_4 = Entry(gg, font=('Arial'))
                        entry_4.place(x=240, y=170)

                        label_5 = Label(gg, text="Book Publication", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=210)
                        entry_5 = Entry(gg, font=('Arial'))
                        entry_5.place(x=240, y=210)

                        label_5 = Label(gg, text="Book Edition", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=250)
                        editiom = []
                        for x in range(1, 21):
                            editiom.append(int(x))
                        dfdf = StringVar(gg)
                        droplist = OptionMenu(gg, dfdf, *editiom)
                        droplist.config(width=20)
                        dfdf.set('Select Book Edition')
                        droplist.place(x=240, y=250)

                        def ppp():
                            if dfdf.get()=='Select Book Edition':
                                dfdf.set('')
                            if entry_2.get()!='':
                                if entry_4.get()!='':
                                    if entry_5.get()!='':
                                        if dfdf.get()!='':
                                            query = "select * from add_book where b_name=\'" + str(
                                                entry_2.get()) + "\' and b_author=\'" + str(
                                                entry_4.get()) + "\' and b_publication=\'" + str(
                                                entry_5.get()) + "\' and b_edition=\'" + str(
                                                dfdf.get()) + "\'"
                                            cursor.execute(query)
                                            details = cursor.fetchall()

                                            if len(details) > 0:
                                                query = "select * from issue_book where b_name=\'" + str(
                                                    entry_2.get()) + "\' and b_author=\'" + str(
                                                    entry_4.get()) + "\' and b_publication=\'" + str(
                                                    entry_5.get()) + "\' and b_edition=\'" + str(
                                                    dfdf.get()) + "\'"
                                                cursor.execute(query)
                                                details = cursor.fetchall()

                                                if len(details) <= 0:
                                                    query = "delete from add_book where b_name=\'" + str(
                                                        entry_2.get()) + "\' and b_author=\'" + str(
                                                        entry_4.get()) + "\' and b_publication=\'" + str(
                                                        entry_5.get()) + "\' and b_edition=\'" + str(dfdf.get()) + "\'"
                                                    cursor.execute(query)
                                                    connection.commit()

                                                    query = "select * from add_book where b_name=\'" + str(
                                                        entry_2.get()) + "\' and b_author=\'" + str(
                                                        entry_4.get()) + "\' and b_publication=\'" + str(
                                                        entry_5.get()) + "\' and b_edition=\'" + str(
                                                        dfdf.get()) + "\'"
                                                    cursor.execute(query)
                                                    details = cursor.fetchall()

                                                    if len(details) > 0:
                                                        showwarning('warning', 'Book\'s Can\'t Be Deleted')
                                                    else:
                                                        showinfo('Deleted Successfully',
                                                                 'Book Deleted Successfully')
                                                        gg.destroy()
                                                else:
                                                    showwarning('warning', 'This Book Is Already Issued')
                                            else:
                                                showwarning('warning', 'This Book is not in Library')
                                        else:
                                            showwarning('warning','Please Select The Book Edition')
                                    else:
                                        showwarning('warning','Please Enter The Book Publication')
                                else:
                                    showwarning('warning','Please Enter The Book Author')
                            else:
                                showwarning('warning','Please Enter The Book Title')

                        Button(gg, text='Submit', width=15, bg='brown', fg='white', command=ppp).place(x=260, y=290)
                        gg.resizable(False, False)
                        gg.mainloop()

                    def first_mode():
                        rmb.destroy()
                        adb = Tk()
                        label_1 = Label(adb, text="Decrease Book", width=20, font=("bold", 20))
                        label_1.place(x=90, y=5)
                        adb.geometry('500x400')
                        label_11 = Label(adb, text=dddd, width=0, font=("bold", 11))
                        label_11.place(x=0, y=0)
                        label_1 = Label(adb, text="Book Title", width=20, font=("Arial", 10))
                        label_1.place(x=80, y=130)
                        entry_1 = Entry(adb, font=('Arial'))
                        entry_1.place(x=240, y=130)

                        label_4 = Label(adb, text="Book Author", width=20, font=("Arial", 10))
                        label_4.place(x=80, y=170)
                        entry_4 = Entry(adb, font=('Arial'))
                        entry_4.place(x=240, y=170)

                        label_5 = Label(adb, text="Book Publication", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=210)
                        entry_5 = Entry(adb, font=('Arial'))
                        entry_5.place(x=240, y=210)

                        label_5 = Label(adb, text="Edition", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=250)
                        editiom = []
                        for x in range(1, 21):
                            editiom.append(int(x))
                        c = StringVar(adb)
                        droplist = OptionMenu(adb, c, *editiom)
                        droplist.config(width=20)
                        c.set('Select Book Edition')
                        droplist.place(x=240, y=250)

                        label_9 = Label(adb, text="No Of Books To Decrease", width=20, font=("Arial", 10))
                        label_9.place(x=80, y=290)
                        entry_9 = Entry(adb, font=('Arial'))
                        entry_9.place(x=240, y=290)



                        def submit():
                            if c.get() == 'Select Book Edition':
                                c.set('')
                            if str(entry_1.get()) != '':
                                if str(entry_4.get()) != '':
                                    if str(entry_5.get()) != '':
                                        if str(c.get()) != '':
                                            if str(entry_9.get()) != '':
                                                if str(entry_9.get()).isnumeric():
                                                    query = "select * from add_book where b_name=\'" + str(
                                                        entry_1.get()) + "\' and b_author=\'" + str(
                                                        entry_4.get()) + "\' and b_publication=\'" + str(
                                                        entry_5.get()) + "\' and b_edition=\'" + str(c.get()) + "\'"
                                                    cursor.execute(query)
                                                    details = cursor.fetchall()
                                                    if len(details) > 0:
                                                        details = details[0]
                                                        no_of_booooooo = int(details[5])
                                                        if no_of_booooooo>int(entry_9.get()):
                                                            ohhhhh = no_of_booooooo - int(entry_9.get())
                                                            query = "update add_book set no_of_books=\'" + str(
                                                                ohhhhh) + "\' where b_id=\'" + str(details[0]) + "\'"
                                                            cursor.execute(query)
                                                            connection.commit()
                                                            query = "select no_of_books from add_book where b_id=\'" + str(
                                                                details[0]) + "\'"
                                                            cursor.execute(query)
                                                            details = cursor.fetchall()
                                                            details = details[0]
                                                            details = int(details[0])
                                                            if details == ohhhhh:
                                                                showinfo('Successfully', 'Books Increased Successfully')
                                                                adb.destroy()
                                                            else:
                                                                showwarning('warning',
                                                                            'Books Can\'t Increased Because Of Some Reason')
                                                        else:
                                                            showwarning('Warning','No Of Books Is Greater Than Your Entered')
                                                    else:
                                                        showwarning('warning', 'This Book Is Not In Library')
                                                else:
                                                    showwarning('warning', 'No Of Books Must be In Integer')
                                            else:
                                                showwarning('warning', 'Please Enter The No Of Books To Decrease')
                                        else:
                                            showwarning('warning', 'Please select The Book Edition')
                                    else:
                                        showwarning('warning', 'Please Enter The Book Publication')
                                else:
                                    showwarning('warning', 'Please Enter The Book Author')

                            else:
                                showwarning('Warning', 'Please Enter the Book Title')

                        Button(adb, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=260,
                                                                                                           y=330)
                        adb.resizable(False, False)
                        adb.mainloop()



                    Button(rmb, text='By Entering Name \nof Book', width=15, bg='brown', fg='white',
                           command=submit_book).place(x=120, y=50)
                    Button(rmb, text='Decrease\n Book', width=15, bg='brown', fg='white',
                           command=first_mode).place(x=70, y=100)
                    rmb.resizable(False, False)
                    rmb.mainloop()
                else:
                    showwarning('Warning','Please add At Least one book in the library')

            # Completed
            def get_qr_code():
                query = "select * from add_book"
                cursor.execute(query)
                details = cursor.fetchall()
                if len(details)>0:
                    llll = Tk()
                    label_1 = Label(llll, text="Select The Book", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    llll.title(string='Select Book')
                    label_11 = Label(llll, text=dddd, width=0, font=("bold", 11))
                    label_11.place(x=0, y=0)
                    label_5 = Label(llll, text="Select book", width=20, font=("Arial", 10))
                    label_5.place(x=80, y=100)
                    query = "select * from add_book order by b_name asc"
                    cursor.execute(query)
                    details = cursor.fetchall()
                    editiom = []
                    for x in details:
                        if x[1] == 'NULL':
                            pass
                        else:
                            editiom.append(str(x[1])+' - '+str(x[2]))
                    c = StringVar(llll)
                    droplist = OptionMenu(llll, c, *editiom)
                    droplist.config(width=20)
                    c.set('Select Book Details')
                    droplist.place(x=240, y=100)
                    llll.geometry('500x300')
                    llll.resizable(False, False)

                    def ppp():
                        if c.get()=='Select Book Edition':
                            c.set('')
                        def ggggg(c):
                            l = int(len(os.listdir('BarCode/')))
                            l = l + 1
                            filename = ('BarCode/' + str(l))
                            print(filename)
                            result = c.split('-')
                            query = "select b_id from add_book where b_name= \'" + str(result[0]) + "\' "
                            cursor.execute(query)
                            details = cursor.fetchall()
                            print(details)
                            if len(details) > 0:

                                details = details[0]
                                details = details[0]
                                url = pyqrcode.create(details)
                                url.svg(filename + '.svg', scale=8)
                                return filename + '.svg'
                                # details = details[0]
                                # details = details[0]
                                # # url = pyqrcode.create(details)
                                # # url.svg(filename + '.svg', scale=8)
                                # # import code128
                                # # with open(filename + '.svg','w') as f:
                                # #     f.write(code128.svg(int(details)))
                                # print(details)
                                # name = generate('code128', str(details), output=filename)
                                # return name
                            else:
                                showerror('Error','This Book is not in library')


                        if c.get()!='':
                            filename = ggggg(c.get())
                            wd = os.getcwd()
                            print(wd)
                            wwd = ''
                            for x in wd:
                                if x == '\\':
                                    x = '\\\\'
                                    wwd = wwd + x
                            wd = wd + '\\' + filename
                            open_web_browser(wd)
                            llll.destroy()
                        else:
                            showwarning('Warning','Please select the book')

                    Button(llll, text='Submit', width=15, bg='brown', fg='white', command=ppp).place(x=260, y=190)
                    llll.mainloop()
                else:
                    showwarning('Warning','There is no any book in the library')


            def Scan_QR_CODEE():
                def barcodeReader(image, bgr):
                    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    barcodes = decode(gray_img)

                    for decodedObject in barcodes:
                        points = decodedObject.polygon

                        pts = np.array(points, np.int32)
                        pts = pts.reshape((-1, 1, 2))
                        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                    cv2.putText(frame, 'Press Q For Exit', (30, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                (0, 255, 0), 4)
                    for bc in barcodes:
                        cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    bgr, 2)

                        return bc.data.decode("utf-8")

                bgr = (8, 70, 208)
                cap = cv2.VideoCapture(0)
                ok = True
                while ok:
                    ret, frame = cap.read()
                    barcode = barcodeReader(frame, bgr)
                    if barcode != None:
                        ok = False
                        cap.release()
                        cv2.destroyAllWindows()
                        return barcode
                    cv2.imshow('Barcode reader', frame)
                    code = cv2.waitKey(10)
                    if code == ord('q'):
                        break


            def Scan_QR_CODE_book_details():
                all_book_details = Scan_QR_CODEE()
                query = "select * from add_book where b_id=\'" + str(all_book_details) + "\'"
                cursor.execute(query)
                details = cursor.fetchall()
                if len(details) > 0:
                    search_book_qr_code(all_book_details)
                else:
                    showerror('Error', 'This Book is not in library')


            # Completed
            def know_book_details():
                aaa = askyesno("askyesno", "Do You Want Search for particular Book yes/no")
                if aaa == True:
                    kkk = Tk()
                    label_1 = Label(kkk, text="Know Book Details", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    kkk.geometry('500x200')
                    label_1 = Label(kkk, text="Enter Name of Book", width=20, font=("Arial", 10))
                    label_1.place(x=80, y=130)
                    entry_1 = Entry(kkk, font=('Arial'))
                    entry_1.place(x=240, y=130)
                    def gett(event):
                        if entry_1.get() != '':
                            ah = entry_1.get()
                            query = "select * from add_book where b_name like \'%" + str(ah) + "%\'"
                            cursor.execute(query)
                            kh = cursor.fetchall()
                            if len(kh) > 0:
                                get_book_detailss(entry_1.get())
                                kkk.destroy()
                            else:
                                print(showerror('ShowError', 'There is no book with this name'))
                        else:
                            print(showwarning('ShowError', 'Please Enter book Name'))
                    kkk.bind('<Return>',gett)
                    Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=lambda :gett('')).place(x=260, y=170)
                    kkk.mainloop()
                else:
                    get_book_detailss('False')


            def bgbgbgbgbgbgbgbg():
                rmb = Tk()
                label_1 = Label(rmb, text="See Book Details", width=0, font=("bold", 20))
                label_1.place(x=7, y=5)
                rmb.geometry('250x200')

                Button(rmb, text='Scan Qr\nCode', width=8, height=2, bg='brown', fg='white', command=Scan_QR_CODE_book_details).place(x=10,
                                                                                                               y=50)
                Button(rmb, text='By Manually \nEntering Name \nof Book', width=15, bg='brown', fg='white',
                       command=know_book_details).place(x=120, y=50)
                rmb.resizable(False, False)
                rmb.mainloop()




            # Completed
            def issue_book():
                query = "select * from add_book"
                cursor.execute(query)
                nnnnnn = cursor.fetchall()
                if len(nnnnnn)>0:

                    aaa = askyesno("askyesno", "Do You want to scan qr code or not yes/no")
                    if aaa==False:
                        ads = Tk()
                        ads.resizable(False, False)

                        label_1 = Label(ads, text="Issue Book", width=20, font=("bold", 20))
                        label_1.place(x=120, y=5)
                        ads.geometry('600x400')

                        label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                        label_0.place(x=80, y=90)
                        entry_0 = Entry(ads, font=('Arial'))
                        entry_0.place(x=240, y=90)

                        label_3 = Label(ads, text="Duration(days)", width=20, font=("Arial", 10))
                        label_3.place(x=80, y=290)
                        x = 250
                        Branch = ['15', '30']
                        c = StringVar(ads)
                        droplist = OptionMenu(ads, c, *Branch)
                        droplist.config(width=20)
                        c.set('Select Duration')
                        droplist.place(x=240, y=290)

                        label_2 = Label(ads, text="Book Title", width=20, font=("Arial", 10))
                        label_2.place(x=80, y=130)
                        entry_2 = Entry(ads, font=('Arial'))
                        entry_2.place(x=240, y=130)

                        label_4 = Label(ads, text="Book Author", width=20, font=("Arial", 10))
                        label_4.place(x=80, y=170)
                        entry_4 = Entry(ads, font=('Arial'))
                        entry_4.place(x=240, y=170)

                        label_5 = Label(ads, text="Book Publication", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=210)
                        entry_5 = Entry(ads, font=('Arial'))
                        entry_5.place(x=240, y=210)

                        label_5 = Label(ads, text="Book Edition", width=20, font=("Arial", 10))
                        label_5.place(x=80, y=250)
                        editiom = []
                        for x in range(1, 21):
                            editiom.append(int(x))
                        dfdf = StringVar(ads)
                        droplist = OptionMenu(ads, dfdf, *editiom)
                        droplist.config(width=20)
                        dfdf.set('Select Book Edition')
                        droplist.place(x=240, y=250)

                        def submit():
                            if c.get()=='Select Duration':
                                c.set('')
                            if dfdf.get()=='Select Book Edition':
                                dfdf.set('')
                            if entry_0.get() != '':
                                query = "select * from student where enrollment_no= \'" + str(entry_0.get()) + "\' "
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if len(details) > 0:
                                    if entry_2.get()!='':
                                        query = "select * from add_book where b_name=\'"+str(entry_2.get())+"\'"
                                        cursor.execute(query)
                                        details = cursor.fetchall()
                                        if len(details)>0:
                                            if entry_4.get()!='':
                                                query = "select * from add_book where b_name=\'" + str(
                                                    entry_2.get()) + "\' and b_author=\'" + str(entry_4.get()) + "\'"
                                                cursor.execute(query)
                                                details = cursor.fetchall()
                                                if len(details)>0:
                                                    if entry_5.get()!='':
                                                        query = "select * from add_book where b_name=\'" + str(
                                                            entry_2.get()) + "\' and b_author=\'" + str(
                                                            entry_4.get()) + "\' and b_publication=\'"+str(entry_5.get())+"\'"
                                                        cursor.execute(query)
                                                        details = cursor.fetchall()
                                                        if len(details)>0:
                                                            if dfdf.get()!='':
                                                                if c.get()!='':
                                                                    query = "select * from issue_book where enrollment_no=\'"+str(entry_0.get())+"\' and b_name=\'" + str(
                                                            entry_2.get()) + "\' and b_author=\'" + str(
                                                            entry_4.get()) + "\' and b_publication=\'"+str(entry_5.get())+"\'"
                                                                    cursor.execute(query)
                                                                    already_issued = cursor.fetchall()
                                                                    if len(already_issued)>0:
                                                                        showwarning('warninig','This Student Already Issued This Book')
                                                                        ads.destroy()
                                                                    else:
                                                                        if int(c.get()) == 15:
                                                                            dddd = "" + str(day) + "-" + str(
                                                                                month) + "-" + str(year)
                                                                            specified_date = datetime(int(year),
                                                                                                      int(month),
                                                                                                      int(day))
                                                                            new_date = specified_date + timedelta(15)
                                                                            y = new_date.year
                                                                            m = new_date.month
                                                                            d = new_date.day
                                                                            new_date = str(d) + "-" + str(
                                                                                m) + "-" + str(y)
                                                                        elif int(c.get()) == 30:
                                                                            dddd = "" + str(day) + "-" + str(
                                                                                month) + "-" + str(year)
                                                                            specified_date = datetime(int(year),
                                                                                                      int(month),
                                                                                                      int(day))
                                                                            new_date = specified_date + timedelta(30)
                                                                            y = new_date.year
                                                                            m = new_date.month
                                                                            d = new_date.day
                                                                            new_date = str(d) + "-" + str(
                                                                                m) + "-" + str(y)

                                                                        query = "select * from add_book where b_name=\'" + str(
                                                                            entry_2.get()) + "\' and b_author=\'" + str(
                                                                            entry_4.get()) + "\' and b_publication=\'" + str(
                                                                            entry_5.get()) + "\'"
                                                                        cursor.execute(query)
                                                                        no_of_books = cursor.fetchall()
                                                                        no_of_books = no_of_books[0]
                                                                        ohh_bawa = int(no_of_books[5]) - 1
                                                                        query = "update add_book set no_of_books=\'" + str(
                                                                            ohh_bawa) + "\' where b_name=\'" + str(
                                                                            entry_2.get()) + "\' and b_author=\'" + str(
                                                                            entry_4.get()) + "\' and b_publication=\'" + str(
                                                                            entry_5.get()) + "\'"
                                                                        cursor.execute(query)
                                                                        connection.commit()

                                                                        query = "select * from student where enrollment_no=\'" + str(
                                                                            entry_0.get()) + "\'"
                                                                        cursor.execute(query)
                                                                        all_student_details = cursor.fetchall()
                                                                        all_student_details = all_student_details[0]

                                                                        query = "insert into issue_book values(\'" + str(
                                                                            all_student_details[0]) + "\',\'" + str(
                                                                            all_student_details[1]) + "\',\'" + str(
                                                                            all_student_details[2]) + "\',\'" + str(
                                                                            no_of_books[0]) + "\',\'" + str(
                                                                            no_of_books[1]) + "\',\'" + str(
                                                                            no_of_books[4]) + "\',\'" + str(
                                                                            no_of_books[3]) + "\',\'" + str(
                                                                            no_of_books[2]) + "\',\'" + str(
                                                                            chacha_date) + "\',\'" + str(
                                                                            new_date) + "\',\'" + str(0) + "\')"
                                                                        cursor.execute(query)
                                                                        connection.commit()

                                                                        query = "select no_of_books from add_book where b_name=\'" + str(
                                                                            entry_2.get()) + "\' and b_author=\'" + str(
                                                                            entry_4.get()) + "\' and b_publication=\'" + str(
                                                                            entry_5.get()) + "\'"
                                                                        cursor.execute(query)
                                                                        llllllllllllllllllllll = cursor.fetchall()
                                                                        llllllllllllllllllllll = llllllllllllllllllllll[0]
                                                                        llllllllllllllllllllll = int(llllllllllllllllllllll[0])

                                                                        query = "select * from issue_book where enrollment_no=\'" + str(
                                                                            entry_0.get()) + "\' and b_name=\'" + str(
                                                                            entry_2.get()) + "\' and b_author=\'" + str(
                                                                            entry_4.get()) + "\' and b_publication=\'" + str(
                                                                            entry_5.get()) + "\'"
                                                                        cursor.execute(query)
                                                                        bbbbbbbbbbbbbbbbb = cursor.fetchall()

                                                                        if llllllllllllllllllllll==ohh_bawa and len(bbbbbbbbbbbbbbbbb)>0:
                                                                            showinfo('Issued Successfully','Books Issued Successfully')
                                                                            ads.destroy()
                                                                        else:
                                                                            showwarning('warning','Books Can\'t be Issued')

                                                                else:
                                                                    showwarning('warning','Please Select The Duration')
                                                            else:
                                                                showwarning('warning','Please select The Book Edition')
                                                        else:
                                                            showwarning('warning','This Publications did\'t match with the given book and author')
                                                    else:
                                                        showwarning('Warning','Please Enter The Publication')
                                                else:
                                                    showwarning('warning', 'The Author With this books did\'t match')
                                                    entry_4.delete(0,len(entry_4.get()))
                                            else:
                                                showwarning('warning','Pleas Enter The Book Author ')

                                        else:
                                            showwarning('warning','This Book is not in library')
                                            entry_2.delete(0, len(entry_2.get()))
                                    else:
                                        showwarning('warning','Please Enter The Book Title First')
                                else:
                                    showwarning('Warning', 'Please enter valid Enrollment no')
                                    entry_0.delete(0, len(entry_0.get()))
                            else:
                                showwarning('Warning', 'Please enter the enrollment no first')

                        Button(ads, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=280, y=330)
                        ads.mainloop()

                    else:
                        ads = Tk()
                        ads.resizable(False, False)

                        label_1 = Label(ads, text="Issue Book", width=20, font=("bold", 20),anchor='center')
                        label_1.place(x=120, y=5)
                        ads.geometry('500x400')

                        label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                        label_0.place(x=80, y=90)
                        entry_0 = Entry(ads, font=('Arial'))
                        entry_0.place(x=240, y=90)

                        def qr():
                            barcode = None

                            def barcodeReader(image, bgr):
                                gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                barcodes = decode(gray_img)

                                for decodedObject in barcodes:
                                    points = decodedObject.polygon

                                    pts = np.array(points, np.int32)
                                    pts = pts.reshape((-1, 1, 2))
                                    cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                                cv2.putText(frame, 'Press Q For Exit', (30, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                            (0, 255, 0), 4)
                                for bc in barcodes:
                                    cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30),
                                                cv2.FONT_HERSHEY_SIMPLEX, 1,
                                                bgr, 2)

                                    return bc.data.decode("utf-8")

                            bgr = (8, 70, 208)
                            cap = cv2.VideoCapture(0)
                            ok = True
                            while ok:
                                ret, frame = cap.read()
                                barcode = barcodeReader(frame, bgr)
                                if barcode != None:
                                    ok = False
                                    cap.release()
                                    cv2.destroyAllWindows()
                                    return barcode
                                cv2.imshow('Barcode reader', frame)
                                code = cv2.waitKey(10)
                                if code == ord('q'):
                                    break


                        def kala_kauaa():
                            if entry_0.get()!='':
                                query = "select * from student where enrollment_no=\'" + str(entry_0.get()) + "\'"
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if len(details)>0:
                                    barcode = qr()
                                    if barcode!=None:
                                        query = "select * from add_book where b_id=\'"+str(barcode)+"\'"
                                        cursor.execute(query)
                                        all_book_details = cursor.fetchall()
                                        all_book_details = all_book_details[0]

                                        if len(all_book_details)>0:
                                            label_2 = Label(ads, text="✓ Scanned Succesfully", width=20,
                                                            font=("Arial", 10))
                                            label_2.place(x=380, y=130)

                                            label_3 = Label(ads, text="Duration(days)", width=20, font=("Arial", 10))
                                            label_3.place(x=80, y=170)
                                            x = 250
                                            Branch = ['15', '30']
                                            c = StringVar(ads)
                                            droplist = OptionMenu(ads, c, *Branch)
                                            droplist.config(width=20)
                                            c.set('Select Duration')
                                            droplist.place(x=240, y=170)


                                            def submittttttttttttttttt():
                                                if c.get()=='Select Duration':
                                                    c.set('')
                                                if c.get()!='':
                                                    query = "select * from issue_book where where b_id=\'"+str(barcode)+"\' and enrollment_no=\'"+str(entry_0.get())+"\'"
                                                    cursor.execute(query)
                                                    already_issued = cursor.fetchall()
                                                    if len(already_issued)>0:
                                                        showwarning('warning', 'This Student Already Isuued This Book')
                                                    else:
                                                        if int(c.get()) == 15:
                                                            dddd = "" + str(day) + "-" + str(
                                                                month) + "-" + str(year)
                                                            specified_date = datetime(int(year),
                                                                                      int(month),
                                                                                      int(day))
                                                            new_date = specified_date + timedelta(15)
                                                            y = new_date.year
                                                            m = new_date.month
                                                            d = new_date.day
                                                            new_date = str(d) + "-" + str(
                                                                m) + "-" + str(y)
                                                        elif int(c.get()) == 30:
                                                            dddd = "" + str(day) + "-" + str(
                                                                month) + "-" + str(year)
                                                            specified_date = datetime(int(year),
                                                                                      int(month),
                                                                                      int(day))
                                                            new_date = specified_date + timedelta(30)
                                                            y = new_date.year
                                                            m = new_date.month
                                                            d = new_date.day
                                                            new_date = str(d) + "-" + str(
                                                                m) + "-" + str(y)

                                                        query = "select * from add_book where b_id=\'" + str(
                                                            barcode) + "\'"
                                                        cursor.execute(query)
                                                        no_of_books = cursor.fetchall()
                                                        no_of_books = no_of_books[0]
                                                        ohh_bawa = int(no_of_books[5]) - 1

                                                        query = "update add_book set no_of_books=\'" + str(
                                                            ohh_bawa) + "\' where b_id=\'" + str(barcode) + "\'"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "select * from student where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        all_student_details = cursor.fetchall()
                                                        all_student_details = all_student_details[0]

                                                        query = "insert into issue_book values(\'" + str(
                                                            all_student_details[0]) + "\',\'" + str(
                                                            all_student_details[1]) + "\',\'" + str(
                                                            all_student_details[2]) + "\',\'" + str(
                                                            no_of_books[0]) + "\',\'" + str(
                                                            no_of_books[1]) + "\',\'" + str(
                                                            no_of_books[4]) + "\',\'" + str(
                                                            no_of_books[3]) + "\',\'" + str(
                                                            no_of_books[2]) + "\',\'" + str(
                                                            chacha_date) + "\',\'" + str(
                                                            new_date) + "\',\'" + str(0) + "\')"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "select no_of_books from add_book where b_id=\'" + str(
                                                            barcode) + "\'"
                                                        cursor.execute(query)
                                                        llllllllllllllllllllll = cursor.fetchall()
                                                        llllllllllllllllllllll = llllllllllllllllllllll[0]
                                                        llllllllllllllllllllll = int(llllllllllllllllllllll[0])

                                                        query = "select * from issue_book where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\' and where b_id=\'" + str(
                                                            barcode) + "\'"
                                                        cursor.execute(query)
                                                        bbbbbbbbbbbbbbbbb = cursor.fetchall()

                                                        if llllllllllllllllllllll == ohh_bawa and len(
                                                                bbbbbbbbbbbbbbbbb) > 0:
                                                            showinfo('Issued Successfully', 'Books Issued Successfully')
                                                            ads.destroy()
                                                        else:
                                                            showwarning('warning', 'Books Can\'t be Issued')
                                                else:
                                                    showwarning('warning','Please Select The Duration first')

                                            Button(ads, text='Submit', width=15, bg='brown', fg='white',
                                                   command=submittttttttttttttttt).place(x=280, y=210)


                                        else:
                                            showwarning('warning','Please Scan The valid Bar Code')
                                    else:
                                        showwarning('Warning','Please Scan The Bar Code First')
                                else:
                                    showwarning('warning','Please Enter The Valid Enrollment No')
                                    entry_0.delete(0,len(entry_0.get()))
                            else:
                                showwarning('warning','Please Enter The Enrollment No')



                        Button(ads, text='Scan Qr Code', width=15, bg='brown', fg='white',command=kala_kauaa).place(x=240,y=130)
                        ads.mainloop()















            def create_admin():
                ads = Tk()
                ads.resizable(False, False)
                label_1 = Label(ads, text="Create Librarian", width=20, font=("bold", 20))
                label_1.place(x=120, y=5)
                ads.geometry('500x300')
                label_0 = Label(ads, text="Username", width=20, font=("Arial", 10))
                label_0.place(x=80, y=90)
                entry_0 = Entry(ads, font=('Arial'))
                entry_0.place(x=240, y=90)
                label_1 = Label(ads, text="Password", width=20, font=("Arial", 10))
                label_1.place(x=80, y=130)
                entry_1 = Entry(ads, font=('Arial'),show='*')
                entry_1.place(x=240, y=130)
                label_2 = Label(ads, text="Again Password", width=20, font=("Arial", 10))
                label_2.place(x=80, y=170)
                entry_2 = Entry(ads, font=('Arial'),show='*')
                entry_2.place(x=240, y=170)

                label_3 = Label(ads, text="Mobile No", width=20, font=("Arial", 10))
                label_3.place(x=80, y=210)
                entry_3 = Entry(ads, font=('Arial'))
                entry_3.place(x=240, y=210)

                def submit():
                    if entry_0.get()!='':
                        query = "select username from librarian where username=\'"+str(entry_0.get())+"\'"
                        cursor.execute(query)
                        details = cursor.fetchall()
                        if len(details)==0:
                            if entry_1.get()!='':
                                if entry_2.get()!='':
                                    if entry_1.get()==entry_2.get():
                                        if entry_3.get()!='':
                                            if str(entry_3.get()).isnumeric():
                                                if len(entry_3.get())==10:
                                                    query = "insert into librarian values(\'" + str(
                                                        entry_0.get()) + "\',\'" + str(entry_1.get()) + "\',\'" + str(entry_3.get()) + "\')"
                                                    cursor.execute(query)
                                                    connection.commit()
                                                    query = "select * from librarian where username=\'" + str(
                                                        entry_0.get()) + "\' and password=\'" + str(
                                                        entry_1.get()) + "\'"
                                                    cursor.execute(query)
                                                    details = cursor.fetchall()
                                                    if len(details) > 0:
                                                        showinfo('Congratulation\'s', 'User Added')
                                                        ads.destroy()
                                                    else:
                                                        showerror('Error', 'User does\'t added')
                                                        ads.destroy()
                                                else:
                                                    showerror('Error', 'Password does\'t matched')
                                                    entry_1.delete(0, len(entry_1.get()))
                                                    entry_2.delete(0, len(entry_2.get()))
                                            else:
                                                showwarning('Warning','Mobile No can\'t be Character')
                                                entry_3.delete(0,len(entry_3.get()))
                                        else:
                                            showwarning('Warning','Mobile No Can\'t be Empty')

                                else:
                                    showwarning('Missing','Please enter the password again')
                            else:
                                showwarning('Warning','Please enter the password')
                        else:
                            showwarning('Not Valid','Please use another username \n because this is already in use')
                            entry_0.delete(0,len(entry_0.get()))
                    else:
                        showwarning('Missing','Please enter the username')
                Button(ads, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=280, y=250)
                ads.mainloop()




            def see_all_details_having_fine():
                student_having_fine()



            # Return Book
            def return_book():
                adb = Tk()
                label_1 = Label(adb, text="Return Book", width=20, font=("bold", 20))
                label_1.place(x=90, y=5)
                adb.geometry('500x500')

                label_0 = Label(adb, text="Enrollment No", width=20, font=("Arial", 10))
                label_0.place(x=80, y=90)
                entry_0 = Entry(adb, font=('Arial'))
                entry_0.place(x=240, y=90)

                label_1 = Label(adb, text="Book Title", width=20, font=("Arial", 10))
                label_1.place(x=80, y=130)
                entry_1 = Entry(adb, font=('Arial'))
                entry_1.place(x=240, y=130)

                label_2 = Label(adb, text="Book Author", width=20, font=("Arial", 10))
                label_2.place(x=80, y=170)
                entry_2 = Entry(adb, font=('Arial'))
                entry_2.place(x=240, y=170)

                label_3 = Label(adb, text="Book Publication", width=20, font=("Arial", 10))
                label_3.place(x=80, y=210)
                entry_3 = Entry(adb, font=('Arial'))
                entry_3.place(x=240, y=210)

                label_5 = Label(adb, text="Edition", width=20, font=("Arial", 10))
                label_5.place(x=80, y=250)
                editiom = []
                for x in range(1, 21):
                    editiom.append(int(x))
                c = StringVar(adb)
                droplist = OptionMenu(adb, c, *editiom)
                droplist.config(width=20)
                c.set('Select Book Edition')
                droplist.place(x=240, y=250)

                global count
                count = 0

                def fine_submit():
                    global count
                    if c.get()=='Select Book Edition':
                        c.set('')
                    if entry_0.get()!='':
                        query = "select * from student where enrollment_no=\'"+str(entry_0.get())+"\'"
                        cursor.execute(query)
                        details = cursor.fetchall()
                        if len(details)>0:
                            if entry_1.get()!='':
                                if entry_2.get()!='':
                                    if entry_3.get()!='':
                                        if c.get()!='':
                                            query = "select * from add_book where b_name=\'"+str(entry_1.get())+"\' and b_author=\'"+str(entry_2.get())+"\' and b_publication=\'"+str(entry_3.get())+"\' and b_edition=\'"+str(c.get())+"\'"
                                            cursor.execute(query)
                                            details = cursor.fetchall()
                                            if len(details)>0:
                                                query = "select * from issue_book where b_name=\'" + str(
                                                    entry_1.get()) + "\' and b_author=\'" + str(
                                                    entry_2.get()) + "\' and b_publication=\'" + str(
                                                    entry_3.get()) + "\' and b_edition=\'" + str(c.get()) + "\' and enrollment_no=\'"+str(entry_0.get())+"\'"
                                                cursor.execute(query)
                                                details = cursor.fetchall()
                                                if len(details) > 0:
                                                    details = details[0]
                                                    fine_amount = details[10]
                                                    if int(fine_amount)>0:
                                                        label_3 = Label(adb, text="Fine Amount", width=20,
                                                                        font=("Arial", 10))
                                                        label_3.place(x=80, y=290)
                                                        Branchh = ['' + str(fine_amount) + '']
                                                        query = "select * from issue_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\' and enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        issued_book_details = cursor.fetchall()
                                                        issued_book_details = issued_book_details[0]

                                                        d = StringVar(adb)
                                                        droplist = OptionMenu(adb, d, *Branchh)
                                                        droplist.config(width=20)
                                                        d.set(str(issued_book_details[10]))
                                                        droplist.place(x=240, y=290)
                                                        count +=1
                                                        if count==1:
                                                            Button(adb, text='Submit', width=15, bg='brown',fg='white', command=fine_submit).place(x=280, y=330)
                                                            return ''


                                                        query = "select * from student where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        student_details = cursor.fetchall()
                                                        student_details = student_details[0]

                                                        query = "select * from issue_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\' and enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        issued_book_details = cursor.fetchall()
                                                        issued_book_details = issued_book_details[0]

                                                        query = "insert into fine_history values(\'" + str(
                                                            student_details[0]) + "\',\'" + str(
                                                            student_details[1]) + "\',\'" + str(
                                                            student_details[2]) + "\',\'" + str(
                                                            student_details[3]) + "\',\'" + str(
                                                            issued_book_details[3]) + "\',\'" + str(
                                                            issued_book_details[4]) + "\',\'" + str(
                                                            issued_book_details[5]) + "\',\'" + str(
                                                            issued_book_details[8]) + "\',\'" + str(
                                                            issued_book_details[9]) + "\',\'" + str(5) + "\',\'" + str(
                                                            issued_book_details[10]) + "\')"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "delete from issue_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\' and enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "select no_of_books from add_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\'"
                                                        cursor.execute(query)
                                                        ddddddddddddddd = cursor.fetchall()
                                                        ddddddddddddddd = ddddddddddddddd[0]
                                                        ddddddddddddddd = int(ddddddddddddddd[0]) + 1

                                                        query = "update add_book set no_of_books=\'" + str(
                                                            ddddddddddddddd) + "\' where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\'"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "select * from issue_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\' and enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        m1 = cursor.fetchall()

                                                        query = "select no_of_books from add_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\'"
                                                        cursor.execute(query)
                                                        m2 = cursor.fetchall()
                                                        m2 = m2[0]
                                                        m2 = int(m2[0])

                                                        if len(m1) > 0 and ddddddddddddddd != m2:
                                                            showwarning('warning', 'This Books Can\'t Be Returned')
                                                        else:
                                                            showinfo('Successfully', 'Book returned Successfully')
                                                            adb.destroy()
                                                    else:
                                                        count += 1
                                                        if count == 1:
                                                            Button(adb, text='Submit', width=15, bg='brown', fg='white',
                                                                   command=fine_submit).place(x=280, y=330)
                                                            return ''
                                                        query = "delete from issue_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\' and enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "select no_of_books from add_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\'"
                                                        cursor.execute(query)
                                                        ddddddddddddddd = cursor.fetchall()
                                                        ddddddddddddddd = ddddddddddddddd[0]
                                                        ddddddddddddddd = int(ddddddddddddddd[0]) + 1

                                                        query = "update add_book set no_of_books=\'" + str(
                                                            ddddddddddddddd) + "\' where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\'"
                                                        cursor.execute(query)
                                                        connection.commit()

                                                        query = "select * from issue_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\' and enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        m1 = cursor.fetchall()

                                                        query = "select no_of_books from add_book where b_name=\'" + str(
                                                            entry_1.get()) + "\' and b_author=\'" + str(
                                                            entry_2.get()) + "\' and b_publication=\'" + str(
                                                            entry_3.get()) + "\' and b_edition=\'" + str(
                                                            c.get()) + "\'"
                                                        cursor.execute(query)
                                                        m2 = cursor.fetchall()
                                                        m2 = m2[0]
                                                        m2 = int(m2[0])

                                                        if len(m1) > 0 and ddddddddddddddd != m2:
                                                            showwarning('warning', 'This Books Can\'t Be Returned')
                                                        else:
                                                            showinfo('Successfully', 'Book returned Successfully')
                                                            adb.destroy()
                                                else:
                                                    showwarning('warning', 'This Student Did\'t Issued This Book')
                                            else:
                                                showwarning('warning','This Book Is not In Library')
                                        else:
                                            showwarning('warning','Please Select The Book Edition')
                                    else:
                                        showwarning('warning','Please Enter The Book Publication')
                                else:
                                    showwarning('warning','Please Enter The Book Author')
                            else:
                                showwarning('warning','Please Enter The Book Title')
                        else:
                            showwarning('warning','This Enrollment Is not Valid')
                            entry_0.delete(0,len(entry_0.get()))
                    else:
                        showwarning('warning','Please Enter The Enrollment No')






                Button(adb, text='Cheack For Fine', width=15, bg='brown', fg='white', command=fine_submit).place(x=280, y=330)
                adb.mainloop()
            def qr():
                barcode = None

                def barcodeReader(image, bgr):
                    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    barcodes = decode(gray_img)

                    for decodedObject in barcodes:
                        points = decodedObject.polygon

                        pts = np.array(points, np.int32)
                        pts = pts.reshape((-1, 1, 2))
                        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

                    cv2.putText(frame, 'Press Q For Exit', (30, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                (0, 255, 0), 4)
                    for bc in barcodes:
                        cv2.putText(frame, bc.data.decode("utf-8") + " - " + bc.type, (30, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    bgr, 2)

                        return bc.data.decode("utf-8")

                bgr = (8, 70, 208)
                cap = cv2.VideoCapture(0)
                ok = True
                while ok:
                    ret, frame = cap.read()
                    barcode = barcodeReader(frame, bgr)
                    if barcode != None:
                        ok = False
                        cap.release()
                        cv2.destroyAllWindows()
                        return barcode
                    cv2.imshow('Barcode reader', frame)
                    code = cv2.waitKey(10)
                    if code == ord('q'):
                        break
            def return_book_via_scan_qr_code():

                ads = Tk()
                ads.resizable(False, False)

                label_1 = Label(ads, text="Return Book", width=20, font=("bold", 20))
                label_1.place(x=120, y=5)
                ads.geometry('600x400')

                label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                label_0.place(x=80, y=90)
                entry_0 = Entry(ads, font=('Arial'))
                entry_0.place(x=240, y=90)



                def submit_for_book():
                    if entry_0.get() != '':
                        query = "select * from student where enrollment_no=\'" + str(entry_0.get()) + "\'"
                        cursor.execute(query)
                        details = cursor.fetchall()
                        if len(details) > 0:
                            qr_code = qr()
                            query = "select * from add_book where b_id=\'"+str(qr_code)+"\'"
                            cursor.execute(query)
                            details = cursor.fetchall()
                            if len(details)>0:
                                query = "select * from issue_book where enrollment_no=\'"+str(entry_0.get())+"\' and b_id=\'"+str(qr_code)+"\'"
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if len(details)>0:
                                    query = "select fine_amount from issue_book where enrollment_no=\'"+str(entry_0.get())+"\' and b_id=\'"+str(qr_code)+"\'"
                                    cursor.execute(query)
                                    details = cursor.fetchall()
                                    details = details[0]
                                    fine_amount = int(details[0])
                                    if fine_amount>0:
                                        label_3 = Label(ads, text="Fine Amount", width=20, font=("Arial", 10))
                                        label_3.place(x=80, y=170)
                                        Branch = ['' + str(fine_amount) + '']
                                        c = StringVar(ads)
                                        droplist = OptionMenu(ads, c, *Branch)
                                        droplist.config(width=20)
                                        c.set('select fine amount')
                                        droplist.place(x=240, y=170)

                                        def shyamshyam():
                                            query = "select * from issue_book where enrollment_no=\'" + str(
                                                entry_0.get()) + "\' and b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            issue_details = cursor.fetchall()
                                            issue_details = issue_details[0]
                                            print(issue_details)



                                            query = "select * from student where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            student_details = cursor.fetchall()
                                            student_details = student_details[0]
                                            print(student_details)



                                            query = "delete from issue_book where enrollment_no=\'" + str(
                                                entry_0.get()) + "\' and b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select no_of_book_issued from student where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            bdd = cursor.fetchall()
                                            bdd = bdd[0]
                                            bdd = int(bdd[0])
                                            bdd -= 1
                                            query = "update student set no_of_book_issued=\'" + str(
                                                bdd) + "\' where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            connection.commit()

                                            query = "select no_of_books from add_book where b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            fffff = cursor.fetchall()
                                            fffff = fffff[0]
                                            fffff = int(fffff[0]) + 1
                                            query = "update add_book set no_of_books=\'" + str(
                                                fffff) + "\' where b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select * from issue_book where enrollment_no=\'" + str(
                                                entry_0.get()) + "\' and b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            aa = cursor.fetchall()

                                            query = "select no_of_books from add_book where b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            bb = cursor.fetchall()
                                            bb = bb[0]
                                            bb = int(bb[0])

                                            query = "select no_of_book_issued from student where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            cc = cursor.fetchall()
                                            cc = cc[0]
                                            cc = int(cc[0])

                                            query = "insert into fine_history values(\'" + str(
                                                student_details[0]) + "\',\'" + str(student_details[1]) + "\',\'" + str(
                                                student_details[2]) + "\',\'" + str(student_details[3]) + "\',\'" + str(
                                                issue_details[3]) + "\',\'" + str(issue_details[4]) + "\',\'" + str(
                                                issue_details[5]) + "\',\'" + str(issue_details[8]) + "\',\'" + str(
                                                issue_details[9]) + "\',\'" + str(
                                                int(int(issue_details[10]) / 5)) + "\',\'" + str(
                                                issue_details[10]) + "\') "
                                            cursor.execute(query)
                                            connection.commit()




                                            if int(cc) == int(bdd) and int(bb) == int(fffff) and len(
                                                    aa) == 0:
                                                showinfo('Info', 'Book Removed Sucessfully')
                                                ads.destroy()
                                            else:
                                                showerror('Error', 'Book Can\'t be returned')
                                                ads.destroy()


                                        def sssssss():
                                            if c.get()=='select fine amount':
                                                c.set('')
                                            if c.get()!='':
                                                shyamshyam()
                                            else:
                                                showwarning('Warning','Please select the fine amount first')
                                        Button(ads, text='submit', width=15, bg='brown', fg='white',
                                               command=sssssss).place(
                                            x=280, y=230)
                                    else:
                                        label_6 = Label(ads, text="✓ No Fine Due", width=20, font=("Arial", 15))
                                        label_6.place(x=200, y=170)
                                        def shyamshyam():
                                            query = "delete from issue_book where enrollment_no=\'" + str(
                                                entry_0.get()) + "\' and b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select no_of_book_issued from student where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            bdd = cursor.fetchall()
                                            bdd = bdd[0]
                                            bdd = int(bdd[0])
                                            bdd -= 1
                                            query = "update student set no_of_book_issued=\'" + str(
                                                bdd) + "\' where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            connection.commit()

                                            query = "select no_of_books from add_book where b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            fffff = cursor.fetchall()
                                            fffff = fffff[0]
                                            fffff = int(fffff[0]) + 1
                                            query = "update add_book set no_of_books=\'" + str(
                                                fffff) + "\' where b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select * from issue_book where enrollment_no=\'" + str(
                                                entry_0.get()) + "\' and b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            aa = cursor.fetchall()

                                            query = "select no_of_books from add_book where b_id=\'" + str(qr_code) + "\'"
                                            cursor.execute(query)
                                            bb = cursor.fetchall()
                                            bb = bb[0]
                                            bb = int(bb[0])

                                            query = "select no_of_book_issued from student where enrollment_no=\'" + str(
                                                entry_0.get()) + "\'"
                                            cursor.execute(query)
                                            cc = cursor.fetchall()
                                            cc = cc[0]
                                            cc = int(cc[0])

                                            if int(cc) == int(bdd) and int(bb) == int(fffff) and len(
                                                    aa) == 0:
                                                showinfo('Info', 'Book Returned Sucessfully')
                                                ads.destroy()
                                            else:
                                                showerror('Error', 'Book Can\'t be returned')
                                                ads.destroy()

                                        Button(ads, text='submit', width=15, bg='brown', fg='white',
                                               command=shyamshyam).place(
                                            x=280, y=230)

                                else:
                                    showwarning('Warning','This student did\'t issued this book')
                            else:
                                showwarning('Warning','This book is not in library Please scan the valid qr code')

                        else:
                            showwarning('Warninig', 'Please Enter The Valid Enrollment no')
                            entry_0.delete(0, len(entry_0.get()))
                    else:
                        showwarning('Warninng', 'Please enter the enrollment no')

                Button(ads, text='Scan Qr Code', width=15, bg='brown', fg='white',
                       command=submit_for_book).place(
                    x=280, y=230)
                ads.mainloop()
            def lllllll():
                ads = Tk()
                ads.resizable(False, False)

                label_1 = Label(ads, text="Return Book", width=9, font=("bold", 20))
                label_1.place(x=40, y=5)
                ads.geometry('250x100')


                def vvvvvvvvvvvv():
                    ads.destroy()
                    return_book()
                def sssssssssssssss():
                    ads.destroy()
                    return_book_via_scan_qr_code()
                Button(ads, text='By Entering Name \nof Book', width=15, bg='brown', fg='white',
                       command=vvvvvvvvvvvv).place(x=120, y=50)

                Button(ads, text='Scan Qr\nCode', width=8, height=2, bg='brown', fg='white', command=sssssssssssssss).place(x=10,y=50)
                ads.mainloop()





            def get_all_issued_student_details():
                aaa = askyesno("askyesno", "Do You Want Search for particular user yes/no")
                if aaa == True:
                    kkk = Tk()
                    label_1 = Label(kkk, text="Know Student Details", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    kkk.geometry('500x200')
                    label_1 = Label(kkk, text="Enter Name of Student", width=20, font=("Arial", 10))
                    label_1.place(x=80, y=130)
                    entry_1 = Entry(kkk, font=('Arial'))
                    entry_1.place(x=240, y=130)
                    def gett():
                        if entry_1.get() != '':
                            ah = entry_1.get()
                            query = "select * from student where name like \'%" + str(ah) + "%\'"
                            cursor.execute(query)
                            kh = cursor.fetchall()
                            if len(kh) > 0:
                                get_all_student_who_issue_book(entry_1.get())
                                kkk.destroy()
                            else:
                                print(showerror('ShowError', 'There is no student with this name'))
                        else:
                            print(showwarning('ShowError', 'Please Enter Name'))
                    Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=gett).place(x=260, y=170)
                    kkk.mainloop()
                else:
                    get_all_student_who_issue_book('False')


            def get_all_fine_history():

                aaa = askyesno("askyesno", "Do You Want Search for particular user yes/no")
                if aaa == True:
                    kkk = Tk()
                    label_1 = Label(kkk, text="Know Student Details", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)
                    kkk.geometry('500x200')
                    label_1 = Label(kkk, text="Enter Name of Student", width=20, font=("Arial", 10))
                    label_1.place(x=80, y=130)
                    entry_1 = Entry(kkk, font=('Arial'))
                    entry_1.place(x=240, y=130)
                    def gett():
                        if entry_1.get() != '':
                            ah = entry_1.get()
                            query = "select * from student where name like \'%" + str(ah) + "%\'"
                            cursor.execute(query)
                            kh = cursor.fetchall()
                            if len(kh) > 0:
                                admin_fine_history(entry_1.get())
                                kkk.destroy()
                            else:
                                print(showerror('ShowError', 'There is no student with this name'))
                        else:
                            print(showwarning('ShowError', 'Please Enter Name'))
                    Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=gett).place(x=260, y=170)
                    kkk.mainloop()
                else:
                    admin_fine_history('False')




            def import_csv():
                filename = []
                a = os.listdir()
                for x in a:
                    if len(x) > 5:
                        if x[-5:] == '.xlsx':
                            print('yes')
                            filename.append(x)


                if len(filename)>0:
                    llll = Tk()
                    label_1 = Label(llll, text="Select The Excel File", width=20, font=("bold", 20))
                    label_1.place(x=90, y=5)

                    llll.title(string='Select File')
                    label_11 = Label(llll, text=dddd, width=0, font=("bold", 11))
                    label_11.place(x=0, y=0)

                    label_5 = Label(llll, text="Select File", width=20, font=("Arial", 10))
                    label_5.place(x=80, y=100)
                    c = StringVar(llll)
                    droplist = OptionMenu(llll, c, *filename)
                    droplist.config(width=20)
                    c.set('Select The Excel File')
                    droplist.place(x=240, y=100)
                    llll.geometry('500x300')
                    llll.resizable(False, False)

                    def ggggggggg():
                        if c.get()=='Select The Excel File':
                            c.set('')
                        if c.get()!='':
                            s = pd.read_excel(str(c.get()))
                            a = s[['enrollment_no', 'name', 'branch', 'semester', 'address', 'mobile_no',
                                   'DOB']].to_numpy().tolist()
                            i = 2
                            b = str()
                            f_date = date(int(year), int(month), int(day))
                            query = "select * from student"
                            cursor.execute(query)
                            student_details = cursor.fetchall()
                            kkkkkkkkkkkkkkkkkkkk = []
                            for x in student_details:
                                kkkkkkkkkkkkkkkkkkkk.append(x[0])
                            if len(kkkkkkkkkkkkkkkkkkkk)>0:
                                bef_len = len(student_details)
                            else:
                                bef_len=0
                            for x in a:
                                # print(x)
                                ff = str(x[6])
                                ff = str(ff[:10])
                                a = ff.split('-')
                                if str(x[0]) == 'nan' or str(x[1]) == 'nan' or str(x[2]) == 'nan' or str(
                                        x[3]) == 'nan' or str(x[4]) == 'nan' or str(x[5]) == 'nan' or str(
                                        x[6]) == 'NaT':
                                    b += 'Something is missing in Row :- ' + str(i) + '\n'
                                else:
                                    ddddddddddd = str(a[2]) + '-' + str(a[1]) + '-' + str(a[0])
                                    ddddddddd = str(a[0]) + '-' + str(a[1]) + '-' + str(a[2])
                                    print(ddddddddd)
                                    if str(x[0]) not in kkkkkkkkkkkkkkkkkkkk:
                                        date_format = '%Y-%m-%d'
                                        cheack_validate = validate(ddddddddd, date_format)
                                        if cheack_validate == True:
                                            l_date = date(int(a[0]), int(a[1]), int(a[2]))
                                            delta = l_date - f_date
                                            new_year = (delta.days + delta.seconds / 86400) / 365.2425
                                            best_age = int(abs(new_year))
                                            print(best_age)
                                            if int(best_age) > 13:
                                                if str(x[5]).isnumeric():
                                                    if len(str(x[5]))==10:
                                                        query = "insert into student values(\'" + str(
                                                            x[0]) + "\',\'" + str(
                                                            x[1]) + "\',\'" + str(
                                                            x[2]) + "\',\'" + str(x[3]) + "\',\'" + str(
                                                            best_age) + "\',\'" + str(
                                                            x[4]) + "\',\'" + str('shyam') + "\',\'" + str(
                                                            0) + "\',\'" + str(
                                                            x[5]) + "\',\'" + str(
                                                            ddddddddddd) + "\')"
                                                        cursor.execute(query)
                                                        connection.commit()
                                                    else:
                                                        b += 'Row '+str(i)+' Mobile No format is wrong\n'
                                            else:
                                                b += 'Row ' + str(i) + ' Age Must Be Greater Then 13 ' + '\n'
                                        else:
                                            b += 'Row ' + str(i) + ' date is not valid ' + '\n'

                                i += 1
                            query = "select * from student"
                            cursor.execute(query)
                            aft_len = len(cursor.fetchall())
                            if aft_len > bef_len:
                                showinfo('Information', 'Data Inserted successfully')
                            else:
                                showwarning('warning', 'Data Can\'t be inserted because data is already present in the database')
                            if b != '':
                                showerror('Error', b)
                        else:
                            showwarning('Warning','Please Select The File ')


                    Button(llll, text='Submit', width=15, bg='brown', fg='white',command=ggggggggg).place(x=260, y=190)
                    llll.mainloop()
                else:
                    showwarning('warning','There is No any file with the extension \'.xlsx\'')






                # showwarning('Warning','This is under progress ')







            def edit_all_book_details():
                add = Tk()
                label_1 = Label(add, text="Increase Book", width=15, font=("bold", 20))
                label_1.place(x=57, y=45)
                add.title(string='Select the mode of Increasing the book')
                label_11 = Label(add, text=dddd, width=0, font=("bold", 11))
                label_11.place(x=0, y=0)


                def set_the_query_for():
                    add.destroy()
                    bbaarcode = qr()
                    if bbaarcode!=None:
                        query = "select * from add_book where b_id=\'"+str(bbaarcode)+"\'"
                        cursor.execute(query)
                        ddetails = cursor.fetchall()
                        if len(ddetails)>0:
                            adb = Tk()
                            label_1 = Label(adb, text="Edit Book Details", width=20, font=("bold", 20))
                            label_1.place(x=200, y=5)
                            adb.geometry('700x500')

                            query = "select * from add_book where b_id=\'" + str(bbaarcode) + "\'"
                            cursor.execute(query)
                            all_details = cursor.fetchall()
                            all_details = all_details[0]

                            label_1 = Label(adb, text="Book Id", width=20, font=("Arial", 10))
                            label_1.place(x=200, y=130)
                            entry_1 = Entry(adb, font=('Arial'), cursor='no')
                            entry_1.place(x=360, y=130)
                            entry_1.insert(0, all_details[0])
                            entry_1.config(state=DISABLED)

                            label_2 = Label(adb, text="Book Name", width=20, font=("Arial", 10))
                            label_2.place(x=200, y=170)
                            entry_2 = Entry(adb, font=('Arial'))
                            entry_2.place(x=360, y=170)
                            entry_2.insert(0, all_details[1])

                            label_3 = Label(adb, text="Book Author", width=20, font=("Arial", 10))
                            label_3.place(x=200, y=210)
                            entry_3 = Entry(adb, font=('Arial'))
                            entry_3.place(x=360, y=210)
                            entry_3.insert(0, all_details[2])

                            label_4 = Label(adb, text="Book Publication", width=20, font=("Arial", 10))
                            label_4.place(x=200, y=250)
                            entry_4 = Entry(adb, font=('Arial'))
                            entry_4.place(x=360, y=250)
                            entry_4.insert(0, all_details[3])

                            label_7 = Label(adb, text="Book Edition", width=20, font=("Arial", 10))
                            label_7.place(x=200, y=290)
                            editiom = []
                            for x in range(1, 21):
                                editiom.append(int(x))
                            c = StringVar(adb)
                            droplist = OptionMenu(adb, c, *editiom)
                            droplist.config(width=20)
                            c.set(str(all_details[4]))
                            droplist.place(x=360, y=290)

                            label_6 = Label(adb, text="No Of Books", width=20, font=("Arial", 10))
                            label_6.place(x=200, y=330)
                            entry_6 = Entry(adb, font=('Arial'), cursor='no')
                            entry_6.place(x=360, y=330)
                            entry_6.insert(0, all_details[5])
                            entry_6.config(state=DISABLED)

                            def sanjay_and_shyam():
                                if entry_2.get()!='':
                                    if entry_3.get()!='':
                                        query = "select * from add_book where b_id=\'"+str(bbaarcode)+"\' and b_edition=\'" + str(c.get()) + "\' and b_publication=\'"+str(entry_4.get())+"\' and b_author=\'"+str(entry_3.get())+"\'"
                                        cursor.execute(query)
                                        cccccccc = cursor.fetchall()
                                        if len(cccccccc) > 0:
                                            showwarning('warrning','The Provided Details is already exists')
                                        else:
                                            query = "update add_book set b_name=\'" + str(
                                                entry_2.get()) + "\',b_author=\'" + str(
                                                entry_3.get()) + "\',b_edition=\'" + str(
                                                c.get()) + "\' where b_id=\'" + str(bbaarcode) + "\'"
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select * from add_book where b_id=\'" + str(bbaarcode) + "\'"
                                            cursor.execute(query)
                                            ddeettaaiillss = cursor.fetchall()
                                            ddeettaaiillss = ddeettaaiillss[0]
                                            if ddeettaaiillss[1] == str(entry_2.get()) and ddeettaaiillss[2] == str(
                                                    entry_3.get()) and ddeettaaiillss[4] == str(c.get()):
                                                showinfo('Information', 'Data Inserted Successfully')
                                                adb.destroy()
                                            else:
                                                showwarning('warning', 'Data Can\'t be inserted because of some issue')

                                    else:
                                        showwarning('warning','Please Enter The Author Of Book')
                                else:
                                    showwarning('warning','Please Enter The Book Name')

                            Button(adb, text='Save', width=15, bg='brown', fg='white', cursor='hand2',command=sanjay_and_shyam).place(x=370, y=390)
                            adb.resizable(False, False)
                            adb.mainloop()
                        else:
                            showwarning('warning','Please scan the valid book')
                    else:
                        showwarning('warning','Please scan the qr code first')




                def set_details_using_name_of_book():
                    add.destroy()
                    addd = Tk()
                    label_1 = Label(addd, text="Edit Book Details", width=20, font=("bold", 20))
                    label_1.place(x=120, y=5)
                    label_4 = Label(addd, text="Name Of Book", width=20, font=("Arial", 10))
                    label_4.place(x=80, y=100)
                    entry_4 = Entry(addd, font=('Arial'))
                    entry_4.place(x=240, y=100)

                    def ssss():
                        return entry_4.get()

                    def llllllllllll():
                        book_name = ssss()
                        addd.destroy()
                        query = "select * from add_book where b_name=\'"+str(book_name)+"\'"
                        cursor.execute(query)
                        details = cursor.fetchall()
                        if len(details)>0:
                            adb = Tk()
                            label_1 = Label(adb, text="Edit Book Details", width=20, font=("bold", 20))
                            label_1.place(x=200, y=5)
                            adb.geometry('700x500')

                            query = "select * from add_book where b_name=\'"+str(book_name)+"\'"
                            cursor.execute(query)
                            details = cursor.fetchall()
                            details = details[0]

                            label_1 = Label(adb, text="Book Id", width=20, font=("Arial", 10))
                            label_1.place(x=200, y=130)
                            entry_1 = Entry(adb, font=('Arial'), cursor='no')
                            entry_1.place(x=360, y=130)
                            entry_1.insert(0, details[0])
                            entry_1.config(state=DISABLED)

                            label_2 = Label(adb, text="Book Name", width=20, font=("Arial", 10))
                            label_2.place(x=200, y=170)
                            entry_2 = Entry(adb, font=('Arial'))
                            entry_2.place(x=360, y=170)
                            entry_2.insert(0, details[1])

                            label_3 = Label(adb, text="Book Author", width=20, font=("Arial", 10))
                            label_3.place(x=200, y=210)
                            entry_3 = Entry(adb, font=('Arial'))
                            entry_3.place(x=360, y=210)
                            entry_3.insert(0, details[2])

                            label_4 = Label(adb, text="Book Publication", width=20, font=("Arial", 10))
                            label_4.place(x=200, y=250)
                            entry_4 = Entry(adb, font=('Arial'))
                            entry_4.place(x=360, y=250)
                            entry_4.insert(0, details[3])

                            label_7 = Label(adb, text="Book Edition", width=20, font=("Arial", 10))
                            label_7.place(x=200, y=290)
                            editiom = []
                            for x in range(1, 21):
                                editiom.append(int(x))
                            c = StringVar(adb)
                            droplist = OptionMenu(adb, c, *editiom)
                            droplist.config(width=20)
                            c.set(str(details[4]))
                            droplist.place(x=360, y=290)

                            label_6 = Label(adb, text="No Of Books", width=20, font=("Arial", 10))
                            label_6.place(x=200, y=330)
                            entry_6 = Entry(adb, font=('Arial'), cursor='no')
                            entry_6.place(x=360, y=330)
                            entry_6.insert(0, details[5])
                            entry_6.config(state=DISABLED)

                            def sanjay_and_shyam():
                                if entry_2.get() != '':
                                    if entry_3.get() != '':
                                        query = "select * from add_book where b_name=\'" + str(entry_2.get()) + "\' and b_edition=\'" + str(c.get()) + "\' and b_publication=\'" + str(entry_4.get()) + "\' and b_author=\'" + str(entry_3.get()) + "\'"
                                        cursor.execute(query)
                                        cccccccc = cursor.fetchall()
                                        if len(cccccccc)>0:
                                            showwarning('warrning','The Provided Details is already exists')
                                        else:
                                            query = "update add_book set b_name=\'" + str(
                                                entry_2.get()) + "\',b_author=\'" + str(
                                                entry_3.get()) + "\',b_edition=\'" + str(
                                                c.get()) + "\',b_publication=\'" + str(
                                                entry_4.get()) + "\' where b_name=\'" + str(book_name) + "\'"
                                            cursor.execute(query)
                                            connection.commit()
                                            query = "select * from add_book where b_name=\'" + str(entry_2.get()) + "\'"
                                            cursor.execute(query)
                                            ddeettaaiillss = cursor.fetchall()
                                            ddeettaaiillss = ddeettaaiillss[0]
                                            if ddeettaaiillss[1] == str(entry_2.get()) and ddeettaaiillss[2] == str(
                                                    entry_3.get()) and ddeettaaiillss[4] == str(c.get()):
                                                showinfo('Information', 'Data Inserted Successfully')
                                            else:
                                                showwarning('warning', 'Data Can\'t be inserted because of some issue')
                                    else:
                                        showwarning('warning', 'Please Enter The Author Of Book')
                                else:
                                    showwarning('warning', 'Please Enter The Book Name')

                            Button(adb, text='Save', width=15, bg='brown', fg='white', cursor='hand2',
                                   command=sanjay_and_shyam).place(x=370, y=390)
                            adb.resizable(False, False)
                            adb.mainloop()
                        else:
                            showwarning('Warning','This book is not in library')

                    addd.geometry('500x300')
                    Button(addd, text='Submit', width=15, bg='brown', fg='white',command=llllllllllll).place(x=260,y=140)
                    addd.resizable(False, False)
                    addd.mainloop()


                Button(add, text='Scan Qr Code', width=15, height=2, bg='brown', fg='white',command=set_the_query_for).place(x=10, y=90)
                Button(add, text='Or By Book Name', width=15, height=2, bg='brown', fg='white',command=set_details_using_name_of_book).place(x=150, y=90)
                add.geometry('300x200')
                add.resizable(False, False)
                add.mainloop()





            def change_password():
                cpa = Tk()
                cpa.geometry('500x300')
                cpa.resizable(False, False)
                label_6 = Label(cpa, text="Change Password", width=20, font=("bold", 20))
                label_6.place(x=90, y=5)
                label_1 = Label(cpa, text="Password", width=20, font=("Arial", 10))
                label_1.place(x=80, y=130)
                entry_1 = Entry(cpa, font=('Arial'), show='*')
                entry_1.place(x=240, y=130)
                label_2 = Label(cpa, text="Again Password", width=20, font=("Arial", 10))
                label_2.place(x=80, y=170)
                entry_2 = Entry(cpa, font=('Arial'), show='*')
                entry_2.place(x=240, y=170)

                # Completed
                def Check_pass_match():
                    if entry_1.get()!='':
                        if entry_2.get()!='':
                            if entry_1.get()==entry_2.get():
                                query = "select password from admin where username=\'" + str(username) + "\'"
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if entry_1.get()!=details[0][0]:
                                    query = "update admin set password=\'"+str(entry_1.get())+"\' where username=\'"+str(username)+"\'"
                                    cursor.execute(query)
                                    connection.commit()
                                    query = "select password from admin where username=\'" + str(username) + "\'"
                                    cursor.execute(query)
                                    details = cursor.fetchall()
                                    if entry_1.get()==details[0][0]:
                                        showinfo('Information','Password Changed Successully')
                                        cpa.destroy()
                                    else:
                                        showwarning('warning','Something going wrong')
                                else:
                                    showwarning('warning','password can\'t be same as previous one')
                            else:
                                showwarning('warning','Password Did\'t matched')
                        else:
                            showwarning('warning','Please Enter The password')
                    else:
                        showwarning('warning','Please Enter The Password')


                Button(cpa, text='Change Password', width=15, bg='brown', fg='white',
                       command=Check_pass_match).place(
                    x=260, y=220)
                cpa.mainloop()





            def mera_nam_lakan():
                add = Tk()
                label_1 = Label(add, text="Add Book", width=10, font=("bold", 20))
                label_1.place(x=57, y=5)
                add.title(string='Select the mode of adding the book')
                label_11 = Label(add, text=dddd, width=0, font=("bold", 11))
                label_11.place(x=0, y=0)

                Button(add, text='Import CSV', width=15, height=2, bg='brown', fg='white', command=import_csv).place(
                    x=10,
                    y=50)
                Button(add, text='Add Manually', width=15, height=2, bg='brown', fg='white', command=add_student).place(
                    x=150, y=50)
                add.geometry('280x200')
                add.resizable(False, False)
                add.mainloop()


            query = "select * from admin where username=\'"+str(username)+"\'"
            cursor.execute(query)
            all_admin = cursor.fetchall()

            query = "select * from librarian where username=\'"+str(username)+"\'"
            cursor.execute(query)
            library_details = cursor.fetchall()

            ad = Tk()
            if len(all_admin)>0:
                label_1 = Label(ad, text="Admin", width=20, bg='#8FBC8F',fg='black', font=("Algerian", 20))
                label_1.place(x=80, y=5)
            elif len(library_details):
                label_1 = Label(ad, text="Librarian", width=20, bg='#8FBC8F', fg='black', font=("Algerian", 20))
                label_1.place(x=80, y=5)
            ad.title(string='Admin')
            label_11 = Label(ad, text=dddddddddd, width=0, font=("bold", 11), bg='#8FBC8F',fg='black')
            label_11.place(x=390, y=0)
            label_5 = Label(ad, text="Admin Profile", width=20, font=("bold", 9), bg='#8FBC8F',fg='black')
            label_5.place(x=380, y=280)
            # Completed
            Button(ad, text='Add Book', width=8, height=2, command=kkkk,bg='#BDB76B', fg='black',cursor='hand2').place(x=10, y=50)
            # Completed
            Button(ad, text='Add Student', width=10, height=2,command=mera_nam_lakan,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=90, y=50)
            # Completed
            if len(all_admin)>0:
                Button(ad, text='Call Librarien', width=18, height=2, command=calling_librarian,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=180, y=50)
            elif len(library_details)>0:
                Button(ad, text='Call Administrator', width=18, height=2, command=calling, bg='#BDB76B', fg='black',
                       cursor='hand2').place(x=180, y=50)
            # Completed
            Button(ad, text='Know Student Detail\'s', width=22, height=2, command=student_id_password,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=330, y=50)
            # Completed
            Button(ad, text='Remove \nBook', width=8, height=2, command=remove_book,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=10, y=100)
            # Completed
            Button(ad, text='Issue Book', width=10, height=2,  command=issue_book,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=90, y=100)
            # Not Completed
            Button(ad, text='Return Book', width=18, height=2, command=lllllll ,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=180, y=100)
            # Completed
            Button(ad, text='No of books \n that are not in library', width=22, height=2, command=no_of_book_not_in_library,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=330, y=100)
            # Completed
            Button(ad, text='Forgot \n QR Code', width=8, height=2,  command=get_qr_code,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=10, y=150)
            # Completed
            Button(ad, text='Know Book Detail\'s', width=22, height=2,
                   command=bgbgbgbgbgbgbgbg,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=330, y=150)
            Button(ad, text='Fine History', width=22, height=2,
                   command=get_all_fine_history,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=330, y=200)
            if len(all_admin)>0:
                Button(ad, text='Create \nLibrarian', width=10, height=2,   command=create_admin,bg='#BDB76B', fg='black', cursor = 'hand2').place(
                    x=90, y=150)
            Button(ad, text='Student\'s Having Fine', width=18, height=2,  command=see_all_details_having_fine,bg='#BDB76B', fg='black', cursor = 'hand2').place(x=180, y=150)
            Button(ad, text='Student\'s Isuued Book', width=18, height=2,  command=get_all_issued_student_details,bg='#BDB76B', fg='black', cursor = 'hand2' ).place(x=180, y=200)
            ad.geometry('500x300')
            # Button(ad, text='Edit Book Details', width=18, height=2, command=edit_all_book_details,
            #        bg='#BDB76B', fg='black', cursor='hand2').place(x=180, y=250)
            ad.resizable(False, False)
            Button(ad, text='Change\n Password', width=10, height=2, command=change_password, bg='#BDB76B', fg='black',
                   cursor='hand2').place(
                x=90, y=200)

            if len(all_admin)>0:
                ad.title('Admin')
            elif len(library_details):
                ad.title('Librarian')
            ad.title('Admin')
            # p = PhotoImage(file="shyam.png")
            # ad.iconphoto(False, p)
            ad.configure(bg='#8FBC8F')

            def update():  # take process bar for example
                gggg = str()
                now = pappu.now()
                current_time = now.strftime("%H:%M:%S")
                if int(current_time[:2]) > 12:
                    gggg += str(int(current_time[:2]) - 12) + str(current_time[2:])
                else:
                    gggg = current_time
                label_5 = Label(ad, text=gggg, bg='#8FBC8F', fg='black', font=("bold", 15))
                label_5.place(x=0, y=0)
                ad.after(1000, update)

            update()

            def mmmmmmmmmmmmm():
                # print(mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm())
                label_11 = Label(ad, text=mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm(), bg='#8FBC8F', fg='black', width=0,
                                 font=("bold", 11))
                label_11.place(x=380 - len(mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm()), y=0)

                ad.after(1000, mmmmmmmmmmmmm)

            mmmmmmmmmmmmm()




            ad.mainloop()
    except Error as e:
        print('This is not opeating', e)
    finally:
        connection.close()
        print(connection.is_connected())
if __name__ == '__main__':
    showwarning('Info', 'Please Login first using \'Log_in.py\' file')
    exit(0)
