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
from open_in_web_browser import open_web_browser
from Scan_Qr_Code import scan
from print_all_book_not_in_library import print_all_details_book_not_in_library
from know_student_id_password import know_student_id_password
from Date_Validate import validate
from get_bok_details import get_book_detailss
from students_haing_fine import student_having_fine



def admin(username,password):
    count = 0
    tdate = date.today()
    day = tdate.day
    month = tdate.month
    year = tdate.year
    print(day, ' ', month, " ", year)
    dddd = "" + str(day) + "-" + str(month) + "-" + str(year) + ""
    try:
        connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
        if connection.is_connected():
            cursor = connection.cursor()
            # Completed
            def genrate_qrcode():
                l = int(len(os.listdir('BarCode/')))
                l = l + 1
                filename = ('BarCode/' + str(l))
                sss = True
                while sss:
                    s = str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9)) + str(randint(0, 9))
                    query = "select * from add_book where b_id= \'"+str(s)+"\' "
                    cursor.execute(query)
                    details = cursor.fetchall()
                    if len(details)>0:
                        pass
                    elif len(details)<=0:
                        sss = False
                print(s)
                url = pyqrcode.create(s)
                url.svg(filename + '.svg', scale=8)
                return s,filename+'.svg'
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
                                            if c.get() != '':
                                                c = int(c.get())
                                                query = "select * from add_book where b_name= \'" + str(
                                                    entry_1.get()) + "\' "
                                                cursor.execute(query)
                                                alll = cursor.fetchall()
                                                if len(alll) == 0:
                                                    s, filename = genrate_qrcode()
                                                    query = "insert into add_book values(\'" + str(s) + "\',\'" + str(
                                                        entry_1.get()) + "\',\'" + str(entry_2.get()) + "\',\'" + str(
                                                        entry_3.get()) + "\',\'" + str(c) + "\',\'" + str(
                                                        entry_4.get()) + "\')"
                                                    cursor.execute(query)
                                                    connection.commit()
                                                    query = "select * from add_book where b_name= \'" + str(
                                                        entry_1.get()) + "\' "
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
                                                    print(showwarning('ALREADY IN LIBRARY',
                                                                      'This Book is already added in the library'))
                                                    adb.destroy()
                                            else:
                                                print(showwarning('EDITION', 'Select the Edition'))
                                        except:
                                            print(showerror('PLEASE USE DIGIT',
                                                            'Enter no of books in digit \n not in letter'))
                                            entry_4.delete(0, len(entry_4.get()))
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
                        submiitt(c)

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
                            label_1 = Label(adb, text="Add Book", width=20, font=("bold", 20))
                            label_1.place(x=90, y=5)
                            adb.geometry('500x300')
                            label_11 = Label(adb, text=dddd, width=0, font=("bold", 11))
                            label_11.place(x=0, y=0)
                            label_1 = Label(adb, text="Book Title", width=20, font=("Arial", 10))
                            label_1.place(x=80, y=130)
                            entry_1 = Entry(adb, font=('Arial'))
                            entry_1.place(x=240, y=130)
                            label_4 = Label(adb, text="No Of Books to be increased", width=20, font=("Arial", 10))
                            label_4.place(x=80, y=170)
                            entry_4 = Entry(adb, font=('Arial'))
                            entry_4.place(x=240, y=170)

                            def submit():
                                if entry_1.get() != '':
                                    if entry_4.get() != '':
                                        try:
                                            kkk = int(entry_4.get())
                                            query = "select * from add_book where b_name= \'" + str(
                                                entry_1.get()) + "\' "
                                            print('1')
                                            cursor.execute(query)
                                            alll = cursor.fetchall()
                                            print('2')
                                            if len(alll) > 0:
                                                alll = alll[0]
                                                nobtbad = alll[5]
                                                print('3')
                                                nobtbad = int(nobtbad) + int(entry_4.get())
                                                print('9')
                                                query = "update add_book set no_of_books= \'" + str(
                                                    nobtbad) + "\' where b_name=\'" + str(entry_1.get()) + "\' "
                                                cursor.execute(query)
                                                print('10')
                                                connection.commit()
                                                print('4')
                                                query = "select * from add_book where b_name= \'" + str(
                                                    entry_1.get()) + "\' "
                                                cursor.execute(query)
                                                alll = cursor.fetchall()
                                                alll = alll[0]
                                                nobtbadd = alll[5]
                                                print('5')
                                                if int(nobtbad) == int(nobtbadd):
                                                    print(showinfo('Book Increased succcesfully',
                                                                   'Book Increased succesfully'))
                                                    adb.destroy()
                                                else:
                                                    print(showerror('Book Not Increased',
                                                                    'Book Can\'t be increased just\n because of some problem'))
                                            else:
                                                print(showerror('Book Not Found',
                                                                'This book is not in library please enter the \n valid book name'))
                                                entry_1.delete(0, len(entry_1.get()))
                                        except:
                                            print(showwarning('MISSING',
                                                              'Please Enter the no of books in digit \n not in character'))
                                            entry_4.delete(0, len(entry_4.get()))
                                    else:
                                        print(showwarning('MISSING', 'Please Enter the no of books'))
                                else:
                                    print(showwarning('MISSING', 'Please Enter the name of the book'))

                            Button(adb, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=260,
                                                                                                               y=210)
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


                Button(add, text='Add New Book', width=15, height=2, bg='brown', fg='white', command=add_book).place(x=10,
                                                                                                                y=50)
                Button(add, text='Increase Book', width=15, height=2, bg='brown', fg='white',command=kkkkkk).place(x=150, y=50)
                add.geometry('300x200')
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
                        print(showerror('ShowError', 'Call Has Been Sent to the Provided Mobile Number'))
                    else:
                        print(showerror('ShowError', 'There is some issue while calling'))
                elif aaa == 'False':
                    print(showerror('ShowError', 'Call is cancled'))

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
                Branch = ['CSE', 'EE', 'EC', 'ME', 'CE']
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
                    rmb.geometry('250x100')

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
                        gg.geometry('500x300')

                        label_1 = Label(gg, text="Enter the name of book", width=20, font=("Arial", 10))
                        label_1.place(x=80, y=150)
                        entry_1 = Entry(gg, font=('Arial'))
                        entry_1.place(x=240, y=150)

                        def ppp():
                            if entry_1.get() != '':
                                query = "select * from add_book where b_name=\'" + str(entry_1.get()) + "'"
                                cursor.execute(query)
                                all_dd = cursor.fetchall()
                                if len(all_dd) > 0:
                                    query = "delete from add_book where b_name=\'" + str(entry_1.get()) + "\'"
                                    cursor.execute(query)
                                    connection.commit()
                                    query = "select * from add_book where b_name=\'" + str(entry_1.get()) + "'"
                                    cursor.execute(query)
                                    all_dd = cursor.fetchall()
                                    if len(all_dd) == 0:
                                        print(showinfo('Congratulations', 'Book Deleted Successfully'))
                                        gg.destroy()
                                    else:
                                        print(showerror('ShowError', 'Book Can\'t be deleted because of some problem'))
                                        gg.destroy()
                                else:
                                    print(showerror('ShowError', 'This Book is not in Library'))
                                    gg.destroy()
                            else:
                                print(showwarning('ShowError', 'Please enter the name of book'))
                                entry_1.delete(0, len(entry_1.get()))

                        Button(gg, text='Submit', width=15, bg='brown', fg='white', command=ppp).place(x=260, y=190)
                        gg.resizable(False, False)
                        gg.mainloop()

                    Button(rmb, text='By Entering Name \nof Book', width=15, bg='brown', fg='white',
                           command=submit_book).place(x=120, y=50)
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
                    query = "select * from add_book"
                    cursor.execute(query)
                    details = cursor.fetchall()
                    editiom = []
                    for x in details:
                        if x[1] == 'NULL':
                            pass
                        else:
                            editiom.append(x[1])
                    c = StringVar(llll)
                    droplist = OptionMenu(llll, c, *editiom)
                    droplist.config(width=20)
                    c.set('Select Book Edition')
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
                            query = "select b_id from add_book where b_name= \'" + str(c) + "\' "
                            cursor.execute(query)
                            details = cursor.fetchall()
                            if len(details) > 0:
                                details = details[0]
                                details = details[0]
                                url = pyqrcode.create(details)
                                url.svg(filename + '.svg', scale=8)
                                return filename + '.svg'
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
                    def gett():
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
                    Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=gett).place(x=260, y=170)
                    kkk.mainloop()
                else:
                    get_book_detailss('False')


            # Completed
            def issue_book():
                query = "select * from add_book"
                cursor.execute(query)
                nnnnnn = cursor.fetchall()
                if len(nnnnnn)>0:

                    ads = Tk()
                    ads.resizable(False, False)

                    label_1 = Label(ads, text="Issue Book", width=20, font=("bold", 20))
                    label_1.place(x=120, y=5)
                    ads.geometry('600x400')

                    label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                    label_0.place(x=80, y=90)
                    entry_0 = Entry(ads, font=('Arial'))
                    entry_0.place(x=240, y=90)
                    aaa = askyesno("askyesno", "Do You want to scan qr code or not yes/no")

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

                    if aaa == False:
                        label_2 = Label(ads, text="Name Of Book", width=20, font=("Arial", 10))
                        label_2.place(x=80, y=170)
                        entry_2 = Entry(ads, font=('Arial'))
                        entry_2.place(x=240, y=170)
                    else:
                        def pp():
                            global b_code
                            b_code = qr()
                            if b_code != None:
                                print('shyam sheel')
                                label_2 = Label(ads, text="✓ Scanned Succesfully", width=20, font=("Arial", 10))
                                label_2.place(x=380, y=170)
                                global qr_code_scanned
                                qr_code_scanned = 1
                                print(qr_code_scanned)

                        Button(ads, text='Scan Qr Code', width=15, bg='brown', fg='white', command=pp).place(x=240,
                                                                                                             y=170)

                    label_3 = Label(ads, text="Duration(days)", width=20, font=("Arial", 10))
                    label_3.place(x=80, y=130)
                    x = 250
                    Branch = ['15', '30']
                    c = StringVar(ads)
                    droplist = OptionMenu(ads, c, *Branch)
                    droplist.config(width=20)
                    c.set('Select Duration')
                    droplist.place(x=240, y=130)

                    def submit():
                        if c.get() == 'Select Duration':
                            c.set('')
                        if aaa == False:
                            if entry_0.get() != '':
                                query = "select * from student where enrollment_no= \'" + str(entry_0.get()) + "\' "
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if len(details) > 0:
                                    if c.get() != '':
                                        if entry_2.get() != '':
                                            query = "select * from add_book where b_name= \'" + str(
                                                entry_2.get()) + "\'"
                                            cursor.execute(query)
                                            details = cursor.fetchall()
                                            if len(details) > 0:
                                                query = "select * from issue_book where enrollment_no= \'" + str(
                                                    entry_0.get()) + "\' and b_name= \'" + str(entry_2.get()) + "\' "
                                                cursor.execute(query)
                                                details = cursor.fetchall()
                                                if len(details) == 0:
                                                    query = "select no_of_books from add_book where b_name= \'" + str(
                                                        entry_2.get()) + "\' "
                                                    cursor.execute(query)
                                                    details = cursor.fetchall()
                                                    details = details[0]
                                                    details = int(details[0])
                                                    if details > 0:
                                                        if int(c.get()) == 15:
                                                            dddd = "" + str(day) + "-" + str(month) + "-" + str(year)
                                                            specified_date = datetime(int(year), int(month), int(day))
                                                            new_date = specified_date + timedelta(15)
                                                            y = new_date.year
                                                            m = new_date.month
                                                            d = new_date.day
                                                            new_date = str(d) + "-" + str(m) + "-" + str(y)
                                                        elif int(c.get()) == 30:
                                                            dddd = "" + str(day) + "-" + str(month) + "-" + str(year)
                                                            specified_date = datetime(int(year), int(month), int(day))
                                                            new_date = specified_date + timedelta(30)
                                                            y = new_date.year
                                                            m = new_date.month
                                                            d = new_date.day
                                                            new_date = str(d) + "-" + str(m) + "-" + str(y)
                                                        details -= 1
                                                        query = "update add_book set no_of_books=\'" + str(
                                                            details) + "\' where b_name= \'" + str(
                                                            entry_2.get()) + "\' "
                                                        cursor.execute(query)
                                                        connection.commit()
                                                        query = "select * from add_book where b_name= \'" + str(
                                                            entry_2.get()) + "\' "
                                                        cursor.execute(query)
                                                        book_details = cursor.fetchall()
                                                        book_details = book_details[0]
                                                        query = "select * from student where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        student_details = cursor.fetchall()
                                                        student_details = student_details[0]
                                                        query = "insert into issue_book values(\'" + str(
                                                            entry_0.get()) + "\',\'" + str(
                                                            student_details[1]) + "\',\'" + str(
                                                            student_details[2]) + "\',\'" + str(
                                                            book_details[0]) + "\',\'" + str(
                                                            book_details[1]) + "\',\'" + str(
                                                            book_details[4]) + "\',\'" + str(
                                                            book_details[3]) + "\',\'" + str(
                                                            book_details[2]) + "\',\'" + str(dddd) + "\',\'" + str(
                                                            new_date) + "\',\'" + str(0) + "\')"
                                                        cursor.execute(query)
                                                        connection.commit()
                                                        query = "select * from issue_book where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\' and b_name= \'" + str(
                                                            entry_2.get()) + "\' "
                                                        cursor.execute(query)
                                                        ddddddd = cursor.fetchall()
                                                        if len(ddddddd) > 0:
                                                            query = "select no_of_book_issued from student where enrollment_no=\'" + str(
                                                                entry_0.get()) + "\'"
                                                            cursor.execute(query)
                                                            nobisd = cursor.fetchall()
                                                            nobisd = nobisd[0]
                                                            nobisd = nobisd[0]
                                                            print(nobisd)
                                                            query = "select * from issue_book where enrollment_no=\'" + str(
                                                                entry_0.get()) + "\'"
                                                            cursor.execute(query)
                                                            lllll = cursor.fetchall()
                                                            lllll = str(int(len(lllll)) + int(nobisd))
                                                            print(lllll)
                                                            query = "update student set no_of_book_issued=\'" + str(
                                                                lllll) + "\' where enrollment_no=\'" + str(
                                                                entry_0.get()) + "\'"
                                                            cursor.execute(query)
                                                            connection.commit()
                                                            showinfo('Info', 'Book Issued Succesfully')
                                                            ads.destroy()
                                                        else:
                                                            showerror('Error',
                                                                      'Book\'s can\'t be issue just because \n of some problem')
                                                            ads.destroy()
                                                    else:
                                                        showwarning('Warning',
                                                                    'This is no more books are available with this name')
                                                else:
                                                    showwarning('Warning', 'This student already issued this book')
                                                    ads.destroy()
                                            else:
                                                showwarning('Warning', 'Please enter the valid book name')
                                                entry_2.delete(0, len(entry_2.get()))
                                        else:
                                            showwarning('Warning', 'Please enter the name of the book')
                                    else:
                                        showwarning('Warning', 'Please select the duration')
                                else:
                                    showwarning('Warning', 'Please enter valid Enrollment no')
                                    entry_0.delete(0, len(entry_0.get()))
                            else:
                                showwarning('Warning', 'Please enter the enrollment no first')
                        else:
                            if c.get() == 'Select Duration':
                                c.set('')
                            if entry_0.get() != '':
                                query = "select * from student where enrollment_no= \'" + str(entry_0.get()) + "\' "
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if len(details) > 0:
                                    if c.get() != '':
                                        if qr_code_scanned == 1:
                                            print('Qr code scanned :- ', qr_code_scanned)
                                            print(b_code)
                                            query = "select * from add_book where b_id= \'" + str(b_code) + "\' "
                                            cursor.execute(query)
                                            details = cursor.fetchall()
                                            if len(details) > 0:
                                                query = "select * from issue_book where enrollment_no= \'" + str(
                                                    entry_0.get()) + "\' and b_id= \'" + str(b_code) + "\' "
                                                cursor.execute(query)
                                                details = cursor.fetchall()
                                                if len(details) == 0:
                                                    query = "select no_of_books from add_book where b_id= \'" + str(
                                                        b_code) + "\' "
                                                    cursor.execute(query)
                                                    details = cursor.fetchall()
                                                    details = details[0]
                                                    details = int(details[0])
                                                    if details > 0:
                                                        if int(c.get()) == 15:
                                                            dddd = "" + str(day) + "-" + str(month) + "-" + str(year)
                                                            specified_date = datetime(int(year), int(month), int(day))
                                                            new_date = specified_date + timedelta(15)
                                                            y = new_date.year
                                                            m = new_date.month
                                                            d = new_date.day
                                                            new_date = str(d) + "-" + str(m) + "-" + str(y)
                                                        elif int(c.get()) == 30:
                                                            dddd = "" + str(day) + "-" + str(month) + "-" + str(year)
                                                            specified_date = datetime(int(year), int(month), int(day))
                                                            new_date = specified_date + timedelta(30)
                                                            y = new_date.year
                                                            m = new_date.month
                                                            d = new_date.day
                                                            new_date = str(d) + "-" + str(m) + "-" + str(y)
                                                        details -= 1
                                                        query = "update add_book set no_of_books=\'" + str(
                                                            details) + "\' where b_id= \'" + str(b_code) + "\' "
                                                        cursor.execute(query)
                                                        connection.commit()
                                                        query = "select * from add_book where b_id= \'" + str(
                                                            b_code) + "\' "
                                                        cursor.execute(query)
                                                        book_details = cursor.fetchall()
                                                        book_details = book_details[0]
                                                        query = "select * from student where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\'"
                                                        cursor.execute(query)
                                                        student_details = cursor.fetchall()
                                                        student_details = student_details[0]
                                                        query = "insert into issue_book values(\'" + str(
                                                            entry_0.get()) + "\',\'" + str(
                                                            student_details[1]) + "\',\'" + str(
                                                            student_details[2]) + "\',\'" + str(b_code) + "\',\'" + str(
                                                            book_details[1]) + "\',\'" + str(
                                                            book_details[4]) + "\',\'" + str(
                                                            book_details[3]) + "\',\'" + str(
                                                            book_details[2]) + "\',\'" + str(dddd) + "\',\'" + str(
                                                            new_date) + "\',\'" + str(0) + "\')"
                                                        cursor.execute(query)
                                                        connection.commit()
                                                        query = "select * from issue_book where enrollment_no=\'" + str(
                                                            entry_0.get()) + "\' and b_id=\'" + str(b_code) + "\'"
                                                        cursor.execute(query)
                                                        ddddddd = cursor.fetchall()
                                                        if len(ddddddd) > 0:
                                                            query = "select no_of_book_issued from student where enrollment_no=\'" + str(
                                                                entry_0.get()) + "\'"
                                                            cursor.execute(query)
                                                            nobisd = cursor.fetchall()
                                                            nobisd = nobisd[0]
                                                            nobisd = nobisd[0]
                                                            print(nobisd)
                                                            query = "select * from issue_book where enrollment_no=\'" + str(
                                                                entry_0.get()) + "\'"
                                                            cursor.execute(query)
                                                            lllll = cursor.fetchall()
                                                            lllll = str(int(len(lllll)) + int(nobisd))
                                                            print(lllll)
                                                            query = "update student set no_of_book_issued=\'" + str(
                                                                lllll) + "\' where enrollment_no=\'" + str(
                                                                entry_0.get()) + "\'"
                                                            cursor.execute(query)
                                                            connection.commit()
                                                            showinfo('Info', 'Book Issued Succesfully')
                                                            ads.destroy()
                                                        else:
                                                            showerror('Error',
                                                                      'Book\'s can\'t be issue just because \n of some problem')
                                                    else:
                                                        showwarning('Warning', 'This Book is now not in library')
                                                        ads.destroy()
                                                else:
                                                    showwarning('Warning', 'This Student is already issued this book')
                                                    ads.destroy()
                                            else:
                                                showwarning('Warning',
                                                            'This Book is not in library\n please scan the valid qr code')
                                        else:
                                            print('Qr code scanned :- ', qr_code_scanned)
                                            showwarning('Warning', 'Please Scan qr code first')
                                    else:
                                        showwarning('Warning', 'Please select the duration')
                                else:
                                    showwarning('Warning', 'Please enter valid Enrollment no')
                                    entry_0.delete(0, len(entry_0.get()))
                            else:
                                showwarning('Warning', 'Please enter the enrollment no first')

                    Button(ads, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=280, y=230)
                    ads.mainloop()
                else:
                    showwarning('Error','Please Add At Least one book in library')



            def create_admin():
                ads = Tk()
                ads.resizable(False, False)
                label_1 = Label(ads, text="Create Admin", width=20, font=("bold", 20))
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

                def submit():
                    if entry_0.get()!='':
                        query = "select username from admin where username=\'"+str(entry_0.get())+"\'"
                        cursor.execute(query)
                        details = cursor.fetchall()
                        if len(details)==0:
                            if entry_1.get()!='':
                                if entry_2.get()!='':
                                    if entry_1.get()==entry_2.get():
                                        query = "insert into admin values(\'"+str(entry_0.get())+"\',\'"+str(entry_1.get())+"\')"
                                        cursor.execute(query)
                                        connection.commit()
                                        query = "select * from admin where username=\'"+str(entry_0.get())+"\' and password=\'"+str(entry_1.get())+"\'"
                                        cursor.execute(query)
                                        details = cursor.fetchall()
                                        if len(details)>0:
                                            showinfo('Congratulation\'s','User Added')
                                            ads.destroy()
                                        else:
                                            showerror('Error','User does\'t added')
                                            ads.destroy()
                                    else:
                                        showerror('Error','Password does\'t matched')
                                        entry_1.delete(0,len(entry_1.get()))
                                        entry_2.delete(0,len(entry_2.get()))
                                else:
                                    showwarning('Missing','Please enter the password again')
                            else:
                                showwarning('Warning','Please enter the password')
                        else:
                            showwarning('Not Valid','Please use another username \n because this is already in use')
                            entry_0.delete(0,len(entry_0.get()))
                    else:
                        showwarning('Missing','Please enter the username')


                Button(ads, text='Submit', width=15, bg='brown', fg='white', command=submit).place(x=280, y=210)
                ads.mainloop()




            def see_all_details_having_fine():
                student_having_fine()



            # Return Book
            def return_book():
                ads = Tk()
                ads.resizable(False, False)

                label_1 = Label(ads, text="Return Book", width=20, font=("bold", 20))
                label_1.place(x=120, y=5)
                ads.geometry('600x400')

                label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                label_0.place(x=80, y=90)
                entry_0 = Entry(ads, font=('Arial'))
                entry_0.place(x=240, y=90)

                label_2 = Label(ads, text="Name Of Book", width=20, font=("Arial", 10))
                label_2.place(x=80, y=130)
                entry_2 = Entry(ads, font=('Arial'))
                entry_2.place(x=240, y=130)

                global count
                count = 0

                def fine_submit():
                    query = "delete from issue_book where enrollment_no=\'" + str(
                        entry_0.get()) + "\' and b_name=\'" + str(
                        entry_2.get()) + "\'"
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

                    query = "select no_of_books from add_book where b_name=\'" + str(
                        entry_2.get()) + "\'"
                    cursor.execute(query)
                    fffff = cursor.fetchall()
                    fffff = fffff[0]
                    fffff = int(fffff[0]) + 1
                    query = "update add_book set no_of_books=\'" + str(
                        fffff) + "\' where b_name=\'" + str(entry_2.get()) + "\'"
                    cursor.execute(query)
                    connection.commit()
                    query = "select * from issue_book where enrollment_no=\'" + str(
                        entry_0.get()) + "\' and b_name=\'" + str(
                        entry_2.get()) + "\'"
                    cursor.execute(query)
                    aa = cursor.fetchall()

                    query = "select no_of_books from add_book where b_name=\'" + str(
                        entry_2.get()) + "\'"
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
                        showinfo('Info', 'Book Removed Sucessfully')
                        ads.destroy()
                    else:
                        showerror('Error', 'Book Can\'t be returned')
                        ads.destroy()


                def cheack_for_fine():
                    if entry_0.get() != '':
                        query = "select * from student where enrollment_no=\'" + str(entry_0.get()) + "\'"
                        cursor.execute(query)
                        details = cursor.fetchall()
                        if len(details) > 0:
                            if entry_2.get()!='':
                                query = "select * from issue_book where enrollment_no=\'" + str(
                                    entry_0.get()) + "\'"
                                cursor.execute(query)
                                details = cursor.fetchall()
                                if len(details):
                                    query = "select * from add_book where b_name=\'" + str(entry_2.get()) + "\'"
                                    cursor.execute(query)
                                    details = cursor.fetchall()
                                    if len(details):
                                        query = "select * from issue_book where enrollment_no=\'" + str(
                                            entry_0.get()) + "\' and b_name=\'" + str(entry_2.get()) + "\'"
                                        cursor.execute(query)
                                        details = cursor.fetchall()
                                        if len(details) > 0:
                                            query = "select fine_amount from issue_book where enrollment_no=\'" + str(
                                                entry_0.get()) + "\' and b_name=\'" + str(entry_2.get()) + "\'"
                                            cursor.execute(query)
                                            details = cursor.fetchall()
                                            print(details)
                                            details = details[0]
                                            print(details)
                                            details = int(details[0])
                                            print(details)
                                            if details > 0:
                                                label_3 = Label(ads, text="Fine Amount", width=20, font=("Arial", 10))
                                                label_3.place(x=80, y=170)
                                                Branch = ['' + str(details) + '']
                                                c = StringVar(ads)
                                                droplist = OptionMenu(ads, c, *Branch)
                                                droplist.config(width=20)
                                                c.set('select fine amount')
                                                droplist.place(x=240, y=170)

                                                def kkkkk():
                                                    if c.get() == 'select fine amount':
                                                        c.set('')
                                                    if c.get() != '':
                                                        fine_submit()
                                                    else:
                                                        showwarning('Warning', 'Please select the fine first')

                                                Button(ads, text='Submit', width=15, bg='brown', fg='white',
                                                       command=kkkkk).place(
                                                    x=280, y=230)
                                            else:
                                                label_6 = Label(ads, text="✓ No Fine Due", width=20, font=("Arial", 15))
                                                label_6.place(x=200, y=170)
                                                Button(ads, text='Submit', width=15, bg='brown', fg='white',
                                                       command=fine_submit).place(
                                                    x=280, y=230)
                                        else:
                                            showwarning('Not Issued', 'This student did\'t issued this book')
                                            entry_2.delete(0, len(entry_2.get()))
                                    else:
                                        showerror('Error',
                                                  'This Book is not in libraray \n Please Enter the valid book detail\'s')
                                        entry_2.delete(0, len(entry_2.get()))
                                else:
                                    showinfo('Not Issued', 'This student did\'t issued any Book')
                                    ads.destroy()
                            else:
                                showwarning('Missing','Please Enter The Name Of Book')
                        else:
                            showerror('Error', 'This enrollment is not valid')
                            entry_0.delete(0, len(entry_0.get()))
                    else:
                        showwarning('Missing', 'Please Enter The Enrollment No')



                Button(ads, text='Cheack For Fine', width=15, bg='brown', fg='white', command=cheack_for_fine).place(x=280, y=230)
                ads.mainloop()
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

                label_1 = Label(ads, text="Return Book", width=20, font=("bold", 20))
                label_1.place(x=7, y=5)
                ads.geometry('250x100')

                label_0 = Label(ads, text="Enrollment No", width=20, font=("Arial", 10))
                label_0.place(x=80, y=90)
                entry_0 = Entry(ads, font=('Arial'))
                entry_0.place(x=240, y=90)

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








            ad = Tk()
            label_1 = Label(ad, text="Admin", width=20, font=("bold", 20))
            label_1.place(x=90, y=5)
            ad.title(string='Admin')
            label_11 = Label(ad, text=dddd, width=0, font=("bold", 11))
            label_11.place(x=0, y=0)
            # Completed
            Button(ad, text='Add Book', width=8, height=2, bg='brown', fg='white',command=kkkk).place(x=10, y=50)
            # Completed
            Button(ad, text='Add Student', width=10, height=2, bg='brown', fg='white',command=add_student).place(x=90, y=50)
            # Completed
            Button(ad, text='Call Administrator', width=18, height=2, bg='brown', fg='white',command=calling).place(x=180, y=50)
            # Completed
            Button(ad, text='Know Student Detail\'s', width=22, height=2, bg='brown', fg='white',command=student_id_password).place(x=330, y=50)
            # Completed
            Button(ad, text='Remove \nBook', width=8, height=2, bg='brown', fg='white',command=remove_book).place(x=10, y=100)
            # Completed
            Button(ad, text='Issue Book', width=10, height=2, bg='brown', fg='white',command=issue_book).place(x=90, y=100)
            # Not Completed
            Button(ad, text='Return Book', width=18, height=2, bg='brown', fg='white',command=lllllll ).place(x=180, y=100)
            # Completed
            Button(ad, text='No of books \n that are not in library', width=22, height=2, bg='brown', fg='white',command=no_of_book_not_in_library).place(x=330, y=100)
            # Completed
            Button(ad, text='Forgot \n QR Code', width=8, height=2, bg='brown', fg='white', command=get_qr_code).place(x=10, y=150)
            # Completed
            Button(ad, text='Know Book Detail\'s', width=22, height=2, bg='brown', fg='white',
                   command=know_book_details).place(x=330, y=150)
            if username=='admin' and password=='admin':
                Button(ad, text='Create Admin', width=10, height=2, bg='brown', fg='white', command=create_admin).place(
                    x=90, y=150)
            Button(ad, text='Student\'s Haing Fine', width=18, height=2, bg='brown', fg='white',command=see_all_details_having_fine ).place(x=180, y=150)
            ad.geometry('500x300')
            ad.resizable(False, False)
            ad.mainloop()
    except Error as e:
        print('This is not opeating', e)
if __name__ == '__main__':
    showinfo('Info', 'Please Login first using \'Log_in.py\' file')
    exit(0)
