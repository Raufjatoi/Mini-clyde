import os
import tkinter as tk
import speech_recognition as sr
r = None  # Declare the recognizer globally


r = None  # Declare the recognizer globally

def start_listening():
    global r, mic, stop_button
    # Rest of the code...

def stop_listening():
    global r, mic
    if r:
        r.stop()
    if mic:
        mic.__exit__()


def recognize_speech(audio):
    try:
        text = r.recognize_google(audio, language='en-US')
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error with the speech recognition service: {e}"

# Create the main window
root = tk.Tk()
root.title("Speech to Text")
root.geometry("400x200")
root.configure(bg='#6A0DAD')  # Set background color to purple

# Example styling
root.option_add('*Font', 'Arial 12')
root.option_add('*Button*Font', 'Arial 12 bold')
root.option_add('*Button*Background', '#3498db')  # Set button background color to blue
root.option_add('*Button*Foreground', 'white')

# Create a label for the title
title_label = tk.Label(root, text="Speech to Text", font=("Arial", 20, "bold"), fg='#6A0DAD', bg='#3498db')
title_label.pack(pady=10)

# Create an entry widget for displaying the recognized text
text_var = tk.StringVar()
entry = tk.Entry(root, textvariable=text_var, width=40)
entry.pack(pady=10)

# Create a button to start listening
start_button = tk.Button(root, text="Start Listening", command=start_listening)
start_button.pack(pady=10)

# Create a button to stop listening
stop_button = tk.Button(root, text="Stop Listening", command=stop_listening, state=tk.DISABLED)
stop_button.pack(pady=10)

# Start the main loop
root.mainloop()
