import os
import subprocess as sp

print()
os.system("tput bold setaf 0")
os.system("cat Outlook.txt")
os.system("tput sgr0")
print("-------------------------------------------------------")
dm = input("Select your domain: ")
print("-------------------------------------------------------")

domain_dict = {
    "1":"Core Linux",
    "2":"Computer Vision",
    "3":"Data Science",
    "4":"Containers"
    }


print(domain_dict[f"{dm}"])
print()
