#!/usr/bin/env python3
import zipfile, requests, io

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
r = requests.get(url)
zf = zipfile.ZipFile(io.BytesIO(r.content))
print("".join((data.comment).decode('utf-8') for data in zf.infolist()))
