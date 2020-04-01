# Script to Automate

import requests
import json
import time
import io
from tkinter import filedialog
from tkinter import *

SUBMIT_URL = 'https://api.crxcavator.io/v1/submit'
# RESULTS_URL = 'https://api.crxcavator.io/v1/metadata/{extension_id}'
API_KEY = 'fsgqjSSovyhzlLxGagIkwlPSMwKHXPSr'

extension_id = []
bad_extension = []
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select Extension List file",filetypes = (("text files","*.txt"),("all files","*.*")))
with open(root.filename, "r") as extensionList:
    for line in extensionList:
        stripped_line = line.strip()
        extension_id.append(stripped_line)
print(extension_id)

file1 = io.open("output.txt", "w", encoding='utf-8')

def scan_extension(id):
    head = {'Content-Type': 'application/json', 'API-Key': API_KEY}
    data = json.dumps({'extension_id': id})
    res = requests.post(SUBMIT_URL, headers=head, data=data).json()
    time.sleep(1)
    if "error" in res:
        print(res['error'])


def submit_extension(extension):
    res = requests.get('https://api.crxcavator.io/v1/metadata/%s' % extension).json()
    if res is None:
        print(extension + "is not found, submitting for scan.")
        scan_extension(extension)
        bad_extension.append(extension)
        return
    full_url = "https://crxcavator.io/report/" + extension
    extensionid = res['extension_id']
    name = res['name']
    rating = res['rating']
    ratingusers = res['rating_users']
    users = res['users']
    print(
        "ID: " + extensionid + "\n" +
        "Name: " + name + "\n" +
        "Rating: " + str(rating) + "\n"
        "# of Ratings: " + str(ratingusers) + "\n"
        "# of Users: " + str(users) + "\n" +
        "Full Risk URL: " + full_url + "\n\n"
    )
    file1.write(
        "ID: " + extensionid + "\n" +
        "Name: " + name + "\n" +
        "Rating: " + str(rating) + "\n"
        "# of Ratings: " + str(ratingusers) + "\n"
        "# of Users: " + str(users) + "\n" +
        "Full Risk URL: " + full_url + "\n\n"
    )

for i in extension_id:
    try:
        submit_extension(i)
    except Exception as e:
        print(e)

file1.write("IDs not found. potentially malicious: \n"
            + '%s' % bad_extension
            )


file1.close()