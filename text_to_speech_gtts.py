# we are using package gtts which stands for Google Text To Speech and its also an interface with Google translate text to speech API
# before starting just check you have python and pip install.
# after checking all your requirement now install gtts package by writing "pip install gtts" on your terminal
# now import gTTS function from gtts library
from gtts import gTTS

# import os, it is available default by the python
import os

# give text you want machine to speak
myText = "We are using gtts library for text to speech conversion"

# provide language you want to create audio file
language = "en"

# pass text and language to gtts engine, also we marked slow = false
# as it will tell module to convert audio should in high speed
output = gTTS(text = myText, lang= language, slow= False)

# saving our audio in form of .mp3 form by using save function
output.save("audio.mp3")

# play our audio using os package and it will play audio by your default player.
os.system("start audio.mp3")

## -----------------For Audio Book making ----------------
# we can also use txt file as input by using file handling function open() and set file as read mode and  then store all text in one variable
# In replacement of line 11 we can write
# f = open("filename.txt", "r")
# myText = f.read().replace("\n", " ")
# and add " f.close() "  on line 19

# Important : stay connected to internet while running this program
