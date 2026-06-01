fname = r"/home/ucuber/Workspace/kurse/kurs-python/materialien/small_sample.log"
with open(fname) as fd:
    zeichen = list(fd.read())

with open(fname) as fd:
    worte = fd.read().split(" ")

with open(fname) as fd:
    # zeilen = fd.readlines() # liest mit \n
    zeilen = fd.read().splitlines() # Entfernt \n - ist manchmal sinnvoller

print(type(zeichen), len(zeichen), zeichen[:20])
print(type(worte), len(worte), worte[:20])
print(type(zeilen), len(zeilen), zeilen[:20])

