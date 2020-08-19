import pyttsx3
engine = pyttsx3.init()
while True:
    speech = input("Speak to convert")
    engine.say(speech)
    engine.runAndWait()
    if speech == 'exit':
        break 
