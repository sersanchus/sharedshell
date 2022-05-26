""" Launching lots of commands with sharedshell """

import random
import string
import subprocess

import sys
sys.path.append('sharedshell')

import sharedshell

with sharedshell.SharedShell() as shell:

    for i in range(10000):
        hash = ''.join([random.choice(string.ascii_letters) for j in range(30)])
        shell.run('echo ' + hash, stdout=subprocess.DEVNULL)
