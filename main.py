import pyttsx3
engine=pyttsx3.init()
text="Walter Anthony, welcome home"
engine.say(text)
engine.runAndWait()
rate=engine.getProperty("rate")
print(rate)
engine.say(text)
engine.runAndWait