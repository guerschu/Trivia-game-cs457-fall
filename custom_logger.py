import datetime

def logIt(event):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('./syslog.txt', 'a') as file:
        file.write(current_time)
        file.write(event)
        file.write('\n')