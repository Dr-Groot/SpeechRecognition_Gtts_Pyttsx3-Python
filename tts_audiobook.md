# DESIGNING AUDIO BOOK WITH GTTS AND PYTTSX3

An audiobook (or a talking book) is a recording of a book or other work being read out loud. A reading of the complete text is described as "unabridged",
while readings of a shorter version are an abridgement.

![image](https://user-images.githubusercontent.com/63160825/120917003-81e69d80-c6ca-11eb-8ba4-e10fdb432e2c.png)

Before going further we need to know how its work, basically we need a **text file** or you can get any article or book in **.txt** format. Then we will get that file
set in read mode using **File Handling**. After setting up then we convert the text into a audio file with the help of [Gtts](tts_gtts.md) or with [Pyttsx3](tts_pyttssx3.md).

I will show you with both the ways, but if you have not much understaning in Pyttsx3 and Gtts then go with these links: 
+ For Gtts [Click Here](tts_gtts.md)
+ For Pyttsx3 [Click Here](tts_pyttsx3.md)

Now lets go with the working module of **Audio Book**:

> FIRST GET ANY TEXT FILE IN .TXT FORMAT THEN GO WITH THESE CODE.

## USING GTTS

We have taken text file as "text.txt", Then

```python
# importing gtts library
from gtts import gTTS

# setting text file in read mode using file handling
f = open("text.txt", "r")

# setting up text 
myText = f.read().replace("\n", " ")

# setting up language we want machine to convert this text file.
language = "en"

# passing text and language to engine with slow as false.
output = gTTS(text=myText, lang=language, slow=False)

# saving that audio file as ".mp3" format using save function
output.save("audio.mp3")
```

## USING PYTTSX3

We have taken text file as "text.txt", Then

```python
# importing pyttsx3 module
import pyttsx3

# setting up engine by creating object
engine = pyttsx3.init()

# getting voices property
voices = engine.getProperty("voices")

# setiing up voice as male voice, you can go with female voice also by setting up index as 1
engine.setProperty("voice", voices[0].id)

# setting up text speech rate 
engine.setProperty("rate", 200)

# opening file in read mode using file handling
f= open("text.txt", "r")

# storing text in mytext by using read function
mytext = f.read().replace("\n", " ")

# asking machine to speak mytext
engine.say(mytext)

# stoping our machine
engine.runAndWait()
```

<br />

You can also save that file in mp3 format by adding

```python
engine.save_to_file(mytext, "audio.mp3")
```

## EXTRA

You can also build visual app or web application for Audio Book using html,css and flask for Web App and also Tkinter for Application.

THANK YOU !

[HOME](README.md)
