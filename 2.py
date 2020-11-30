#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup, Comment

# open url and read html
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
page = urlopen(url)
html = page.read().decode("utf-8")

c = []
# parse html with BeautifulSoup and store found comments into c
soup = BeautifulSoup(html,'html.parser')
for comments in soup.findAll(text=lambda text:isinstance(text, Comment)):
    c.append(comments.extract())

# save last comment in c as a string called cyphertext
cyphertext = str(c[len(c) - 1])

count = {}
# iterate through characters in cyphertext while counting into dict count
for char in cyphertext:
    count[char] = count.get(char, 0) + 1

avg_count = 0
# define rarity by getting an average of the counts
for total in count:
    avg_count += count[total]

avg_count /= len(count)

solution = []
# append 'rare' characters from count into solution
for a in count:
    if (count[a] < (avg_count * 0.2)):
        solution.append(a)

# replace old solution to supposed new solution
new_url = url.replace("ocr","".join(solution))
print(new_url)
