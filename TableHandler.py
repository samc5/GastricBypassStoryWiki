"""
Sam Cowan, Anna Fang, Sadi Nirloy of Gastric Bypass Train
"""

import sqlite3   #enable control of an sqlite database

DB_FILE="discobandit"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
def seed(): #Creates login and homepage tables, should be run before anything else (other than clear)
	c.execute("create table if not exists logins(username text primary key, password text not null);")
	c.execute("create table if not exists homepage(title text, idnum integer primary key);")
def clear(): #clears homepage and all story tables but not login table. Useful in testing, not so much in actual websites
	c.execute(f'select name from sqlite_master where type = "table" and name = "homepage"')
	bool = c.fetchone()
	if bool:
		count = storyCount()
		#print(count)
		for i in range(count):
			c.execute(f'drop table if exists table{i}')
		c.execute('drop table if exists homepage')
	

def register(username, password): #adds user/password to logins table
	c.execute(f'select count(username) from logins where username = "{username}"')
	num = c.fetchone()[0]
	if num == 1:
		print("uh that username has already been taken") #tell user the username already exists and do this whole thing again
	else:
		c.execute(f'insert into logins values("{username}", "{password}")')

def checkLogin(username, password): #checks if password is right
	c.execute(f'select password from logins where username = "{username}"')
	pw = c.fetchone()[0]
	if pw == password:
		return True
	else:
		return False
def storyCount(): #counts how many stories on homepage
	c.execute('select count(title) from homepage;')
	num = c.fetchone()[0]
	return num
def list_of_pages(): #2D array of tables on homepage
	num = storyCount()
	matrix = [[] for i in range(num)]
	#matrix = [ [' '] * 2 for i in range(num)]
	for i in range(num):
		command = f'select title from homepage where idnum = {i};'
		#print(i)
		#print(command)
		c.execute(command)
		title = str(c.fetchone()[0])
		#print(title)
		matrix[i] = [title,i]
		#matrix.append(c.fetchone()[0])
	return matrix

def start_story(title, text, username): #creates a table for the story, adds it to homepage db, puts in the first entry
	count = storyCount()
	c.execute(f'create table if not exists table{count}(idnum integer, title text, entrynum integer primary key, entrytext text, username text)')
	c.execute(f'insert into table{count} values({count},"{title}", 0, "{text}", "{username}")')
	c.execute(f'insert into homepage values("{title}", {count})')
def user_check(username, idnum): #checks if username has already edited the story
	c.execute(f'select 1 from table{idnum} where username = "{username}"')
	bool = c.fetchone()
	if bool:
		return True
	return False
def addToStory(idnum, text, username): #adds new entry to story
	if not user_check(username,idnum):
		count = entryCount(idnum)
		title = getTitle(idnum)
		#print(title)
		c.execute(f'insert into table{idnum} values({idnum}, "{title}", {count}, "{text}", "{username}")')
	else:
		print("something has gone wrong - you've already edited the story")

def getTitle(idnum): #returns title of a story
	c.execute(f'select title from homepage where idnum = {idnum}')
	title = str(c.fetchone()[0])
	#print(title)
	return title

def story(idnum): #returns string of the entire story
	string = ""
	count = entryCount(idnum)
	c.execute(f'select entrytext from table{idnum}')
	for i in c.fetchmany(count):
		string += str(i[0]) + " "
	return string
def prevEntry(idnum): #returns string of latest entry
	count = entryCount(idnum)
	c.execute(f'select entrytext from table{idnum} where entrynum = {count - 1}')
	return str(c.fetchone()[0])
def entryCount(idnum): #counts entries in a story
	c.execute(f'select count(entrytext) from table{idnum}')
	count = c.fetchone()[0]
	return count
# #==========================================================
clear()
seed()
register("testUsername","whondurfulpassword")	
print(checkLogin("testUsername","whondurfulpassword"))
print(checkLogin("testUsername","notwhondurfulpassword"))
start_story("Sammy the Seal", "is it you, Agnes?", "sydHoff")
print(user_check("sydHoff",0))
addToStory(0,"No, Mrs. Jackson.","sydHoff (parody)")
addToStory(0,"Well then who could be barking like a seal?","sydHoff (real)")
print(list_of_pages())
print(story(0))
print(prevEntry(0))
# #==========================================================
db.commit() #save changes
db.close()  #close database


