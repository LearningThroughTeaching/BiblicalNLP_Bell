import os
from googletrans import Translator
from tkinter import Tk, Text, Scrollbar, Frame
import json

# Specify the path to the file
file_path = "C:\\Users\\Kbell\\Downloads\\BiblicalNLP_Bell\\data\\greek_text\\1_john_greek.txt"

# Read the contents of the file
with open(file_path, "r", encoding="utf-8") as file:
    try:
        greek_text = file.read()
        print("File content:", greek_text)
    except Exception as e:
        print("Error reading file:", str(e))
        greek_text = ""

# Convert the text to JSON format
text_json = json.dumps([{"text": greek_text}])

# Translate the Greek text to English
translator = Translator(service_urls=['translate.google.com'])
try:
    english_text = translator.translate(text_json, src="el", dest="en").text
except Exception as e:
    print("Translation failed:", str(e))
    english_text = ""

# Create a window to display the English translation
window = Tk()
window.title("Greek to English Translation of 1 John")
window.geometry("800x600")

# Create a frame to hold the text widget and scrollbar
frame = Frame(window)
frame.pack(fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Create a text widget to display the English translation
text_widget = Text(frame, wrap="word", yscrollcommand=scrollbar.set)
text_widget.pack(fill="both", expand=True)
text_widget.insert("1.0", english_text)

# Configure the scrollbar to work with the text widget
scrollbar.config(command=text_widget.yview)

# Start the main event loop
window.mainloop()
