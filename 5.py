#!/usr/bin/env python3
from urllib.request import urlopen
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.load(urlopen(url))

for line in data:
    print("".join([s * h for s,h in line]))
