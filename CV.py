import os,time
import subprocess as sp

print()
os.system("tput bold setaf 0")
print("""
\t\t############################
\t\t#                          #
\t\t#      ComputerVision      #
\t\t#                          #
\t\t############################
""")
os.system("tput sgr0")
print("-----------------------------------------------------------")
os.system("echo -e $(cat Outlook-CV.txt)")
os.system("tput bold setaf 0")
ch = int(input("\nEnter your choice: "))
os.system("tput sgr0")

def statusOP(op):
    if op == 0: 
        return sp.getoutput("echo -e '\033[1;36mSUCCESS \033[0;0m'")
    else: 
        return sp.getoutput("echo -e '\033[1;31mERROR \033[0;0m'")

