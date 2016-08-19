import time

""" calculating current time """

time_=time.time()
secs_in_day=60*60*24 #seconds in a day
secs_in_curr_day=int(time_%secs_in_day) #time in current day in seconds
hour=int(secs_in_curr_day//3600)
minutes=int(secs_in_curr_day//60-hour*60)
seconds=int(secs_in_curr_day-hour*3600-minutes*60)
print ("\nCurrent time:")
print ("\n{:02d}:{:02d}:{:02d}\n".format(hour,minutes,seconds))