#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment
import re

# open url and read html
url = "http://www.pythonchallenge.com/pc/def/equality.html"
page = urlopen(url)
html = page.read().decode("utf-8")

cyphertext = []
# parse html with BeautifulSoup and store found comments into cyphertext
soup = BeautifulSoup(html,'html.parser')
for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
    cyphertext.append(comments.extract())

# define regex that satifies hint
regex = r"[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]"
match = re.findall(regex, str(cyphertext))

# solve for new_url
new_url = url.replace("equality","".join(i[4] for i in match))
print(new_url)

# test solution
response = urlopen(new_url)
print(response.getcode())
