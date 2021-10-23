import subprocess as sp
import os

#################
os.system("tput bold setaf 0")
os.system("figlet -c < line.txt")
os.system("figlet -c 'Menu'")
os.system("figlet -c < line.txt")

os.system("echo -e $(cat options.txt)")

os.system("tput sgr0")
#################

ch = int(input("Enter your choice: "))
print(ch)



def statusOP(op):
    os.system("tput bold")
    os.system("tput setaf 6")
    if op == 0: print("SUCCESS")
    else: print("ERROR")
    os.system("tput sgr0")

if ch == 1:
    op = sp.getstatusoutput("date")
    print(op[1])
    statusOP(op[0])

elif ch == 2:
    op = sp.getstatusoutput("cal")
    print(op[1])
    statusOP(op[0])
    
elif ch == 3:
    op = sp.getstatusoutput("ip addr show enp0s3 | grep inet | head -n 1")
    print("Your IPv4 is : ", op[1].split(' ')[5])
    statusOP(op[0])

elif ch == 4:
    op = sp.getstatusoutput("route -n")
    print(op[1])
    statusOP(op[0])
    
elif ch == 5:
    op = sp.getstatusoutput("ss -ta")
    print(op[1])
    statusOP(op[0])
elif ch == 6:
    op = sp.getstatusoutput("lscpu")
    print(op[1])
    statusOP(op[0])
elif ch == 7:
    op = sp.getstatusoutput("ls -a")
    print(op[1])
    statusOP(op[0])
elif ch == 8:
    op = sp.getstatusoutput("free -m")
    print(op[1])
    statusOP(op[0])
elif ch == 9:
    os.system("sl") #Can't use sp.get...
elif ch == 10:
    file_name = input("Enter file path(Your system):")
    remote_ip = input("Enter remote IP: ")
    remote_dir = input("Where you want to send(Remote system): ")
    op = sp.getstatusoutput("scp {0} {1}:{2}".format(file_name, remote_ip, remote_dir))
    #print(op[1])
    statusOP(op[0])
elif ch == 11:
    ip = input("(Root)Remote IP: ")
    cmd = input("Command name: ")
    op = sp.getstatusoutput("ssh root@{1} {0}".format(cmd,ip))
    print(op[1])
    statusOP(op[0])
elif ch == 12:
    svc = input("Enter the service name: ")
    op = sp.getstatusoutput("systemctl start {0}".format(svc))
    print(op[1])
    statusOP(op[0])
elif ch == 14:
    #svc = input("Enter the service name: ")
    op = sp.getstatusoutput("cat >> a.txt")
    print(op[1])
    statusOP(op[0])
elif ch == 13:
    fp = input("Enter file path: ")
    op = sp.getstatusoutput("cat {0}".format(fp))
    print(op[1])
    statusOP(op[0])
elif ch == 15:
    fp = input("Enter file path: ")
    op = sp.getstatusoutput("cat {0}".format(fp))
    print(op[1])
    statusOP(op[0])
elif ch == 16:
    #os.system("ping -c3 8.8.8.8")
    op = sp.getstatusoutput("ping -c3 8.8.8.8")
    print(op[1])
    statusOP(op[0])
elif ch == 17:
    wb = input("Enter website name: ")
    op = sp.getstatusoutput("nslookup {0}".format(wb))
    print(op[1])
    statusOP(op[0])
    
