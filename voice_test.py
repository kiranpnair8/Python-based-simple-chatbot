import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio)
        print("You said:", recognized_text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")


        
