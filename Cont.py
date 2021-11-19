import os
import subprocess as sp

print()
os.system("tput bold setaf 0")
print("""
\t\t############################
\t\t#                          #
\t\t#        Containers        #
\t\t#                          #
\t\t############################
""")
os.system("tput sgr0")
print("-----------------------------------------------------------")
os.system("echo -e $(cat Outlook-Cont.txt)")
os.system("tput bold setaf 0")
ch = int(input("\nEnter your choice: "))
os.system("tput sgr0")

def statusOP(op):
    if op == 0: 
        return sp.getoutput("echo -e '\033[1;36m SUCCESS \033[0;0m'")
    else: 
        return sp.getoutput("echo -e '\033[1;31m ERROR \033[0;0m'")



if ch == 1:
    print("\n   Running Compatibility test:\n")
    yum = sp.getstatusoutput("yum install   docker-ce --nobest")
    svc = sp.getstatusoutput("systemctl  status  docker")
    print(" · Docker-ce is installed...\t {0}".format(statusOP(yum[0])))
    #statusOP(yum[0])
    print(" · Docker daemone running...\t {0}\n".format(statusOP(svc[0])))
    #statusOP(svc[0])

elif ch == 2:
    print()
    os.system("echo -e '\033[1;32mActive containers:\033[0;0m'")
    ac = sp.getstatusoutput("docker ps")
    print(ac[1])
    os.system("echo -e '\033[1;33m\nAll containers:\033[0;0m'")
    da = sp.getstatusoutput('docker ps -a --format "{{.ID}}:: {{.Status}}\t :: {{.Names}}"')
    print(da[1])

elif ch == 3:
    print()
    os.system("echo -e '\033[1;32mAll Images:\033[0;0m'")
    ac = sp.getstatusoutput("docker images")
    print(ac[1])
    