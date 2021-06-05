# TEXT TO SPEECH USING GTTS

We are using package gtts which stands for **Google Text To Speech** and its also an interface with Google translate text to speech API.  We will import the 
gTTS library from the gtts module which can be used for speech translation. The text variable is a string used to store the user's input.

> **HISTORY :** Google Text-to-Speech is a screen reader application developed by Google for the Android operating system. It powers applications to read aloud 
> the text on the screen with support for many languages. 

![image](https://user-images.githubusercontent.com/63160825/120884338-48e1f680-c600-11eb-8d68-bf56d186cfac.png)

<br />

Before getting starting just check you have python and pip install. After checking all your requirement now install gtts package.

```python
pip install gtts
```

Now lets go with this library,

```python
from gtts import gTTS

# import os, it is available default by the python
import os

# give text you want machine to speak
myText = "We are using gtts library for text to speech conversion"

# provide language you want to create audio file
language = "en"

# pass text and language to gtts engine
output = gTTS(text = myText, lang= language, slow= False)

# saving our audio in form of .mp3 form by using save function
output.save("audio.mp3")

# play our audio using os package and it will play audio by your default player.
os.system("start audio.mp3")
```

<br />

## EXPLANATION:

First of all we import **gTTS** from gtts along with **os** which is a default library available by the python.

We use **myText** for storing the text which we want machine to speak. In **language** we store the language we want to listen the machine, we have set the language to **"en"** which stands for **English**. 

Now in gtts engine we have passed the text along with the language and set slow = Flase which means it will tell module to convert audio should in high speed.

Using the **save function** we save the audio in the form of **.mp3** format and then by using the next line it will play the audio file with the default player.


## EXTRA

We can also use any text file as an input and it will generate its audio file, it is sort of **audiobook making** . For that we will use **File Handling** we will open the file in the read mode using **open("filename", "r")**  and store it and the use that stored text for converting into audio.

In replacement of **myText** write:

```python
f = open("filename.txt", "r")
myText = f.read().replace("\n", " ")
```

And then close the file at the end:

```python
f.close()
```

