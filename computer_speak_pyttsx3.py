# import pyttsx3 and to know more about pyttsx3 working https://github.com/Dr-Groot/Python/blob/main/text_to_speech_pyttsx3.py
import pyttsx3

# create object
engine = pyttsx3.init()

# get property of voices
voices = engine.getProperty('voices')

# set voice id means male or female
engine.setProperty('voice', voices[0].id)

# set speed of speaking as default is 200
engine.setProperty('rate', 250)

# defining a function that will speak the value pass to it
# and by this function it will increase the code re usability
def speak(st):
    # set st to listen
    engine.say(st)
    engine.runAndWait()

# call the function by passing the value you want to listen
speak('Hello i am using speak function')

# now whenever you want your computer to speak any text you have to just call
# speak function, and you do not have to write code again and again for that
