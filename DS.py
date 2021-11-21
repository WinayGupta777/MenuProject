import os,time
import subprocess as sp

print()
os.system("tput bold setaf 0")
print("""
\t\t############################
\t\t#                          #
\t\t#       DataScience        #
\t\t#                          #
\t\t############################
""")
os.system("tput sgr0")
print("-----------------------------------------------------------")
os.system("echo -e $(cat Outlook-DS.txt)")
os.system("tput bold setaf 0")
ch = int(input("\nEnter your choice: "))
os.system("tput sgr0")

