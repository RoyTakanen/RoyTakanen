import requests
import re
from datetime import datetime, time

f = open("README.md", "r")
file_content = f.read()

projects = requests.get("https://api.github.com/users/kaikkitietokoneista/repos").json()

biggest_time = datetime.strptime("1999-09-27T17:51:22Z", '%Y-%m-%dT%H:%M:%SZ')

for project in projects:
    time_formatted = datetime.strptime(project["pushed_at"], '%Y-%m-%dT%H:%M:%SZ')
    if time_formatted > biggest_time and project["name"] != "kaikkitietokoneista":
        biggest_time = time_formatted
        project_name = project["name"]
        project_url = project["html_url"]

new_content = re.sub(r'currently working on .*', 'currently working on [' + project_name + '](' + project_url + ')', file_content)

f = open("README.md", "w")
f.write(new_content)
f.close()
