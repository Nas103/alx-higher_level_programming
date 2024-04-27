#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
