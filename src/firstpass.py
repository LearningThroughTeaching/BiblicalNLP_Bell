import json

# Read the concordance data from the JSON file
concordance_file_path = "data/greek_concordances/1_john_concordance.json"
with open(concordance_file_path, "r", encoding="utf-8") as concordance_file:
    concordance_data = json.load(concordance_file)

# Extract the "text" and "verse" sections from each entry
text_and_verse_lines = [f"{entry['verse']}: {entry['text']}" for entry in concordance_data if 'text' in entry]

# Display the text and verse lines
for line in text_and_verse_lines:
    print(line)
