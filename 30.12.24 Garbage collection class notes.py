#PYTHON NOTES 30-12-24
#GARBAGE COLLECTION MODULE
#REFERENCE COUNT
import sys
a=[1,2,3]
ref_count=sys.getrefcount(a)
print("Reference count:",ref_count)

import gc
gc.enable()
gc.disable()
l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1
print("Current threshold:",gc.get_threshold())
gc.set_threshold(1,2,2)
collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")
