import speech_recognition as sr

recognizer = sr.Recognizer()

def mic_listening(initial_text_message, end_print_message):
    try:
        print(initial_text_message)

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"{end_print_message} {text}\n")
            return text

    except sr.UnknownValueError:
        print("Google could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

while True:
    text = mic_listening("Say something, to take notes say 'Take Notes'!\n", "You said:")

    if text == 'take notes':
        with open("demofile.txt", "a") as f:
            note_text = mic_listening("Say what you want to write to your textfile!\n", "You said:")
            if note_text:
                f.write(note_text + "\n")
                print("Note written to demofile.txt")
    elif text == 'stop listening':
        print("Stopping the program.")
        break