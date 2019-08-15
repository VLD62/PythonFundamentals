#import datetime
#
#def addSecs(tm, secs):
#    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
#    fulldate = fulldate + datetime.timedelta(seconds=secs)
#    return fulldate.time()
#
#
#if __name__ == "__main__":
#    leave_time = datetime.datetime.strptime(input(), '%H:%M:%S')
#    number_of_steps = float(input())
#    seconds_per_step = float(input())
#
#    print(f'Time Arrival: {addSecs(leave_time,number_of_steps*seconds_per_step)}')


if __name__ == "__main__":
    hh, mm, ss = list(map(int, input().split(":")))
    number_of_steps = int(input())
    seconds_per_step = int(input())
    total_seconds = (hh*3600 + mm*60 + ss + number_of_steps * seconds_per_step) % (24 * 3600)
    hours = int(total_seconds / 60 / 60)
    mins = int(total_seconds / 60 % 60)
    secs = int(total_seconds % 60)
    print('Time Arrival: %02d:%02d:%02d' % (hours, mins, secs))
