#!/usr/bin/python

import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print "Operation done sucessfully" + response.text;

url1 = "https://reqres.in/api/login"
payload = {"email":"peter@klaven","password":"cityslicka"}
response1 = requests.post(url1, data=payload)
print(response1.text)
