#install the module used for text to speech conversion
import pyttsx3
#init function to get the engine instance in order to satisfy the speech conversion process
engine=pyttsx3.init()
#here input any text you want to convert to audio
text="Walter Anthony, welcome home"
engine.say(text)
#here the text is being processed
engine.runAndWait()
