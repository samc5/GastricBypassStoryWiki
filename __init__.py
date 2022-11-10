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

app = Flask(__name__)
app.secret_key = os.urandom(32)


logins = {
    "tophr": "mykolyk"
}

@app.route("/", methods = ["POST", "GET"])
def home_page():
  #Some print lines
    print(len(request.form))
    print(len(request.args))
    print(session)
    print(request.form)
    print(request.args)
  #If a post form is received, set up the session
    if(len(request.form) > 0):
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
  #If a get form is received, set the session
    if(len(request.args) > 0):
        session["username"] = request.args["username"]
        session["password"] = request.args["password"]
  #If there is a session currently
    if(len(session) > 0):

    #If the username is not registered in login
      if(not session["username"] in logins.keys()):
        return "<h1>Who are you? I have no recollection of a " + str(session["username"]) + ".</h1>"
    #If the password does not match the provided username
      if (not logins[session["username"]] == session["password"]):
        return "<h1> Not the right password. SOUND THE INTRUDER ALERT!!!</h1>"
    #If the username is in logins and the password in session matches
      return render_template("landing.html", username = session["username"])
  #If there is no session
    return render_template("login_and_register.html")

@app.route("/logout")
def logout():
  session.pop("username")
  session.pop("password")
  print(session)
  return redirect("/")

if __name__ == "__main__":
  app.debug = True
  app.run()
