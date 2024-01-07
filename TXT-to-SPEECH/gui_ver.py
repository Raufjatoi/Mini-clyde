import os
import tkinter as tk
from gtts import gTTS

def text_to_speech():
    text = entry.get()
    tts = gTTS(text=text, lang='en')
    tts.save('text_to_speech.mp3')
    os.system('start text_to_speech.mp3')

# Create the main window
root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x200")
root.configure(bg='#6A0DAD')  # Set background color to purple

# Example styling
root.option_add('*Font', 'Arial 12')
root.option_add('*Button*Font', 'Arial 12 bold')
root.option_add('*Button*Background', '#3498db')  # Set button background color to blue
root.option_add('*Button*Foreground', 'white')

# Create a label for the title
title_label = tk.Label(root, text="Text to Speech", font=("Arial", 20, "bold"), fg='#6A0DAD', bg='#3498db')
title_label.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to convert text to speech
convert_button = tk.Button(root, text="Convert", command=text_to_speech)
convert_button.pack(pady=10)

# Start the main loop
root.mainloop()
