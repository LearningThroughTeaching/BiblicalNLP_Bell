from googletrans import Translator
from tkinter import Tk, Text, Scrollbar, Frame

# Hardcoded Greek phrase
greek_text = "Γεια σας, πώς είστε?"

# Translate the Greek text to English
translator = Translator(service_urls=['translate.google.com'])
try:
    english_text = translator.translate(greek_text, src="el", dest="en").text
except Exception as e:
    print("Translation failed:", str(e))
    english_text = ""

# Create a window to display the Greek and English translation
window = Tk()
window.title("Greek to English Translation")
window.geometry("800x600")

# Create a frame to hold the text widgets and scrollbar
frame = Frame(window)
frame.pack(fill="both", expand=True)

# Create a scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Create a text widget to display the Greek text
greek_widget = Text(frame, wrap="word", yscrollcommand=scrollbar.set)
greek_widget.pack(fill="both", expand=True)
greek_widget.insert("1.0", greek_text)
greek_widget.config(state="disabled")

# Add padding between Greek and English translation
padding_widget = Text(frame, height=1)
padding_widget.pack(fill="x")

# Create a text widget to display the English translation
english_widget = Text(frame, wrap="word", yscrollcommand=scrollbar.set)
english_widget.pack(fill="both", expand=True)
english_widget.insert("1.0", english_text)
english_widget.config(state="disabled")

# Configure the scrollbar to work with the text widgets
scrollbar.config(command=lambda *args: _scroll_text_widgets(*args, greek_widget, english_widget))

# Start the main event loop
window.mainloop()
