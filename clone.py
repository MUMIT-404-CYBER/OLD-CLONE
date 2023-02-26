import os, sys
os.system("git pull")
try:
    __import__("old_enc").Main()
except Exception as e:
    exit(str(e))
