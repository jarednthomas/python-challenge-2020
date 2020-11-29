#!/usr/bin/env python3
# removeprefix and removesuffix are part of python 3.9
url = "http://www.pythonchallenge.com/pc/def/map.html"
current_page = url.removeprefix("http://www.pythonchallenge.com/pc/def/")
current_page = current_page.removesuffix(".html")

a = "abcdefghijklmnopqrstuvwzyz"
k = "cdefghijklmnopqrstuvwzyzab"

caesar_shift = current_page.maketrans(a, k)
decoded_url = current_page.translate(caesar_shift)
new_url = url.replace(current_page, decoded_url)

print(new_url)
