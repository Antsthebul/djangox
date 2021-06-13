# Django Serving Linux terminal with X-Term

**Not been tested for windows**

This code displays a linux terminal in the web browser by combining the Xterm.js library and Websockets using Django channels.

**Disclaimer:**
This projects your linux terminal in your web browser in its current process. Be mindful of the fact your communicating
with your Linux kernel, as the currently logged in user!. Running commands you aren't sure can be extremely dangerous..Otherwise, Happy hacking!

## Setup
After cloning this repo, the code for using Xterm is in index.html. So you may use your own or the one provided.

1. Create a venv and install Django. 
2. `pip install channels`
3. `python manage.py runserver`

Head over to localhost:8000/terminal/

You should see the word *connected* in green

## Exit
1. In the web browser type `exit`
2. Press any key to completely disconnect*

You should see the word *disconnected*

## **Issues**:
1. Becuase the current syntax causes the calling terminal to be projected to the browser. Terminal MUST be end
 - before CTRL-C to end Django shell

2. *When exiting, to fully disconnect another keystroke needs to be inputted in the terminal
---

**Further development**
1. Enable user to program further options.
     - window resize
     - cursor type
     - cursor style
     - color

2. Enable pre-configure security options
