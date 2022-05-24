import webbrowser as web
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

#add the ability to control devices


def assistant(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def greeting():
    temp_hour = datetime.datetime.now()
    hour = int(temp_hour.strftime("%H"))
    time_of_day = ""
    if hour < 12:
        time_of_day = "Good Morning"
    elif 12 < hour < 18:
        time_of_day = "Good Afternoon"
    else:
        time_of_day = "Good Evening"
    assistant('{time} Sir. How can I help today.'.format(time = time_of_day))

def farewell():
    temp_hour = datetime.datetime.now()
    hour = int(temp_hour.strftime("%H"))
    time_of_day = ""
    if hour < 12:
        assistant("Have a good morning sir")
    elif 12 < hour < 18:
        assistant("Goodbye sir")
    else:
        assistant("Goodnight sir")


def audioinput():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening");
        audio = aud.listen(source)
        try:
            print("understanding")
            phrase = aud.recognize_google(audio, language='en-us')
            print("you said: ", phrase)
        except Exception as exp:
            print(exp);
            assistant("Can you repeat that");
            return 'None'
        return phrase


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    greeting()

    while (True):
        phrase = audioinput().lower();

        if "exit" in phrase:
            exit()
        elif "hey" in phrase:
            assistant("How may I help you sir")
        elif "bye" in phrase:
            farewell()
