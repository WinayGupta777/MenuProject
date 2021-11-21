import os,time
import subprocess as sp

while True:
    os.system("clear")
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
            return sp.getoutput("echo -e '\033[1;36mSUCCESS \033[0;0m'")
        else: 
            return sp.getoutput("echo -e '\033[1;31mERROR \033[0;0m'")



    if ch == 1:
        print("\n   Running Compatibility test:\n")
        yum = sp.getstatusoutput("yum install   docker-ce --nobest")
        svc = sp.getstatusoutput("systemctl  status  docker")
        print(" · Docker-ce is installed...\t {0}".format(statusOP(yum[0])))
        time.sleep(1)
        print(" · Docker daemone running...\t {0}\n".format(statusOP(svc[0])))
        time.sleep(1)
        input("\nPress Enter to continue... ")
    elif ch == 2:
        print()
        os.system("echo -e '\033[1;32mActive containers:\033[0;0m'")
        ac = sp.getstatusoutput("docker ps")
        print(ac[1])
        os.system("echo -e '\033[1;33m\nAll containers:\033[0;0m'")
        da = sp.getstatusoutput('docker ps -a --format "{{.ID}}:: {{.Status}}\t :: {{.Names}}"')
        print(da[1])
        print("\n",statusOP(da[0]))
        input("\nPress Enter to continue... ")
    elif ch == 3:
        print()
        os.system("echo -e '\033[1;32mAll Images:\033[0;0m'")
        ac = sp.getstatusoutput("docker images")
        print(ac[1])
        print("\n",statusOP(ac[0]))
        input("\nPress Enter to continue... ")        
    elif ch == 4:
        print()
        nm = input("Enter Image's Name[:TAG]: ")
        print()
        os.system(f"docker pull {nm}\n")
        input("\nPress Enter to continue... ")
    elif ch == 5:
        print()
        img = input("From which image? :")
        e = input("Write ENV variable('N' if not) :")
        v = input("Link storage('N' if not) :")
        p = input("Enable PATing('N' if not) :")
        nm = input("Enter name :")
        if 'N' in e:
            if 'N' in v:
                if 'N' in p: 
                    sp.getstatusoutput(f"docker run -dit --name {nm} {img}")
                else: 
                    sp.getstatusoutput(f"docker run -dit --name {nm} -p {p} {img}")
            elif 'N' in p:
                sp.getstatusoutput(f"docker run -dit --name {nm} -v {v} {img}")
            sp.getstatusoutput(f"docker run -dit --name {nm} -p {p} -v {v} {img}")
        elif 'N' in v:
            if 'N' in p:
                sp.getstatusoutput(f"docker run -dit --name {nm} -e {e} {img}")
            sp.getstatusoutput(f"docker run -dit --name {nm} -p {p} -e {e} {img}")
        elif 'N' in p:
            if 'N' in v:
                sp.getstatusoutput(f"docker run -dit --name {nm}  -e {e} {img}")
            sp.getstatusoutput(f"docker run -dit --name {nm} -v {v} -e {e} {img}")
        else: sp.getstatusoutput(f"docker run -dit --name {nm} -v {v} -e {e} -p {p} {img}")
        input("\nPress Enter to continue... ")
    elif ch == 6:
        print()
        stop = input("Enter Container's Name/ID: ")
        op = sp.getstatusoutput(f"docker stop {stop}")
        print(op[1])
        print("\n",statusOP(op[0]))
        input("\nPress Enter to continue... ")
    elif ch == 7:
        print()
        ask = input("Remove all[y/n]: ")
        if 'y' in ask:
            op = sp.getstatusoutput("docker rm -f ${docker ps -a -q}")
            print(op[1])
            statusOP(op[0])
        rm = input("Enter Container's Name/ID: ")
        op = sp.getstatusoutput(f"docker rm {rm}")
        print(op[1])
        print("\n",statusOP(op[0]))
        input("\nPress Enter to continue... ")
    elif ch == 8:
        print()
        pl = sp.getstatusoutput("docker pull httpd")
        r = sp.getstatusoutput("docker rm w1")
        op = sp.getstatusoutput('docker run -dit --name w1 -p 8080:80 httpd')
        if op[0]==0:
            il = sp.getoutput("ifconfig  | grep -m4 'inet 19' | head -n 3")
            ip = il.split(' ')[9]
            print(f"You get service from: http://{ip}:8080")
            print("Web Server deployed successfully")
            print("\n",statusOP(op[0]))
        input("\nPress Enter to continue... ")
    elif ch == 9:
        print()
        fD = sp.getstatusoutput("gdown https://drive.google.com/uc?id=1tefDNWjx_VrdvWTq3Tc0ViAaXmlva5Ql")
        print(f" · Fetching required files...  \t {statusOP(fD[0])}")
        time.sleep(2)
        bI = sp.getstatusoutput("docker build -t imgml .")
        print(f" · Building fresh image...  \t {statusOP(bI[0])}")
        time.sleep(2)
        yr = input("\n   Enter experience(in yrs): ")
        fD = sp.getstatusoutput(f"docker  run -it  imgml {yr}")
        print(f" · Launching Container...  \t {statusOP(fD[0])}")
        time.sleep(2)
        print(fD[1])
        input("\nPress Enter to continue... ")
    elif ch==10:
        break

print("\n\tRedirecting to 'Home Page' page ...")
time.sleep(2)
os.system("python3 New.py")