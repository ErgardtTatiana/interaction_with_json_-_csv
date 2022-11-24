import json
import csv
from files import CSV_FILE_PATH
from files import JSON_FILE_PATH

with open(JSON_FILE_PATH, "r") as f:
    users = json.load(f)
    modified_users = []

for elem in users:
    modified_users.append({
        'name': elem['name'],
        'gender': elem['gender'],
        'address': elem['address'],
        'age': elem['age'],
        'books': []
    })

with open(CSV_FILE_PATH, newline='') as f:
    books = list(csv.DictReader(f))
    for elem in books:
        del elem['Publisher']

for i in range(len(books)):
    j = i % len(users)
    modified_users[j]['books'].append(books[i])

with open("result.json", "w") as f:
    reference = json.dumps(modified_users, indent=4)
    f.write(reference)
