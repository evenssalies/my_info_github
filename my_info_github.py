# update_info.py
import json
import datetime

# Read existing data
try:
    with open("my_info_github.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {"user": "YourUsername", "github_folder": "", "publications_folder": "", "conversation_history": []}

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