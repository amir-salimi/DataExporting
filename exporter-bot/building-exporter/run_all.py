a = [
"bayut-address1500.py ",
"bayut-address2000.py ",
"bayut-address2500.py ",
"bayut-address3000.py ",
"bayut-address3500.py",
]

from subprocess import call
import os

for i in a:
    os.system(f'python {i} &')