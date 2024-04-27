#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

def fetch_status():
    """
    Fetches status from the given URL and displays the response body
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", utf8_content)

    if __name__ == "__main__":
        fetch_status()
