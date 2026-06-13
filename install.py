import os

os.system("pip install kahoot --break-system-packages")
os.system("pip install flask --break-system-packages")

if os.name == "posix":
    os.system("wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64")
    os.system("chmod +x cloudflared-linux-amd64")
    os.system("sudo mv cloudflared-linux-amd64 /usr/bin/cloudflared")
elif os.name == "nt":
    os.system("winget install Cloudflare.cloudflared")