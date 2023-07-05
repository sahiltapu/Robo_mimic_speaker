import os
import pyttsx3


if __name__ == '__main__':
    break_statement = ["BYE","Bye","bye"] #Breaking loop words #
    engine = pyttsx3.init()
    print("__Welcome to Robo Speaker__")
    while True:
        x = input("Enter what you want me to pronounce :: ")
        if x in break_statement:
            engine.say("Thank you for using me.")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()