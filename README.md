# Django Serving Linux terminal with X-Term


This code displays a linux terminal in the web browser by combining the Xterm.js library,  Websockets, and Django channels.

**Disclaimer:**
This projects your linux terminal to your web browser in *its current process*. Be mindful of the fact that you're communicating
with your Linux kernel as the currently logged in user! Running commands you aren't sure of can be extremely dangerous..Otherwise, Happy hacking!

## Setup
After cloning this repo, the code for using Xterm is in index.html. So you may use your own or the one provided.

1. Create a venv and install Django. 
2. After Django is installed, `pip install channels`
3. Start server, `python manage.py runserver`

Head over to http://localhost:8000/terminal/

You should see the word *connected* in green

## Exit
1. In the web browser type `exit`
2. Press any key to completely disconnect*

You should see the word *disconnected*, and the button to *Connect* will be available

## **Issues**:
1. Because the current syntax causes the calling terminal to be projected to the browser. The terminal session MUST 
be ended (inside browser)before CTRL-C will successfully kill Django shell

2. *When exiting, to fully disconnect another keystroke needs to be inputted in the terminal
---

**Further development**
1. Enable user to customize further options.
     - window resize
     - cursor type
     - cursor style
     - color

2. Enable pre-configured functionality for security.
