import os
import time
from _posts import *

timestr = time.strftime("%Y-%m-%d")

# old_file = os.path.join("_posts", my_file_name)
# new_file = os.path.join("_posts", "b.kml")
def nameUpdate():
    oldName(my_time)
    pass
def oldName(list):
    oldname = list[0]+"-MyUpdate.md"
    pass

my_time = ["2014-3-3"]
my_time.insert(0,timestr)
my_time.pop()
print(timestr)
print(my_time)

# os.rename(old_file, new_file)
