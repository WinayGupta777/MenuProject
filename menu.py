import subprocess as sp
import os,time

#################
# os.system("tput bold setaf 0")
# os.system("figlet -c < line.txt")
# os.system("figlet -c 'Menu'")
# os.system("figlet -c < line.txt")
while True:
    os.system("clear")
    print()
    os.system("tput bold setaf 0")
    print("""
    \t\t############################
    \t\t#                          #
    \t\t#        Core Linux        #
    \t\t#                          #
    \t\t############################
    """)
    os.system("tput sgr0")
    print("--------------------------------------------------------------------")
    os.system("echo -e $(cat options.txt)")
    os.system("tput sgr0")
    #################

    ch = int(input("Enter your choice: "))
    print()



    def statusOP(op):
        if op == 0: 
            print(sp.getoutput("echo -e '\033[1;36mSUCCESS \033[0;0m'"))
        else: 
            print( sp.getoutput("echo -e '\033[1;31mERROR \033[0;0m'"))
        # os.system("tput bold")
        # os.system("tput setaf 6")
        # if op == 0: print("SUCCESS")
        # else: print("ERROR")
        # os.system("tput sgr0")


    if ch == 1:
        op = sp.getstatusoutput("date")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 2:
        op = sp.getstatusoutput("cal")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 3:
        op = sp.getstatusoutput("ip addr show enp0s3 | grep inet | head -n 1")
        print("Your IPv4 is : ", op[1].split(' ')[5])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 4:
        op = sp.getstatusoutput("route -n")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 5:
        op = sp.getstatusoutput("ss -ta")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 6:
        op = sp.getstatusoutput("lscpu")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 7:
        op = sp.getstatusoutput("ls -a")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 8:
        op = sp.getstatusoutput("free -m")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 9:
        os.system("sl") #Can't use sp.get...
    elif ch == 10:
        file_name = input("Enter file path(Your system):")
        remote_ip = input("Enter remote IP: ")
        remote_dir = input("Where you want to send(Remote system): ")
        op = sp.getstatusoutput("scp {0} {1}:{2}".format(file_name, remote_ip, remote_dir))
        #print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 11:
        ip = input("(Root)Remote IP: ")
        cmd = input("Command name: ")
        op = sp.getstatusoutput("ssh root@{1} {0}".format(cmd,ip))
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 12:
        svc = input("Enter the service name: ")
        op = sp.getstatusoutput("systemctl start {0}".format(svc))
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 14:
        #svc = input("Enter the service name: ")
        op = sp.getstatusoutput("cat >> a.txt")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 13:
        fp = input("Enter file path: ")
        op = sp.getstatusoutput("cat {0}".format(fp))
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 15:
        fp = input("Enter file path: ")
        op = sp.getstatusoutput("cat {0}".format(fp))
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 16:
        #os.system("ping -c3 8.8.8.8")
        op = sp.getstatusoutput("ping -c3 8.8.8.8")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 17:
        wb = input("Enter website name: ")
        op = sp.getstatusoutput("nslookup {0}".format(wb))
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 18:
        pkg = input("Enter Package name: ")
        ping = sp.getstatusoutput("ping -c1 8.8.8.8")
        if ping[0]==0:
            os.system("yum install {0} -y".format(pkg))
            statusOP(0)
        input("\nPress Enter to continue... ")
    elif ch == 19:
        fn = input("Enter file name: ")
        dn = input("Enter Folder name: ")
        os.system("find {0} -user root -name {1}".format(dn,fn))
        statusOP(0)
        input("\nPress Enter to continue... ")
    elif ch == 20:
        un = input("Username: ")
        os.system("useradd {0}".format(un))
        statusOP(0)
        input("\nPress Enter to continue... ")
    elif ch == 21:
        os.system("python3")
        statusOP(0)
        input("\nPress Enter to continue... ")
    elif ch == 22:
        str = input("Say to cow: ")
        os.system(f"cowsay {str}")
        statusOP(0)
        input("\nPress Enter to continue... ")
    elif ch == 23:
        fire = sp.getstatusoutput("systemctl stop firewalld")
        statusOP(fire[0])
        input("\nPress Enter to continue... ")
    elif ch == 24:
        os.system("cmatrix")
    elif ch == 25:
        op = sp.getstatusoutput("lsblk")
        print(op[1])
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch == 26:
        disk = input("Enter Disk's name: ")
        size = input("Enter size of partintion: ")
        #("parted  -s {} mklabel msdos")
        # os.system(f"parted {disk} print")  
        # os.system("parted {disk} mkpart primary ") 
        print("Sorry! We are working on this.")
        statusOP(1)     
        input("\nPress Enter to continue... ")
    elif ch == 27:
        disk = input("Enter Disk's name: ")
        os.system(f"parted {disk} print")
        no = input("\nWhich partition(Number): ")
        op = sp.getstatusoutput(f"parted {disk} rm {no}")
        statusOP(op[0])
        input("\nPress Enter to continue... ")
    elif ch==28:
        se = sp.getstatusoutput("getenforce")
        print(f"SELINUX={se[1]}")
        statusOP(se[0])
        input("\nPress Enter to continue... ")
    elif ch == 29:
        st = input("Select mode(1/0)? :")
        if st == '1':
            os.system("setenforce 1")
            statusOP(0)
        elif st =='0':
            os.system("setenforce 0")
            statusOP(0)
        else: print("Mode not supported!")
        input("\nPress Enter to continue... ")
    elif ch == 30:
        break

print("\n\tRedirecting to 'Home Page' page ...")
time.sleep(2)
os.system("python3 New.py")
