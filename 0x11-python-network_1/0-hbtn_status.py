#!/usr/bin/python3
# fetch a request
from urllib.request import urlopen
with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    output = f"Body response:\n\t- type: {type(body)}\n\t- content: {body}\n\
    \t- utf8 content: {bytes.decode(body)}"
    print(output)
