'''
This is an alarm program. 
Please check my countdown and Timer repository
 for a better way of writing the same program.
'''

import winsound
import time

def my_alarm():
    try:
        my_time = list(map(int,input("Enter time in hour min sec \n").split()))
        if len(my_time) == 3:
            total_seconds = my_time[0]*60*60 + my_time[1]*60+ my_time[2]
            time.sleep(total_seconds)
            frequency = 2500 
            duration = 1000
            winsound.Beep(frequency,duration)
        else:
            print("Enter time in correct format")
            my_alarm()
    except Exception as e:
        print('THis is the exception\n',e,'So, please enter correct details')
        my_alarm()


my_alarm()
