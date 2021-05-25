# want to know GTTS  basic code and how it works then go to https://github.com/Dr-Groot/Python/blob/main/text_to_speech_gtts.py
# import gTTS function form gtts library
from gtts import gTTS

# importing operating system
import os

# setting up language
language = "en"

# we can directly add number in mytext in form of string but it is just practice
# program how to convert number in text form and then speak

# getting number from the user
n = int(input("Enter the number"))

# reversing the number
rnum = 0
while n != 0:
    digit = n % 10
    rnum= rnum *10 + digit
    n = n//10

# converting number to text and storing it in st variable
l = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
st = ""
while rnum != 0:
    digit = rnum % 10
    st = st + l[digit] + " "
    rnum = rnum // 10

# getting text to be converting into audio
mytext = st

# converting text into gTTS function and using slow = False as converted audio should be in high speed
output = gTTS(text= mytext, lang= language, slow= False)

# saving audio file as audio.mp3 using save function
output.save("audio.mp3")

# playing audio using os package and it will play using default player of the system
os.system("start output.mp3")
