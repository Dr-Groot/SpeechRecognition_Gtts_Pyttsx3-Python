# install pyttsx3 using "pip install pyttsx3" on your terminal
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


# --------------------------GUIDE-------------------------
# You can also adjust rate, volume, voice, etc. by using:
# import pyttsx3
# engine = pyttsx3.init() # object creation

# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()
