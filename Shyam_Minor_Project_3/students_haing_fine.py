from tkinter import *
from tkinter.messagebox import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys
import mysql.connector
from mysql.connector import Error




def student_having_fine():
    connection = mysql.connector.connect(host='localhost', database='library', user='root', password='root')
    cursor = connection.cursor()
    query = "select * from issue_book where fine_amount>0 order by b_name asc"
    cursor.execute(query)
    all_admin_username_pas = cursor.fetchall()
    print(all_admin_username_pas)
    if len(all_admin_username_pas)>0:
        rl = len(all_admin_username_pas)
        print(rl)
        cl = len(all_admin_username_pas[0])
        print(cl)

        class Window(QWidget):
            def __init__(self):
                super().__init__()

                self.title = "PyQt5 Tables"
                self.top = 100
                self.left = 100
                self.width = 1250
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

                self.tableWidget.setItem(0, 0, QTableWidgetItem("Enrollment no"))
                self.tableWidget.setItem(0, 1, QTableWidgetItem("Name"))
                self.tableWidget.setItem(0, 2, QTableWidgetItem("Branch"))
                self.tableWidget.setItem(0, 3, QTableWidgetItem("Book Id"))
                self.tableWidget.setItem(0, 4, QTableWidgetItem("Book Name"))
                self.tableWidget.setItem(0, 5, QTableWidgetItem("Book Edition"))
                self.tableWidget.setItem(0, 6, QTableWidgetItem("Book Publication"))
                self.tableWidget.setItem(0, 7, QTableWidgetItem("Book Author"))
                self.tableWidget.setItem(0, 8, QTableWidgetItem("Issued Date"))
                self.tableWidget.setItem(0, 9, QTableWidgetItem("Exp Date"))
                self.tableWidget.setItem(0, 10, QTableWidgetItem("Fine Amount"))

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
        print(showerror('Error','There is no any Students Having Fine'))


if __name__ == '__main__':
    showwarning('Info', 'Please Login first using \'Log_in.py\' file')
    exit(0)
