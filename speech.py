import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init()

r = sr.Recognizer()
with sr.Microphone() as source:
   
    print("-->Say Something :")
    def say():
        audio = r.listen(source)
        text = r.recognize_google(audio)
        you=format(text).upper()
        return you
    
    while True:
        def main():
            wake=say()
            print(wake)
            if 'DEMO' in wake:2
                x=say()
                print(x)
                if 'BOARD 1' or 'BOARD ONE' in x:
                    if 'SWITCH 1' or 'SWITCH ONE' in x:
                        if 'ON' in x:
                            print("-->switch 1 turned on") 
                            engine.say(x)
                            engine.runAndWait()

                        elif 'OF' in x:
                            print("-->switch 1 turned on")
                elif 'BOARD 2' or 'BOARD TWO' or 'BOARD TO' in x:
                    if 'SWITCH 2' or 'SWITCH TWO' in x:
                        if 'ON' in x:
                            print("-->switch 2 turned on")
                        elif 'OF' in x:
                            print("-->switch 2 turned on")  
        
        try:    
            main()                              
        except:
            print("Sorry could not recognize what you said")