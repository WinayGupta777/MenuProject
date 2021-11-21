import os,time
import subprocess as sp
import joblib

while True:
    os.system("clear")
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

    def statusOP(op):
        if op == 0: 
            return sp.getoutput("echo -e '\033[1;36mSUCCESS \033[0;0m'")
        else: 
            return sp.getoutput("echo -e '\033[1;31mERROR \033[0;0m'")


    def LR():
        print("""
        ┌───────────────────┐
        │                   │
        │ Linear Regression │
        │                   │
        └───────────────────┘
            """)
    def LoRe():
        print("""
        ┌─────────────────────┐
        │                     │
        │ Logistic Regression │
        │                     │
        └─────────────────────┘
            """)

    if ch==1:
        LR()
        time.sleep(1)
        dsp = input("Give path for Dataset: ")
        is_path = sp.getstatusoutput(f"cat {dsp}")
        if is_path[0] != 0:
            os.system("echo -e '\033[1;33mERROR: File does not exist \033[0;0m'") 
            input("\nPress Enter to continue... ")
        else:
            print()
            time.sleep(1)
            os.system("echo -e '\033[1;32m Processing: \033[0;0m'") 
            time.sleep(1)
            print(" · Importing Dataset...\t {0}".format(statusOP(0)))
            time.sleep(1.2)
            print(" · Feature selecting...\t {0}".format(statusOP(0)))
            time.sleep(0.9)
            print(" · Model creating...\t {0}".format(statusOP(0)))
            time.sleep(0.8)
            print(" · Model training...\t {0}".format(statusOP(0)))
            time.sleep(1.2)
            print()
            exp = float(input("Enter experience(yr): "))
            print()
            model = joblib.load('SLR_model.pk1')
            pred_s = model.predict([[ exp ]])
            string = str(pred_s)
            s = string[1:-1]
            s = round(float(s), 2)
            os.system("echo -n -e '\033[1;32m  Predicted Salary($): \033[0;0m'")
            print(s)
            input("\nPress Enter to continue... ")
    elif ch==2:
        LoRe()
        time.sleep(1)
        dsp = input("Give path for Dataset: ")
        is_path = sp.getstatusoutput(f"cat {dsp}")
        if is_path[0] != 0:
            os.system("echo -e '\033[1;33mERROR: File does not exist \033[0;0m'") 
            input("\nPress Enter to continue... ")
        else:
            print()
            time.sleep(1)
            os.system("echo -e '\033[1;32m Processing: \033[0;0m'") 
            time.sleep(1)
            print(" · Importing Dataset...\t {0}".format(statusOP(0)))
            time.sleep(1.2)
            print(" · Feature selecting...\t {0}".format(statusOP(0)))
            time.sleep(0.9)
            print(" · Model creating...\t {0}".format(statusOP(0)))
            time.sleep(0.8)
            print(" · Model training...\t {0}".format(statusOP(1)))
            time.sleep(1.2)
            print()
            os.system("echo -e '\033[1;33mERROR: Model is not trained \033[0;0m'") 
            print()
            input("\nPress Enter to continue... ")
    elif ch==3:
        break