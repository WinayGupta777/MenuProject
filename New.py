import os
import subprocess as sp
import time

os.system("clear")
print()
os.system("tput bold setaf 0")
os.system("cat Outlook.txt")
os.system("tput sgr0")
dm = input("\n\nSelect your domain('q' for quit): ")
print("-------------------------------------------------------")

domain_dict = {
    "1":"Core Linux",
    "2":"Computer Vision",
    "3":"Data Science",
    "4":"Containers",
    "q":"Closing program..."
    }

if dm=='q':
    print(domain_dict[f"{dm}"])
    print()
    time.sleep(2)
elif dm=='1':
    print("\n\tRedirecting to '{}' page ...".format(domain_dict[f"{dm}"]))
    time.sleep(2)
elif dm=='2':
    print("\n\tRedirecting to '{}' page ...".format(domain_dict[f"{dm}"]))
    time.sleep(2)
elif dm=='3':
    print("\n\tRedirecting to '{}' page ...".format(domain_dict[f"{dm}"]))
    time.sleep(2)
    os.system("python3 DS.py")
elif dm=='4':
    print("\n\tRedirecting to '{}' page ...".format(domain_dict[f"{dm}"]))
    time.sleep(2)
    os.system("python3 Cont.py")
