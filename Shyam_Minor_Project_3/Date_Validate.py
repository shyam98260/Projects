import datetime
date_string = '2017-12-31'
date_format = '%Y-%m-%d'

def validate(date_string,date_format):
    try:
        date_obj = datetime.datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

if __name__=="__main__":
    print(showerror('ShowError', 'Please Run the Login.py First to access all the services'))
    exit(0)