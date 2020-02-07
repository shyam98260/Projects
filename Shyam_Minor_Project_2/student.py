from tkinter import *
from tkinter.messagebox import *
import mysql.connector
from mysql.connector import Error
from pyzbar.pyzbar import decode
import cv2
import numpy as np
from playsound import playsound
from twilio.rest import Client
from no_of_book_issued_student import no_of_book_issued_student
from get_bok_details import get_book_detailss
from books_having_fine import books_fine
from search_using_qr_code import search_book_qr_code


def student(username,password):
    connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
    cursor = connection.cursor()
    query = "select * from issue_book where enrollment_no=\'"+username+"\' and fine_amount>0"
    cursor.execute(query)
    details = cursor.fetchall()

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
                            print(showerror('ShowError', 'Call Has Been Sent to the Provided Mobile Number'))
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



            ad = Tk()
            query = "select name from student where enrollment_no=\'" + str(username) + "\'"
            cursor.execute(query)
            dddd = cursor.fetchall()
            print(dddd)
            dddd = dddd[0]
            dddd = dddd[0]
            label_1 = Label(ad, text="Welcome " + str(dddd), width=20, font=("bold", 20))
            label_1.place(x=90, y=5)
            label_5 = Label(ad, text="Student Profile", width=20, font=("bold", 9))
            label_5.place(x=380, y=280)
            Button(ad, text='Search Books', width=10, height=2, bg='brown', fg='white',
                   command=know_book_details).place(x=10, y=50)
            Button(ad, text='Scan QR Code \n to see book detail\'s', width=13, height=2, bg='brown',
                   fg='white', command=Scan_QR_CODE_book_details).place(x=100, y=50)
            Button(ad, text='Call HOD', width=10, height=2, bg='brown', fg='white', command=calling).place(
                x=230, y=50)
            Button(ad, text='Change Password', width=22, height=2, bg='brown', fg='white',
                   command=change_password).place(x=330, y=50)
            Button(ad, text='Book Issued', width=10, height=2, bg='brown', fg='white',
                   command=book_issued).place(x=10, y=100)
            Button(ad, text='Book\'s Having \n Fine', width=13, height=2, bg='brown', fg='white',
                   command=get_book_having_fine).place(
                x=100, y=100)
            ad.geometry('500x300')
            ad.resizable(False, False)
            ad.mainloop()
    except Error as e:
        print('This is not opeating', e)


if __name__=='__main__':
    showinfo('Info','Please Login first using \'Log_in.py\' file')
    exit(0)





