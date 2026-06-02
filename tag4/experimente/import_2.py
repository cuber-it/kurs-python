def mach_was(): # Liegt in __main__
    print("HUHU")

from modul_1 import mach_was # Lädt mach_was nach __main__ überlädt existierende
from modul_2 import mach_was # Lädt mach_was nach __main__ - überlädt uweites mach_was

print(dir())

mach_was() # ruft mach_was aus __main__
mach_was() # dito


import modul_1 # lädt alle Namen nach __main__.modul_1 -> __main__.modul_1.mach_was
import modul_2 # lädt alle Namen nach __main__.modul_2 -> __main__.modul_2.mach_was

print(dir())

modul_1.mach_was()
modul_2.mach_was()
