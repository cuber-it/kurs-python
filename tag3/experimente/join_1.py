fname = r"/home/ucuber/Workspace/kurse/kurs-python/materialien/small_sample.log"
with open(fname) as fd:
    zeilen = fd.read().splitlines() # Entfernt \n - ist manchmal sinnvoller

print("|||".join(zeilen))
