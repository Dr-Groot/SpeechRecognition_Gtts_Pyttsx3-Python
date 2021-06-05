# TEXT TO SPEECH USING PYTTSX3

Pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

![image](https://user-images.githubusercontent.com/63160825/120885475-babd3e80-c606-11eb-9a01-bf8bc9716566.png)


First install **Python** and **pip** on your system, then install **pyttsx3** by:

```python
pip install pyttsx3
```

Then go with,

```python
# importing pyttsx3 library
import pyttsx3

# creating object
engine = pyttsx3.init()

# getting details of current voice
voices = engine.getProperty('voices')

# setting up the voice, you can change index to get mail or female voice
engine.setProperty('voice', voices[0].id)

# or if you want to check how many voice do you have you can switch between different index and run
# print(voices[index].id)

# setting up the voice rate
engine.setProperty('rate', 200)

# setting up what we want to listen
engine.say("Hello, i love python")

# Ending up with
engine.runAndWait()
```

## EXPLANATION

Import pyttsx3 first, then we create object by **pyttsx3.init()** , After all setting up we gather details of current voice by **engine.getProperty('voices')** 
and storing in voices

Next, we set up the voice by **engine,setProperty('voice', voices[0].id)** , changing index can change voices- 0 for **Male** and 1 for **Female** .

Then we set rate by **engine.setProperty('rate', 200)** , we can change the word per second by changing the number but by deafult it is 200. Then

We set up what we want to listen by using **enigne.say("text")**, machine will speak up the text which we have given in the argument and ten we end by **enigne.runANdWait()**


## EXTRA

We can adjust rate, volume, voice, etc.

RATE: 

```python
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate
```

<br />

VOLUME:

```python
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
```

<br />

VOICE:

```python
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
```

<br />

SAVING VOICE TO FILE

```python
engine.save_to_file('Hello World', 'test.mp3')
```

It will save the file in **.mp3** format.
