import pyautogui as spam
import time

limit=input("Enter No of messages: ")
msg=input("Enter the message need to send: ")

i=0

time.sleep(5)

while(i<int(limit)):
    spam.typewrite(msg)
    spam.press("Enter")
    i+=1