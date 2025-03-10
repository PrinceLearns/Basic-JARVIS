import speech_recognition as sr
import os
from win32com.client import Dispatch
import webbrowser
import google.generativeai as genai
from dotenv import dotenv_values

chatStr = ''

def ai(query):
    global chatStr
    print(chatStr)
# Set up the API key 
    env_vars = dotenv_values(".env")
    genai.configure(api_key= env_vars.get("GenaiAPIKey"))

    chatStr += f"Prince: {query}\n Jarvis:"

# Choose a model
    model = genai.GenerativeModel("gemini-2.0-flash") 

    prompt = chatStr

# Generate response
    response = model.generate_content(prompt)

    reply = response.text

    chatStr += reply + '\n'

    speak(reply)

    return reply


def speak(text):
    sapi = Dispatch("SAPI.SpVoice")
    sapi.speak(text)

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source: 

        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language = "en-in")
            print(f"User said {query}")
            return query
        
        except Exception as e:
            return "Some Error occurred. Sorry From JARVIS"

if __name__ == '__main__':
    
    speak("Hello I am Jarvis A.I. Created by Prince.")

    while True:
        print("Listening....")

        query = takecommand()

#add more sites
        sites = [["Youtube","https://youtube.com/"], ["chat gpt","https://chatgpt.com/"],]
        folders = [["Steam","C:\\Users\\Public\\Desktop\\Steam.lnk"], ["Brave", "C:\\Users\\princ\\OneDrive\\Desktop\\Brave.lnk"], ]

        for site in sites:

            if f"Open {site[0]}".lower() in query.lower():
                print(f"Opening {site[0]}......")
                speak(f"Opening {site[0]} Sir.")

                webbrowser.open(site[1])
                break

#add more folders
        for folder in folders:

            if f"Open {folder[0]}".lower() in query.lower():
                print(f"Opening {folder[0]}.....")
                speak(f"Opening {folder[0]} Sir.")

                os.startfile(folder[1])
                break
            
        if f"Stop JARVIS".lower() in query.lower():
            print("Closing JARVIS.....")
            speak("Thank You Sir.")
            break

        else :
            print("Chatting....")
            ai(query)