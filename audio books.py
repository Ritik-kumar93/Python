from gtts import gTTS
import os
a="hey guys welcome to my youtube channel monster and thanks for watching this video"
l='en'
m=gTTS(text=a,lang=l,slow=False)
m.save("hello.mp3")
os.system("mpg321 hello.mp3")
