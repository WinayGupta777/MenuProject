import os
import subprocess as sp

print()
os.system("tput bold setaf 0")
os.system("cat Outlook-DS.txt")
os.system("tput sgr0")
print("-------------------------------------------------------")
dm = input("Select your domain: ")