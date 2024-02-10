import json
import requests
import tkinter as tk
from tkinter import Label, Entry, Button, Scrollbar, Listbox, END, Y

def search_artist():
    artist_name = entry.get()
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + artist_name)
    data = response.json()

    listbox.delete(0, END)
    for result in data["results"]:
        listbox.insert(END, result["trackName"])

# Create the main window
root = tk.Tk()
root.title("iTunes Song Search")

# Create and place widgets
label = Label(root, text="Enter the artist:")
label.pack(pady=10)

entry = Entry(root, width=30)
entry.pack(pady=10)

search_button = Button(root, text="Search", command=search_artist)
search_button.pack(pady=10)

listbox = Listbox(root, width=50, height=15)
listbox.pack(pady=10)
listbox_scrollbar = Scrollbar(root, orient="vertical")
listbox_scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=listbox_scrollbar.set)
listbox_scrollbar.config(command=listbox.yview)

# Start the Tkinter event loop
root.mainloop()





'''

import json 
import requests
a = input("Enter the artist : ")

response = requests.get("https://itunes.apple.com/search?entitity=song&limit=50&term=" + a)
print(json.dumps(response.json(),indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])

 '''   