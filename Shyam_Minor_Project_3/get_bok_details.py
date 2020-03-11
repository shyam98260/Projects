from tkinter import *
from tkinter.messagebox import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
import mysql.connector
from mysql.connector import Error


def get_book_detailss(p):
    connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
    if connection.is_connected():
        cursor = connection.cursor()
        if str(p)=='False':
            query = "select * from add_book  order by b_name asc"
        else:
            query = "select * from add_book where b_name like \'%" + str(p) + "%\' order by b_name asc"
        cursor.execute(query)
        all_admin_username_pas = cursor.fetchall()
        if len(all_admin_username_pas)>0:
            # print(all_admin_username_pas)
            rl = len(all_admin_username_pas)
            cl = len(all_admin_username_pas[0])

            class Window(QWidget):
                def __init__(self):
                    super().__init__()
                    self.title = "PyQt5 Tables"
                    self.top = 100
                    self.left = 100
                    self.width = 1200
                    self.height = 400
                    self.InitWindow()

                def InitWindow(self):
                    self.setWindowIcon(QtGui.QIcon("icon.png"))
                    self.setWindowTitle(self.title)
                    self.setGeometry(self.top, self.left, self.width, self.height)
                    self.creatingTables()
                    self.show()

                def creatingTables(self):
                    self.tableWidget = QTableWidget()
                    self.tableWidget.setRowCount(rl + 1)
                    self.tableWidget.setColumnCount(cl+2)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setItem(0, 0, QTableWidgetItem("Book Id"))
                    self.tableWidget.setItem(0, 1, QTableWidgetItem("Book Name"))
                    self.tableWidget.setItem(0, 2, QTableWidgetItem("Book Author"))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem("Book Publication"))
                    self.tableWidget.setItem(0, 4, QTableWidgetItem("Book Edition"))
                    self.tableWidget.setItem(0, 5, QTableWidgetItem("Total No Of Books"))
                    self.tableWidget.setItem(0, 6, QTableWidgetItem("Issued"))
                    self.tableWidget.setItem(0, 7, QTableWidgetItem("Availablity"))



                    i, j = 0, 0
                    for x in all_admin_username_pas:
                        i = i + 1
                        j = 0
                        # print(x)
                        for y in range(len(x)+2):
                            if j<=5:
                                self.tableWidget.setItem(i, j, QTableWidgetItem(x[j]))
                            if j==6:
                                query = "select * from issue_book where b_id=\'"+str(x[0])+"\'"
                                cursor.execute(query)
                                mahendra = cursor.fetchall()
                                if len(mahendra)<=0:
                                    # print('shyam sheel')
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(0)))
                                else:
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(len(mahendra))))
                            if j==7:
                                query = "select * from issue_book where b_id=\'" + str(x[0]) + "\'"
                                cursor.execute(query)
                                mahendra = cursor.fetchall()
                                if len(mahendra)<=0:
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(int(x[5]))))
                                else:
                                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(int(x[5])-len(mahendra))))
                            j = j + 1
                    self.vBoxLayout = QVBoxLayout()
                    self.vBoxLayout.addWidget(self.tableWidget)
                    self.setLayout(self.vBoxLayout)

            App = QApplication(sys.argv)
            window = Window()
            App.exec()
        else:
            print(showerror('Not in library','There is no any book \n that are not in library'))
if __name__=="__main__":
    print(showerror('ShowError', 'Please Run the Login.py First to access all the services'))
    exit(0)