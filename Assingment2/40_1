import time
import threading

def currentTime(count,WaitSeconds):
    print(time.ctime())
    count -= 1
    if count!=0:
        threading.Timer(WaitSeconds, currentTime,[count,WaitSeconds]).start()
             
def printCurrentTime(totalmins=1,WaitSeconds=2):
    count = (totalmins*60)/WaitSeconds + 1
    currentTime(count,WaitSeconds)
    
if __name__ == "__main__":
    try:
        printCurrentTime(1,5)
    except Exception as e:
        print(e)
