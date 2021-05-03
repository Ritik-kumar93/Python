import win32com.client as w
s=w.Dispatch("SAPI.SpVoice")
while 1:
    print("enter the word you want to speak")
    t=input()
    s.speak(t)
