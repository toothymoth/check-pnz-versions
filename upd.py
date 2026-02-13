import requests as req
import time
import zlib

download_url = "https://cdn-sp.tortugasocial.com/avataria-ru/app/"

pnz = "pnz-city_"
#current_version = "98.85.1"
v1 = 100
v2 = 80
v3 = 1
f = open("pnz-lists.txt", "a")

while True:
    current_version = f"{v1}.{v2}.{v3}"
    dumb = req.get(download_url+pnz+current_version+".swf")
    if dumb.ok:
        file = dumb.content
        try:
            file_decompress = zlib.decompress(file[8:])
        except zlib.error:
            print(download_url+pnz+current_version+".swf")
            break
        indexClass = file_decompress.find(b"AppManager")
        isObf = "not obfuscated"
        if indexClass == -1:
            isObf = "obfuscated"
        f.write(f'{download_url+pnz+current_version+".swf"},{isObf}\n')
        if isObf == "not obfuscated":
            print(current_version, "NOT OBFUSCATED FOUND")
    v3 -= 1
    if v3 == 0:
        v3 = 199
        v2 -= 1
    if v2 == 0:
        v2 = 199
        v1 -= 1
    if v1 == 0:
        break
    print(current_version, "progress")

    #time.sleep(0.005)



