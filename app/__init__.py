"""
Gastric Bypass Train: Sam, Anna, Sadi
6 November, 2022
"""
from flask import Flask
from flask import session
from flask import render_template
from flask import request
from flask import redirect
import os
import utl.TableHandler as tbl_hndl

app = Flask(__name__)
app.secret_key = os.urandom(32)

#SQLite set up
tbl_hndl.seed()

@app.route("/", methods = ["POST", "GET"])
def home_page():
    #print(request.form)
    notice = ""
    if ("login" in request.form):
        print ("Logging in " + request.form["username"])
    if ("register" in request.form):
        if (not tbl_hndl.register( request.form["username"],  request.form["password"])):
            notice = "Username Taken"
        else:
            notice = "User Registered. Please Log In."
    return render_template("login_and_register.html", message = notice)

@app.route("/logout")
def logout():
  session.pop("username")
  session.pop("password")
  print(session)
  return redirect("/")


if __name__ == "__main__":
  app.debug = True
  app.run()
