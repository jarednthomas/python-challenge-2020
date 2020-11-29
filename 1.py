#!/usr/bin/env python3

url = "http://www.pythonchallenge.com/pc/def/map.html"
current_page = url[(len(url) - 8):(len(url) - 5)]

a = "abcdefghijklmnopqrstuvwzyz"
k = "cdefghijklmnopqrstuvwzyzab"

caesar_shift = current_page.maketrans(a, k)
decoded_url = current_page.translate(caesar_shift)
new_url = url.replace(current_page, decoded_url)

print(new_url)