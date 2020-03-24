import pyautogui
import time
import sys
import keyboard
import datetime

def isCancel(str):
    return (str+" ").upper().startswith('C')

def initCancel():
    print("Canceled. Program will now Exit.")
    sys.exit(0)

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


print("Welcome to JiggleTime v0.2!\n")

validHours = False
validMinutes = False

while (not validHours):
    hours = input("How many HOURS would you like this program to run for?\n(Alternatively, type 'cancel' to cancel.)\n>")
    if (isCancel(hours)):
       initCancel()
    elif (not hours.replace(".", "").isnumeric() or float(hours) <= 0):
        print("Please enter a valid number of hours.")
    elif (float(hours) > 24):
        print("That's a lot of hours, and this program doesn't want to be responsible for something bad happening because of that. Try a smaller number.")
    else:
        validHours = True
        print()

while (not validMinutes):
    minutes = input("How often in MINUTES would you like the mouse to move?\n(Alternatively, type 'cancel' to cancel.)\n>")
    if (isCancel(minutes)):
       initCancel()
    elif(not minutes.replace(".", "").isnumeric() or float(minutes) <= 0):
        print("Please enter a valid number of minutes.")
    elif (float(minutes) > float(hours)*60):
        print("Error: Minute interval is longer than the specified runtime in hours. Try something else.")
    else:
        validMinutes = True



print("\n======INITIATING JIGGLE TIME======")
startTime = datetime.datetime.now()
print("\nStart Time:", startTime.time())
print()
minutes = float(minutes)
hours = float(hours)
jiggleCount = 0

print("Type CTRL+C to Cancel while the program is running.")
print("Cancel will be delayed until the next jiggle.\n")
for i in range ((int)((hours*60)/minutes)):
    print("jiggling...")
    pyautogui.moveRel(25, 0, duration=0.25)
    pyautogui.moveRel(-25, 0, duration=0.25)
    jiggleCount = jiggleCount+1
    time.sleep(60*minutes)
pyautogui.moveRel(-25, 0, duration=0.25)

endTime = datetime.datetime.now()
print("\nEnd Time:", endTime.time())

print("\n========END OF JIGGLE TIME========")

print()
print(jiggleCount, "jiggles were had in approximately", int((endTime-startTime).total_seconds()/60), "minute(s).")
print()
print("Press Esc to exit the program.")

while(True):
    try:
        if (keyboard.is_pressed('Esc')):
            print("The program will now terminate.")
            time.sleep(1)
            sys.exit(0)
        time.sleep(1)
    except:
        break
        


