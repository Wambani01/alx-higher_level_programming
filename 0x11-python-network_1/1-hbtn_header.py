#!/usr/bin/python3
# retrieving a header from a urllib request

from urllib.request import urlopen
from sys import argv

url = argv[1]
with urlopen(url) as response:
    header = response.getheader("X-Request-Id")
print(header)
