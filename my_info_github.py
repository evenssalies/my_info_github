# update_info.py
import json
import datetime

# Read existing data
#   Create empty file my_info_github.json if it doesn't exist
try:
    with open("my_info_github.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"user": "82128",
            "name": {"forename": "Evens", "surname": "Salies"},
            "github_folder": "C:/Users/82128/Documents/GitHub",
            "conversation_history": []}
    with open("my_info_github.json", "w") as f:
        json.dump(data, f, indent=2)

# Add new entry
new_entry = {
    "date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "topic": "Current conversation topic",
    "notes": "Summary of what was discussed."
}
data["conversation_history"].append(new_entry)

# Write back to file
with open("my_info_github.json", "w") as f:
    json.dump(data, f, indent=2)