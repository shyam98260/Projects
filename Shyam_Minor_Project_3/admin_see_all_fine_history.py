from tkinter import *
from tkinter.messagebox import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
import mysql.connector
from mysql.connector import Error


def admin_fine_history(username):
    connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
    if connection.is_connected():
        cursor = connection.cursor()
        if username=='False':
            query = "select * from fine_history order by b_name asc"
        else:
            query = " select * from fine_history where name like \'%" + str(username) + "%\' order by b_name asc"
        cursor.execute(query)
        all_admin_username_pas = cursor.fetchall()
        if len(all_admin_username_pas)>0:
            print(all_admin_username_pas)
            rl = len(all_admin_username_pas)
            cl = len(all_admin_username_pas[0])

            class Window(QWidget):
                def __init__(self):
                    super().__init__()
                    self.title = "PyQt5 Tables"
                    self.top = 100
                    self.left = 100
                    self.width = 1300
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
                    self.tableWidget.setColumnCount(cl)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setItem(0, 0, QTableWidgetItem("Enrollment No"))
                    self.tableWidget.setItem(0, 1, QTableWidgetItem("Name"))
                    self.tableWidget.setItem(0, 2, QTableWidgetItem("Branch"))
                    self.tableWidget.setItem(0, 3, QTableWidgetItem("Semester"))
                    self.tableWidget.setItem(0, 4, QTableWidgetItem("Book Id"))
                    self.tableWidget.setItem(0, 5, QTableWidgetItem("Book Name"))
                    self.tableWidget.setItem(0, 6, QTableWidgetItem("Book Edition"))
                    self.tableWidget.setItem(0, 7, QTableWidgetItem("Issue Date"))
                    self.tableWidget.setItem(0, 8, QTableWidgetItem("EXP Date"))
                    self.tableWidget.setItem(0, 9, QTableWidgetItem("Day"))
                    self.tableWidget.setItem(0, 10, QTableWidgetItem("Fine"))
                    i, j = 0, 0
                    for x in all_admin_username_pas:
                        i = i + 1
                        j = 0
                        for y in x:
                            self.tableWidget.setItem(i, j, QTableWidgetItem(y))
                            j = j + 1
                    self.vBoxLayout = QVBoxLayout()
                    self.vBoxLayout.addWidget(self.tableWidget)
                    self.setLayout(self.vBoxLayout)

            App = QApplication(sys.argv)
            window = Window()
            App.exec()
        else:
            print(showerror('Not in library', 'There is no any fine'))
if __name__=="__main__":
    print(showerror('ShowError', 'Please Run the Login.py First to access all the services'))
    exit(0)
