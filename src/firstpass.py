import json
from googletrans import Translator
from tkinter import Tk, Text, Scrollbar, Frame, Toplevel
from tkinter import Label

# Read the text from the file
file_path = "data/greek_text/1_john_greek.txt"
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

greek_text = "".join(lines)

# Remove "1John " at the beginning of each line
lines = [line.replace("1John ", "") for line in lines]
greek_text = "".join(lines)

# Load the concordance data from the JSON file
concordance_file_path = "data/greek_concordances/1_john_concordance.json"
with open(concordance_file_path, "r", encoding="utf-8") as concordance_file:
    concordance_data = json.load(concordance_file)

# Create a window to display the Greek text
window = Tk()
window.title("1 John Greek Text")
window.geometry("800x600")

# Create a frame to hold the text widget and scrollbar
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

# Configure the scrollbar to work with the text widget
scrollbar.config(command=greek_widget.yview)

# Function to display concordance information on mouse hover
def display_concordance_info(event):
    word = greek_widget.get("current wordstart", "current wordend")
    for verse in concordance_data:
        for word_info in verse["verse"]:
            if word_info["word"] == word:
                # Create a smaller window to display the concordance information
                info_window = Toplevel(window)
                info_window.title("Concordance Information")
                info_window.geometry("400x200")
                
                # Display the relevant information in the smaller window
                info_text = f"Word: {word_info['word']}\nNumber: {word_info['number']}\nText: {word_info['text']}"
                info_label = Label(info_window, text=info_text)
                info_label.pack()
                
                # Highlight the matching word in blue
                start_index = greek_widget.search(word, "1.0", stopindex="end", nocase=True)
                while start_index:
                    end_index = f"{start_index}+{len(word)}c"
                    greek_widget.tag_add("highlight", start_index, end_index)
                    greek_widget.tag_config("highlight", background="blue")
                    start_index = greek_widget.search(word, end_index, stopindex="end", nocase=True)
                
                # Print the matches to the console
                print(f"Matches for '{word}':")
                for verse in concordance_data:
                    for word_info in verse["verse"]:
                        if word_info["word"] == word:
                            print(f"Verse: {verse['verse_number']}, Word: {word_info['word']}")
                
                return

# Bind the mouse hover event to the display_concordance_info function
greek_widget.bind("<Enter>", display_concordance_info)

# Start the main event loop
window.mainloop()
