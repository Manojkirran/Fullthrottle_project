# Fullthrottle_project
 Interview Project In this Project i have design an API to serve that data in the json format and the below is my API link.
 API:http://manojkirran.pythonanywhere.com/members

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django , djangorestframework,faker(used to create DUMMY Data).

'''bash
pip install django
pip install djangorestframework
pip install Faker
'''
## Usage

import requests
import json
response = requests.get("http://manojkirran.pythonanywhere.com/members")

text = json.dumps(response.json(), sort_keys=False, indent=4)
print(text)

## Contributing
get requests are welcome.

##Instruction
•	You can create a N number of dummy data using PopulateDummydata.py
•	And this design and implemented in Django and restframework
•	I have hosted my application in pythonanywhere 




