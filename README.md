# P00: Wiki Project by Gastric Bypass Train
## Sam Cowan (PM), Anna Fang (Co-Devo), Sadi Nirloy (Co-Devo)

### Description of website/app:
- This app shows off the capabilities of a wiki through a fun story-writing game.
- Users can create account(s) and log in, with a flask session storing their login info for future visits
- User can create a story or add to an existing story (ONE TIME PER STORY), which stores entry into the local sqlite3 database shared by all users on a machine
- Flask HTML templates pull information from the database to be displayed on the website

### Launch Codes
#### How to clone/install
1. Navigate in your terminal to the directory in which you would like to store the Story wiki using `cd`
2. Clone the repository to your local file system by entering 
`git clone git@github.com:samc5/GastricBypassStoryWiki.git` into the terminal
3. `cd GastricBypassStoryWiki/` to navigate into the repo. Keep in mind that you can use tab to autocomplete for many cd commands (or c/p)
4. Create a virtual environment (you can do this anywhere but the following instruction are for creating it inside of the repo: `python3 -m venv <VENV_NAME>`
5. NOTE: writing `python` instead of `python3` will work on lab machines but the alias is not necessarily on other computers; I would recommend using `python3`because of this
6.  `cd <VENV_NAME>` to enter the virtual environment
7. Install the required python libraries into your venv with 
`pip install -r ../requirements.txt` (Again, this will be different if your venv is located elsewhere)
##### Now, you're ready to run it!
#### How to Run
1. In your terminal type `python3 ../__init__.py`. This will run the main flask app.
2. Among the many items of feedback this provides you is `Running on http://127.0.0.1:5000`. Copy the link posted within into the URL bar of any browser. 
3. You can now navigate the website. Feel free to place your terminal in a corner of the screen to see some of the output put out when you fill out a form

##### Broad Progress Meter:
[⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⣀⣀⣀] - INCOMPLETE BUT ON SCHEDULE
