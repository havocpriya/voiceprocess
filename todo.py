import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# File path to the audio file
audio_file_path = "C:\Users\HP\Desktop\voiceprocess.py\0b888e7e883240dbb775e7ce806660d2 (1).wav"  # Replace with the actual path to your audio file

# Reading the audio file and storing it in the audio_text variable
with sr.AudioFile(audio_file_path) as source:
    print("Processing audio file...")
    audio_text = r.record(source)
    print("Audio file processed")

# recognize_() method will throw a request error if the API is unreachable, hence using exception handling
try:
    # using Google speech recognition
    print("Text: " + r.recognize_google(audio_text))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

