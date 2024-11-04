# Voice_Assistant ~ Void

## About The Project

Console Application which help to do your daily work routine.

## Why Void

- It can search on wikipedia.
- It can open YouTube, Spotify, Whatsapp (if installed on your pc) and other cool stuff.
- You can easily add your command.

## Built With

- Python 3

## Installation

To install the dependencies required for this project, run the following command:

```bash
pip install -r requirements.txt
```

## Running the Code

To run the code, use the following command:

```bash
python void.py
```

## Adding Your Own Command

To add your own command, you can modify the `void.py` file by adding an `elif` block with your voice command and corresponding action. For example:

```python
elif 'your voice command' in query:
    speak("Your command")
    # Your code here
```

## Acknowledgements

- Python 3 language
- wikipedia library
- pyttsx3 library
- os library
- speech_recognition library
- webbrowser library
