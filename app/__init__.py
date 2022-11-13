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
def entrance():
    #print(request.form)
    print(session)
    notice = ""
    if ("login" in request.form):
        #print ("Logging in " + request.form["username"])
        if (tbl_hndl.checkLogin( request.form["username"],  request.form["password"])):
            session["username"] = request.form["username"]
            session["password"] = request.form["password"]
            username = session["username"]
        else: 
            notice = "Wrong Username or Password"

    if ("register" in request.form):
        if (not tbl_hndl.register( request.form["username"],  request.form["password"])):
            notice = "Username Taken"
        else:
            notice = "User Registered. Please Log In."
    if (len(session) > 0):
        return redirect("/homepage")
    return render_template("login_and_register.html", message = notice)

@app.route("/homepage", methods=["POST", "GET"])
def home_page():
	print(session)
	matrix = tbl_hndl.list_of_pages()
	print (matrix)
	table_form = matrix

	return render_template("landing.html", table = table_form)

@app.route("/make_story", methods=["POST", "GET"])
def make_story():
	title = request.form["title"]
	text = request.form["opening"]
	if (len(title) > 0 and len(text) > 0):
		tbl_hndl.start_story(title, text, session["username"])
	return redirect("/homepage")

@app.route("/logout")
def logout():
  session.pop("username")
  session.pop("password")
  username = ""
  print(session)
  return redirect("/")


if __name__ == "__main__":
  app.debug = True
  app.run()
