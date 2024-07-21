import datetime
import wikipedia
import webbrowser
import os
import pyttsx3
import wikipediaapi
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
import pyjokes
from ecapture import ecapture as ec
import time
import wolframalpha
import random
import smtplib
from googlesearch import search


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

# Function to get the user's name from the input field
def get_name():
    global name
    name = name_entry.get()
    if name.strip() == "":
        name = "User"  # Default name if the user didn't provide any
    name_label.config(text=f"Hi {name}, How can I assist you?")
    wishme(name)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(name):
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak(f"Hello Good Morning {name}")
    elif 12 <= hour < 18:
        speak(f"Hello Good Afternoon {name}")
    else:
        speak(f"Hello Good Evening {name}")
    speak("How can I assist you? What are you looking for?")

def Latewishme(name):
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak(f"Good Morning {name}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon {name}")
    else:
        speak(f"Have a good sleep {name}")
    speak("How can I assist you? What are you looking for?")

def takecommand(name):
    try:
        speak(f"Typing to {name} ......")
        query = input_text.get("1.0", tk.END).lower()
        speak(f"{name} you said : {query} \n")
        return query.strip()

    except Exception as ex:
        speak(f"{name} can you say that again please ......")
        return "none"

def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(query)

    if page.exists():
        response = f"According to Wikipedia, here is some information about {query}:\n"
        response += page.summary[:500]  # Get the first 500 characters of the summary
        speak(response)
        return response
    else:
        response = f"I'm sorry, I couldn't find information about {query} on Wikipedia."
        speak(response)
        return response

def on_enter_pressed(event):
    query = takecommand(name)
    output_text.delete("1.0", tk.END)
    if 'open wikipedia' in query:
        speak('Searching Wikipedia...')
        statement = query.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'hi' in query or 'hello' in query:
        response = "Hello! How can I assist you today? "
        speak(response)
    elif 'open visual studio code' in query:
        response = "Access granted. Opening Visual Studio Code..."
        speak(response)
        npath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(npath)
    elif 'open virtualbox' in query:
        response = "Opening VirtualBox..."
        speak(response)
        npath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
        os.startfile(npath)
    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube..."
        speak(response)
    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "robo camera", "img.jpg")
    elif 'search' in query:
        statement = query.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)
    elif 'what is the time' in query or 'time' in query:
        Time = datetime.datetime.now().strftime("%I:%M:%S %p")
        speak(f"The time is {Time}")
        response = Time

    elif 'open cisco packet tracer' in query:
        speak("Access granted, Opening Cisco packet tracer")
        path =    "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Cisco Packet Tracer\Cisco Packet Tracer.lnk"
        os.startfile(path)
    elif 'joke' in query:
        Jokes = pyjokes.get_joke(language='en', category='neutral')
        response = Jokes
        speak(Jokes)
    elif 'who are you' in query or 'what can you do' in query:
        speak('I am Musni Voice Assistant version 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome, gmail and ,predict time,take a photo,search wikipedia,predict weather and open some Desktop applications'
              'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
    elif "who made you" in query or "who created you" in query or "who discovered you" in query:
        speak("I was built by Musni.")

    elif 'bye' in query:
        speak('your personal assistant is shutting down,Good bye')
        root.destroy()

    elif 'sleep pc' in query:
        speak('Putting the PC sleep Now......')
        os.system("rundll32.exe powrprof.dll, SetSuspendState Sleep.")

    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
        response = "Opening Google..."
        speak(response)
    elif 'who is aysha' in query.lower():
        speak("Aysha Nuha, my Bubu, epitomizes everything meaningful in my life. Her presence is a soothing melody in the chaos, a beacon of light in darkness. With her, every moment becomes a cherished memory, every hurdle seems conquerable. She embodies love, strength, and grace, painting my world with hues of happiness. In her arms, I find solace, in her smile, my sanctuary.")

    elif 'what is the time' in query:
        strtime = datetime.datetime.now().strftime("%I:%M:%S %p")
        response = f"My dear friend, the time is {strtime}"
        speak(response)


    elif 'open chatgpt' in query:
        webbrowser.open("https://chat.openai.com/")
        response = "ChatGPT is my friend, Opening ChatGPT......."
        speak(response)

    elif 'shutdown' in query:
        speak(f"Ok My dear Friend {name} see you soon")
        os.system("shutdown /s /t 1")



    else:
        response = "I am sorry, I don't understand that. Can you please repeat or ask something else?"
        speak(response)
    output_text.insert(tk.END, response)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Musni personal Assistant")
    root.geometry("600x400")

    style = ttk.Style()

    # Adding the input field for the user's name
    name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
    name_label.pack(pady=10)
    name_entry = tk.Entry(root, font=("Arial", 12), bg="#F0F0F0", fg="black")
    name_entry.pack(fill=tk.X, padx=10)
    name_button = tk.Button(root, text="Submit", command=get_name, font=("Arial", 12))
    name_button.pack(pady=5)

    # Label for assistant's greetings
    input_label = tk.Label(root, text="Musni Personal Assistant", font=("Arial", 14))
    input_label.pack(pady=10)

    # Text area for user input
    input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), height=3, bg="#F0F0F0", fg="black")
    input_text.pack(fill=tk.X, padx=10)

    # Text area for assistant's responses
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), height=7, bg="#F0F0F0", fg="black")
    output_text.pack(fill=tk.X, padx=10, pady=10)

    # Bind the enter key to the on_enter_pressed function
    input_text.bind("<Return>", on_enter_pressed)

    # Start the main Tkinter event loop
    root.mainloop()
