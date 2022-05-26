""" Launching lots of commands with subprocess """

import random
import string
import subprocess

for i in range(10000):
    hash = ''.join([random.choice(string.ascii_letters) for j in range(30)])
    ret = subprocess.run('echo ' + hash, shell=True, stdout=subprocess.DEVNULL)
