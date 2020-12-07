#!/usr/bin/env python3
from urllib.request import urlopen
import pickle

uri = "http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.load(urlopen(uri))

for line in data:
    print("".join([i * j for i, j in line]))
