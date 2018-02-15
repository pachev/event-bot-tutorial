# event-bot-tutorial

Repository of tutorial from https://pachevjoseph.com/posts/python-discord-bot

### Requirements

* Python 3.6+

## Installation

### Python Virtual Environment

This project is best ran in a virtual environment. You can use [pyvenv][3],
which comes with python 3 and greater. The virtual enviroment lets you run
different versions of python and packages from other projects.

#### Installation (Unix)

First install python3+ on your machine which should come with [pip][4]. If
not, download from link provided.

1. `python3 -m venv env` - Create a virtual environment in the env folder
2. `source env/bin/activate` - Load the environment
3. `pip install -r requirements.txt` - Install dependencies
4. `deactivate` - Unloads the environment

#### Installation (Windows)

Note - Most documentation is for unix systems. Differences between windows and unix are: `env\Scripts\` instead of `env/bin/` and libraries go in `env\Lib\` rather than `env/lib/`)

First install python3+ on your machine and then download and install [pip][4].
Then from the root of the project run:

1. `pip install virtualenv` - Install virtualenv if not already done soCreate a virtual environment in the venv folder
2. `virtualenv venv` - This creates will create a series of directories and scripts
3. `venv/Scripts/activate` - Load the enviroment (There should be a (venv) before the current directory path name
4. `pip install -r requirements.txt` - Install dependencies
5. `deactivate` - Unloads the environment

## Running

Once dependencies are running, make sure that the environmental variable `BOT_TOKEN` is set to your bot token.
Use `python bot.py` in order to run the bot.
