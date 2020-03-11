from datetime import date
import calendar
import datetime
def mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm():
    tdate = date.today()
    day = tdate.day
    month = tdate.month
    year = tdate.year
    # print(day, ' ', month, " ", year)

    kkkkkkkkkk = "" + str(day) + " " + str(month) + " " + str(year) + ""

    def findDay(date):
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        return (calendar.day_name[born])

    mmmmmmmmm = {1: ' Jan', 2: ' Feb', 3: ' Mar', 4: ' Apr', 5: ' May', 6: ' June', 7: ' July', 8: ' Aug', 9: ' Sep',
                 10: ' Oct', 11: ' Nov', 12: ' Dec'}
    dddd = str(findDay(kkkkkkkkkk)) + " , " + str(day) + mmmmmmmmm[
        int(month)]  # "-" + str(month) + "-" + str(year) + ""
    return dddd