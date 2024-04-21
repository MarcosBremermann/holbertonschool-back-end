#!/usr/bin/python3
import urllib3

resp = urllib3.request("GET", "https://jsonplaceholder.typicode.com")
print(resp.status)
