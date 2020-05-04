from subprocess import call
import time

def executionTime(path):
    starttime = time.time()
    call(["Python","{}".format(path)])
    endtime = time.time()
    return(endtime - starttime)

if __name__ == "__main__":
    try:
        program32_path = "C:\\Users\\priya\\Desktop\\32nd.py"
        timetaken = executionTime(program32_path)
        print timetaken
    except Exception as e:
        print(e)
