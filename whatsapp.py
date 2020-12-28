import pywhatkit
number = int(input("Mobile Number:"))
text = input("Text:")
time = input("Time(Hours):")
minute = input("Time(Minutes):")
pywhatkit.sendwhatmsg(f"+91 {number}",text,int(time),int(minute))
