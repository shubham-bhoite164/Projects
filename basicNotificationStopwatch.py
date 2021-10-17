import time
from plyer import notification
print("Welcome to one shot Stopwatch. Please enter your desired time.\nKeep in mind the below instructions")
s=input("Enter the time with number then after some space unit of time : ")
a=s
s=s.lower()
s=s.strip().split()
if 'm' in a:
    n=int(s[0])*60
elif 'h' in a:
    n=int(s[0]*60*60)
elif 's' in a:
    n=int(s[0])

#print(n)

while True:
    time.sleep(n)
    notification.notify(
        title="Time is up !",
        message=" The stopwatch for "+a+" time is up",
        timeout=10
    )
    
    break

print("The stopwatch has Ended ")