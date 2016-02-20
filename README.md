# Pet Project

My first Python, Django, and Django REST Framework project.  Evolving prototype for a CRM and POS tool for something I can't elaborate on, although it should be pretty obvious.  OK that was probably an elaboration.

Will eventually pair well with the front end which I'll also be creating, because I'm a full stack kinda guy.

![alt text](http://www.jonathanadamski.com/_public/github/i-have-no-idea-what-im-doing.jpg "They'll let anyone on the Internet these days.")


##To start:
###On Mac
1.  `chmod +x setup.sh`
2.  `./setup.sh`


###On PC or Linux:
Do the big ole list below manually.
*I don't particularily care for Mac or PC or Linux, but I happen to be creating this on a Mac and I'm the only person who matters.*

###Setup.sh
Setup.sh is going to try and hold your hand through the scary parts.  It will, allegedly:
1. Install homebrew
2. Install Python 3+
3. Install mysql
4. Install virtualenv via pip
5. Make a directory ~/Projects
6. Create a virtual environment at ~/Projects/env
7. Use that virtual environment to
  1. Install the latest Django via pip
  2. Install the latest Django REST Framework via pip
    
You can pass a `-f` flag to `setup.sh` if you want to trust me and tell the prompts to shut up.  But that ignores all the work I put in to writing this script and the countdown of doom.


###Lazy.sh
Once `setup.sh` has finished, you can start the boat up in one swoop assuming you didn't do anything funny like move junk around:

`. ./lazy.sh`

* disclaimer:  i don't even use this myself, so...*


####kbye