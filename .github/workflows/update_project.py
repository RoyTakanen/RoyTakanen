import requests
import re

f = open("README.md", "r")
file_content = f.read()

all_events = requests.get("https://api.github.com/users/RoyTakanen/events").json()

push_events = list(filter(lambda event: event['type'] == "PushEvent", all_events))

github_user = push_events[0]["actor"]["login"]
project_name = push_events[0]["repo"]["name"].replace(github_user + "/", "", 1)
project_url = "https://github.com/" + push_events[0]["repo"]["name"]

new_content = re.sub(r'currently working on .*', 'currently working on [' + project_name + '](' + project_url + ')', file_content)

f = open("README.md", "w")
f.write(new_content)
f.close()
