#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time:", start_time.time())
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print("Stop time: ", stop_time.time())
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds
    hours = minutes // 60
    minutes = minutes % 60

    # display results
    print("ELAPSED TIME")
    if days > 0:
        print("Days:", days)
    print("Hours/minutes: ", "{0:0>2}".format(hours), ":", "{0:0>2}".format(minutes), sep="")
    print("Seconds: ", seconds, ".", microseconds, sep="")

if __name__ == "__main__":
    main()
