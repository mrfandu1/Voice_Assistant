import pyttsx3
import speech_recognition as spr
import wikipedia
import webbrowser
import os
import time

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = spr.Recognizer()
    with spr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


def play_song(song_name):

    #Remove the comment from the below code to search for the song on specific app (YouTube or SpotifyWeb or SpotifyApp)

    #Search for the song on YouTube
    #youtube_search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    #webbrowser.open(youtube_search_url)

    #Search for the song on SpotifyWeb
    #spotify_search_url = f"https://open.spotify.com/search/{song_name.replace(' ', '%20')}"
    #webbrowser.open(spotify_search_url)

    # Or, play the song directly on Spotify App (if installed)
    spotify_path = os.path.expandvars("C:\\Users\\Chandan\\AppData\\Roaming\\Spotify\\Spotify.exe")
    try:
        os.startfile(spotify_path)
        # Wait for a moment to let Spotify launch
        time.sleep(2)
        
        # Then search for the song using Spotify URI
        spotify_uri = f"spotify:search:{song_name.replace(' ', '%20')}"
        os.system(f"start {spotify_uri}")
        
        speak(f"Searching for {song_name} on Spotify")
    except Exception as e:
        speak("Could not find Spotify on your system")
        print(e)


if __name__ == '__main__':

    speak("Void Assistant Activated ")
    print("Void Assistant Activated")
    speak("How can i help you?")
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")

        elif 'open whatsapp' in query:  #if installed in your system
            speak("opening whatsapp")
            loc = "C:\\Users\\Chandan\\AppData\\Roaming\\Whatsapp\\Whatsapp.exe"   #change the path according to your system
            os.startfile(loc)
        
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        #you can add more local disk by adding elif 'local disk e' in query: and so on
    
       
        elif 'open vs' in query:
                speak("opening visual studio code")
                code_path = "C:\\Users\\Chandan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)
    
        elif 'open notepad' in query:
                speak("opening notepad")
                notepad_path = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(notepad_path)

        elif 'play' in query:
            song_name = query.replace('play', '').strip()
            play_song(song_name)

        elif 'exit' in query:
            speak("exiting")
            exit(0)
