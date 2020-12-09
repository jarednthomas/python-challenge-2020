#!/usr/bin/env python3
from string import ascii_lowercase as alpha

url = "http://www.pythonchallenge.com/pc/def/map.html"
cyphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

k = 2
caesar_shift = str.maketrans(alpha, (alpha[k:] + alpha[:k]))

#decoded_text = cyphertext.translate(caesar_shift)
#print(decoded_text)

current_page = url[(len(url) - 8):(len(url) - 5)]
decoded_url = current_page.translate(caesar_shift)
new_url = url.replace(current_page, decoded_url)
print(new_url)
