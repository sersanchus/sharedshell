""" Launching lots of commands with os.system """

import os
import random
import string

for i in range(10000):
    hash = ''.join([random.choice(string.ascii_letters) for j in range(30)])
    os.system('echo ' + hash + ' > ' + os.devnull)
