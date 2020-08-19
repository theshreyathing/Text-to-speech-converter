import pyttsx3
engine = pyttsx3.init()
while True:
    speech = input("Speak to convert")
    engine.say(speech)
    engine.runAndWait()
    if speech == 'exit':
        break 
sound = engine.getProperty('voices')
print(sound)
engine.setProperty('voice',sound[0].id)
engine.say("I will speak in Male voice")
engine.setProperty('voice',sound[1].id)
engine.say("I will speak this text in female voice")
engine.runAndWait()