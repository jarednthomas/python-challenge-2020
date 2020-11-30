#!/usr/bin/env python3
from urllib.request import urlopen
import re

#n = "12345"
#n = str(16044/2)
#n = "63579"
n = "66831"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
regex = r"[0-9]{3,}"
nothing = re.compile(regex)

while True:
    content = urlopen(url % n).read().decode('utf-8')
    print(content)
    match = nothing.search(content)
    if match == None:
        break
    n = match.group(0)
