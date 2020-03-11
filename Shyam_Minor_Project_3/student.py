from datetime import date ,time,timedelta,datetime
from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from mysql.connector import Error
from pyzbar.pyzbar import decode
import cv2
import numpy as np
from twilio.rest import Client
from no_of_book_issued_student import no_of_book_issued_student
from get_bok_details import get_book_detailss
from books_having_fine import books_fine
from search_using_qr_code import search_book_qr_code
from student_get_all_fine_history import get_all_fine_historyy
from tkinter.filedialog import askopenfile
import shutil
import os
from webbrowser import open_new
from Date_Validate import validate
import datetime
import calendar



def student(username,password):
    count = 0
    tdate = date.today()
    day = tdate.day
    month = tdate.month
    year = tdate.year
    print(day, ' ', month, " ", year)
    dddd = "" + str(day) + "-" + str(month) + "-" + str(year) + ""
    connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
    cursor = connection.cursor()
    query = "select * from issue_book where enrollment_no=\'"+username+"\' and fine_amount>0"
    cursor.execute(query)
    details = cursor.fetchall()

    kkkkkkkkkk = "" + str(day) + " " + str(month) + " " + str(year) + ""

    def findDay(date):
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])

    mmmmmmmmm = {1: ' Jan', 2: ' Feb', 3: ' Mar', 4: ' Apr', 5: ' May', 6: ' June', 7: ' July', 8: ' Aug', 9: ' Sep',
                 10: ' Oct', 11: ' Nov', 12: ' Dec'}
    dddddddddd = str(findDay(kkkkkkkkkk)) + " , " + str(day) + mmmmmmmmm[
        int(month)]  # "-" + str(month) + "-" + str(year) + ""



    if len(details)>0:
        aaa = showwarning('Fine','You Are Having Fine in some books \n please see the list')
        barcode_scaned = 0

    try:
        connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
        if connection.is_connected():
            cursor = connection.cursor()

            # Complete
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
                    if entry_1.get() == '' and entry_2.get() == '':
                        print(showerror('ShowError', 'Please Enter the password in both the boxes'))
                        lll = len(entry_2.get())
                        entry_2.delete(0, lll)
                        lll = len(entry_1.get())
                        entry_1.delete(0, lll)
                    elif entry_1.get() == '' and entry_2.get() != '':
                        print(showerror('ShowError', 'Please Enter the password in both the boxes'))
                        lll = len(entry_2.get())
                        entry_2.delete(0, lll)
                        lll = len(entry_1.get())
                        entry_1.delete(0, lll)
                    elif entry_1.get() != '' and entry_2.get() == '':
                        print(showerror('ShowError', 'Please Enter the password in both the boxes'))
                        lll = len(entry_2.get())
                        entry_2.delete(0, lll)
                        lll = len(entry_1.get())
                        entry_1.delete(0, lll)
                    elif entry_1.get() != entry_2.get():
                        print(showerror('ShowError', 'Password Did\'t match'))
                        lll = len(entry_2.get())
                        entry_2.delete(0, lll)
                        lll = len(entry_1.get())
                        entry_1.delete(0, lll)
                    elif entry_1.get() == entry_2.get():
                        try:
                            cursor = connection.cursor()
                            query = "select password from student where enrollment_no=\'" + username + "\'"
                            cursor.execute(query)
                            passs = cursor.fetchall()
                            passs = passs[0]
                            mmmmmm = passs[0]
                            cursor = connection.cursor()
                            if str(mmmmmm) != str(entry_2.get()):
                                query = "update student set password=\'" + str(
                                    entry_2.get()) + "\' where enrollment_no=\'" + str(username) + "\'"
                                cursor.execute(query)
                                connection.commit()

                                cursor = connection.cursor()
                                query = "select password from student where enrollment_no=\'" + username + "\'"
                                cursor.execute(query)
                                passs = cursor.fetchall()
                                for x in passs:
                                    if x[0] == entry_1.get():
                                        ap = showinfo('Congratulation', 'Password Changed Successfully')
                                        if ap == 'ok':
                                            cpa.destroy()
                                            break
                            else:
                                showerror('Error', 'Password can\'t be same ad previous one ')
                                entry_1.delete(0, len(entry_1.get()))
                                entry_2.delete(0, len(entry_2.get()))
                        except:
                            print(showerror('ShowError', 'Something Goes Wrong'))

                Button(cpa, text='Change Password', width=15, bg='brown', fg='white',
                       command=Check_pass_match).place(
                    x=260, y=220)
                cpa.mainloop()

            def book_issued():
                no_of_book_issued_student(username)

            def calling():
                try:
                    account_sid = "ACe36c77e6302d6870ebd91d83fbb2b28a"
                    auth_token = "abe3760c7c33f11c29779409afdcc1a9"
                    client = Client(account_sid, auth_token)
                    aaa = askyesno("askyesno", "Do You Want to Call or Not")
                    if aaa == True:
                        call = client.calls.create(to="+918223859046", from_="+12015617688",
                                                   url="http://demo.twilio.com/docs/voice.xml")
                        if call.sid != None:
                            print(showinfo('Call Connected', 'Call Has Been Sent to the Registered Mobile Number'))
                        else:
                            print(showerror('ShowError', 'There is some issue while calling'))
                    elif aaa == 'False':
                        print(showerror('ShowError', 'Call is cancled'))
                except:
                    showerror('Error', 'Make sure your pc connected with internet')

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

                    Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=gett).place(x=260,
                                                                                                     y=170)
                    kkk.mainloop()
                else:
                    get_book_detailss('False')

            def get_book_having_fine():
                books_fine(username)

            def Scan_QR_CODE():
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
                all_book_details = Scan_QR_CODE()
                query = "select * from add_book where b_id=\'" + str(all_book_details) + "\'"
                cursor.execute(query)
                details = cursor.fetchall()
                if len(details) > 0:
                    search_book_qr_code(all_book_details)
                else:
                    showerror('Error', 'This Book is not in library')




            def get_all_fine_history():
                get_all_fine_historyy(username)



            def edit_profile():
                found = 0
                content = None
                filee = 'Images/'
                jjjjjjjjj = os.listdir('Images/')
                u_length  = len(username)
                for x in jjjjjjjjj:
                    if x[:u_length]==str(username):
                        found=1
                        filee += str(x)
                adb = Tk()
                label_1 = Label(adb, text="Edit Profile", width=20, font=("bold", 20))
                label_1.place(x=200, y=5)
                adb.geometry('700x500')

                query = "select * from student where enrollment_no=\'"+str(username)+"\'"
                cursor.execute(query)
                all_details = cursor.fetchall()
                all_details = all_details[0]

                label_1 = Label(adb, text="Name", width=20, font=("Arial", 10))
                label_1.place(x=200, y=130)
                entry_1 = Entry(adb, font=('Arial'))
                entry_1.place(x=360, y=130)
                entry_1.insert(0,all_details[1])


                label_2 = Label(adb, text="Enrollment No", width=20, font=("Arial", 10))
                label_2.place(x=200, y=170)
                entry_2 = Entry(adb, font=('Arial'),cursor='no')
                entry_2.place(x=360, y=170)
                entry_2.insert(0, all_details[0])
                entry_2.config(state=DISABLED)


                label_3 = Label(adb, text="Branch", width=20, font=("Arial", 10))
                label_3.place(x=200, y=210)
                entry_3 = Entry(adb, font=('Arial'),cursor='no')
                entry_3.place(x=360, y=210)
                entry_3.insert(0, all_details[2])
                entry_3.config(state=DISABLED)


                label_4 = Label(adb, text="Semester", width=20, font=("Arial", 10))
                label_4.place(x=200, y=250)
                entry_4 = Entry(adb, font=('Arial'),cursor='no')
                entry_4.place(x=360, y=250)
                entry_4.insert(0, all_details[3])
                entry_4.config(state=DISABLED)


                label_5 = Label(adb, text="Age", width=20, font=("Arial", 10))
                label_5.place(x=200, y=410)
                entry_5 = Entry(adb, font=('Arial'),cursor='no')
                entry_5.place(x=360, y=410)
                entry_5.insert(0, all_details[4])
                entry_5.config(state=DISABLED)


                label_6 = Label(adb, text="Address", width=20, font=("Arial", 10))
                label_6.place(x=200, y=290)
                entry_6 = Entry(adb, font=('Arial'))
                entry_6.place(x=360, y=290)
                entry_6.insert(0, all_details[5])

                label_7 = Label(adb, text="Mobile No", width=20, font=("Arial", 10))
                label_7.place(x=200, y=330)
                entry_7 = Entry(adb, font=('Arial'))
                entry_7.place(x=360, y=330)
                entry_7.insert(0, all_details[8])

                label_8 = Label(adb, text="DOB", width=20, font=("Arial", 10))
                label_8.place(x=200, y=370)
                entry_8 = Entry(adb, font=('Arial'))
                entry_8.place(x=360, y=370)
                entry_8.insert(0, all_details[9])



                def lllllllllllllll():
                    try:
                        global filee
                        file = askopenfile(mode='r', filetypes=[('Images Files', '*.img'), ('Images Files', '*.png'),
                                                                ('Images Files', '*.jpg'), ('Images Files', '*.jpeg'), ('Images Files', '*.psd')])
                        if file!=None:
                            global filee
                            hhhhhhhhh = file.name.index('.')
                            extension = file.name[hhhhhhhhh:]
                            fileee = open('Images/' + str(username) + '.png', 'w+') #str(extension)
                            shutil.copy(file.name, fileee.name)
                            filee = fileee.name
                            showinfo('Info', 'Image Uploaded Successfully')
                        else:
                            showinfo('Information','Please select an image')
                    except:
                        showerror('Error','Becaues of some issue image can\'t be uploaded')




                if found==0:
                    filee = 'Images/'+'default.png'
                filee = os.getcwd()+'/'+filee
                print(filee)
                def nnnnnnnnnn():
                    foundd = 0
                    k = os.getcwd()+'/Images/'
                    jjjjjjjjj = os.listdir('Images/')
                    u_length = len(username)
                    for x in jjjjjjjjj:
                        if x[:u_length] == str(username):
                            foundd = 1
                            k += str(x)
                            break
                    print('This file is opening',k)
                    if foundd==1:
                        open_new(k)
                    elif foundd==0:
                        k = os.getcwd()+'/Images/'+'default.png'
                        open_new(k)
                Button(adb, text='See Image', width=15, bg='brown', fg='white', cursor='hand2',
                       command=lambda :nnnnnnnnnn()).place(x=50, y=100)


                def submittttt():
                    if entry_1.get!='':
                        if entry_6.get()!='':
                            if entry_8.get()!='':
                                try:
                                    mmmm = entry_8.get()
                                    mmmm = mmmm[3:5]
                                    yyyy = entry_8.get()
                                    yyyy = yyyy[0:2]
                                    dob = entry_8.get()
                                    dob = dob[6:10]
                                    age = str(int(year) - int(dob))
                                    date_string = "" + dob + "-" + mmmm + "-" + yyyy + ""
                                    date_format = '%Y-%m-%d'
                                    cheack_validate = validate(date_string, date_format)
                                except:
                                    showwarning('Warning', 'Please enter the valid DOB')
                                    entry_8.delete(0, len(entry_8.get()))
                                    return ''
                                if cheack_validate == True:
                                    if int(age) > 13:
                                        if entry_7.get()!='':
                                            try:
                                                int(entry_7.get())
                                                print('mobile sahi h')
                                                if len(entry_7.get())==10:

                                                    def ddddddddd(pppppp):
                                                        llll = pppppp
                                                        c = llll[len(llll) - 4:]
                                                        a = ''
                                                        b = ''
                                                        for xx in llll[0:2]:
                                                            if xx == '1' or xx == '2' or xx == '3' or xx == '4' or xx == '5' or xx == '6' or xx == '7' or xx == '8' or xx == '9' or xx == '0':
                                                                a = a + xx
                                                        for yy in llll[len(llll) - 7:len(llll) - 4]:
                                                            if yy == '1' or yy == '2' or yy == '3' or yy == '4' or yy == '5' or yy == '6' or yy == '7' or yy == '8' or yy == '9' or yy == '0':
                                                                b = b + yy
                                                        f_date = date(int(year), int(month), int(day))
                                                        l_date = date(int(c), int(b), int(a))
                                                        delta = l_date - f_date
                                                        new_year = (delta.days + delta.seconds / 86400) / 365.2425
                                                        best_age = int(abs(new_year))
                                                        return best_age

                                                    age = ddddddddd(str(entry_8.get()))
                                                    label_00 = Label(adb, text="Age", width=20, font=("Arial", 10))
                                                    label_00.place(x=200, y=410)
                                                    entry_00 = Entry(adb, font=('Arial'), cursor='no')
                                                    entry_00.place(x=360, y=410)
                                                    entry_00.insert(0, str(age))
                                                    entry_00.config(state=DISABLED)




                                                    print('Kam h')
                                                    query = "update student set name=\'"+str(entry_1.get())+"\', address=\'"+str(entry_6.get())+"\', mobile_no=\'"+str(entry_7.get())+"\', DOB=\'"+str(entry_8.get())+"\',age=\'"+str(age)+"\' where enrollment_no=\'"+str(username)+"\'"
                                                    cursor.execute(query)
                                                    connection.commit()
                                                    print('data ja chuka h')
                                                    query = "select * from student where enrollment_no=\'"+str(username)+"\'"
                                                    cursor.execute(query)
                                                    lllllllllllllllllllllll = cursor.fetchall()
                                                    lllllllllllllllllllllll = lllllllllllllllllllllll[0]
                                                    if lllllllllllllllllllllll[1]==str(entry_1.get()) and lllllllllllllllllllllll[5]==str(entry_6.get()) and lllllllllllllllllllllll[8]==str(entry_7.get()) and lllllllllllllllllllllll[9]==str(entry_8.get()):
                                                        showinfo('Information','Data Updated Successfully')
                                                    else:
                                                        showwarning('Warning','Data Can\'t be update')
                                                else:
                                                    showwarning('Warning','Mobile no Must be 10 digit')
                                            except:
                                                showwarning('Warning','Mobile No Can\'t be character')
                                                entry_7.delete(0,len(entry_7.get()))
                                                return ''
                                        else:
                                            showwarning('Warning','Mobile No Can\'t be empty')
                                    else:
                                        showwarning('Warning', 'Age Must Be Grater Then 13 at least')
                            else:
                                showwarning('Enter Date','Please enter the date')
                        else:
                            showwarning('Warning','Address Can\' be empty')
                    else:
                        showwarning('Warning','Name Can\'be empty')


                Button(adb, text='Upload Image', width=15, bg='brown', fg='white',cursor='hand2',command=lambda:lllllllllllllll()).place(x=50, y=170)
                Button(adb, text='Save', width=15, bg='brown', fg='white',cursor='hand2',command=submittttt).place(x=370, y=450)
                adb.resizable(False, False)
                adb.mainloop()




            # def student_id_password():
            #     aaa = askyesno("askyesno", "Do You Want Search for particular user yes/no")
            #     if aaa == True:
            #         kkk = Tk()
            #         label_1 = Label(kkk, text="Know Student Details", width=20, font=("bold", 20))
            #         label_1.place(x=90, y=5)
            #         kkk.geometry('500x200')
            #         label_1 = Label(kkk, text="Enter Name of Student", width=20, font=("Arial", 10))
            #         label_1.place(x=80, y=130)
            #         entry_1 = Entry(kkk, font=('Arial'))
            #         entry_1.place(x=240, y=130)
            #         def gett():
            #             if entry_1.get() != '':
            #                 ah = entry_1.get()
            #                 query = "select * from student where name like \'%" + str(ah) + "%\'"
            #                 cursor.execute(query)
            #                 kh = cursor.fetchall()
            #                 if len(kh) > 0:
            #                     know_student_id_password(entry_1.get())
            #                     kkk.destroy()
            #                 else:
            #                     print(showerror('ShowError', 'There is no student with this name'))
            #             else:
            #                 print(showwarning('ShowError', 'Please Enter Name'))
            #         Button(kkk, text='Submit', width=15, bg='brown', fg='white', command=gett).place(x=260, y=170)
            #         kkk.mainloop()
            #     else:
            #         know_student_id_password('False')














            ad = Tk()
            query = "select name from student where enrollment_no=\'" + str(username) + "\'"
            cursor.execute(query)
            dddd = cursor.fetchall()
            print(dddd)
            dddd = dddd[0]
            dddd = dddd[0]
            dddd = str(dddd)
            dddd = dddd.split()
            label_1 = Label(ad, text="Welcome " + str(dddd[0]), width=20, bg='#8FBC8F',fg='black', font=("Algerian", 20))
            label_1.place(x=90, y=35)
            label_5 = Label(ad, text="Student Profile", width=20, font=("bold", 9), bg='#8FBC8F',fg='black')
            label_5.place(x=380, y=280)
            label_11 = Label(ad, text=dddddddddd, width=0, font=("bold", 11), bg='#8FBC8F',fg='black')
            label_11.place(x=390, y=0)
            Button(ad, text='Search Books', width=10, height=2, bg='#BDB76B', fg='black',command=know_book_details).place(x=10, y=80)
            Button(ad, text='Scan QR Code \n to see book detail\'s', width=16, height=2, bg='#BDB76B', fg='black', command=Scan_QR_CODE_book_details).place(x=100, y=80)
            Button(ad, text='Call HOD', width=12, height=2, bg='#BDB76B', fg='black', command=calling).place(
                x=230, y=80)
            Button(ad, text='Change Password', width=22, height=2,bg='#BDB76B', fg='black',
                   command=change_password).place(x=330, y=80)
            Button(ad, text='Book Issued', width=10, height=2, bg='#BDB76B', fg='black',
                   command=book_issued).place(x=10, y=130)
            Button(ad, text='Book\'s Having \n Fine', width=16, height=2, bg='#BDB76B', fg='black',
                   command=get_book_having_fine).place(
                x=100, y=130)
            Button(ad, text='Fine History', width=12, height=2, bg='#BDB76B', fg='black', command=get_all_fine_history).place(
                x=230, y=130)
            Button(ad, text='Edit Profile', width=22, height=2, bg='#BDB76B', fg='black',
                   command=edit_profile).place(x=330, y=130)




            ad.geometry('500x300')
            ad.resizable(False, False)
            ad.title('Student')
            ad.configure(bg='#8FBC8F')
            ad.mainloop()
    except Error as e:
        print('This is not opeating', e)


if __name__=='__main__':
    showwarning('Info','Please Login first using \'Log_in.py\' file')
    exit(0)





