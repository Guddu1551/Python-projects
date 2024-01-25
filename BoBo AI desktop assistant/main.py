import speech_recognition as sr
import win32com.client
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""


def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"User: {query}\n BoBo: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    try:
        speaker.Speak(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        return "Sorry, I didn't understand"


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n          ***************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    # todo: Wrap this inside of a  try catch block
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/prompt- {random.randint(1, 255555555)}", "w") as f:
        with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)


# def say(text):
#     os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google_cloud(audio, language="en-in")
            print(f"You said: {query}")
            return query
        except Exception as e:
            return "Sorry, I didn't understand"


if __name__ == "__main__":
    speaker.Speak("I am BoBo, the desktop A.I.")
    while True:
        print("I am listening")
        query = takeCommand()
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wiki", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} .....")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "D:\Guddu\Doraemon_Theme_Song_Gintama.mp3"
            os.system(f"play {musicPath}")

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"the time is {strfTime}")

        elif "Using A I".lower() in query.lower():
            ai(prompt=query)

        elif "BoBo Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
